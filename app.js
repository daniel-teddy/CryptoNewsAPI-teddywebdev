const express = require("express");
const requestRoutes = require("./routes/requestRoutes");

const app = express();
app.use(express.json());

app.use("/requests", requestRoutes);

const PORT = process.env.PORT || 4889;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
