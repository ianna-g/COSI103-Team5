/**
 * clear the input fields for the content of the bedtime story
 */
const clearFields = () => {
    document.getElementById("contentBox").value = "";
  };
  
/**
* Checks valid input field, catches/displays errors, calls callGPTAPI() if every input field is valid
*/
const generateStory = () => {
    document.getElementById("errors").innerHTML = "";
    var errorMsg = "";
    var errors = false;

    const content = document.getElementById("contentBox").value;
  
    if (content.length == 0) {
      errors = true;
      errorMsg += "<li>Content field of your story is missing!</li>";
      document.getElementById("errors").innerHTML = "<ul>" + errorMsg + "</ul>";
    } else {
      document.getElementById("generate").disabled = true;
      callGPTAPI(content);
    }
  };
  
/**
*
* @param {*} input
* makes a post request that generates a response and saves data to db
*/
const callGPTAPI = (content) => {
    $.ajax({
    url: "http://localhost:3000/shaithea/generate_bedtime_story",
    type: "post",
    data: {
        name: content,
        prompt: content,
    },
    success: function (response) {
        // $("#errors").text(response);
        location.reload();
        console.log("user data input!");
    },
    error: function (err) {
        $("#errors").text(err);
    },
    });
};
  