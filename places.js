const PORT = 8000;
const axios = require("axios");
const cheerio = require("cheerio");
const express = require("express");
const app = express();

const url =
  "https://www.google.com/maps/search/Restaurants/@35.1082963,32.6466555,8.76z/data=!4m2!2m1!6e5?entry=ttu";

app.get("/", function (req, res) {
  res.json("This is my webscraper");
});

app.get("/results", (req, res) => {
  axios(url)
    .then((response) => {
      const html = response.data;
      const $ = cheerio.load(html);

      // Select the div with class 'w6VYqd'
      const divsWithClass = $(".w6VYqd");

      res.json(divsWithClass.html());
    })
    .catch((err) => console.log(err));
});

app.listen(PORT, () => console.log(`server running on PORT ${PORT}`));
