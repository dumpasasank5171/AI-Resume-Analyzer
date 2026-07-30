import re


def extract_email(text):

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    if match:
        return match.group()

    return "Not Found"


def extract_phone(text):

    patterns = [
        r"\+\d{1,3}\s?\d{10}",
        r"\d{10}",
        r"\(\d{3}\)\s?\d{3}-\d{4}",
        r"\d{3}[-.\s]\d{3}[-.\s]\d{4}",
        r"\+\d{1,3}[-\s]?\(\d{3}\)\s?\d{3}[-.\s]?\d{4}"
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:
            return match.group().strip()

    return "Not Found"


def extract_linkedin(text):

    match = re.search(
        r"(https?://)?(www\.)?linkedin\.com/[A-Za-z0-9_/\-]+",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group()

    if "linkedin" in text.lower():
        return "LinkedIn Mentioned"

    return "Not Found"


def extract_github(text):

    match = re.search(
        r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_/\-]+",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group()

    if "github" in text.lower():
        return "GitHub Mentioned"

    return "Not Found"


def extract_portfolio(text):

    matches = re.findall(
        r"(https?://[^\s|]+|www\.[^\s|]+|[A-Za-z0-9.-]+\.(?:com|dev|io|me|net))",
        text,
        re.IGNORECASE
    )

    for url in matches:

        url = url.strip()

        if (
            "gmail" in url.lower()
            or "linkedin" in url.lower()
            or "github" in url.lower()
        ):
            continue

        return url

    return "Not Found"


def extract_name(text):

    lines = text.strip().split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        line = re.sub(r"\+?\d[\d\s().-]{8,}", "", line)

        line = re.sub(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            "",
            line
        )

        line = line.replace("|", " ")

        words = line.split()

        name_words = []

        for word in words:

            if word.isalpha() and len(word) > 1:

                if word.upper() == word or word.istitle():

                    name_words.append(word)

        if 2 <= len(name_words) <= 6:
            return " ".join(name_words).title()

    return "Not Found"


def extract_details(text):

    return {
        "Name": extract_name(text),
        "Email": extract_email(text),
        "Phone": extract_phone(text),
        "LinkedIn": extract_linkedin(text),
        "GitHub": extract_github(text),
        "Portfolio": extract_portfolio(text)
    }
