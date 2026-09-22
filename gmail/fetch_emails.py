import re

from gmail.service import get_gmail_service


def clean_text(text):

    text = re.sub(r"[^\x00-\x7F]+", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def fetch_latest_emails(max_results=100):

    service = get_gmail_service()

    results = service.users().messages().list(
        userId="me",
        maxResults=max_results
    ).execute()

    messages = results.get("messages", [])

    emails = []

    for message in messages:

        msg = service.users().messages().get(
            userId="me",
            id=message["id"]
        ).execute()

        headers = msg["payload"]["headers"]

        subject = ""
        sender = ""
        date = ""

        for header in headers:

            if header["name"] == "Subject":
                subject = header["value"]

            elif header["name"] == "From":
                sender = header["value"]

            elif header["name"] == "Date":
                date = header["value"]

        snippet = clean_text(
            msg.get("snippet", "")
        )

        emails.append({

            "id": message["id"],

            "subject": clean_text(subject),

            "sender": clean_text(sender),

            "date": date,

            "snippet": snippet

        })

    return emails