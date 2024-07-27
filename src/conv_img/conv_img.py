"""
conv_img 
Yet another CLI utility to batch convert image files
"""

from PIL import Image
from pathlib import Path


def convert_img(src: Path, dest: Path, max_size: int) -> None:
    """Convert the image at src and save it at dest, resizing to max_size if original
    image exceeds max size."""
    #print("   converting")
    img = Image.open(src)
    img = resize(img, max_size=max_size)
    img.save(dest, optimize=True)


def convert_path(*, p: Path, dest: str, target_suffix: str) -> Path:
    """
    from source path, create destination path (not making any directories)
    """
    if dest == "%": # in place
        return p.with_suffix(target_suffix)
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
    if not target_suffix.startswith ("."):
        raise SyntaxError(f"The target suffix has to start with .: '{target_suffix}'")
    print(f"target suffix: {target_suffix}'")
    print(f"max_size: {max_size}")

    for c, p in enumerate(Path(".").glob(filemask), start=1):
        p2 = convert_path(
            p=p, dest=dest, target_suffix=target_suffix
        )  # haven't created new dir yet
        print(f"{c}:{p.name} -> {p2}")
        if p2.exists():
            print(f"   exists already")
        else:
            if act:
                p2.parent.mkdir(parents=True, exist_ok=True)
                convert_img(p, p2, max_size=max_size)
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
