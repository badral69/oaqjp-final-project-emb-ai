function RunSentimentAnalysis() {
    const textToAnalyze = document.getElementById("textToAnalyze").value;
    const outputDiv = document.getElementById("output");

    outputDiv.textContent = "Analysing...";

    fetch(`/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`)
        .then(response => response.text())
        .then(data => { outputDiv.textContent = data; })
        .catch(() => { outputDiv.textContent = "Error contacting the server. Please try again."; });
}
