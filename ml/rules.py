import re

IMPORTANT_KEYWORDS = [
    "interview",
    "internship",
    "offer",
    "offer letter",
    "deadline",
    "assignment",
    "meeting",
    "exam",
    "fee",
    "hackathon",
    "quiz",
    "selection",
    "selected",
    "joining",
    "job",
    "placement",
    "training",
    "certificate",
    "verification"
]

AVERAGE_KEYWORDS = [
    "linkedin",
    "message",
    "invitation",
    "connection",
    "network",
    "github",
    "discord",
    "event",
    "webinar"
]

LOW_KEYWORDS = [
    "sale",
    "discount",
    "offer ends",
    "shopping",
    "beauty",
    "amazon deals",
    "flipkart",
    "promotion",
    "newsletter",
    "unsubscribe",
    "coupon"
]


IMPORTANT_SENDERS = [
    "google",
    "microsoft",
    "amazon",
    "accenture",
    "infosys",
    "tcs",
    "wipro",
    "cognizant",
    "hack2skill",
    "unstop",
    ".edu",
    ".ac.in"
]


LOW_SENDERS = [
    "tirabeauty",
    "myntra",
    "meesho",
    "ajio",
    "newsletter",
    "marketing",
    "offers"
]


def apply_rules(subject, sender):

    text = f"{subject} {sender}".lower()

    score = 0


    # Important Keywords
    for word in IMPORTANT_KEYWORDS:

        if word in text:
            score += 2


    # Average Keywords
    for word in AVERAGE_KEYWORDS:

        if word in text:
            score += 1


    # Low Keywords
    for word in LOW_KEYWORDS:

        if word in text:
            score -= 2


    # Important Senders
    for sender_name in IMPORTANT_SENDERS:

        if sender_name in text:
            score += 2


    # Low Senders
    for sender_name in LOW_SENDERS:

        if sender_name in text:
            score -= 2


    return score