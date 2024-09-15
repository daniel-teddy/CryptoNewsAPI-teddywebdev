const express = require("express");
const {
  getAllRequests,
  getRequestById,
  createRequest,
  updateRequest,
  softDeleteRequest,
} = require("../controllers/requestsController");
const { requestSchema } = require("../validations/requestValidation");

const router = express.Router();

const validateRequest = async (req, res, next) => {
  try {
    await requestSchema.validate(req.body);
    next();
  } catch (err) {
    res.status(400).json({ error: err.errors });
  }
};

router.get("/all", getAllRequests);
router.get("/:id", getRequestById);
router.post("/create", validateRequest, createRequest);
router.put("/update/:id", validateRequest, updateRequest);
router.delete("/delete/:id", softDeleteRequest);

module.exports = router;
