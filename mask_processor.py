import argparse
import sys
import numpy as np
from PIL import Image

def process_image(
    src_path="data/src.jpg",
    mask_path="data/mask.png",
    output_path="data/result.png"):
    try:
        src = np.array(Image.open(src_path).convert("RGBA"))
        mask = np.array(
            Image.open(mask_path)
            .resize(src.shape[1::-1], Image.BILINEAR)
            .convert("RGBA"))

        src[mask[..., -1] == 0] = [255, 255, 255, 0]
        Image.fromarray(src).save('data/result.png')
        print("Created File: " + output_path)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def main():
    main_arg_parser = argparse.ArgumentParser(
        description="The script to crop the area two images intersect")
    main_arg_parser.add_argument(
        '-s',
        '--source',
        type=str,
        default='data/src.jpg',
        help='The path of a source image')
    main_arg_parser.add_argument(
        '-m',
        '--mask',
        type=str,
        default='data/mask.png',
        help='The path of a mask image')
    main_arg_parser.add_argument(
        '-o',
        '--output',
        type=str,
        default='data/result.png',
        help="The path of a processed image")
    args = main_arg_parser.parse_args()

    process_image(args.source, args.mask, args.output)

if __name__ == "__main__":
    main()
