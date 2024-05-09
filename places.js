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

// Endpoint to return all places in a single array
app.get("/places-data/all", async (req, res) => {
  try {
    res.json(allPlaces);
  } catch (err) {
    console.error("Error sending all places data:", err);
    res.status(500).json({ error: "Internal server error" });
  }
});

app.get("/places-data/museums", async (req, res) => {
  try {
    res.json(museums);
  } catch (err) {
    console.error("Error sending museums data:", err);
    res.status(500).json({ error: "Internal server error" });
  }
});

app.get("/places-data/restaurants", async (req, res) => {
  try {
    res.json(restaurants);
  } catch (err) {
    console.error("Error sending restaurants data:", err);
    res.status(500).json({ error: "Internal server error" });
  }
});

app.get("/places-data/hospitals", async (req, res) => {
  try {
    res.json(hospitals);
  } catch (err) {
    console.error("Error sending hospitals data:", err);
    res.status(500).json({ error: "Internal server error" });
  }
});

app.get("/places-data/hotels", async (req, res) => {
  try {
    res.json(hotels);
  } catch (err) {
    console.error("Error sending hotels data:", err);
    res.status(500).json({ error: "Internal server error" });
  }
});

app.get("/places-data/officials", async (req, res) => {
  try {
    res.json(officials);
  } catch (err) {
    console.error("Error sending officials data:", err);
    res.status(500).json({ error: "Internal server error" });
  }
});

app.get("/places-data/pharmacies", async (req, res) => {
  try {
    res.json(pharmacies);
  } catch (err) {
    console.error("Error sending pharmacies data:", err);
    res.status(500).json({ error: "Internal server error" });
  }
});

app.listen(PORT, () => console.log(`Server running on PORT ${PORT}`));
