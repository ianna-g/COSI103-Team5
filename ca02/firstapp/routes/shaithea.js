const express = require('express');
const router = express.Router();

const nlpCloud = require("../public/javascript/nlpcloud.js");
const { isLoggedIn } = require("./pwauth.js");
const PrevQueries = require("../models/PrevQueries.js");

router.get("/", isLoggedIn, async (req, res, next) => {
    var prevQueries = [];
    try {
      prevQueries = await PrevQueries.find({ userId: req.user._id });
      console.log("done finding previous documents");
    } catch (error) {
      console.log("there was an error fetching all previous queries:", error);
    }
    // console.log(pages);
    res.render("shaithea_app", { prevQueries: prevQueries });
  });

  router.get("/about", (req, res, next) => {
    res.render("shaithea_about");
  });

  router.post("/generate_bedtime_story", async (req, res, next) => {
    const request = req.body.prompt;
  
    try {
      console.log("trying");
      const story = await nlpCloud.generateBedtimeStory(request);
      const code = new PrevQueries({
        name: req.body.name,
        input: req.body.prompt,
        output: story.story,
        userId: req.user._id,
      });
      await code.save();
      res.redirect("/shaithea");
    } catch (error) {
      console.log("ERROR: " + error);
    }
  });

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
      console.log("inside /shaithea/remove/:queryId")
      await PrevQueries.deleteOne({_id:req.params.queryId});
      res.redirect('/shaithea')
});

module.exports = router;