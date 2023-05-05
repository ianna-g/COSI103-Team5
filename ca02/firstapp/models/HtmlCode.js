"use strict";
const mongoose = require("mongoose");
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var HtmlCodeSchema = Schema({
  name: String,
  description: String,
  code: String,
  userId: { type: ObjectId, ref: "user" },
});


module.exports = mongoose.model("HtmlCode", HtmlCodeSchema);
