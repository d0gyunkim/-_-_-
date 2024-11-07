from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Collecting form data
    current_company = request.form['current_company']
    role = request.form['role']
    experience = request.form['experience']
    main_tasks = request.form['main_tasks']

    # API header and body setup
    header = {
        "project": "KHU_PROMPTHON_018",
        "apiKey": os.getenv("WANTED_API_KEY")
    }
    body = {
        "hash": "2cc6f00d01058516d8d0ac3b062a2547679aaef311d22b82400aa82f8ef4be47", 
        "params": {
            "task": f"1. Current Company: {current_company}\n2. Role: {role}\n3. Experience: {experience}\n4. Main Tasks: {main_tasks}",
            "current_company": current_company,
            "role": role,
            "experience": experience,
            "main_tasks": main_tasks
        }
    }

    URL = os.getenv("WANTED_API_URL")
    response = requests.post(URL, headers=header, json=body)

    if response.ok:
        content = response.json()["choices"][0]["message"]["content"]
        return jsonify({"content": content})
    else:
        return jsonify({"error": "Failed to fetch data"}), 400

if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
