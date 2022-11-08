import requests

from flask import Flask, send_file
from flask_cors import CORS


app = Flask(__name__)
CORS(app, origins=["*"])


@app.route("/resume.pdf", methods=["GET"])
def get_pdf():
    url = "https://github.com/anmho/resume/raw/main/main.pdf"
    response = requests.get(url, stream=True)

    print(response.status_code)

    with open("resume.pdf", "wb") as resume:
        resume.write(response.content)

    return send_file("resume.pdf")


if __name__ == "__main__":
    app.run(debug=True)
