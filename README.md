# Emotion Detector

An AI-based web application that detects emotions in text using the Watson NLP library.

## Project Name
**Emotion Detector** – Final Project (oaqjp-final-project-emb-ai)

## Description
This application uses IBM Watson NLP to analyse text and identify the dominant emotion
among: anger, disgust, fear, joy, and sadness.

## Features
- Emotion detection via Watson NLP REST API
- Flask web deployment
- Unit tested with `unittest`
- Static code analysis with `pylint` (10/10)

## Project Structure
```
├── EmotionDetection/
│   ├── __init__.py
│   └── emotion_detection.py
├── templates/
│   └── index.html
├── static/
│   └── mywebscript.js
├── test_emotion_detection.py
├── server.py
└── README.md
```

## Setup
```bash
pip install flask requests
python3 server.py
```

## Running Tests
```bash
python3 -m unittest test_emotion_detection -v
```

## Static Code Analysis
```bash
pylint server.py
```
