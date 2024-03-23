const PORT = process.env.PORT || 8000;
const express = require("express");
const axios = require("axios");
const cheerio = require("cheerio");
const app = express();

const newspapers = [
  {
    name: "cryptonews",
    address: "https://cryptonews.com/news/",
    base: "https://cryptonews.com",
  },
  {
    name: "cryptonews",
    address: "https://cryptonews.com/news/page/2/",
    base: "https://cryptonews.com",
  },
  {
    name: "cryptonews",
    address: "https://cryptonews.com/news/page/3/",
    base: "https://cryptonews.com",
  },
  {
    name: "cryptonews",
    address: "https://cryptonews.com/news/page/4/",
    base: "https://cryptonews.com",
  },
];

const productDef = [];
const productLinks = [
  {
    name: "pm1",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=3E4E9FDEECD7480DA8F56B4FA5C5F923",
    base: "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=3E4E9FDEECD7480DA8F56B4FA5C5F923",
  },
  {
    name: "pm2",
    address: "https://bzmhsp.page.link/z9BSW",
    base: "https://bzmhsp.page.link/z9BSW",
  },
];

const extractProductsDetails = (tbodyElement) => {
  const title = tbodyElement.find("h4").text();
  const imageUrl = tbodyElement.find("img").attr("src");

  productDef.push({
    title,
    imageUrl,
  });
};

const fetchProducts = async (productLink) => {
  try {
    const response = await axios.get(productLink.address);
    const html = response.data;
    const $ = cheerio.load(html);

    // Handle articles within <article> tags
    $("tbody", html).each(function () {
      const tbodyElement = $(this);
      extractProductsDetails(tbodyElement);
    });

    // Handle articles within <div class="news-one"> tags
    // $("div.news-one", html).each(function () {
    //   const articleElement = $(this);
    //   extractNewsOneDetails(articleElement, productLinks.base);
    // });
  } catch (error) {
    console.error(
      `Error fetching articles for ${productLink.name}: ${error.message}`
    );
  }
};

const fetchAllProducts = async () => {
  for (const productLink of productLinks) {
    await fetchProducts(productLink);
  }
};
const articles = [];

const fetchArticles = async (newspaper) => {
  try {
    const response = await axios.get(newspaper.address);
    const html = response.data;
    const $ = cheerio.load(html);

    // Handle articles within <article> tags
    $("article", html).each(function () {
      const articleElement = $(this);
      extractArticleDetails(articleElement, newspaper.base);
    });

    // Handle articles within <div class="news-one"> tags
    $("div.news-one", html).each(function () {
      const articleElement = $(this);
      extractNewsOneDetails(articleElement, newspaper.base);
    });
  } catch (error) {
    console.error(
      `Error fetching articles for ${newspaper.name}: ${error.message}`
    );
  }
};

const extractArticleDetails = (articleElement, base) => {
  const title = articleElement.find("a.article__title").text();
  const url = articleElement.find("a.article__title").attr("href");
  const imageUrl = articleElement.find("img.img-fluid").attr("src");
  const category = articleElement.find("a.article__badge--md").text().trim();
  const date = articleElement.find(".article__badge-date").attr("data-utctime");
  const shortDescription = articleElement
    .find(".short-description")
    .text()
    .trim();

  articles.push({
    title,
    url: url,
    imageUrl,
    category,
    date,
    shortDescription,
    source: newspapers[0].name, // Assuming there is only one newspaper in the array
  });
};

const extractNewsOneDetails = (articleElement, base) => {
  const title = articleElement.find("div.news-one-title a").text();
  const url = articleElement.find("a").attr("href");
  const imageUrl = articleElement.find("img").attr("src");
  const category = articleElement.find("a.news-one-category").text().trim();
  const date = articleElement.find(".article__badge-date").attr("data-utctime");

  articles.push({
    title,
    url: url,
    imageUrl,
    category,
    date,
    shortDescription: "", // No short description in the news-one structure
    source: newspapers[0].name, // Assuming there is only one newspaper in the array
  });
};

const fetchAllArticles = async () => {
  for (const newspaper of newspapers) {
    await fetchArticles(newspaper);
  }
};

const events = [
  {
    eventId: 1,
    category: "category",
    eventLocalAddress: "local address",
    eventName: "Orange Festival",
    Description:
      "Since 1977, this event held by Guzelyurt Municipality, has been the venue for a festival that originally celebrated the orange harvest.",
    date_range: {
      start_date: "2024-06-27",
      end_date: "2024-07-10",
    },
    image:
      "https://www.visitncy.com/wp-content/uploads/2020/02/Orange-Festival-9.jpg",
    location: {
      link: "https://goo.gl/maps/BiFJydpqabtS4iie8",
      local_range: {
        latitude: "2024-09-05",
        longitude: "2024-09-06",
      },
    },
    added_by_user: 1,
  },
  {
    eventId: 2,
    category: "category",
    eventLocalAddress: "local address",
    eventName: "Tatlisu Carob Festival",
    Description:
      "This annual festival held by the Tatlisu Municipality contributes to the promotion of the region and the continuation of carob and molasses production.",
    date_range: {
      start_date: "2024-09-05",
      end_date: "2024-09-06",
    },
    image:
      "https://www.visitncy.com/wp-content/uploads/2020/02/Orange-Festival-9.jpg",
    location: {
      link: "https://goo.gl/maps/gqCneKW9RvNaEkGQ8",
      local_range: {
        latitude: "2024-09-05",
        longitude: "2024-09-06",
      },
    },
    added_by_user: 2,
  },
  {
    eventId: 3,
    category: "category",
    eventLocalAddress: "local address",
    eventName: "Eco Day Fest",
    Description:
      "North Cyprus is a prime spot for due to its unspoilt nature and prominence local life, and a destination that truly takes you far away from the hum of fast-paced western culture.",
    date_range: {
      start_date: "2024-10-08",
      end_date: "2024-10-11",
    },
    image:
      "https://www.visitncy.com/wp-content/uploads/2020/02/join-ecotourismfest.jpg",
    location: {
      link: "https://goo.gl/maps/iCSBe1GNixhoojqt5",
      local_range: {
        latitude: "2024-09-05",
        longitude: "2024-09-06",
      },
    },
    added_by_user: 3,
  },
  {
    eventId: 4,
    category: "category",
    eventLocalAddress: "local address",
    eventName: "Kite Festival",
    Description:
      "In April, North Cyprus celebrates the Kite Festival, where hundreds of kites take to the sky. It is a colourful event that is popular with both locals and tourists.",
    date_range: {
      start_date: "2024-04-20",
      end_date: "2024-04-28",
    },
    image:
      "https://www.cyprusparadise.com/media/17494/kite-festival-north-cyprus.jpg",
    location: {
      link: "https://bit.ly/43lB37t",
      local_range: {
        latitude: "2024-09-05",
        longitude: "2024-09-06",
      },
    },
    added_by_user: 4,
  },
  {
    eventId: 5,
    category: "category",
    eventLocalAddress: "local address",
    eventName: "2nd International Student Congress",
    Description: "Migration and Health Perspectives",
    date_range: {
      start_date: "2024-04-25",
      end_date: "2024-04-27",
    },
    image:
      "https://neu.edu.tr/wp-content/uploads/2024/02/07/2._Uluslararasi_Ogrenci_Kongresi_eng_kopya.jpg?ver=c4c9a6e73985515e376cb8aeb29bb6f0",
    location: {
      link: "https://bit.ly/3v8Ny9O",
      local_range: {
        latitude: "2024-09-05",
        longitude: "2024-09-06",
      },
    },
    added_by_user: 5,
  },
];
app.get("/", (req, res) => {
  res.json(
    "Welcome to my Crypto News API\n\nGo to \n /news to see news articles \n"
  );
});

app.get("/products", async (req, res) => {
  await fetchAllProducts();
  res.json(productDef);
});
app.get("/news", async (req, res) => {
  await fetchAllArticles();
  res.json(articles);
});
app.get("/events", async (req, res) => {
  res.json(events);
});

app.listen(PORT, () => console.log(`Server running on PORT ${PORT}`));
