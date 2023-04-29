const express = require("express");
const router = express.Router();
const ToDoItem = require("../models/ToDoItem");
const axios = require("axios");

router.get("/", (req, res, next) => {
  res.render("minsung_app");
});

router.get("/about", (req, res, next) => {
  res.render("minsung_about");
});

module.exports = router;
