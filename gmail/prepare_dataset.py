import pandas as pd


def create_labeled_dataset():
    df = pd.read_csv("dataset/emails.csv")

    # Create empty label column
    df["label"] = ""

    # Save new dataset
    df.to_csv("dataset/labeled_emails.csv", index=False)

    print("Labeled dataset created successfully!")