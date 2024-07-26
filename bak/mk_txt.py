"""
Make a text file per folder and pre-fill it with some info
"""

from pathlib import Path


def write_file(fn, adir):
    print(f"Writing file {fn}")
    with open(fn, "w") as file:
        file.write(f"Magazin:{adir}\n")
        file.write("Aufnahme Datum/Jahr:\n")
        file.write("Aufnahme Ort(e):\n")
        file.write("Wer ist zu sehen:\n\n")
        file.write("Was ist zu sehen:\n\n")
        file.write("Was sollen wir noch zu den Fotos für die Nachwelt hinterlegen?:\n")


# start from pwd
for p in Path().glob("**/*"):
    if p.is_dir() and len(p.parents) == 2:
        print(f"{p.name}")
        fn = p / "Dokumentation.txt"
        if not fn.exists():
            write_file(fn, p.name)
        # raise SyntaxError("Stop here")
