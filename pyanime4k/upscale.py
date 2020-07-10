#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: PyAnime4K upscaler
Author: TianZerL
Editor: K4YT3X, TianZerL
"""

# local imports
from pyanime4k import ffmpeg_handler
from pyanime4k.ac import AC
from pyanime4k.ac import Parameters
from pyanime4k.ac import Codec
from pyanime4k.ac import ProcessorType

# built-in imports
import pathlib
import os
import tempfile


def _sanitize_input_paths(input_paths):
    """ sanitize input file paths

    Args:
        input_paths (any): input paths variable to sanitize
    """
    sanitized_list = []

    # if input is single file in string format
    # convert it into pathlib.Path object
    if isinstance(input_paths, str):
        sanitized_list.append(pathlib.Path(input_paths))

    # if the input is single file instead of a list
    # convert it into a list
    elif isinstance(input_paths, pathlib.Path):
        sanitized_list.append(input_paths)

    # if the input is already a list
    # make sure all elements are path objects
    elif isinstance(input_paths, list):
        for path in input_paths:

            # if the path is not a pathlib.Path object
            # convert it into an object
            if not isinstance(path, pathlib.Path):
                sanitized_list.append(pathlib.Path(path))

            # otherwise, the path is clean
            else:
                sanitized_list.append(path)

    # return the sanitized lsit
    return sanitized_list


def show_upscaled_image(source_path: pathlib.Path, parameters: Parameters = Parameters(), GPU_mode: bool = False, ACNet: bool = True):
    """ display an image processed by Anime4K09 or ACNet

    Args:
        source_path: input file path.
        parameters (Parameters, optional): custom arguments passed to Anime4KCPP.
        GPU_mode (bool, optional): enable GPU mode. Defaults to False.
        ACNet (bool, optional): enable ACNet mode. Defaults to True.

    Raises:
        ACError
    """
    if GPU_mode:
        if ACNet:
            ac_object = AC(False, True, type=ProcessorType.GPUCNN,
                           parameters=parameters)
        else:
            ac_object = AC(True, False, type=ProcessorType.GPU,
                           parameters=parameters)
    else:
        if ACNet:
            ac_object = AC(False, False, type=ProcessorType.CPUCNN,
                           parameters=parameters)
        else:
            ac_object = AC(False, False, type=ProcessorType.CPU,
                           parameters=parameters)
    ac_object.load_image(str(source_path))
    ac_object.process()
    ac_object.show_image()


def upscale_images(input_paths: list, output_suffix: str = "_output", output_path: pathlib.Path = None, parameters: Parameters = Parameters(), GPU_mode: bool = False, ACNet: bool = True):
    """ upscale a list of image files with Anime4K

    Args:
        input_paths (list): list of input file paths
        output_suffix (str, optional): output files. Defaults to "_output".
        output_path (pathlib.Path, optional): parent directory of output paths. Defaults to None.
        parameters (Parameters, optional): custom arguments passed to Anime4KCPP.
        GPU_mode (bool, optional): enable GPU mode. Defaults to False.
        ACNet (bool, optional): enable ACNet mode. Defaults to True.

    Raises:
        FileExistsError: when output path exists and isn't a directory
        ACError
    """

    # sanitize input list
    input_paths = _sanitize_input_paths(input_paths)

    # if destination path unspecified
    if output_path is None:

        # destination path is first input file's parent directory
        output_path = input_paths[0].parent

    # if destination path doesn't exist
    if not output_path.exists():
        # create directory and its parents if necessary
        output_path.mkdir(parents=True, exist_ok=True)

    # else if it already exists but isn't a directory
    elif not output_path.is_dir():
        raise FileExistsError(
            'destination path already exists and isn\'t a directory')

    # create Anime4K object
    if GPU_mode:
        if ACNet:
            ac_object = AC(False, True, type=ProcessorType.GPUCNN,
                           parameters=parameters)
        else:
            ac_object = AC(True, False, type=ProcessorType.GPU,
                           parameters=parameters)
    else:
        if ACNet:
            ac_object = AC(False, False, type=ProcessorType.CPUCNN,
                           parameters=parameters)
        else:
            ac_object = AC(False, False, type=ProcessorType.CPU,
                           parameters=parameters)
    # process each of the files in the list
    for path in input_paths:

        # anime4k load and process image
        ac_object.load_image(str(path))
        ac_object.process()

        # construct destination file path object
        output_file_path = output_path.joinpath((path.stem + output_suffix + path.suffix))
            
        print(f'Saving file to: {output_file_path}')
        ac_object.save_image(str(output_file_path))


def upscale_videos(input_paths: list, output_suffix: str = "_output", output_path: pathlib.Path = None, parameters: Parameters = Parameters(), GPU_mode: bool = False, ACNet: bool = True, codec: Codec = Codec.MP4V):
    """ upscale a list of video files with Anime4k

    Args:
        input_paths (list): list of input file paths
        output_suffix (str, optional): output files suffix. Defaults to "_output".
        output_path (pathlib.Path, optional): parent directory of output paths. Defaults to None.
        parameters (Parameters, optional): custom arguments passed to Anime4KCPP.
        GPU_mode (bool, optional): enable GPU mode. Defaults to False.
        ACNet (bool, optional): enable ACNet mode. Defaults to True.
        codec (Codec, optional): codec for video encodeing.  Defaults to MP4V

    Raises:
        FileExistsError: when output path exists and isn't a directory
        ACError
    """

    # sanitize input list
    input_paths = _sanitize_input_paths(input_paths)

    # if destination path unspecified
    if output_path is None:

        # destination path is first input file's parent directory
        output_path = input_paths[0].parent

    # if destination path doesn't exist
    if not output_path.exists():
        # create directory and its parents if necessary
        output_path.mkdir(parents=True, exist_ok=True)

    # else if it already exists but isn't a directory
    elif not output_path.is_dir():
        raise FileExistsError(
            'destination path already exists and isn\'t a directory')

    # set parameters to video mode
    parameters.videoMode = True

    # create anime4k object
    if GPU_mode:
        if ACNet:
            ac_object = AC(False, True, type=ProcessorType.GPUCNN,
                           parameters=parameters)
        else:
            ac_object = AC(True, False, type=ProcessorType.GPU,
                           parameters=parameters)
    else:
        if ACNet:
            ac_object = AC(False, False, type=ProcessorType.CPUCNN,
                           parameters=parameters)
        else:
            ac_object = AC(False, False, type=ProcessorType.CPU,
                           parameters=parameters)

    # process each of the files in the list
    for path in input_paths:

        # create temporary directory to save the upscaled video
        temporary_directory = pathlib.Path(tempfile.mkdtemp())
        temporary_video_file_path = temporary_directory.joinpath('temp.mp4')

        # process and save video file to temp/temp.mp4
        ac_object.load_video(str(path))
        ac_object.set_save_video_info(str(temporary_video_file_path), codec)
        ac_object.process_with_progress()
        ac_object.save_video()

        ffmpeg_handler.migrate_audio_streams(upscaled_video=temporary_video_file_path,
                                             original_video=path,
                                             output_path=(output_path.joinpath(path.stem + output_suffix + path.suffix)))
