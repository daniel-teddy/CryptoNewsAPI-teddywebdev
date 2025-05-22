const PORT = process.env.PORT || 8000;
const express = require("express");
const axios = require("axios");
const cheerio = require("cheerio");
const cors = require("cors");
const app = express();

// Enable CORS for all origins
app.use(cors());

const link = {
  name: "sun doviz",
  address: "https://sun.portburda.com/widget_w_300.php",
};

const exchangeRates = [];
let lastUpdated;

axios
  .get(link.address)
  .then((response) => {
    const html = response.data;
    const $ = cheerio.load(html);

    // Find the update time row
    const updateRow = $("tr").filter((_, el) => {
      const text = $(el).text();
      return text.includes("Son Güncelleme");
    });

    // Extract the update time from the second column
    const updateCell = updateRow.find("td").eq(1);
    if (updateCell.length) {
      const rawUpdateText = updateCell.html();
      lastUpdated = rawUpdateText
        ? rawUpdateText
            .split("<br>")[0]
            .trim()
            .replace(/<font[^>]*>/g, "")
            .replace(/<\/font>/g, "")
        : "Unknown";
    } else {
      lastUpdated = "Unknown";
    }

    // Find all table rows and process currency data
    $("tr").each(function () {
      const columns = $(this).find("td");

      // Check if this row has exactly 3 columns (currency rows)
      if (columns.length === 3) {
        const firstColumnText = $(columns[0]).text().trim();

        // Skip rows that contain "Son Güncelleme" or other non-currency content
        if (
          firstColumnText.includes("Son Güncelleme") ||
          firstColumnText.includes("(392)") ||
          firstColumnText === "" ||
          !$(columns[1])
            .text()
            .trim()
            .match(/^\d+\.?\d*$/)
        ) {
          return; // Skip this row
        }

        // Extract currency code (USD, EUR, GBP, etc.)
        const currency = firstColumnText
          .replace(/\s+/g, " ")
          .trim()
          .split(" ")
          .pop();
        const buyRate = $(columns[1]).text().trim();
        const sellRate = $(columns[2]).text().trim();

        // Only add if we have valid numeric rates
        if (
          currency &&
          buyRate &&
          sellRate &&
          buyRate.match(/^\d+\.?\d*$/) &&
          sellRate.match(/^\d+\.?\d*$/)
        ) {
          exchangeRates.push({
            currency,
            buyRate,
            sellRate,
          });
        }
      }
    });

    console.log("Scraped exchange rates:", exchangeRates);
    console.log("Last updated:", lastUpdated);
  })
  .catch((error) => {
    console.error("Error scraping data:", error);
  });

app.get("/", (req, res) => {
  res.json(
    "Welcome to my exchange-rates API\n\nGo to \n /exchange-rates to see more \n"
  );
});

app.get("/exchange-rates", (req, res) => {
  res.json({ lastUpdated, rates: exchangeRates });
});

app.get("/exchange-rates/:currency", (req, res) => {
  const { currency } = req.params;
  const rate = exchangeRates.find(
    (item) => item.currency === currency.toUpperCase()
  );
  if (rate) {
    res.json({ lastUpdated, rate });
  } else {
    res.status(404).json({ message: `Currency ${currency} not found.` });
  }
});

app.listen(PORT, () => console.log(`server running on PORT ${PORT}`));
