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
        r"\+91[-\s]?\d{10}",
        r"\d{5}\s\d{3}\s\d{3}",
        r"\d{4}\s\d{3}\s\d{3}",
        r"\(\d{3}\)\s?\d{3}[-.\s]?\d{4}",
        r"\d{3}[-.\s]\d{3}[-.\s]\d{4}",
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

    # Remove all email addresses first
    text = re.sub(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        " ",
        text
    )

    matches = re.findall(
        r"(https?://[^\s|]+|www\.[^\s|]+|\b[a-zA-Z0-9-]+\.(?:dev|io|me|tech|app|site)\b)",
        text,
        re.IGNORECASE
    )

    for url in matches:

        lower = url.lower()

        if any(site in lower for site in [
            "linkedin",
            "github",
            "gmail",
            "hotmail",
            "yahoo",
            "outlook",
            "email"
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
        "cv",
        "contact",
        "education",
        "skills",
        "projects",
        "experience",
        "career",
        "objective",
        "summary",
        "profile"
    }

    bad_words = {
        "india", "usa", "street", "road", "avenue",
        "university", "college", "school",
        "city", "state", "district",
        "pittsburgh", "visakhapatnam",
        "hyderabad", "bangalore",
        "mumbai", "delhi",
        "london", "new", "york",
        "pa", "ca", "ny"
    }

    lines = [line.strip() for line in text.split("\n") if line.strip()]

    candidates = []

    for i, line in enumerate(lines[:20]):

        original = line
        lower = line.lower()

        if any(word in lower for word in skip_words):
            continue

        if "@" in lower:
            continue

        if "linkedin" in lower or "github" in lower:
            continue

        line = re.sub(r"\+\d.*$", "", line).strip()
        line = re.sub(r"\d[\d\s().+-]{6,}$", "", line).strip()

        line = re.sub(r"[^A-Za-z\s.'-]", " ", line)

        words = [w for w in line.split() if w]

        if len(words) < 2 or len(words) > 5:
            continue

        if any(w.lower() in bad_words for w in words):
            continue

        valid = True

        for word in words:

            if len(word) == 1:
                continue

            if word.endswith("."):
                continue

            if not (word.istitle() or word.isupper()):
                valid = False
                break

        if not valid:
            continue

        score = 0

        # Higher priority for lines near the top
        score += max(0, 20 - i)

        # Prefer ALL CAPS names
        if original.isupper():
            score += 40

        # Prefer 2-4 word names
        if 2 <= len(words) <= 4:
            score += 15

        candidates.append((score, " ".join(words)))

    if candidates:
        candidates.sort(reverse=True)
        return candidates[0][1]

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
