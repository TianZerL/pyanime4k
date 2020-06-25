# PyAnime4K

PyAnime4K is a simple, fast and powerful Anime4K Python implementation.

## Installation

PyAnime4K can be installed easily through `pip`(For Windows).

```shell
pip install pyanime4k
```
## Compile Anime4KCPP for pyanime4k
1. Clone [Anime4KCPP](https://github.com/TianZerL/Anime4KCPP)
2. Follow [this](https://github.com/TianZerL/Anime4KCPP/wiki/Building), and for pyanime4k, only core and c wrapper is needed.  Make sure CMake option `Build_C_wrapper` is turned on, and if you want to build core and c wrapper in one file, turned on `Build_C_wrapper_with_core` (recommend)

## Manual installation
1. Clone the repo   
2. Download from release or compile the Anime4KCPP core and Anime4KCPP C Wrapper.  
3. - Copy `ac.dll` and `Anime4KCPPCore.dll` (if turned off Build_C_wrapper_with_core option of Anime4KCPP in CMake) and  `opencv_world430.dll` to the pyanime4k/wrapper (Windows)  
   - Copy `libac.so` to the pyanime4k/wrapper (Linux)  
   - Copy `libac.dylib` to the pyanime4k/wrapper (macOS)  
4. Enjoy  

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

### Preview a video with OpenCV

```python
from pyanime4k import ac
import cv2

video = cv2.VideoCapture(r"D:\Temp\anime4k\P1-1.m4v")
a = ac.AC()
while True:
    v,f = video.read()
    if not v:
        break
    # the default color format of OpenCV is BGR
    f = a.proccess_image_with_numpy(f)
    cv2.imshow("video", f)
    cv2.waitKey(1)

```

### Specify GPU

You can specify GPU for processing if you have more than one GPU

```python
from pyanime4k import ac

# print GPU list to get pID and dID of each GPU
ac.AC.list_GPUs()

# check GPU support
flag, info = ac.AC.check_GPU_support(pID=1, dID=0)

# init AC core with pID and dID
if flag:
    a = ac.AC(platformID=1, deviceID=0)

print(info)

# to check the current GPU
print(a.get_current_GPU_info())

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

# BGR, RGB and YUV444 is supported
a.load_image_from_numpy(img, input_type=ac.AC_INPUT_RGB)

# start processing
a.process()

# save image to numpy array
new_img = a.save_image_to_numpy()

new_img  = Image.fromarray(new_img)
new_img.show()

# from OpenCV
import cv2

img = cv2.imread(r"D:\Temp\anime4k\p1.png")

a.load_image_from_numpy(img,input_type=ac.AC_INPUT_BGR)
a.process()
img = a.save_image_to_numpy()

cv2.imshow("opencv", img)
cv2.waitKey(0)

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

# process with callback function
def print_progress_time(v, t):
    print("%.2f%% elapsed: %.2f remaining:  %.2f" % (v * 100, t, t/v - t), end="\r")

'''
#or
def print_progress(v):
    print("%.2f%%" % (v * 100), end="\r")
'''

# load video file
a.load_video(r"D:\Temp\anime4k\P1-1.m4v")

# specify output video file name
# note that this needs to be done before processing starts
a.set_save_video_info("output_tmp_.mp4", codec=ac.Codec.MP4V)

# start processing with progress value and time callback
a.process_with_progress_time_callback(print_progress_time)

'''
#or
# start processing with progress value callback
a.process_with_progress_callback(print_progress)
'''

# save video to file
a.save_video()

# save video to file
a.save_video()

# merge audio and auto delete tmp file
pyanime4k.migrate_audio_streams("output_tmp.mp4",r"D:\Temp\anime4k\P1-1.m4v","output.mp4")
```

### Process a video with OpenCV

```python
from pyanime4k import ac
import cv2
import time
import threading
import queue

# init VideoCapture and VideoWriter
videoReader = cv2.VideoCapture(r"D:\Temp\anime4k\P1-1.m4v")
fps = videoReader.get(cv2.CAP_PROP_FPS)
h = videoReader.get(cv2.CAP_PROP_FRAME_HEIGHT)
w = videoReader.get(cv2.CAP_PROP_FRAME_WIDTH)
videoWriter = cv2.VideoWriter(
    "output.mp4",
    cv2.VideoWriter_fourcc("m", "p", "4", "v"),
    fps,
    (int(w * 2), int(h * 2)),
)

# init Anime4KCPP
a = ac.AC(initGPU=False, initGPUCNN=True)

# frame queue
q = queue.Queue(12)

# write frames to disk
def writeFrames():
    while True:
        f = q.get()
        videoWriter.write(f)
        q.task_done()


# write frames in new thread
t = threading.Thread(target=writeFrames, daemon=True)
t.start()

s = time.time()

while True:
    v, f = videoReader.read()
    if not v:
        break
    f = a.proccess_image_with_numpy(f)
    q.put(f)

e = time.time()
print("time:", e - s, "s")

# wait for finished
q.join()

videoWriter.release()

```

## Other Anime4K Implementations

- Go
  - [TianZerL/Anime4KGo](https://github.com/TianZerL/Anime4KGo)
- C++
  - [TianZerL/Anime4KCPP](https://github.com/TianZerL/Anime4KCPP)
- C#
  - [shadow578/Anime4kSharp](https://github.com/shadow578/Anime4kSharp)
  - [net2cn/Anime4KSharp](https://github.com/net2cn/Anime4KSharp)
- GLSL
  - [bloc97/Anime4K](https://github.com/bloc97/Anime4K)
- Rust
  - [andraantariksa/Anime4K-rs](https://github.com/andraantariksa/Anime4K-rs)
