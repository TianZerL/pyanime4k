#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: PyAnime4K upscaler
Author: TianZerL
Editor: K4YT3X
"""

# local imports
from pyanime4k import ffmpeg_handler
from pyanime4k.anime4k.anime4kcpp import Anime4K

# built-in imports
import contextlib
import pathlib
import shutil
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


def show_upscaled_image(source_path: pathlib.Path, *args):
    """ display an image processed by Anime4K

    Args:
        input_path (pathlib.Path): path of input image
        args: custom arguments passed to Anime4K

    Default args:
    int passes=2, double strengthColor=0.3, double strengthGradient=1.0,
    double zoomFactor=2.0, bool fastMode=False, bool videoMode=False(do not change it),
    unsigned int maxThreads=std::thread::hardware_concurrency())
    """

    anime4k_object = Anime4K(*args)
    anime4k_object.loadImage(source_path)
    anime4k_object.process()
    anime4k_object.showImage()


def upscale_images(input_paths: list, output_suffix="_output", output_path=None, *args):
    """ upscale a list of image files with Anime4K

    Args:
        input_paths (list): list of input file paths
        output_suffix (str, optional): output files. Defaults to "_output".
        output_path (pathlib.Path, optional): parent directory of output paths. Defaults to None.
        args: custom arguments passed to Anime4K

    Default args:
    int passes=2, double strengthColor=0.3, double strengthGradient=1.0,
    double zoomFactor=2.0, bool fastMode=False, bool videoMode=False(do not change it),
    unsigned int maxThreads=std::thread::hardware_concurrency())

    Raises:
        FileExistsError: when output path exists and isn't a directory
    """

    # sanitize input list
    input_paths = _sanitize_input_paths(input_paths)

    # if destination path unspecified
    if output_path is None:

        # destination path is first input file's parent directory
        output_path = input_paths.parent

    # if destination path doesn't exist
    if not output_path.exists():
        # create directory and its parents if necessary
        output_path.mkdir(parents=True, exist_ok=True)

    # else if it already exists but isn't a directory
    elif not output_path.is_dir():
        raise FileExistsError('destination path already exists and isn\'t a directory')

    # create Anime4K object
    anime4k_object = Anime4K(*args)

    # process each of the files in the list
    for path in input_paths:

        # anime4k load and process image
        anime4k_object.loadImage(path)
        anime4k_object.process()

        # construct destination file path object
        output_file_path = output_path / (path.stem + output_suffix, path.suffix)
        print(f'Saving file to: {output_file_path}')
        anime4k_object.saveImage(str(output_file_path))


def upscale_videos(input_paths: list, output_suffix="_output", output_path=None, *args):
    """ upscale a list of video files with Anime4k

    Args:
        input_paths (list): list of input file paths
        output_suffix (str, optional): output files suffix. Defaults to "_output".
        output_path (pathlib.Path, optional): parent directory of output paths. Defaults to None.
        args: custom arguments passed to Anime4K

    Default args:
    int passes=1, double strengthColor=0.3, double strengthGradient=1.0,
    double zoomFactor=2.0, bool fastMode=False, bool videoMode=True(do not change it),
    unsigned int maxThreads=std::thread::hardware_concurrency())

    Raises:
        FileExistsError: when output path exists and isn't a directory
    """

    # sanitize input list
    input_paths = _sanitize_input_paths(input_paths)

    # if destination path unspecified
    if output_path is None:

        # destination path is first input file's parent directory
        output_path = input_paths.parent

    # if destination path doesn't exist
    if not output_path.exists():
        # create directory and its parents if necessary
        output_path.mkdir(parents=True, exist_ok=True)

    # else if it already exists but isn't a directory
    elif not output_path.is_dir():
        raise FileExistsError('destination path already exists and isn\'t a directory')

    # if arguments are not specified, load default arguments
    if args is None:
        args = (1, 0.3, 1.0, 2.0, False, True)

    # create anime4k object
    anime4k_object = Anime4K(*args)

    # process each of the files in the list
    for path in input_paths:

        # create temporary directory to save the upscaled video
        temporary_directory = pathlib.Path(tempfile.mkdtemp())
        temporary_video_file_path = temporary_directory / 'temp.mp4'

        # process and save video file to temp/temp.mp4
        anime4k_object.setVideoSaveInfo(str(temporary_video_file_path))
        anime4k_object.loadVideo(path)
        anime4k_object.process()
        anime4k_object.saveVideo()

        ffmpeg_handler.migrate_audio_streams(upscaled_video=temporary_video_file_path,
                                             original_video=path,
                                             output_path=(output_path / (path.stem + output_suffix, path.suffix)))

        # delete temporary directory
        with contextlib.suppress(FileNotFoundError):
            shutil.rmtree(temporary_directory)
