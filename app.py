from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Configure API
genai.configure(api_key="AIzaSyB6tkc4h-n9NnNpdVkSqPh2i5cfK4qvU90")
model = genai.GenerativeModel("gemini-1.5-flash")

@app.route("/", methods=["GET", "POST"])
def index():
    translation = ""
    if request.method == "POST":
        source = request.form["source_lang"]
        target = request.form["target_lang"]
        user_input = request.form["text"]
        prompt = f"Translate the following text from {source} to {target}:\n\n{user_input}"
        response = model.generate_content(prompt)
        translation = response.text
    return render_template("index.html", translation=translation)

if __name__ == "__main__":
    app.run(debug=True)

