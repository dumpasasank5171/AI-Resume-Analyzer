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

    match = re.search(
        r"(\+?\d{1,3}[- ]?)?(\d{10})",
        text
    )

    if match:
        return match.group()

    return "Not Found"


def extract_linkedin(text):

    match = re.search(
        r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+",
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
        r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+",
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
        r"(https?://[^\s]+|www\.[^\s]+)",
        text,
        re.IGNORECASE
    )

    for url in matches:

        if (
            "linkedin" not in url.lower()
            and "github" not in url.lower()
            and "gmail" not in url.lower()
        ):
            return url

    return "Not Found"


def extract_name(text):

    lines = text.strip().split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        line = re.sub(r"\+?\d[\d\s-]{8,}", "", line)

        line = re.sub(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            "",
            line
        )

        words = line.split()

        name_words = []

        for word in words:

            if word.isalpha() and word.isupper():
                name_words.append(word)

        if len(name_words) >= 2:
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