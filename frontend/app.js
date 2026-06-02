const API_URL = "http://127.0.0.1:8000/analyze-file";

const fileInput = document.getElementById("resumeFile");
const analyzeBtn = document.getElementById("analyzeBtn");
const statusMessage = document.getElementById("statusMessage");
const resultSection = document.getElementById("resultSection");

const finalScore = document.getElementById("finalScore");
const scoreBreakdown = document.getElementById("scoreBreakdown");
const overallAssessment = document.getElementById("overallAssessment");
const strengthsList = document.getElementById("strengthsList");
const weaknessesList = document.getElementById("weaknessesList");
const suggestionsList = document.getElementById("suggestionsList");
const risksList = document.getElementById("risksList");

function clearList(element) {
  element.innerHTML = "";
}

function renderList(element, items) {
  clearList(element);

  if (!items || items.length === 0) {
    const li = document.createElement("li");
    li.textContent = "No items found.";
    element.appendChild(li);
    return;
  }

  items.forEach((item) => {
    const li = document.createElement("li");
    li.textContent = item;
    element.appendChild(li);
  });
}

function renderScoreBreakdown(breakdown) {
  clearList(scoreBreakdown);

  Object.entries(breakdown).forEach(([key, value]) => {
    const li = document.createElement("li");
    const label = key.replaceAll("_", " ");

    li.textContent = `${label}: ${value}`;
    scoreBreakdown.appendChild(li);
  });
}

function getScoreClass(score) {
  if (score >= 80) {
    return "score-high";
  }

  if (score >= 60) {
    return "score-medium";
  }

  return "score-low";
}

function renderAnalysis(data) {
  const analysis = data.analysis;

  finalScore.classList.remove("score-high", "score-medium", "score-low");
  finalScore.classList.add(getScoreClass(analysis.final_score));

  finalScore.textContent = `${analysis.final_score}%`;
  overallAssessment.textContent = analysis.overall_assessment;

  renderScoreBreakdown(analysis.score_breakdown);
  renderList(strengthsList, analysis.strengths);
  renderList(weaknessesList, analysis.weaknesses);
  renderList(suggestionsList, analysis.improvement_suggestions);
  renderList(risksList, analysis.ats_risks);

  resultSection.classList.remove("hidden");
}

async function analyzeResume() {
  const file = fileInput.files[0];

  if (!file) {
    statusMessage.textContent = "Please select a PDF or DOCX file.";
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  analyzeBtn.disabled = true;
  statusMessage.textContent = "Analyzing resume...";
  resultSection.classList.add("hidden");

  try {
    const response = await fetch(API_URL, {
      method: "POST",
      body: formData
    });

    const data = await response.json();

    if (!response.ok) {
      throw new Error(data.detail || "Something went wrong.");
    }

    renderAnalysis(data);
    statusMessage.textContent = "Analysis completed.";
  } catch (error) {
    statusMessage.textContent = `Error: ${error.message}`;
  } finally {
    analyzeBtn.disabled = false;
  }
}

analyzeBtn.addEventListener("click", analyzeResume);