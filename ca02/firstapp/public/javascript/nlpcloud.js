const NLPCloudClient = require("nlpcloud");

const client = new NLPCloudClient(
  "finetuned-gpt-neox-20b",
  process.env.api_key,
  true
);



const generateHTMLCode = async (prompt) => {
  try {
    const response = await client.textCorrection(prompt);
    return response.data.generated_code;
  } catch (error) {
    console.error(error.response.status);
    console.error(error.response.data.detail);
  }
};

const generateCorrection = async (prompt) => {
  try {
    console.log("generateCorrection");
    const response = await client.gsCorrection(prompt);
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error(error.response.status);
    console.error(error.response.data.detail);
  }
};

const generateBedtimeStory = async (prompt) => {
  try {
    console.log("generateBedtimeStory");
    const response = await client.bedtimeStory(prompt);
    console.log(response.data);
    return response.data;
  } catch (error) {
    console.error(error.response.status);
    console.error(error.response.data.detail);
  }
};

module.exports = {
  generateHTMLCode,
  generateCorrection,
  generateBedtimeStory,
};
