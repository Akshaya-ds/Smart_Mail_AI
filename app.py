from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from ml.predictor import predict_priority
from gmail.fetch_emails import fetch_latest_emails
from gmail.save_csv import save_to_csv

from gmail.labels import (
    get_all_emails,
    save_label
)

app = Flask(__name__)


@app.route("/")
def home():

    emails = fetch_latest_emails()

    save_to_csv(emails)

    return render_template(
        "index.html",
        emails=emails
    )


@app.route("/label", methods=["GET", "POST"])
def label():

    if request.method == "POST":

        email_id = request.form["email_id"]

        label = request.form["label"]

        save_label(
            email_id,
            label
        )

        return redirect("/label")

    emails = get_all_emails()

    return render_template(
        "label.html",
        emails=emails.to_dict("records")
    )

@app.route("/dashboard")
def dashboard():

    emails = fetch_latest_emails()

    predicted_emails = []

    important = 0
    average = 0
    low = 0

    for email in emails:

        priority = predict_priority(
            email["subject"],
            email["snippet"],
            email["sender"]
        )

        email["priority"] = priority

        if priority == "Important":
            important += 1
        elif priority == "Average":
            average += 1
        else:
            low += 1

        predicted_emails.append(email)

    return render_template(
        "dashboard.html",
        emails=predicted_emails,
        total=len(predicted_emails),
        important=important,
        average=average,
        low=low
    )
if __name__ == "__main__":

    app.run(debug=True)