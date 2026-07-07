#!/usr/bin/env python3

import json
import re
from pathlib import Path

from jinja2 import Environment, FileSystemLoader


INPUT_JSON = "hlasyagresora.eu/osoby.json"
TEMPLATE_DIR = "templates"
TEMPLATE_NAME = "person.md.j2"
OUTPUT_DIR = Path("docs/people")


def slugify(text: str) -> str:
    text = text.lower()

    replacements = {
        "á": "a", "ä": "a",
        "č": "c",
        "ď": "d",
        "é": "e",
        "í": "i",
        "ĺ": "l", "ľ": "l",
        "ň": "n",
        "ó": "o", "ô": "o",
        "ŕ": "r",
        "š": "s",
        "ť": "t",
        "ú": "u",
        "ý": "y",
        "ž": "z",
    }

    for src, dst in replacements.items():
        text = text.replace(src, dst)

    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    with open(INPUT_JSON, encoding="utf-8") as f:
        data = json.load(f)

    if isinstance(data, dict):
        data = [data]

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=False,
        trim_blocks=True,
        lstrip_blocks=True,
    )

    template = env.get_template(TEMPLATE_NAME)

    for person in data:
        slug = slugify(
            f"{person['meno']}-{person['priezvisko']}"
        )

        output_file = OUTPUT_DIR / f"{slug}.md"

        markdown = template.render(person=person)

        output_file.write_text(markdown, encoding="utf-8")

        print(f"Generated {output_file}")


if __name__ == "__main__":
    main()
