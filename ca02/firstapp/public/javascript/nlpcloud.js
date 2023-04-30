const NLPCloudClient = require("nlpcloud");

const client = new NLPCloudClient(
  "finetuned-gpt-neox-20b",
  process.env.api_key,
  true
);

const generateHTMLCode = async (prompt) => {
  try {
    const response = await client.codeGeneration(
      `Generate html code using the following description of a web page: ` +
        prompt +
        ` 
    Make sure that the code can be pasted onto a div tag, add words, and assume that there are no external files.`
    );
    return response.data.generated_code;
  } catch (error) {
    console.error(error.response.status);
    console.error(error.response.data.detail);
  }
};

module.exports = {
  generateHTMLCode,
};
