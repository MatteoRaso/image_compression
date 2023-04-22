# Copyright 2023 Matteo raso
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
