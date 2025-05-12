'''
    To learn and use python along with flask and watson 
'''
from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

# Initialize Flask app
app = Flask(__name__)

@app.route('/emotionDetector', methods=['GET'])
def home_analyze():
    ''' invoke detector'''
    text_to_analyze = request.args.get('textToAnalyze', '')

    if text_to_analyze is None or len(text_to_analyze) <= 0:
        return "Invalid Text! Please retry!"

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid Text! Please retry!"
    result = [f"'{emotion}': {value}"
    for emotion, value in response.items() if emotion != "dominant_emotion"]
    dominant = response["dominant_emotion"]

    if dominant is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is {result}." + \
           f" The dominant emotion is {dominant}."

@app.route("/")
def index():
    ''' landing page '''
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
