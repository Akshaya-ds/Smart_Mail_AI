import pandas as pd


def save_to_csv(emails):

    df = pd.DataFrame(emails)

    df.to_csv(
        "dataset/emails.csv",
        index=False
    )

    print("Emails saved successfully!")