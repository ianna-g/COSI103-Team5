const fetch = require("node-fetch");

const { Configuration, OpenAIApi } = require("openai");

const getChatGPTResponse = async (prompt) => {
  const configuration = new Configuration({
    apiKey: process.env.api_key,
  });
  const openai = new OpenAIApi(configuration);

  console.log("###########################");
  // const apiKey = process.env.api_key;
  // const modified_prompt = prompt;

  try {
    const response = await openai.createCompletion({
      model: "text-davinci-003",
      prompt: prompt,
      temperature: 0,
      max_tokens: 150,
      top_p: 1,
      frequency_penalty: 0.5,
      presence_penalty: 0,
      stop: "\n",
    });
    return response;
  } catch (err) {
    console.log("there was an openai API error", err);
    return "error";
  }
};

const testModule = (name, des) => {
  return "working: " + name + ", " + des;
};

module.exports = {
  getChatGPTResponse,
  testModule,
};
