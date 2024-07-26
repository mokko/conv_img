"""Yet another CLI util to convert images"""

__version__ = "0.0.1"  # inital version

import argparse


def conv_img():
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
        "-f",
        "--filemask",
        help="specify a filemask, defaults to '**/*.tif'",
        default="**/*.tif",
    )

    parser.add_argument(
        "-t",
        "--target_suffix",
        help="specify target image format, defaults to '.jpg'",
        default=".jpg",
    )

    parser.add_argument(
        "dest",
        help="specify a destination directory to write to",
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
