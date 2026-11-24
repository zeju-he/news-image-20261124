"""Sum up 24 November 2026 world news in one image.

Deterministic, no network: copies the bundled entry.png to
/output/entry.png. Running twice writes the same bytes.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
