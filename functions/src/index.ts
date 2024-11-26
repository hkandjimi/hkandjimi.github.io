const functions = require("firebase-functions");
const admin = require("firebase-admin");

admin.initializeApp({
  credential: admin.credential.cert(require("../src/surveyApi.json")),
  databaseURL: "https://evaluation-survey-e9fa1.firebaseio.com",
});

const db = admin.firestore();
// const cors = require("cors")({origin: false});
const cors = require("cors")({
  origin: ["http://localhost:4000/", "https://hkandjimi.github.io/"],
});

exports.submitSurveyResponse = functions.https.onRequest((req, res) => {
  cors(req, res, async () => {
    if (req.method !== "POST") {
      return res.status(405).send("Method Not Allowed");
    }
    try {
      console.log(formatResponse(req.body));
      await db.collection("surveyResponses").add(formatResponse(req.body));
      res.status(200).send("Survey response submitted successfully!");
    } catch (error) {
      console.error("Error writing document: ", error);
      res.status(500).send("Internal Server Error");
    }
  });
});
/**
 * Formats the survey responses into a Firestore-compatible document.
 * Combines information from sections and extracts only the responses.
 * @param {any}data - The incoming nested survey response data
 * @return {json}A formatted Firestore document with processed sections.
 */
function formatResponse(data: any): any {
  console.log(JSON.parse(data).sections);
  const formattedSections: Record<string, number[]> = {};

  // Iterate through each section in the data
  JSON.parse(data).sections.forEach((section: any) => {
    console.log(section.title);
    const parsedSection = section;

    const title = parsedSection.title; // Extract title
    const questions = parsedSection.questions; // Extract questions array

    // Flatten responses from all question arrays
    const responses: number[] = questions
        .flatMap((questionSet: string) => JSON.parse(questionSet)) // Parse nested question sets
        .map((q: { response: string | null }) => (q.response ? parseInt(q.response, 10) : null)) // Extract response
        .filter((response) => response !== null); // Remove null responses

    // Add processed responses to the formattedSections map
    formattedSections[title] = responses;
  });

  // Construct the Firestore-compatible document
  return {
    index: JSON.parse(data).index,
    generalFeedback: JSON.parse(data).generalFeedback,
    sections: formattedSections,
  };
}
