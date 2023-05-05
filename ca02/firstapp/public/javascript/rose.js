/**
 * clear the input field
 */
const clearFields = () => {
    document.getElementById("inputBox").value = "";
  };
  
  /**
   * Checks valid input field, catches/displays errors, calls callGPTAPI() if every input field is valid
   */
  const generateTextCorrection = () => {
    document.getElementById("errors").innerHTML = "";
    var errorMsg = "";
    const input = document.getElementById("inputBox").value;
  
    if (input.length == 0) {
      errorMsg += "<li>Input field is missing</li>";
      document.getElementById("errors").innerHTML = "<ul>" + errorMsg + "</ul>";
    } else {
      document.getElementById("generate").disabled = true;
      callGPTAPI(input);
    }
  };
  
  /**
   *
   * @param {*} input
   * makes a post request to /generate_colors that generates a response and saves data to db
   */
  const callGPTAPI = (input) => {
    $.ajax({
      url: "http://localhost:3000/rose/generate_correction",
      type: "post",
      data: {
        name: input,
        prompt: input,
      },
      success: function (response) {
        // $("#errors").text(response);
        // location.reload();
        console.log("user data input!");
      },
      error: function (err) {
        $("#errors").text(err);
      },
    });
  };
  