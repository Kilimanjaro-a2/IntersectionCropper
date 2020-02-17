import sys
import numpy as np
from PIL import Image

def process_image(
    src_path="data/src.jpg",
    mask_path="data/mask.png",
    output_path="data/result.png"
):
    try:
        src = np.array(Image.open(src_path).convert("RGBA"))
        mask = np.array(
            Image.open(mask_path)
            .resize(src.shape[1::-1], Image.BILINEAR)
            .convert("RGBA")
        )

        src[mask[..., -1] == 0] = [255, 255, 255, 0]
        Image.fromarray(src).save('data/result.png')
        print("Created File: " + output_path)
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise

def main():
    process_image()

if __name__ == "__main__":
    main()
