const express = require("express");
const router = express.Router();
const nlpCloud = require("../public/javascript/nlpcloud.js");
const { isLoggedIn } = require("./pwauth.js");
const PrevQueries = require("../models/PrevQueries.js");

/**
 * GET: root for Rose's app
 * Query all PrevQueries documents from db and send to ejs page
 */
router.get("/", isLoggedIn, async (req, res, next) => {
  var prevQueries = [];
  try {
    prevQueries = await PrevQueries.find({ userId: req.user._id });
    console.log("done finding previous documents");
  } catch (error) {
    console.log("there was an error fetching all previous queries:", error);
  }
  // console.log(pages);
  res.render("rose_app", { prevQueries: prevQueries });
});

/**
 * GET: load the about page for Rose's webapp
 */
router.get("/about", (req, res, next) => {
  res.render("rose_about");
});

/**
 * POST: call nlpCloud api and generate HTML code using description given by the user
 * After a response is received, save the data to the database in the form of HtmlCode document
 */
router.post("/generate_correction", async (req, res, next) => {
  const request = req.body.prompt;

  try {
    console.log("trying");
    const correction = await nlpCloud.generateCorrection(request);
    const code = new PrevQueries({
      name: req.body.name,
      input: req.body.prompt,
      output: correction.correction,
      userId: req.user._id,
    });
    await code.save();
    res.redirect("/rose");
  } catch (error) {
    console.log("ERROR: " + error);
  }
});

/**
 * GET: Show a saved user query that was selected by finding the query in the Mongodb collection
 * Then render the before_and_after that shows the prompt then how it was corrected
 */
router.get("/before_and_after/:queryId", isLoggedIn, async (req, res, next) => {
  const id = req.params.queryId;
  try {
    const query = await PrevQueries.findById(id);
    res.render("before_and_after", { input: query.input, output: query.output });
  } catch (error) {
    console.log("There was an error finding document by id", error);
  }
});

router.get('/remove/:queryId',
  isLoggedIn,
  async (req, res, next) => {
      console.log("inside /rose/remove/:queryId")
      await PrevQueries.deleteOne({_id:req.params.queryId});
      res.redirect('/rose')
});

module.exports = router;