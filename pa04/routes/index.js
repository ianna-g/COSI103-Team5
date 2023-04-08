var express = require("express");
var router = express.Router();
const Transaction = require("../models/Transaction");

/* GET home page. */
router.get("/", async (req, res, next) => {
  res.locals.transactions = await Transaction.find();
  console.log(await Transaction.find());
  res.render("index", { title: "Transactions" });
});

module.exports = router;
