const express = require("express");
const router = express.Router();
const nlpCloud = require("../public/javascript/nlpcloud.js");
const HtmlCode = require("../models/HtmlCode.js");
const { isLoggedIn } = require("./pwauth.js");

/**
 * GET: root for minsung's app
 * Query all HtmlCode documents from db and send to ejs page
 */
router.get("/", isLoggedIn, async (req, res, next) => {
  var pages = [];
  try {
    pages = await HtmlCode.find({ userId: req.user._id });
    console.log("done finding html code documents");
  } catch (error) {
    console.log("there was an error fetching all HTMLcode webpages:", error);
  }
  // console.log(pages);
  res.render("minsung_app", { pages: pages });
});

/**
 * GET: load the about page for minsung's webapp
 */
router.get("/about", (req, res, next) => {
  res.render("minsung_about");
});

/**
 * POST: call nlpCloud api and generate HTML code using description given by the user
 * After a response is received, save the data to the database in the form of HtmlCode document
 */
router.post("/generate_html", async (req, res, next) => {
  const description = req.body.prompt;

  try {
    const html_code = await nlpCloud.generateHTMLCode(description);
    console.log(html_code);
    const code = new HtmlCode({
      name: req.body.name,
      description: req.body.prompt,
      code: html_code,
      userId: req.user._id,
    });
    await code.save();
    res.redirect("/minsung");
  } catch (error) {
    console.log("ERROR: " + error);
  }
});

/**
 * GET: Show a saved user page that was selected by finding the html in the Mongodb collection
 * Then render the html_demo_page that loads the html
 */
router.get("/demo_page/:htmlpageId", isLoggedIn, async (req, res, next) => {
  const id = req.params.htmlpageId;
  try {
    const code = await HtmlCode.findById(id);
    res.render("html_demo_page", { code: code.code });
  } catch (error) {
    console.log("There was an error finding document by id", error);
  }
});

module.exports = router;
