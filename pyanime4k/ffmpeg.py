#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: PyAnime4K FFmpeg handler
Author: TianZerL
Editor: K4YT3X
"""

# built-in imports
import pathlib

# third-party imports
import ffmpeg


def migrate_audio_streams(upscaled_video: pathlib.Path, original_video: pathlib.Path, output_path: pathlib.Path):
    upscaled_input = ffmpeg.input(str(upscaled_video.absolute()))
    original_input = ffmpeg.input(str(original_video.absolute()))

    # find upscaled video stream and original audio stream
    upscaled_video = upscaled_input.video
    original_audio = original_input.audio

    # create output file with selected streams
    output = ffmpeg.output(upscaled_video, original_audio, str(output_path.absolute()))
    output.run()
