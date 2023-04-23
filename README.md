# A CLI Lossy Image Compression Program

# Requirements

This program requires `imageio` to be installed.

# How To Use

To compress an image called `foo.png`, type in

```
>>>python image_compression.py foo.png
```

This will output an image called `compressed_foo.png`.

#Warning

While the loss of quality is usually minimal, certain images become almost
completely blacked out. It's not certain what causes this, but it seems to
mostly affect images that were already black and white. Always make sure
that the quality of the compressed image is good before deleting the original.

# License

This program is licensed under the Apache 2.0 license.
