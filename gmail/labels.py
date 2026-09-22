import os
import pandas as pd

DATASET_PATH = "dataset/emails.csv"
LABELED_PATH = "dataset/labeled_emails.csv"


def create_labeled_dataset():

    if os.path.exists(LABELED_PATH):
        return

    df = pd.read_csv(DATASET_PATH)

    # Create label column as object (string)
    df["label"] = ""

    df.to_csv(LABELED_PATH, index=False)


def get_all_emails():

    create_labeled_dataset()

    return pd.read_csv(LABELED_PATH, dtype={"label": str})


def save_label(email_id, label):

    create_labeled_dataset()   # <-- Add this line

    df = pd.read_csv(LABELED_PATH, dtype={"label": str})

    df.loc[df["id"] == email_id, "label"] = str(label)

    df.to_csv(LABELED_PATH, index=False)