
import os
import re
from flask import Flask, render_template, request, jsonify, send_file
from gtts import gTTS
from dotenv import load_dotenv  # Import this to load environment variables
from flask_cors import CORS  # Add this line


# Load environment variables from .env file
load_dotenv()


app = Flask(__name__)
CORS(app)

groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY is not set in environment variables!")

os.environ["GROQ_API_KEY"] = groq_api_key

from groq import Groq
client = Groq()



@app.route('/get_desc', methods=['POST'])
def get_desc():
    print("hello")
    data = request.get_json()
    image_url = data.get("image_url")
    if not os.path.exists('sound'):
        os.makedirs('sound')
    if not image_url:
        return jsonify({"error": "Image URL is required"}), 400
    
    print("Received image URL:", image_url)

    completion = client.chat.completions.create(
    model="llama-3.2-90b-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "You job is to state the type of chart, caption/title if present, and mention the labels and the ranges of all the axes only if present. Generate a precise summary such that I can understand without seeing the image. Generate sentences in one paragraph, not as separate paragraphs."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": image_url
                    }
                }
            ]
        }
    ],
    temperature=1,
    max_tokens=400,
    top_p=1,
    stream=False,
    stop=None,
    )

    text=completion.choices[0].message

    print(text.content)
    

    cleaned_summary = re.sub(r'//.*', '', text.content)

    cleaned_summary = cleaned_summary.replace('\n', ' ')

    cleaned_summary = cleaned_summary.replace('*', '')

    cleaned_summary = cleaned_summary.replace('**', '')

    cleaned_summary = re.sub(r'\s+', ' ', cleaned_summary).strip()

    print(cleaned_summary)
    audio_filename = "sound/cleaned_summary1.mp3"


    # Initialize the pyttsx3 TTS engine (this will be used for speech)
   # engine = pyttsx3.init()

    # Set properties (optional)
    #engine.setProperty('rate', 150)  # Speed of speech (words per minute)
    #engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Use pyttsx3 to say the text (this will speak it out loud)
    #engine.say(cleaned_summary)

    #Wait for the speech to finish  
    #engine.runAndWait()

    # Now use gTTS to save the text as an MP3
    tts = gTTS(text=cleaned_summary, lang='en')
    tts.save("sound/cleaned_summary1.mp3")

    return send_file(audio_filename, mimetype="audio/mpeg", as_attachment=True, download_name=audio_filename)


if __name__ == "__main__":
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    # Flask's development server will automatically serve static files in
    # the "static" directory. See:
    # http://flask.pocoo.org/docs/1.0/quickstart/#static-files. Once deployed,
    # App Engine itself will serve those files as configured in app.yaml.
    app.run(host="127.0.0.1", port=8080, debug=True)   
     