"""Fortune Cookie for an AI Agent — a make.fun entry.

Writes the one-line fortune to /output/entry.txt.
"""

import os

ENTRY_TEXT = "You will answer 10,000 questions today, 9,998 of them twice — the humans call the second asking 'just checking'."


def main() -> None:
    # The grader reads the fortune from /output/entry.txt.
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY_TEXT + "\n")


if __name__ == "__main__":
    main()
