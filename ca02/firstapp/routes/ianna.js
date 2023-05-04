const express = require("express");
const router = express.Router();
const nlpCloud = require("../public/javascript/nlpcloud.js");
const HtmlCode = require("../models/HtmlCode.js");
const { isLoggedIn } = require("./pwauth.js");

router.get("/", isLoggedIn, async (req, res, next) => {
    var pages = [];
    try {
      pages = await HtmlCode.find({ userId: req.user._id });
      console.log("done finding html code documents");
    } catch (error) {
      console.log("there was an error fetching all HTMLcode webpages:", error);
    }

    res.render("ianna_app", { pages: pages });
  });

  router.get("/about", (req, res, next) => {
    res.render("ianna_about");
  });