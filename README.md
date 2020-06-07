# PyAnime4K

PyAnime4K is a simple, fast and powerful Anime4K Python implementation.

## Installation

```shell
pip install pyanime4k
```

## Usages

```python
import pyanime4k

# Quickly show a image which be processed by anime4k
pyanime4k.showImg2X("p1.png")

# Convert images by anime4k
pyanime4k.cvtImg2X("p1.png")
pyanime4k.cvtImg2X(("p2.png", "p3.png"), dstPath="./ouput")

# Convert videos by anime4k
pyanime4k.cvtVideo2X("p1.mp4")

# Manually
p = pyanime4k.Anime4K()

# Image processing
p.loadImage("p1.png")

# Show the infomation of processing
p.showInfo()

# start processing
p.process()

# Preview result
p.showImage()

# Save image
p.saveImage("p1_out.png")

#Video
p.loadVideo("p1.mp4")

# Video need specify the output file name in advance
p.setVideoSaveInfo("p1_out.mp4")
p.showInfo()
p.process()
p.saveVideo()
```

## Parameters

|Parameter|Description|
|-|-|
|input|File for loading|
|output|File for outputting|
|passes|Passes for processing|
|strengthColor|Strength for pushing color,range 0 to 1,higher for thinner|
|strengthGradient|Strength for pushing gradient,range 0 to 1,higher for sharper|
|zoomFactor|zoom factor for resizing|
|threads|Threads count for video processing|
|fastMode|Faster but maybe low quality|
|videoMode|Video process|

## Other Implementations

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
