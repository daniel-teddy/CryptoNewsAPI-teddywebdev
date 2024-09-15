const fs = require("fs");
const path = require("path");
const { v4: uuidv4 } = require("uuid");

const DB_FILE = path.join(__dirname, "../databases/requests.json");

const loadData = () => {
  try {
    const data = fs.readFileSync(DB_FILE, "utf-8");
    return JSON.parse(data);
  } catch (error) {
    console.error("Error reading data from file:", error.message);
    throw new Error("Could not load data from database file.");
  }
};

const saveData = (data) => {
  try {
    fs.writeFileSync(DB_FILE, JSON.stringify(data, null, 4));
  } catch (error) {
    console.error("Error saving data to file:", error.message);
    throw new Error("Could not save data to database file.");
  }
};

exports.getAllRequests = (req, res) => {
  try {
    const data = loadData();
    res.json(data.requests);
  } catch (error) {
    console.error("Error in getAllRequests:", error.message);
    res.status(500).json({ error: "Failed to load data" });
  }
};

exports.getRequestById = (req, res) => {
  const { id } = req.params;
  try {
    const data = loadData();
    const request = data.requests.find(
      (item) => item.id === id && !item.deleted
    );
    if (request) {
      res.json(request);
    } else {
      res.status(404).json({ error: "Request not found" });
    }
  } catch (error) {
    console.error("Error in getRequestById:", error.message);
    res.status(500).json({ error: "Failed to load data" });
  }
};

exports.createRequest = (req, res) => {
  const newRequest = req.body;
  newRequest.id = uuidv4();
  newRequest.deleted = false;

  try {
    const data = loadData();
    data.requests.push(newRequest);
    saveData(data);
    res.status(201).json(newRequest);
  } catch (error) {
    console.error("Error in createRequest:", error.message);
    res.status(500).json({ error: "Failed to save data" });
  }
};

exports.updateRequest = (req, res) => {
  const { id } = req.params;
  const updatedRequest = req.body;
  try {
    const data = loadData();
    const index = data.requests.findIndex(
      (item) => item.id === id && !item.deleted
    );
    if (index !== -1) {
      data.requests[index] = { ...data.requests[index], ...updatedRequest };
      saveData(data);
      res.json(data.requests[index]);
    } else {
      res.status(404).json({ error: "Request not found" });
    }
  } catch (error) {
    console.error("Error in updateRequest:", error.message);
    res.status(500).json({ error: "Failed to save data" });
  }
};

exports.softDeleteRequest = (req, res) => {
  const { id } = req.params;
  try {
    const data = loadData();
    const index = data.requests.findIndex(
      (item) => item.id === id && !item.deleted
    );
    if (index !== -1) {
      data.requests[index].deleted = true;
      saveData(data);
      res.json({ message: "Request soft deleted" });
    } else {
      res.status(404).json({ error: "Request not found" });
    }
  } catch (error) {
    console.error("Error in softDeleteRequest:", error.message);
    res.status(500).json({ error: "Failed to save data" });
  }
};
