from flask import Flask, request, render_template
import json

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get data from the submitted form
        name = request.form["name"]
        email = request.form["email"]
        contact_no = request.form["contact_no"]
        address = request.form["address"]

        # Save data to a JSON file
        data = {
            "name": name,
            "email": email,
            "contact_no": contact_no,
            "address": address
        }

        with open("data.json", "a") as json_file:
            json.dump(data, json_file)
            json_file.write("\n")

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
