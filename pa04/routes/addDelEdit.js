var express = require("express");
var router = express.Router();
const Transaction = require("../models/Transaction");

/* add the value in the body to the list associated to the key */
router.post("/add", async (req, res, next) => {
  const transaction = new Transaction({
    description: req.body.description,
    category: req.body.category,
    amount: req.body.amount,
    date: req.body.date,
  });
  await transaction.save();
  res.redirect("/");
});

/* remove transaction when trash icon is clicked */
router.get("/remove/:transactionId", async (req, res, next) => {
  await Transaction.deleteOne({ _id: req.params.transactionId });
  res.redirect("/");
});

/* redirect to edit page */
router.get("/edit/:transactionId", async (req, res, next) => {
  res.locals.transaction = await Transaction.findOne({
    _id: req.params.transactionId,
  });
  res.render("edit", { title: "Edit Transaction" });
});

router.post("/save/:transactionId", async (req, res, next) => {
  // var updateChanges = {
  //   $set: {
  //     description: req.body.description,
  //     category: req.body.category,
  //     amount: req.body.amount,
  //     date: req.body.date,
  //   },
  // };
  await Transaction.findOneAndUpdate(
    {
      _id: req.params.transactionId,
    },
    {
      $set: {
        description: req.body.description,
        category: req.body.category,
        amount: req.body.amount,
        date: req.body.date,
      },
    }
  );
  res.redirect("/");
});

module.exports = router;
