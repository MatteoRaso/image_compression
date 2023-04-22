import numpy as np
import sys
from imageio.v2 import imread, imwrite

def image_compression(filename):
    """
    A lossy compression algorithm for images.

    Parameters
    ----------
    filename: String, the name of the file we want to compress.

    Returns
    -------
    compressed_file: The compressed image
    """

    image = imread(filename)
    compressed_image = image.astype(np.uint8)
    imwrite("compressed_" + filename, compressed_image)

if sys.argv[1] is not None:
    image_compression(sys.argv[1])
