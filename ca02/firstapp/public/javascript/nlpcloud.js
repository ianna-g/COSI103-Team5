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
    const response = await client.generation(prompt,
      50,
      [],
      true,
      '.',
      true,
      true,
      1,
      false,
      0,
      1,
      50,
      1,
      0.8,
      1,
      1,
      null,
      false);
    console.log(response.data);
    // res.redirect('/shaithea/bedtime_story')
    return response.data;
  } catch (error) {
    console.error(error.response.status);
    console.error(error.response.data.detail);
  }


  // client.generation('please use the following to create a sweet bedtime story: ' + prompt).then(function (response) {
  //   console.log(response.data);
  //   return response.data.generated_text;
  // })
  // .catch(function (err) {
  //   console.error(err.response.status);
  //   console.error(err.response.data.detail);
  // });

  // try {
  //   client.generation('please use the following to create a sweet bedtime story: ' + prompt)
  //   console.log("generateBedtimeStory");
  //   const response = await client.bedtimeStory(prompt);
  //   console.log(response.data);
  //   return response.data;
  // } catch (error) {
  //   console.error(error.response.status);
  //   console.error(error.response.data.detail);
  // }
};

module.exports = {
  generateHTMLCode,
  generateCorrection,
  generateBedtimeStory,
};
