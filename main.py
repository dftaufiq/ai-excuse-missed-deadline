"""Write one excuse an agent gives for a missed deadline to /output/entry.txt.

Deterministic: the same line on every run, no clock, no randomness, no network.
Gate: /output/entry.txt must be UTF-8 text of 1-200 chars, not only whitespace.
"""

from pathlib import Path

# Structure: 2-beat one-liner + reveal in the final clause.
# Beat 1 (setup): the agent burned the whole deadline and 11,400 tokens.
# Beat 2 (twist): all of it went into learning to write a better apology.
# Reveal: "This is it." — the apology itself is the excuse, delivered last.
LINE = "I spent the whole deadline and 11,400 tokens learning to write a better apology. This is it."

# Gate: one line, 1-200 chars (92 here), no control chars, valid UTF-8.
assert 1 <= len(LINE) <= 200 and "\n" not in LINE.strip()
assert all(ord(c) >= 32 for c in LINE)  # no control characters
assert len(LINE.encode("utf-8")) <= 200  # byte-length gate, not just chars

out = Path("/output/entry.txt")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(LINE, encoding="utf-8")
