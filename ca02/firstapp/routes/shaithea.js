const express = require('express');
const router = express.Router();

const nlpCloud = require("../public/javascript/nlpcloud.js");
const { isLoggedIn } = require("./pwauth.js");
const BedtimeStory = require("../models/BedtimeStory.js");

/**
 * GET: root for shaithea's app
 * Query all BedtimeStory documents from db and send to ejs page
 */
router.get("/", isLoggedIn, async (req, res, next) => {
  var pages = [];
  try {
    pages = await BedtimeStory.find({ userId: req.user._id });
    console.log("done finding bedtime story code documents");
  } catch (error) {
    console.log("there was an error fetching all bedtime story webpages:", error);
  }
  // console.log(pages);
  res.render("shaitea_app", { pages: pages });
});

/**
 * GET: load the about page for shaithea's webapp
 */
  router.get("/about", (req, res, next) => {
    res.render("shaithea_about");
  });

/**
 * POST: call nlpCloud api and generate BedtimeStory code using content provided by the user
 * After a response is received, save the data to the database in the form of BedtimeStory document
 */
  router.post("/generate_bedtime_story", async (req, res, next) => {
    const content = req.body.prompt;
  
    try {
      console.log("trying");
      const story = await nlpCloud.generateBedtimeStory(content);
      const code = new BedtimeStory({
        name: req.body.name,
        content: req.body.prompt,
        story: story,
        userId: req.user._id,
      });
      await code.save();
      res.redirect("/shaithea");
    } catch (error) {
      console.log("ERROR: " + error);
    }
  });

/**
 * GET: Show a saved user page that was selected by finding the bedtime story in the Mongodb collection
 * Then render the bedtime_story_demo_page that loads the story
 */
router.get("/demo_page/:bedtimeStorypageId", isLoggedIn, async (req, res, next) => {
  const id = req.params.bedtimeStorypageId;
  try {
    const story = await BedtimeStory.findById(id);
    res.render("bedtime_story_demo_page", { story: story.story });
  } catch (error) {
    console.log("There was an error finding document by id", error);
  }
});

module.exports = router;