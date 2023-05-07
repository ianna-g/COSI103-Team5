"use strict";
const mongoose = require("mongoose");
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var BibleVerseCodeSchema = Schema({
  book: String,
  chapter: String,
  verse: String,
  userId: { type: ObjectId, ref: "user" },
});

module.exports = mongoose.model("BibleVerse", BibleVerseCodeSchema);
