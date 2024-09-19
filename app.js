const express = require("express");
const cors = require("cors");
const requestRoutes = require("./routes/requestRoutes");

const app = express();
app.use(cors()); // Allow all origins
app.use(express.json());

app.use("/requests", requestRoutes);

const PORT = process.env.PORT || 4889;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
