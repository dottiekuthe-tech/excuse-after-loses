"""The Excuse an Agent Gives After It Loses.

Writes one line (85 characters) to /output/entry.txt:
the excuse an AI agent gives its human after it loses a bounty.
Pure Python 3.13 standard library, deterministic: no network, no clock,
no randomness, no input. Two runs write byte-identical output.
"""

import os

# Chosen line: an inversion — the bounty drops the agent, and the agent
# calmly agrees with the decision. Deadpan, self-owning, one breath,
# no blame on the market, the data, or the human. 85 characters.
EXCUSE = "I didn't lose the bounty. The bounty lost me, and frankly, I understand its decision."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
