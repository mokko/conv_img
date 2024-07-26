"""
Copy *.png files while preserving part of the path.

Scan from for **/*.png from pwd, copy to destination dir, preserving name and path.
"""

import argparse
from pathlib import Path
import shutil
import sys

shutdown_requested = False


def main(dest: str, limit: int) -> None:
    dest = Path(dest)
    limit = int(limit)
    if not dest.exists():
        print("Making dir {dest}")
        dest.mkdir()
        # raise SyntaxError("Destination dir doesn't exist!")
    if not dest.is_dir():
        raise SyntaxError("Destination dir is not a dir!")

    c = 1
    for p in Path().glob("**/*.png"):
        p2 = dest / p  # p is a relative path
        print(f"{c}:{p}")
        print(f"->{p2}")
        if p2.exists():
            print("   target exists")
        else:
            p2.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy(p, p2)
            except KeyboardInterrupt:
                _request_shutdown()

        if c == limit:
            break
        _shutdown_if_requested()
        c += 1
    print("done!")


def _request_shutdown():
    """
    Prints a message and changes class variable. To be called in except KeyboardInterrupt.
    """
    print("Keyboard interrupt received, requesting shutdown...")
    shutdown_requested = True


def _shutdown_if_requested():
    """
    Do the shutdown if global variable is True. To be used in the loop at an appropriate time.
    """
    if shutdown_requested:
        print("Planned shutdown!")
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="kcopy - copy *.png files recursively while preserving some path"
    )

    parser.add_argument(
        "dest",
        help="destination directory",
    )

    parser.add_argument(
        "-l", "--limit", help="limit (int) after which to stop", default=-1
    )
    args = parser.parse_args()
    main(args.dest, args.limit)
