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

    lines=[line.strip() for line in text.split("\n") if line.strip()]

    if len(lines)>=2:

        first=re.sub(r"[^A-Za-z]","",lines[0])
        second=re.sub(r"[^A-Za-z]","",lines[1])

        if(
            first.isalpha()
            and second.isalpha()
            and first.isupper()
            and second.isupper()
        ):
            return first+" "+second

    section_words={"experience","education","skills","projects","certifications","languages","interests","references","objective","summary","profile","contact","career","resume","employment","achievements"}

    contact_words={"phone","mobile","email","linkedin","github","portfolio","website","address","city","country"}

    job_words={"engineer","developer","intern","analyst","scientist","manager","designer","student","consultant","architect","researcher","specialist","administrator","technician"}

    location_words={"india","usa","uk","canada","australia","singapore","california","texas","new","york","chicago","mumbai","delhi","bangalore","hyderabad","pune","seattle","san","francisco"}

    for line in lines[:8]:

        lower=line.lower()

        if any(word in lower for word in section_words):
            continue

        if any(word in lower for word in contact_words):
            continue

        if "@" in line:
            continue

        if "http" in lower or "www" in lower:
            continue

        if re.search(r"\d",line):
            continue

        clean=re.sub(r"[^A-Za-z\s.'-]","",line).strip()

        words=clean.split()

        if len(words)==0:
            continue

        if any(word.lower() in job_words for word in words):
            continue

        if any(word.lower() in location_words for word in words):
            continue

        if len(words)==1:
            if words[0][0].isupper():
                return words[0]

        if 2<=len(words)<=4:

            valid=True

            for word in words:

                if len(word)==1:
                    continue

                if not(word[0].isupper() or word.isupper()):
                    valid=False
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
