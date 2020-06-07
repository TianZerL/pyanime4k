# PyAnime4K

PyAnime4K is a simple, fast and powerful Anime4K Python implementation.

## Installation

PyAnime4K can be installed easily through `pip`.

```shell
pip install pyanime4k
```

## Usages

### Upscaling Images

```python
# pathlib.Path path objects are recommended instead of strings
import pathlib

# import pyanime4k library
import pyanime4k

# display single image upscaled with Anime4K
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

You may also create a low-level Anime4K object and handle each of the steps manually.

#### Images

```python
import pyanime4k

p = pyanime4k.Anime4K()

# upscaling a single image
p.loadImage('image1.png')

# show processing information
p.showInfo()

# start processing
p.process()

# preview upscaled image
p.showImage()

# save image to file
p.saveImage('image1_output.png')
```

#### Videos

```python
import pyanime4k

p = pyanime4k.Anime4K()

# load video file
p.loadVideo('video1.mp4')

# specify output video file name
# note that this needs to be done before processing starts
p.setVideoSaveInfo('video1_output.mp4')

# show processing information
p.showInfo()

# start processing
p.process()

# save video to file
p.saveVideo()
```

## Anime4K Parameters

|Parameter|Description|
|-|-|
|input|Input file path|
|output|Output file path|
|passes|Number of passes|
|strengthColor|Color pushing strength; ranges from 0 to 1; the higher the thinner|
|strengthGradient|Gradient pushing strength; ranges from 0 to 1; the higher the sharper|
|zoomFactor|Upscaling scaling factor|
|threads|Number of threads to use for video processing|
|fastMode|Process faster at a cost of potential lower output quality|
|videoMode|Run in video-processing mode|

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
