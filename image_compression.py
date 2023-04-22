import sys
from imageio.v3 import imread, imwrite

def image_compression(filename):
    """
    A lossless compression algorithm for images.

    Parameters
    ----------
    filename: String, the name of the file we want to compress.

    Returns
    -------
    compressed_file: The compressed image
    """

    image = imread(filename)
    imwrite("compressed_" + filename, image)

if sys.argv[1] is not None:
    image_compression(sys.argv[1])
