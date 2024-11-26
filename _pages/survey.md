---
layout: default
permalink: /survey/
title: Hint Evaluation Survey
---
<head>
  <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css" rel="stylesheet">
  <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/material-design-lite/material.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/material-design-lite/material.min.js"></script>
  <style>
    body {
      font-family: "Roboto", "Arial", sans-serif;
      margin: 20px;
    }
    .card {
      margin: 20px 0;
      padding: 20px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
      border-radius: 8px;
      background-color: #ffffff;
    }
    .btn {
      margin-top: 20px;
      text-align: center;
    }
    table {
      width: 100%;
      border-collapse: collapse;
      margin: 20px 0;
    }
    th, td {
      text-align: left;
      padding: 10px;
      border: 1px solid #ddd;
    }
    th {
      background-color: #f5f5f5;
    }
    .survey-question {
      margin-bottom: 15px;
    }
    .likert-scale {
      display: flex;
      justify-content: space-between;
      width: 100%;
      max-width: 400px;
    }
    .center {
      text-align: center;
    }
  </style>
</head>
<body>

<div class="card">
  <h2 class="center">Hint Evaluation Survey</h2>
  <div id="data-container">
    <!-- Evaluation Set Will Be Rendered Here -->
  </div>
  <div id="survey-container">
    <!-- Evaluation Survey Will Be Rendered Here -->
  </div>
  <div class="btn center">
    <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--colored" onclick="nextSet()">Evaluate Next Set</button>
    <button class="mdl-button mdl-js-button mdl-button--raised mdl-button--accent" onclick="submitSurvey()">Submit Response</button>
  </div>
</div>

<script>
  // Sample JSON data
  const data = [
    {
      "student_code": "Student Code Example 1",
      "goal_code": "Goal Code Example 1",
      "edit_script": "Edit Script Example 1",
      "hints_level1": "Hints Level 1 Example 1",
      "hints_level2": "Hints Level 2 Example 1",
      "hints_level3": "Hints Level 3 Example 1"
    },
    {
      "student_code": "Student Code Example 2",
      "goal_code": "Goal Code Example 2",
      "edit_script": "Edit Script Example 2",
      "hints_level1": "Hints Level 1 Example 2",
      "hints_level2": "Hints Level 2 Example 2",
      "hints_level3": "Hints Level 3 Example 2"
    }
    // Add more sets as needed
  ];
 
  const sections =  [
    {
        "title":"Clarity and Comprehension",
        "questions": [
            "The hints are clearly written and easy to understand.",
            "The hints are clearly written and easy to understand.",
            "The hints are clearly written and easy to understand.",
            "The hints use consistent and appropriate terminology for the audience.",
            "The hints use consistent and appropriate terminology for the audience.",
            "The hints use consistent and appropriate terminology for the audience."
        ]
    },
    {
        "title": "Relevance to the Task",
        "questions": [
            "The hints align with the problem and task requirements.",
            "The hints align with the problem and task requirements.",
            "The hints align with the problem and task requirements.",
            "The hints provide actionable guidance for solving the problem.",
            "The hints provide actionable guidance for solving the problem.",
            "The hints provide actionable guidance for solving the problem."
        ]
    },
    {
        "title": "Depth and Completeness",
        "questions": [
            "The hints address all critical conceptual aspects of the task (e.g., input validation, loops, formatting).",
            "The hints address all critical conceptual aspects of the task (e.g., input validation, loops, formatting).",
            "The hints address all critical conceptual aspects of the task (e.g., input validation, loops, formatting).",
            "The hints provide enough information to be useful without overwhelming the user.",
            "The hints provide enough information to be useful without overwhelming the user.",
            "The hints provide enough information to be useful without overwhelming the user."
        ]
    },
    {
        "title": "Specificity and Examples",
        "questions": [
            "The hints are specific and directly applicable to the task(targeted).",
            "The hints are specific and directly applicable to the task(targeted).",
            "The hints are specific and directly applicable to the task(targeted)."
        ]
    },
    {
        "title": "Hallucination and Factual Levels",
        "questions": [
            "The hints accurate and void of fabricated or incorrect information.",
            "The hints accurate and void of fabricated or incorrect information.",
            "The hints accurate and void of fabricated or incorrect information.",
            "The hints are directly relevant to the student and goal code.",
            "The hints are directly relevant to the student and goal code.",
            "The hints are directly relevant to the student and goal code."
        ]
    },
    {
        "title": "Level Specific Evaluation",
        "questions": [
        "The questions encourage critical thinking about the task",
        "The hints provide generic yet practical steps to solve the problem",
        "The hints specific and detailed enough for direct implementation",
        "The questions open-ended and avoid leading the user to a specific solution",
        "The suggestions aligned with good programming practices",
        "The hints include accurate syntax and logic for the given task"
        ]
    }
]

  const surveyResponses = []; // Store survey responses here
  let currentIndex = null; // Current data index

  // Render a random set from the JSON data
  function renderSet() {
    const randomIndex = Math.floor(Math.random() * data.length);
    currentIndex = randomIndex;
    const currentSet = data[randomIndex];

    const dataContainer = document.getElementById("data-container");
    const surveyContainer = document.getElementById("survey-container");

    // Render data
    dataContainer.innerHTML = `
      <table>
        <tr>
          <th colspan="3">Student Code</th>
          <th colspan="3">Goal Code</th>
        </tr>
        <tr>
          <td colspan="3">${currentSet.student_code}</td>
          <td colspan="3">${currentSet.goal_code}</td>
        </tr>
        <tr>
          <th colspan="6">Edit Script</th>
        </tr>
        <tr>
          <td colspan="6">${currentSet.edit_script}</td>
        </tr>
        <tr>
          <th colspan="2">Hints Level 1</th>
          <th colspan="2">Hints Level 2</th>
          <th colspan="2">Hints Level 3</th>
        </tr>
        <tr>
          <td colspan="2">${currentSet.hints_level1}</td>
          <td colspan="2">${currentSet.hints_level2}</td>
          <td colspan="2">${currentSet.hints_level3}</td>
        </tr>
      </table>
    `;

  
    let surveyHTML = ``;
    sections.forEach((section, sectionIndex) => {
      surveyHTML += `<h4>${section.title}</h4><table><tr>
              <th colspan="2">Hints Level 1</th>
              <th colspan="2">Hints Level 2</th>
              <th colspan="2">Hints Level 3</th>
            </tr>`;
      for (let questionIndex = 0; questionIndex < section.questions.length; questionIndex += 3) {
        // const question = section.questions[questionIndex];
        surveyHTML += `
          <div class="survey-question">
            <tr>
              <td colspan="2"><label>${section.questions[questionIndex]}</label>
            <div class="likert-scale">
              <label><input type="radio" name="q${sectionIndex}_${questionIndex}" value="1"> 1</label>
              <label><input type="radio" name="q${sectionIndex}_${questionIndex}" value="2"> 2</label>
              <label><input type="radio" name="q${sectionIndex}_${questionIndex}" value="3"> 3</label>
              <label><input type="radio" name="q${sectionIndex}_${questionIndex}" value="4"> 4</label>
              <label><input type="radio" name="q${sectionIndex}_${questionIndex}" value="5"> 5</label>
            </div></td>
              <td colspan="2"><label>${section.questions[questionIndex+1]}</label>
            <div class="likert-scale">
              <label><input type="radio" name="q${sectionIndex}_${questionIndex+1}" value="1"> 1</label>
              <label><input type="radio" name="q${sectionIndex}_${questionIndex+1}" value="2"> 2</label>
              <label><input type="radio" name="q${sectionIndex}_${questionIndex+1}" value="3"> 3</label>
              <label><input type="radio" name="q${sectionIndex}_${questionIndex+1}" value="4"> 4</label>
              <label><input type="radio" name="q${sectionIndex}_${questionIndex+1}" value="5"> 5</label>
            </div></td>
              <td colspan="2"><label>${section.questions[questionIndex+2]}</label>
            <div class="likert-scale">
              <label><input type="radio" name="q${sectionIndex}_${questionIndex+2}" value="1"> 1</label>
              <label><input type="radio" name="q${sectionIndex}_${questionIndex+2}" value="2"> 2</label>
              <label><input type="radio" name="q${sectionIndex}_${questionIndex+2}" value="3"> 3</label>
              <label><input type="radio" name="q${sectionIndex}_${questionIndex+2}" value="4"> 4</label>
              <label><input type="radio" name="q${sectionIndex}_${questionIndex+2}" value="5"> 5</label>
            </div></td>
            </tr>
          </div>
        `;
      };
      surveyHTML += `</table>`;
    });
    surveyHTML += `<h4>General Feedback</h4>
    <table>
      <div class="survey-question">
      <tr>
          <th colspan="6">
            <label>What are some ways the generated hints could be improved?</label>
          </th>
      </tr>
      <tr>
        <th colspan="6">
          <textarea name="improvement_feedback" rows="5" style='width:100%' placeholder="Your feedback here..."></textarea>
        </th>
      </tr>
      </div>
      <div class="survey-question">
        <tr>
          <th colspan="6">
            <label>Any further comments?</label>
          </th>
        </tr>
        <tr>
          <th colspan="6">
            <textarea name="general_comments" rows="5" style='width:100%' placeholder="Your comments here..."></textarea>
          </th>
        </tr>
      </div>
      </table>
    `;
    surveyContainer.innerHTML = surveyHTML;
  };

  function pushCurrent(){
    const responses = { 
      index: currentIndex,
      sections:[],
      generalFeedback:{}
    };
    sections.forEach((section, sectionIndex) => {
      const sectionResponses = {
        title: section.title,
        questions: []
      };

      for (let questionIndex = 0; questionIndex < section.questions.length; questionIndex += 3) {
        const questionGroup = [];
        
        for (let i = 0; i <3; i++) {
          const question = section.questions[questionIndex + i];
          if (!question) break;
          
          const radioName = `q${sectionIndex}_${questionIndex + i}`;
          const selectedValue = document.querySelector(`input[name="${radioName}"]:checked`);
          
          questionGroup.push({
            question: question, 
            response:selectedValue ? selectedValue.value : 0 // Capture response or 0 if not answered
          });
        }
        
        sectionResponses.questions.push(JSON.stringify(questionGroup));
      }
      console.log(sectionResponses)
      responses.sections.push(sectionResponses);
    });

    // Add general feedback
    const Feedback = document.querySelector("textarea[name='improvement_feedback']").value;
    const Comments = document.querySelector("textarea[name='general_comments']").value;
    
    responses.generalFeedback.improvementFeedback = Feedback;
    responses.generalFeedback.generalComments = Comments;

    surveyResponses.push(JSON.stringify(responses)); // Add to survey responses array
    // alert("Response submitted! Thank you.");
    console.log("Survey Responses:", surveyResponses);
  }
  // Submit survey response
  function submitSurvey() {
    //push current evalution responses before sending to firestore
    pushCurrent()
    //https://us-central1-evaluation-survey-e9fa1.cloudfunctions.net/submitSurveyResponse
    //Submit responses to Firestore API
    fetch("https://us-central1-evaluation-survey-e9fa1.cloudfunctions.net/submitSurveyResponse", {
      method: "POST",
      mode:"cors",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin":"*",
        "Accept": "application/json",
        "Access-Control-Allow-Origin": "http://127.xxx",
        "Access-Control-Allow-Credentials": "true"
      },
      body: surveyResponses
    })
      .then(response => {
        console.log(response)
        if (!response.ok) {
          throw new Error("Network response was not ok " + response.statusText);
        }
        alert("Response submitted successfully!");
      })
      .catch(error => {
        console.error("Error submitting response: ", error);
        alert("Failed to submit response. Please try again later.");
      });
  }


  // Load the next set
  function nextSet() {
    //push current evalution responses before loading new set
    pushCurrent()
    renderSet();
  }

  // Initialize first set
  renderSet();
</script>
</body>

