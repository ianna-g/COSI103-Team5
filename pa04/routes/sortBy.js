// the following sort by methods were created by Ianna and Shaithea
// they are used to sort the data by the different fields in our database
var express = require("express");
var router = express.Router();
const Transaction = require("../models/Transaction");

router.get("/", async (req, res, next) => {

    // Sort By Category:
    // This method returns to the same page except the data is 
    // sorted alphabetically by its category column. 
    if (req.query.sortBy == 'category') {
        sortedTransactions = await Transaction.find({userId:req.user._id}).sort({category:1})
    }

    // Sort By Amount:
    // This method returns to the same page except the data is 
    // sorted in ascending order by its amount column. 

    else if (req.query.sortBy == 'amount') {
        transactions = await Transaction.find({userId:req.user._id}).sort({amount:1})
    }

    // Sort By Description:
    // This method returns to the same page except the data is 
    // sorted alphabetically by its description column. 

    else if (req.query.sortBy == 'description') {
        transactions = await Transaction.find({userId:req.user._id}).sort({description:1})
    }


    // Sort By Date:
    // This method returns to the same page except the data is 
    // sorted from the most recent date to the oldest date using its date column. 

    else if (req.query.sortBy == 'date') {
        transactions = await Transaction.find({userId:req.user._id}).sort({date:1})
    }

    else {
    }
});