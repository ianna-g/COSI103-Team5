/**
 * clear the input fields for name and description
 */
const clearFields = () => {
  document.getElementById("nameBox").value = "";
  document.getElementById("descriptionBox").value = "";
};

/**
 * Checks valid input fields, catches/displays errors, calls callGPTAPI() if every input field is valid
 */
const generateHTML = () => {
  document.getElementById("errors").innerHTML = "";
  var errorMsg = "";
  var errors = false;
  const name = document.getElementById("nameBox").value;
  const des = document.getElementById("descriptionBox").value;

  if (name.length == 0) {
    errors = true;
    errorMsg += "<li>Name field is missing</li>";
  }
  if (des.length == 0) {
    errors = true;
    errorMsg += "<li>Description field is missing</li>";
  } else if (des.split(" ").length < 10) {
    errors = true;
    errorMsg += "<li>Provide a more specific description</li>";
  }

  if (errors == true) {
    document.getElementById("errors").innerHTML = "<ul>" + errorMsg + "</ul>";
  } else {
    document.getElementById("generate").disabled = true;
    callGPTAPI(name, des);
  }
};

/**
 *
 * @param {*} name
 * @param {*} des
 * makes a post request to /generate_html that generates a response and saves data to db
 */
const callGPTAPI = (name, des) => {
  $.ajax({
    url: "http://localhost:3000/minsung/generate_html",
    type: "post",
    data: {
      name: name,
      prompt: des,
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
