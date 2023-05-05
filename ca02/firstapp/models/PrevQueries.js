"use strict";
const mongoose = require("mongoose");
const Schema = mongoose.Schema;
const ObjectId = mongoose.Schema.Types.ObjectId;

var PrevQueriesSchema = Schema({
  name: String,
  input: String,
  output: String,
  userId: { type: ObjectId, ref: "user" },
});


module.exports = mongoose.model("PrevQuesriesSchema", PrevQueriesSchema);
