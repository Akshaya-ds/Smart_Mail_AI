import joblib

from ml.preprocess import preprocess_text
from ml.rules import apply_rules


model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")


LABELS = {
    0: "Low",
    1: "Average",
    2: "Important"
}


def predict_priority(subject, snippet, sender):

    text = f"{subject} {snippet}"

    clean_text = preprocess_text(text)

    vector = vectorizer.transform([clean_text])

    ml_prediction = int(model.predict(vector)[0])

    rule_score = apply_rules(subject, sender)


    # --------------------
    # Hybrid Intelligence
    # --------------------

    final_prediction = ml_prediction

    if rule_score >= 3:
        final_prediction = 2

    elif rule_score <= -2:
        final_prediction = 0

    else:

        if ml_prediction == 0 and rule_score >= 2:
            final_prediction = 1

        elif ml_prediction == 2 and rule_score <= -1:
            final_prediction = 1


    return LABELS[final_prediction]