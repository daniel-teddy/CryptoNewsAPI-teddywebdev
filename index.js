const PORT = process.env.PORT || 8000;
const express = require("express");
const axios = require("axios");
const cheerio = require("cheerio");
const app = express();

const productsLinks = [
  {
    name: "ADAPTÖRLER VE ŞARJ SETLERİ",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=5399AFE1548A4E309941F271D01425BD",
  },
  {
    name: "AKILLI SAATLER",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=4F3D01AD55094459886880E7A4F5D7C5",
  },
  {
    name: "ARAÇ İÇİ AKSESUAR",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=FECF08C3161C44C1ACA1DE254C69A6A0",
  },
  {
    name: "BİLGİSAYAR AKSESUARLARI",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=A324933E6AF44D91B1BFB9896831E646",
  },
  {
    name: "BLUETOOTH HOPARLÖRLER",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=25DB719E787A46F781F8B077788DBEE3",
  },
  {
    name: "CAR CHARGER AND MODULATOR",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=8C68090249C54918B665D06FFB110C5E",
  },
  {
    name: "ÇOĞALTICI",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=0AB0A41399254B0AAE5A86226A596BC8",
  },
  {
    name: "KABLOLAR",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=1B434312A2974274A405FCC3E875BA92",
  },
  {
    name: "KAMERA",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=3E4E9FDEECD7480DA8F56B4FA5C5F923",
  },
  {
    name: "KULAKLIKLAR",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=BBE4012DD5E948AFB7C1C42E8EBCB35C",
  },
  {
    name: "OYUNCU SETLERİ",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=E1FD3F20C47441759B227C3BEE3DDF9D",
  },
  {
    name: "POWERBANK",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=23264E1A600147F6A6A355ECAC5827FF",
  },
  {
    name: "RİNG LİGHTS",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=557A9679A89D48D3A3AE4B85F789966A",
  },
  {
    name: "SAAT KORDONLARI",
    address:
      "https://bizimhesap.com/web/ngn/ext/catalogdisplay?rc=1&guid=1AB45CA33BC542FCA8D13B565B70A3CD",
  },
];

const articles = [];

productsLinks.forEach((productLink) => {
  axios.get(productLink.address).then((response) => {
    const html = response.data;
    const $ = cheerio.load(html);

    $("tr", html).each(function () {
      const title = $(this).find("h4").first().text().trim();
      const imageUrl = $(this)
        .find("a")
        .attr("onclick")
        ?.match(/setSliderClientImages\('(.*?)'\)/)?.[1];
      const price = $(this).find("td.text-center strong").text().trim();

      if (title && imageUrl && price) {
        articles.push({
          title,
          imageUrl,
          price,
          category: productLink.name,
        });
      }
    });
    // console.log(articles);
  });
});

app.get("/", (req, res) => {
  res.json(
    "Welcome to my products API\n\nGo to \n /products to see products articles \n"
  );
});

app.get("/products", (req, res) => {
  res.json(articles);
});

app.listen(PORT, () => console.log(`server running on PORT ${PORT}`));
