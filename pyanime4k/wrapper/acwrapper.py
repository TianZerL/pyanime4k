#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: PyAnime4K acwrapper
Author: TianZerL
Editor: TianZerL
"""

import ctypes
import os
import platform

ac_lib = {
    "Windows": "ac.dll",
    "Linux": "libac.so",
    "Darwin": "libac.dylib",
}

curr_path = os.path.dirname(os.path.realpath(__file__))

if platform.system() == "Windows":
    os.environ['PATH'] += (";" + curr_path)

c_ac = ctypes.cdll.LoadLibrary(
    os.path.join(curr_path, ac_lib[platform.system()]))


class ac_parameters(ctypes.Structure):
    '''
        typedef struct ac_parameters
        {
                int passes;
                int pushColorCount;
                float strengthColor;
                float strengthGradient;
                float zoomFactor;
                ac_bool fastMode;
                ac_bool videoMode;
                ac_bool preprocessing;
                ac_bool postprocessing;
                unsigned char preFilters;
                unsigned char postFilters;
                unsigned int maxThreads;
                ac_bool HDN;
        } ac_parameters;
    '''
    _fields_ = [
        ("passes", ctypes.c_int),
        ("pushColorCount", ctypes.c_int),
        ("strengthColor", ctypes.c_float),
        ("strengthGradient", ctypes.c_float),
        ("zoomFactor", ctypes.c_float),
        ("fastMode", ctypes.c_int),
        ("videoMode", ctypes.c_int),
        ("preprocessing", ctypes.c_int),
        ("postprocessing", ctypes.c_int),
        ("preFilters", ctypes.c_uint8),
        ("postFilters", ctypes.c_uint8),
        ("maxThreads", ctypes.c_uint),
        ("HDN", ctypes.c_int)
    ]


class ac_version(ctypes.Structure):
    '''
        typedef struct ac_version
        {
            char coreVersion[6];
            char wrapperVersion[6];
        } ac_version;
    '''
    _fields_ = [
        ("coreVersion", ctypes.c_char * 6),
        ("wrapperVersion", ctypes.c_char * 6),
    ]


# ac_processType
(
    AC_CPU,
    AC_GPU,
    AC_CPUCNN,
    AC_GPUCNN
) = (
    0, 1, 2, 3
)

# ac_bool
(
    AC_FALSE,
    AC_TRUE
) = (
    0, 1
)

# ac_error
(
    AC_OK,
    AC_ERROR_NULL_INSTANCE,
    AC_ERROR_NULL_PARAMETERS,
    AC_ERROR_INIT_GPU,
    AC_ERROR_PORCESSOR_TYPE,
    AC_ERROR_LOAD_IMAGE,
    AC_ERROR_LOAD_VIDEO,
    AC_ERROR_INIT_VIDEO_WRITER,
    AC_ERROR_GPU_PROCESS,
    AC_ERROR_SAVE_TO_NULL_POINTER,
    AC_ERROR_NOT_YUV444,
    AC_ERROR_VIDEO_MODE_UNINIT
) = (
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
)

# ac_codec
(
    AC_OTHER,
    AC_MP4V,
    AC_DXVA,
    AC_AVC1,
    AC_VP09,
    AC_HEVC,
    AC_AV01
) = (
    -1, 0, 1, 2, 3, 4, 5
)

ac_instance = ctypes.c_void_p

c_ac.acGetVersion.restype = ac_version

c_ac.acGetInstance.restype = ac_instance

c_ac.acGetResultDataLength.restype = ctypes.c_size_t
