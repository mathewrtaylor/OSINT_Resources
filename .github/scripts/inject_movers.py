import re

START = "<!-- MOVERS_START -->"
END = "<!-- MOVERS_END -->"

# The README shows a dedicated banner (section-star-movers.svg) in place of a
# text heading, so strip Movers.md's own "# Star Movers ..." heading here.
HEADING = re.compile(r"^# Star Movers.*\n\n?", re.MULTILINE)

with open("Movers.md") as f:
    body = "".join(f.readlines()[2:]).strip()

body = HEADING.sub("", body, count=1).strip()

block = f"{START}\n{body}\n{END}\n"

with open("README.md") as f:
    readme = f.read()

if START in readme:
    s = readme.index(START)
    e = readme.index(END) + len(END)
    readme = readme[:s] + block + readme[e + 1:]
else:
    lines = readme.splitlines(keepends=True)
    lines.insert(7, "\n" + block + "\n")
    readme = "".join(lines)

with open("README.md", "w") as f:
    f.write(readme)
