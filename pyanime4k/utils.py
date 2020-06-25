#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: PyAnime4K utils
Author: TianZerL
Editor: TianZerL
"""

from pyanime4k import ffmpeg_handler
import contextlib
import os
import tempfile


def migrate_audio_streams(upscaled_video: str, original_video: str, output_path: str) -> None:
    """ migrate audio streams 

    Args:
        upscaled_video (str): path of upscaled video.
        original_video (str): path of original video.
        output_path (str): path to output result.

    Raises:
        FileExistsError: when output path exists and isn't a directory
    """
    ffmpeg_handler.migrate_audio_streams(upscaled_video=upscaled_video,
                                         original_video=original_video,
                                         output_path=output_path)

    with contextlib.suppress(FileNotFoundError):
        os.remove(upscaled_video)
