const PORT = process.env.PORT || 8000;
const express = require("express");
const app = express();

const museums = require("./museums");
const restaurants = require("./restaurants");
const hospitals = require("./hospital");
const hotels = require("./hotels");
const officials = require("./officials");
const pharmacies = require("./pharmacies");

const allPlaces = [
  ...museums,
  ...restaurants,
  ...hospitals,
  ...hotels,
  ...officials,
  ...pharmacies,
];

app.get("/", (req, res) => {
  res.json(
    "This is our custom places API for Cyprus to integrate with the expo app. This is hosted on render. Go to /places-data"
  );
});

app.get("/places-data/all", (req, res) => {
  res.json(allPlaces);
});

app.get("/places-data/museums", (req, res) => {
  res.json(museums);
});

app.get("/places-data/restaurants", (req, res) => {
  res.json(restaurants);
});

app.get("/places-data/hospitals", (req, res) => {
  res.json(hospitals);
});

app.get("/places-data/hotels", (req, res) => {
  res.json(hotels);
});

app.get("/places-data/officials", (req, res) => {
  res.json(officials);
});

app.get("/places-data/pharmacies", (req, res) => {
  res.json(pharmacies);
});

app.listen(PORT, () => console.log(`Server running on PORT ${PORT}`));
