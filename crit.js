const { chromium } = require("playwright");
const express = require("express");

const app = express();
const PORT = 8000;

(async () => {
  const googleUrl =
    "https://www.google.com/maps/search/dentist/@36.3671965,-86.5156829,10z/data=!3m1!4b1?authuser=0&hl=en&entry=ttu";

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  await page.goto(googleUrl);
  await page.waitForSelector('[jstcache="3"]');

  const scrollable = await page.$(
    "xpath=/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]"
  );
  if (!scrollable) {
    console.log("Scrollable element not found.");
    await browser.close();
    return;
  }

  let endOfList = false;
  while (!endOfList) {
    await scrollable.evaluate((node) => node.scrollBy(0, 2000));
    endOfList = await page.evaluate(() =>
      document.body.innerText.includes("You've reached the end of the list")
    );
  }

  const urls = await page.$$eval("a", (links) =>
    links
      .map((link) => link.href)
      .filter((href) => href.startsWith("https://www.google.com/maps/place/"))
  );

  const scrapePageData = async (url) => {
    const newPage = await browser.newPage();
    await newPage.goto(url);
    await newPage.waitForSelector('[jstcache="3"]');

    const nameElement = await newPage.$(
      "xpath=/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[1]/h1"
    );
    const name = nameElement
      ? await newPage.evaluate((element) => element.textContent, nameElement)
      : "";

    const ratingElement = await newPage.$(
      "xpath=/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[1]/span[1]"
    );
    const rating = ratingElement
      ? await newPage.evaluate((element) => element.textContent, ratingElement)
      : "";

    const reviewsElement = await newPage.$(
      "xpath=/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/span[2]/span/span"
    );
    let reviews = reviewsElement
      ? await newPage.evaluate((element) => element.textContent, reviewsElement)
      : "";
    reviews = reviews.replace(/\(|\)/g, "");

    const categoryElement = await newPage.$(
      "xpath=/html/body/div[2]/div[3]/div[8]/div[9]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/span/span/button"
    );
    const category = categoryElement
      ? await newPage.evaluate(
          (element) => element.textContent,
          categoryElement
        )
      : "";

    const addressElement = await newPage.$(
      'button[data-tooltip="Copy address"]'
    );
    const address = addressElement
      ? await newPage.evaluate((element) => element.textContent, addressElement)
      : "";

    const websiteElement =
      (await newPage.$('a[data-tooltip="Open website"]')) ||
      (await newPage.$('a[data-tooltip="Open menu link"]'));
    const website = websiteElement
      ? await newPage.evaluate(
          (element) => element.getAttribute("href"),
          websiteElement
        )
      : "";

    const phoneElement = await newPage.$(
      'button[data-tooltip="Copy phone number"]'
    );
    const phone = phoneElement
      ? await newPage.evaluate((element) => element.textContent, phoneElement)
      : "";

    await newPage.close();

    return { name, rating, reviews, category, address, website, phone, url };
  };

  const results = await Promise.all(urls.map((url) => scrapePageData(url)));

  await browser.close();

  app.get("/results", (req, res) => {
    res.json(results);
  });

  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
})();
