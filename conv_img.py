"""
USAGE
convert -a -f **/*.tif -t .jpgPNG

- loop recursively through directories
- for every *.tif you find make a jpg and saved it to destination directory
- resize if over MAX_SIZE

if no dest specified
folder1/TIFF/filename.tif -> forder1/PNG/filename.png
"""

import argparse
from PIL import Image
from pathlib import Path


def convert_img(src: Path, dest: Path, max_size: int):
    print("   converting")
    img = Image.open(src)
    img = resize(img, max_size=max_size)
    img.save(dest, optimize=True)


def convert_path(*, p: Path, dest: str, target_suffix: str) -> Path:
    """
    from source path, create destination path and make all necessary directories on the way
    """
    name2 = p.with_suffix(target_suffix).name
    dest = Path(dest)
    p2 = dest / p.parent / name2
    return p2


def resize(img, *, max_size: int) -> Image:
    width, height = img.size
    if width > max_size or height > max_size:
        if width > height:
            factor = max_size / width
        else:  # height > width or both equal
            factor = max_size / height
        new_size = (int(width * factor), int(height * factor))
        print(f"   resize {factor:.0%} {new_size}")
        return img.resize(new_size, Image.LANCZOS)
    return img


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
        "-m", "--max_size", type=int, help="max size of pixel", default=6000
    )

    parser.add_argument(
        "-f", "--filemask", help="specify a filemask", default="**/*.tif"
    )

    parser.add_argument(
        "-t", "--target_suffix", help="specify target image format", default=".jpg"
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

    for c, p in enumerate(Path(".").glob(args.filemask), start=1):
        new_p = convert_path(
            p=p, dest=args.dest, target_suffix=args.target_suffix
        )  # haven't created new dir yet
        print(f"{c}:{p.name} -> {new_p}")
        if new_p.exists():
            print(f"   exists already")
        else:
            if args.act:
                new_p.parent.mkdir(parents=True, exist_ok=True)
                convert_img(p, new_p, max_size=args.max_size)
        if c == args.limit:
            print("Limit reached!")
            break
