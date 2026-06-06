const API_URL = "http://127.0.0.1:8000/analyze-file";

const fileInput = document.getElementById("resumeFile");
const analyzeBtn = document.getElementById("analyzeBtn");
const statusMessage = document.getElementById("statusMessage");
const resultSection = document.getElementById("resultSection");

const finalScore = document.getElementById("finalScore");
const scoreLabel = document.getElementById("scoreLabel");
const scoreBreakdown = document.getElementById("scoreBreakdown");
const overallAssessment = document.getElementById("overallAssessment");
const recommendationsList = document.getElementById("recommendationsList");
const strengthsList = document.getElementById("strengthsList");
const weaknessesList = document.getElementById("weaknessesList");
const risksList = document.getElementById("risksList");

function clearList(element) {
  element.innerHTML = "";
}

function renderList(element, items) {
  clearList(element);

  if (!Array.isArray(items) || items.length === 0) {
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

  if (!breakdown) {
    const li = document.createElement("li");
    li.textContent = "No score breakdown found.";
    scoreBreakdown.appendChild(li);
    return;
  }

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
  scoreLabel.textContent = analysis.score_label || "";
  overallAssessment.textContent = analysis.overall_assessment || "No assessment found.";

  renderList(recommendationsList, analysis.top_recommendations);
  renderScoreBreakdown(analysis.score_breakdown);
  renderList(strengthsList, analysis.strengths);
  renderList(weaknessesList, analysis.weaknesses);
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
      body: formData,
      mode: "cors"
    });

    let data;

    try {
      data = await response.json();
    } catch {
      throw new Error("Backend did not return valid JSON.");
    }

    if (!response.ok) {
      throw new Error(data.detail || `Backend returned status ${response.status}`);
    }

    renderAnalysis(data);
    statusMessage.textContent = "Analysis completed.";
  } catch (error) {
    console.error("Frontend request error:", error);
    statusMessage.textContent = `Error: ${error.message}`;
  } finally {
    analyzeBtn.disabled = false;
  }
}

analyzeBtn.addEventListener("click", analyzeResume);