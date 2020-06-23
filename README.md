# PyAnime4K

PyAnime4K is a simple, fast and powerful Anime4K Python implementation.

## Installation

PyAnime4K can be installed easily through `pip`(For Windows).

```shell
pip install pyanime4k
```

## Manual installation
Clone the repo
Download from release or compile the Anime4KCPP core and Anime4KCPP C Wrapper.
Copy `ac.dll` and `Anime4KCPPCore.dll` and  `opencv_world430.dll` to the pyanime4k/wrapper(Windows)
Copy `libac.so` and `libAnime4KCPPCore.so` to the pyanime4k/wrapper(Linux)
Copy `libac.dylib` and `libAnime4KCPPCore.dylib` to the pyanime4k/wrapper(macOS)
Enjoy

## Usages

### Upscaling Images

```python
# pathlib.Path path objects are recommended instead of strings
import pathlib

# import pyanime4k library
import pyanime4k

# display single image upscaled with Anime4KCPP
pyanime4k.show_upscaled_image(pathlib.Path('image1.png'))

# upscale a single image
pyanime4k.upscale_images(pathlib.Path('image1.png'))

# upscale a list of images
images = [
    pathlib.Path('image1.png'),
    pathlib.Path('image2.png')
]

pyanime4k.upscale_images(
    inpuat_paths=images,
    output_path=pathlib.Path('./output')
)
```

### Upscaling Videos

```python
# pathlib.Path path objects are recommended instead of strings
import pathlib

# import pyanime4k library
import pyanime4k

# upscale a single video file
pyanime4k.upscale_videos(pathlib.Path('video1.mp4'))

# upscale multiple files
videos = [
    pathlib.Path('video1.mp4'),
    pathlib.Path('video2.mp4')
]

pyanime4k.upscale_videos(
    input_paths=videos,
    output_path=pathlib.Path('./output')
)
```

### Manual Upscaling

You may also create a low-level AC object and handle each of the steps manually.

```python
from pyanime4k import ac
import pyanime4k

parameters = ac.Parameters()
# enable HDN for ACNet
parameters.HDN = True

a = ac.AC(initGPUCNN = True, parameters = parameters, type=ac.ProcessorType.GPUCNN)

# load image from file
a.load_image(r"D:\Temp\anime4k\p1.png")

# start processing
a.process()

# preview upscaled image
a.show_image()

# save image to file
a.save_image('image1_output.png')

# from PIL and numpy
import numpy as np
from PIL import Image

img = Image.open(r"D:\Temp\anime4k\p1.png").convert("RGB")
img = np.array(img)

# RGB and YUV444 is supported
a.load_image_from_numpy(img, input_type=ac.AC_INPUT_RGB)

# start processing
a.process()

# save image to numpy array
new_img = a.save_image_to_numpy()

new_img  = Image.fromarray(new_img)
new_img.show()

# save image to file
a.save_image('image1_output_1.png')

# let's process video
a.set_video_mode(True)

# load video file
a.load_video(r"D:\Temp\anime4k\P1-1.m4v")

# specify output video file name
# note that this needs to be done before processing starts
a.set_save_video_info("output_tmp.mp4", codec=ac.Codec.MP4V)

# start processing with progress
a.process_with_progress()

# save video to file
a.save_video()

# merge audio and auto delete tmp file
pyanime4k.migrate_audio_streams("output_tmp.mp4",r"D:\Temp\anime4k\P1-1.m4v","output.mp4")
```

## Other Anime4K Implementations

- Go
  - [TianZerL/Anime4KGo](https://github.com/TianZerL/Anime4KGo)
- C++
  - [TianZerL/Anime4KCPP](https://github.com/TianZerL/Anime4KCPP)
- C#
  - [shadow578/Anime4kSharp](https://github.com/shadow578/Anime4kSharp)
  - [net2cn/Anime4KSharp](https://github.com/net2cn/Anime4KSharp)
- Java
  - [bloc97/Anime4K](https://github.com/bloc97/Anime4K)
- Rust
  - [andraantariksa/Anime4K-rs](https://github.com/andraantariksa/Anime4K-rs)
