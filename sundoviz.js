const PORT = process.env.PORT || 8000;
const express = require("express");
const axios = require("axios");
const cheerio = require("cheerio");
const app = express();

const link = {
  name: "sun doviz",
  address: "https://sun.portburda.com/widget_w_300.php",
};

const exchangeRates = [];
let lastUpdated;

axios.get(link.address).then((response) => {
  const html = response.data;
  const $ = cheerio.load(html);
  const updateRow = $("tr").filter((_, el) => {
    const text = $(el).text();
    return text.includes("Son Güncelleme");
  });

  const rawUpdateText = updateRow.find("td[colspan='2'] font").html();
  lastUpdated = rawUpdateText
    ? rawUpdateText.split("<br>")[0].trim()
    : "Unknown";

  $("tbody tr").each(function () {
    const columns = $(this).find("td");
    if (columns.length === 3) {
      const currency = $(columns[0]).text().trim();
      const buyRate = $(columns[1]).text().trim();
      const sellRate = $(columns[2]).text().trim();

      exchangeRates.push({
        currency,
        buyRate,
        sellRate,
      });
    }
  });
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
