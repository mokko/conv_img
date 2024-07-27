"""
USAGE:
    conv_img -m 7000 -a -f **/*.tif -t .jpg dest_dir
    conv_img dest_folder
"""

from PIL import Image
from pathlib import Path


def convert_img(src: Path, dest: Path, max_size: int) -> None:
    """Convert the image at src and save it at dest, resizing to max_size if original
    image exceeds max size."""
    print("   converting")
    img = Image.open(src)
    img = resize(img, max_size=max_size)
    img.save(dest, optimize=True)


def convert_path(*, p: Path, dest: str, target_suffix: str) -> Path:
    """
    from source path, create destination path (not making any directories)
    """
    name2 = p.with_suffix(target_suffix).name
    return Path(dest) / p.parent / name2


def main(
    *,
    act: bool,
    dest: str,
    filemask: str,
    limit: int,
    target_suffix: str,
    max_size: int,
) -> None:
    if limit:
        print(f"limit: {limit}")
    if act:
        print("act: True")
    print(f"filemask: {filemask}")
    print(f"target suffix: {target_suffix}'")
    print(f"max_size: {max_size}")

    for c, p in enumerate(Path(".").glob(filemask), start=1):
        new_p = convert_path(
            p=p, dest=dest, target_suffix=target_suffix
        )  # haven't created new dir yet
        print(f"{c}:{p.name} -> {new_p}")
        if new_p.exists():
            print(f"   exists already")
        else:
            if act:
                new_p.parent.mkdir(parents=True, exist_ok=True)
                convert_img(p, new_p, max_size=max_size)
        if c == limit:
            print("Limit reached!")
            break


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
    pass
