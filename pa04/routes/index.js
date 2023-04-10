var express = require("express");
var router = express.Router();
const Transaction = require("../models/Transaction");

/* GET home page. */
router.get("/", async (req, res, next) => {
  if (req.query.sortBy == "category") {
    res.locals.transactions = await Transaction.find({}).sort({ category: 1 });
  } else {
    res.locals.transactions = await Transaction.find();
  }
  res.render("index", { title: "Transactions" });
  // console.log(transactions);
});

module.exports = router;
