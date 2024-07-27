"""Yet another CLI util to convert images"""

__version__ = "0.0.1"  # inital version

import argparse
from conv_img.conv_img import main


def conv_img():
    parser = argparse.ArgumentParser(
        description="Yet another CLI util to convert images"
    )

    parser.add_argument(
        "-a",
        "--act",
        action="store_true",
        help="signal to carry out conversion instead of just showing what would have been",
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
        "dest",
        help="destination directory to write to",
    )
    args = parser.parse_args()

    main(
        act=args.act,
        dest=args.dest,
        filemask=args.filemask,
        limit=args.limit,
        max_size=args.max_size,
        target_suffix=args.target_suffix,
    )
