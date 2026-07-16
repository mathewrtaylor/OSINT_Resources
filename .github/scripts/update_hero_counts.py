import re

CATEGORY_FILES = {
    "TOOLS": "Tools.md",
    "AI TOOLS": "AI_Tools.md",
    "US INVESTIGATIONS": "United_States_Investigations.md",
    "GEOLOCATION": "Geolocation.md",
    "READING": "Recommended_Reading.md",
    "BOOKMARKS": "Bookmarks.md",
}

HERO_PATH = "assets/readme/hero.svg"
ENTRY_PATTERN = re.compile(r"^- \*\*\[", re.MULTILINE)


def count_entries(path):
    with open(path) as f:
        content = f.read()
    return len(ENTRY_PATTERN.findall(content))


def round_to_5(n):
    return round(n / 5) * 5


def main():
    with open(HERO_PATH) as f:
        svg = f.read()

    for label, filename in CATEGORY_FILES.items():
        count = round_to_5(count_entries(filename))
        pattern = re.compile(
            r"(>{}</text>\s*<text[^>]*>)~\d+(</text>)".format(re.escape(label))
        )
        svg, n = pattern.subn(r"\g<1>~{}\g<2>".format(count), svg)
        if n != 1:
            raise SystemExit(
                "expected exactly one count for {!r} in {}, found {}".format(
                    label, HERO_PATH, n
                )
            )

    with open(HERO_PATH, "w") as f:
        f.write(svg)


if __name__ == "__main__":
    main()
