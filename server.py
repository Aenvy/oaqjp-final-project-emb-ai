"""
Flask application for Emotion Detection
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")


def run_emotion_detection():
    """Run the Flask application."""
    app.run(host="0.0.0.0", port=5000)


@app.route("/emotionDetector")
def detect_emotion():
    """
    Handle emotion detection for a given text.

    Returns:
        str: Formatted emotion response or an error message.
    """
    text_to_detect = request.args.get("textToAnalyze")
    if not text_to_detect:
        return "Invalid text! Please provide text to analyze."

    response = emotion_detector(text_to_detect)
    if not response or not response.get("dominant_emotion"):
        return "Invalid text! Please try again."

    response_text = (
        f"For the given statement, the system response is: "
        f"'anger': {response['anger']}, 'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, 'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. The dominant emotion is "
        f"{response['dominant_emotion']}."
    )
    return response_text


@app.route("/")
def render_index_page():
    """
    Render the index page.

    Returns:
        str: Rendered HTML template for the home page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    run_emotion_detection()
