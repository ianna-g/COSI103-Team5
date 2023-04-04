var express = require("express");
var router = express.Router();
const Transaction = require("../models/Transaction");

/* GET */
router.get("/", async (req, res, next) => {
  res.render("index", { title: "Transactions" });
  res.locals.transactions = await Transaction.find();
});

/* add the value in the body to the list associated to the key */
router.post("/add_transaction", async (req, res, next) => {
  const transaction = new Transaction({
    description: req.body.description,
    category: req.body.category,
    amount: req.body.amount,
    date: req.body.date,
  });
  await transaction.save();
  res.redirect("/");
});

module.exports = router;
