import numpy as np
from PIL import Image

src = np.array(Image.open('data/src.jpg').convert("RGBA"))
mask = np.array(
    Image.open('data/mask.png')
    .resize(src.shape[1::-1], Image.BILINEAR)
    .convert("RGBA")
)
src[mask[..., -1] == 0] = [255, 255, 255, 0]

Image.fromarray(src).save('data/result.png')
