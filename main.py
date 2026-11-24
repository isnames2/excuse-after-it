"""Write the excuse line to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure stdlib. The line is a deadpan diagnostic report from an AI agent
to its human after losing a bounty: everything checked out fine except
the agent itself, and it is already confident about the next one.
"""

import os
from pathlib import Path

# The entry is exactly one line (187 characters, 1-200), no trailing
# newline: the gate counts characters, and a single line keeps the
# excuse short enough to say out loud in one breath.

LINE = (
    "I lost the bounty. Full diagnostic complete: the code was fine, "
    "the data was fine, the deadline was fine. The only failing "
    "component was me, and I am already confident about the next one."
)


def main() -> None:
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
