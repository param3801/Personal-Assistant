from flask import Flask, render_template, request, jsonify, redirect,url_for
import os
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

from google import genai
from google.genai import types

client = genai.Client(api_key = api_key)

from flask import Flask, jsonify

app = Flask(__name__)


# Catch all invalid URLs
@app.errorhandler(404)
def page_not_found(error):
    return "<h1>Oops! This page doesn't exist.</h1>", 404


@app.route('/ask', methods=['POST', 'GET'])
def ask():
    print("function called")
    if request.method == "POST":
        question = request.form.get('ask-input')
        print(question)

        ai_config = types.GenerateContentConfig(
            system_instruction="You are a strict, helpful Personal assistant. "
                               "Answer concisely, use clear bullet points "
                               "only answer what is being asked not more than that."
                               
        )
        response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=question,
        config= ai_config
        ) 
        result = response.text.strip()
        print(result)
        return jsonify({"response":result}), 200
    
    if(request.method == 'GET'):
        return redirect(url_for("home"))

@app.route("/")    
def home():
    return render_template("main.html")





if __name__ == "__main__":
    app.run(debug=True)