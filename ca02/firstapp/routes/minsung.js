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
  // console.log(pages);
  res.render("minsung_app", { pages: pages });
});

router.get("/about", (req, res, next) => {
  res.render("minsung_about");
});

router.post("/generate_html", async (req, res, next) => {
  const description = req.body.prompt;
  // console.log("name:", name);
  // console.log("des:", test);

  try {
    const html_code = await nlpCloud.generateHTMLCode(description);
    console.log(html_code);
    console.log("html_code ^^^^^^^");
    // const test = await chatgpt.getChatGPTResponse(req.body.prompt);
    // const chatResponse = chatgpt.testModule(name, test);
    const code = new HtmlCode({
      name: req.body.name,
      description: req.body.prompt,
      code: html_code, // need to find return string here !!!!!!!!!!!
      userId: req.user._id,
    });
    await code.save();
    res.redirect("/minsung");
  } catch (error) {
    console.log("ERROR: " + error);
  }
  // console.log(req.body.prompt);
  // res.send(JSON.stringify(req.body.prompt));
  // res.redirect("/minsung");
});

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
