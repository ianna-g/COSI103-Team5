"use strict";
const mongoose = require("mongoose");
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var BedtimeStoryCodeSchema = Schema({
  name: String,
  content: String,
  story: String,
  userId: { type: ObjectId, ref: "user" },
});

module.exports = mongoose.model("BedtimeStory", BedtimeStoryCodeSchema);
