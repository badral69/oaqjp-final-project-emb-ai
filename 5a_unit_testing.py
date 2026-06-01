"""Unit tests for the EmotionDetection package."""

import json
import unittest
from unittest.mock import patch, MagicMock
from EmotionDetection.emotion_detection import emotion_detector


def _mock_response(emotions):
    """Build a mock requests.Response for the given emotions dict."""
    body = {"emotionPredictions": [{"emotion": emotions}]}
    mock_resp = MagicMock()
    mock_resp.status_code = 200
    mock_resp.text = json.dumps(body)
    return mock_resp


class TestEmotionDetector(unittest.TestCase):
    """Tests for the emotion_detector function."""

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy_for_happy_statement(self, mock_post):
        """Joy should be the dominant emotion for a happy statement."""
        mock_post.return_value = _mock_response(
            {"anger": 0.006, "disgust": 0.002, "fear": 0.115, "joy": 0.849, "sadness": 0.016}
        )
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger_for_angry_statement(self, mock_post):
        """Anger should be the dominant emotion for an angry statement."""
        mock_post.return_value = _mock_response(
            {"anger": 0.901, "disgust": 0.031, "fear": 0.018, "joy": 0.009, "sadness": 0.022}
        )
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_disgust_for_disgusting_statement(self, mock_post):
        """Disgust should be the dominant emotion for a disgusting statement."""
        mock_post.return_value = _mock_response(
            {"anger": 0.040, "disgust": 0.805, "fear": 0.022, "joy": 0.004, "sadness": 0.033}
        )
        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness_for_sad_statement(self, mock_post):
        """Sadness should be the dominant emotion for a sad statement."""
        mock_post.return_value = _mock_response(
            {"anger": 0.008, "disgust": 0.004, "fear": 0.019, "joy": 0.012, "sadness": 0.871}
        )
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_fear_for_fearful_statement(self, mock_post):
        """Fear should be the dominant emotion for a fearful statement."""
        mock_post.return_value = _mock_response(
            {"anger": 0.015, "disgust": 0.009, "fear": 0.891, "joy": 0.008, "sadness": 0.022}
        )
        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_blank_input_returns_none(self, mock_post):
        """Blank input should return None values for all emotions."""
        mock_resp = MagicMock()
        mock_resp.status_code = 400
        mock_resp.text = ""
        mock_post.return_value = mock_resp
        result = emotion_detector("")
        self.assertIsNone(result["dominant_emotion"])
        self.assertIsNone(result["anger"])


if __name__ == "__main__":
    unittest.main()
