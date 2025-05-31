# PyAnime4K

PyAnime4K is a high performance anime image upscaler based on [Anime4KCPP](https://github.com/TianZerL/Anime4KCPP).

# Install
PyAnime4K can be installed easily through pip.
```shell
pip install pyanime4k
```

You can also build the wheel by yourself.
```shell
# sudo apt install ocl-icd-opencl-dev cmake build-essential
get clone --recurse-submodules https://github.com/TianZerL/pyanime4k.git
cd pyanime4k
pip install scikit-build
python setup.py bdist_wheel
```

# Usages
## Printing Info
```python
import pyanime4k

# Print supported model
pyanime4k.print_model_list()

# Print supported processor
pyanime4k.print_processor_list()

# Print supported devices for image processing
pyanime4k.print_device_list()
```
## Upscaling Images
```python
import pyanime4k

# with OpenCL acceleration, if possible
processor_name = "opencl"

# upscale a single image
pyanime4k.upscale_images("image1.png", processor_name = processor_name)

# upscale a list of images
pyanime4k.upscale_images(["image1.png", "image2.png"], processor_name = processor_name)
```
## Manual Upscaling
```python
import pyanime4k

# Create a processor
processor = pyanime4k.Processor(
    processor_name="cpu",
    device_id=0,
    model_name="acnet-hdn0"
)
# Print processor info
print(processor)
# Read an image
src = pyanime4k.imread("image1.png")
# Process it
dst = processor(src=src, factor=2.0)
# Write to disk
pyanime4k.imwrite("image1_outout.png", dst)
```
## OpenCV
``` Python
import cv2, pyanime4k

img = cv2.imread("image.png")

processor = pyanime4k.Processor(
    processor_name="cpu",
    device_id=0,
    model_name="acnet-hdn0"
)

# opencv load image as BGR, but we need an RGB image
src = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

dst = processor(src)

img = cv2.cvtColor(dst, cv2.COLOR_RGB2BGR)

cv2.imshow("pyanime4k", img)
cv2.waitKey()
```
## Pillow
```python
from PIL import Image
import numpy, pyanime4k

img = Image.open("D:/temp/p1.png")

processor = pyanime4k.Processor(
    processor_name="cpu",
    device_id=0,
    model_name="acnet-hdn0"
)

# We need a numpy array
src = numpy.asarray(img)
dst = processor(src)
img = Image.fromarray(dst)

img.show()
```
