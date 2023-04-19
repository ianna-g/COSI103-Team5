var express = require("express");
var router = express.Router();
const Transaction = require("../models/Transaction");

/* GET home page. */
router.get("/", async (req, res, next) => {
  if (req.query.sortBy == "category") {
    res.locals.transactions = await Transaction.find({}).sort({ category: 1 });
  }else if (req.query.sortBy == 'amount') {
    transactions = await Transaction.find({userId:req.user._id}).sort({amount:1})
} else if (req.query.sortBy == 'description') {
  transactions = await Transaction.find({userId:req.user._id}).sort({description:1})
} else if (req.query.sortBy == 'date') {
  transactions = await Transaction.find({userId:req.user._id}).sort({date:1})
}
  else {
    res.locals.transactions = await Transaction.find();
  }
  res.render("index", { title: "Transactions" });
  // console.log(transactions);
});

module.exports = router;
