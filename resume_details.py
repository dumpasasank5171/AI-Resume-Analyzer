import re


def extract_email(text):

    match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        text
    )

    return match.group() if match else "Not Found"


def extract_phone(text):

    patterns = [
        r"\+\d{1,3}\s?\(?\d{1,4}\)?[-.\s]?\d{3}[-.\s]?\d{4}",
        r"\(\d{3}\)\s?\d{3}[-.\s]?\d{4}",
        r"\d{3}[-.\s]\d{3}[-.\s]\d{4}",
        r"\+91[-\s]?\d{10}",
        r"\d{10}"
    ]

    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group().strip()

    return "Not Found"


def extract_linkedin(text):

    match = re.search(
        r"(https?://)?(www\.)?linkedin\.com/[^\s|]+",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group()

    return "LinkedIn Mentioned" if "linkedin" in text.lower() else "Not Found"


def extract_github(text):

    match = re.search(
        r"(https?://)?(www\.)?github\.com/[^\s|]+",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group()

    return "GitHub Mentioned" if "github" in text.lower() else "Not Found"


def extract_portfolio(text):

    matches = re.findall(
        r"(https?://[^\s|]+|www\.[^\s|]+|[A-Za-z0-9.-]+\.(?:com|dev|io|me|net))",
        text,
        re.IGNORECASE
    )

    for url in matches:

        lower = url.lower()

        if any(x in lower for x in [
            "gmail",
            "linkedin",
            "github",
            "hotmail",
            "yahoo",
            "outlook"
        ]):
            continue

        return url

    return "Not Found"


def extract_name(text):

    skip_words = {
        "resume",
        "resume sample",
        "functional resume sample",
        "curriculum vitae",
        "cv"
    }

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    for line in lines[:10]:

        lower = line.lower()

        if any(word in lower for word in skip_words):
            continue

        if "@" in line:
            continue

        if "linkedin" in lower or "github" in lower:
            continue

        if re.search(r"\d{3,}", line):
            continue

        line = re.sub(r"[^\w\s.]", " ", line)

        words = line.split()

        if len(words) < 2 or len(words) > 5:
            continue

        valid = True

        for word in words:

            if len(word) == 1:
                continue

            if "." in word:
                continue

            if not (word.istitle() or word.isupper()):
                valid = False
                break

        if valid:
            return " ".join(words)

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
