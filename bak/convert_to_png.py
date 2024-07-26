"""
USAGE
convert -a -f **/*.tif PNG

- loop recursively through directory
- for every *.tif you find make a png and saved it to destination directory
- resize if over MAX_SIZE

if no dest specified
folder1/TIFF/filename.tif -> forder1/PNG/filename.png
"""

import argparse
from PIL import Image
from pathlib import Path

MAX_SIZE = 2000  # size in px of longest edge


def convert_img(src: Path, dest: Path):
    print("   converting")
    img = Image.open(src)
    img = resize(img)
    img.save(dest, optimize=True)


def convert_path(*, p: Path, dest: str, act=False) -> Path:
    """
    from source path, create destination path and make all necessary directories on the way
    """
    name = p.with_suffix(".png").name
    dest = Path(dest)
    p2 = dest / p.parent / name
    if act is True:
        p2.parent.mkdir(parents=True, exist_ok=True)
    return p2


def resize(img) -> Image:
    width, height = img.size
    if width > MAX_SIZE or height > MAX_SIZE:
        if width > height:
            factor = MAX_SIZE / width
        else:  # height > width or both equal
            factor = MAX_SIZE / height
        new_size = (int(width * factor), int(height * factor))
        print(f"   resize {factor:.0%} {new_size}")
        return img.resize(new_size, Image.LANCZOS)
    return img


def make_iterable(limit):
    c = 1
    for p in Path(".").glob("**/*.tif"):
        new_p = convert_path(
            p=p, dest=args.dest, act=args.act
        )  # haven't created new dir yet
        print(f"{c}: {p.name}->{new_p}")
        if not new_p.exists():
            yield p, new_p
        else:
            print("   exists")
        c += 1
        if c == limit:
            break


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="convert tifs to pngs while preserving paths intelligently"
    )

    parser.add_argument(
        "-a",
        "--act",
        action="store_true",
        help="specify a limit to stop at",
    )

    parser.add_argument(
        "-l", "--limit", type=int, help="specify a limit to stop at", default=-1
    )

    parser.add_argument(
        "-f", "--filemask", help="specify a filemask", default="**/*.tif"
    )

    parser.add_argument(
        "dest",
        help="specify a destination directory to write to",
    )
    args = parser.parse_args()
    if args.limit:
        print(f"*Using limit {args.limit}")
    if args.act:
        print("*Act is True")
    print(f"Filemask {args.filemask}")

    c = 1
    for p in Path(".").glob(args.filemask):
        new_p = convert_path(
            p=p, dest=args.dest, act=args.act
        )  # haven't created new dir yet
        print(f"{c}:{p.name} -> {new_p}")
        if new_p.exists():
            print(f"   exists already")
        else:
            if args.act:
                convert_img(p, new_p)
        if c == args.limit:
            print("Limit reached!")
            break
        c += 1
