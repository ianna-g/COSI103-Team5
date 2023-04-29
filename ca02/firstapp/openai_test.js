const { Configuration, OpenAIApi } = require("openai");

const config = new Configuration({
  apiKey: "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",
});

const openai = new OpenAIApi(config);

const runPrompt = async () => {
  const prompt = "Tell me a joke about a cat eating pasta.";

  const response = await openai.createCompletion({
    model: "text-davinci-003",
    prompt: prompt,
    max_tokens: 2048,
    temperature: 1,
  });

  console.log(response.data);
};

runPrompt();
