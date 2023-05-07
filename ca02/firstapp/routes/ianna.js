const express = require("express");
const router = express.Router();

const nlpCloud = require("../public/javascript/nlpcloud.js");
const { isLoggedIn } = require("./pwauth.js");
const BibleVerse = require("../models/BibleVerse.js");

router.get("/", isLoggedIn, async (req, res, next) => {
    var BibleVerse = [];
    try {
        BibleVerse = await BibleVerse.find({ userId: req.user._id });
      console.log("done finding verses");
    } catch (error) {
      console.log("there was an error fetching all BibleVerse webpages:", error);
    }

    res.render("ianna_app", { BibleVerse: BibleVerse });
  });

  router.get("/about", (req, res, next) => {
    res.render("ianna_about");
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
      const code = new BibleVerse({
        name: req.body.name,
        input: req.body.prompt,
        output: correction.correction,
        userId: req.user._id,
      });
      await code.save();
      res.redirect("/ianna");
    } catch (error) {
      console.log("ERROR: " + error);
    }
  });
  
  /**
   * GET: Show a saved user bible verse that was selected by finding the bible verse in the Mongodb collection
   * Then render the before_and_after that shows the prompt then how it was corrected
   */
  router.get("/before_and_after/:BibleVersePageId", isLoggedIn, async (req, res, next) => {
    const id = req.params.BibleVersePageId;
    try {
      const bible = await BibleVersePage.findById(id);
      res.render("before_and_after", { input: bible.input, output: bible.output });
    } catch (error) {
      console.log("There was an error finding document by id", error);
    }
  });
  
  router.get('/remove/:BibleVersePageId',
    isLoggedIn,
    async (req, res, next) => {
        console.log("inside /ianna/remove/:BibleVersePageId")
        await BibleVersePage.deleteOne({_id:req.params.BibleVersePageId});
        res.redirect('/ianna')
  });
  
  module.exports = router;