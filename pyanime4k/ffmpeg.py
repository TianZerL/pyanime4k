#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ffmpy3


def mergeAudio(srcV, srcA, dst):
    """Merge Audio from source file to the output file by FFmpeg"""

    f = ffmpy3.FFmpeg(
        inputs={srcV: None, srcA: None}, outputs={dst: "-c copy -map 0:0 -map 1:1 -y"}
    )
    f.run()
