// the following sort by method was created by Rose
// they are used to group the data by category and show the total amount per category
var express = require("express");
var router = express.Router();
const Transaction = require("../models/Transaction");

// The page should show up when at the /groupBy page
router.get("/", async (req, res, next) => {
    let results = await Transaction.aggregate(
        [
            {$group:{
                _id:'$category',
                amount:{$sum:'$amount'}
            }
            }
        ]
    )
    res.render('groupBy',{ title: "Transactions Summed by Category", results })
});
module.exports = router;
