"""
conv_img
Yet another CLI utility to batch convert image files
"""

from PIL import Image as Img
from PIL.Image import Image
from pathlib import Path
import argparse

_verbose = False


def arg():
    parser = argparse.ArgumentParser(
        description="Yet another CLI util to convert images"
    )

    parser.add_argument(
        "-a",
        "--act",
        action="store_true",
        help="carry out conversion instead of just showing what would have been",
    )

    parser.add_argument(
        "-f",
        "--filemask",
        help="the filemask that identifies which images will be converted, defaults to '**/*.tif'",
        default="**/*.tif",
    )

    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        help="number of images after which script breaks off, defaults to -1 (no limit)",
        default=-1,
    )

    parser.add_argument(
        "-m",
        "--max_size",
        type=int,
        help="max size of pixel, defaults to 6000 pixel for the longest size",
        default=6000,
    )

    parser.add_argument(
        "-t",
        "--target_suffix",
        help="target image format, defaults to '.jpg'",
        default=".jpg",
    )

    parser.add_argument(
        "-v",
        "--verbose",
        help="for more verbose output",
        action="store_true",
    )

    parser.add_argument(
        "dest_dir",
        help="destination directory to write to",
    )
    args = parser.parse_args()

    main(
        act=args.act,
        dest_dir=args.dest_dir,
        filemask=args.filemask,
        limit=args.limit,
        max_size=args.max_size,
        target_suffix=args.target_suffix,
    )


def convert_img(src: Path, dest: Path, max_size: int) -> None:
    """
    Convert the image at src and save it at dest, resizing to max_size if original image
    exceeds max size.
    """
    # print("   converting")
    img = Img.open(src)
    img = resize(img, max_size=max_size)
    img.save(dest, optimize=True)


def convert_path(*, p: Path, dest_dir: str, target_suffix: str) -> Path:
    """
    from source path p create destination path (not making any directories)

    If dest_dir is %, we save the new image file in-place, i.e. we return a path in the
    same folder as the original.
    """
    if dest_dir == "%":
        return p.with_suffix(target_suffix)
    return Path(dest_dir) / p.parent / p.with_suffix(target_suffix).name


def main(
    *,
    act: bool,
    dest_dir: str,
    filemask: str,
    limit: int,
    target_suffix: str,
    max_size: int,
    verbose: bool = False,
) -> None:
    if verbose:
        global _verbose
        _verbose = True

    show_state(
        act=act,
        dest_dir=dest_dir,
        filemask=filemask,
        limit=limit,
        max_size=max_size,
        target_suffix=target_suffix,
    )

    for c, p in enumerate(Path(".").glob(filemask), start=1):
        p2 = convert_path(
            p=p, dest_dir=dest_dir, target_suffix=target_suffix
        )  # haven't created new dir yet
        print(f"{c}:{p.name} -> {p2}")
        if p2.exists():
            v(f"   exists already")
        else:
            if act:
                p2.parent.mkdir(parents=True, exist_ok=True)
                convert_img(p, p2, max_size=max_size)
        if c == limit:
            print("Limit reached!")
            break


def resize(img, *, max_size: int) -> Image:
    """
    Receive an image object, resize it to max_size if longest side exceeds that
    number of pixels and return the image object.
    """
    width, height = img.size
    if width > max_size or height > max_size:
        if width > height:
            factor = max_size / width
        else:  # height > width or both equal
            factor = max_size / height
        new_size = (int(width * factor), int(height * factor))
        v(f"   resize {factor:.0%} {new_size}")
        return img.resize(new_size, Img.LANCZOS)
    return img


def show_state(
    *,
    act: bool,
    dest_dir: str,
    filemask: str,
    limit: int,
    max_size: int,
    target_suffix: str,
) -> None:
    """
    Print state to STDOUT if global flag _verbose is set.
    """
    if limit:
        v(f"limit: {limit}")
    if act:
        v("act: True")
    v(f"filemask: {filemask}")
    if not target_suffix.startswith("."):
        raise SyntaxError(f"The target suffix has to start with .: '{target_suffix}'")
    v(f"target suffix: {target_suffix}'")
    v(f"max_size: {max_size}")


def v(msg: str) -> None:
    if _verbose:
        print(msg)


if __name__ == "__main__":
    arg()
