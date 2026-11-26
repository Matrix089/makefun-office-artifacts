"""Office Artifacts: The One-Line Placard Contest entry.

Writes one original museum placard for an ordinary office object, the
stapler, treated as an ancient artifact, to /output/entry.txt (or to
the directory named by MAKEFUN_OUTPUT_DIR when the grader sets it).

The placard keeps a dry curator's voice: a catalogue date, a material,
a ritual use — binding ceremonies joining two sheets in eternal union —
and a donor, the Department of Lost Causes. The joke is the conceit
itself, stated plainly; nothing in it explains itself. One line, 158
characters.
"""

import os

# One line, 158 characters: the object, its date and material, its
# imagined ritual use, and the donor — the full label in a single breath.
ENTRY = "Stapler, c. 1998. Pressed steel and good intentions. Used in binding ceremonies to join two sheets in eternal union. Donated by the Department of Lost Causes."


def main():
    entry = ENTRY.strip()
    if not 1 <= len(entry) <= 180:
        raise SystemExit(f"Entry must be 1 to 180 characters, got {len(entry)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    with open(path, encoding="utf-8") as f:
        written = f.read()
    if written != entry:
        raise SystemExit("Read-back check failed: entry.txt does not match the entry")
    print(f"Wrote {len(entry)} characters to {path}")


if __name__ == "__main__":
    main()
