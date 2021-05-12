#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: PyAnime4K acwrapper
Author: TianZerL
Editor: K4Yt3X
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
    os.environ["PATH"] += ";" + curr_path
    c_ac = ctypes.windll.LoadLibrary(os.path.join(curr_path, ac_lib[platform.system()]))
else:
    c_ac = ctypes.cdll.LoadLibrary(os.path.join(curr_path, ac_lib[platform.system()]))


class ac_parameters(ctypes.Structure):
    """
    typedef struct ac_parameters
    {
        int passes;
        int pushColorCount;
        double strengthColor;
        double strengthGradient;
        double zoomFactor;
        ac_bool fastMode;
        ac_bool preprocessing;
        ac_bool postprocessing;
        unsigned char preFilters;
        unsigned char postFilters;
        unsigned int maxThreads;
        ac_bool HDN;
        int HDNLevel;
        ac_bool alpha;
    } ac_parameters;
    """

    _fields_ = [
        ("passes", ctypes.c_int),
        ("pushColorCount", ctypes.c_int),
        ("strengthColor", ctypes.c_double),
        ("strengthGradient", ctypes.c_double),
        ("zoomFactor", ctypes.c_double),
        ("fastMode", ctypes.c_int),
        ("preprocessing", ctypes.c_int),
        ("postprocessing", ctypes.c_int),
        ("preFilters", ctypes.c_uint8),
        ("postFilters", ctypes.c_uint8),
        ("maxThreads", ctypes.c_uint),
        ("HDN", ctypes.c_int),
        ("HDNLevel", ctypes.c_int),
        ("alpha", ctypes.c_int),
    ]


class ac_version(ctypes.Structure):
    """
    typedef struct ac_version
    {
        char coreVersion[6];
        char wrapperVersion[6];
    } ac_version;
    """

    _fields_ = [
        ("coreVersion", ctypes.c_char * 6),
        ("wrapperVersion", ctypes.c_char * 6),
    ]


class ac_OpenCLAnime4K09Data(ctypes.Structure):
    """
    typedef struct ac_OpenCLAnime4K09Data
    {
        unsigned int pID;
        unsigned int dID;
        int OpenCLQueueNum;
        ac_bool OpenCLParallelIO;
    } ac_OpenCLAnime4K09Data;
    """

    _fields_ = [
        ("pID", ctypes.c_uint),
        ("dID", ctypes.c_uint),
        ("OpenCLQueueNum", ctypes.c_int),
        ("OpenCLParallelIO", ctypes.c_int),
    ]


class ac_OpenCLACNetData(ctypes.Structure):
    """
    typedef struct ac_OpenCLACNetData
    {
        unsigned int pID;
        unsigned int dID;
        int OpenCLQueueNum;
        ac_bool OpenCLParallelIO;
        ac_CNNType CNNType;
    } ac_OpenCLACNetData;
    """

    _fields_ = [
        ("pID", ctypes.c_uint),
        ("dID", ctypes.c_uint),
        ("OpenCLQueueNum", ctypes.c_int),
        ("OpenCLParallelIO", ctypes.c_int),
        ("CNNType", ctypes.c_int),
    ]


class ac_CUDAData(ctypes.Structure):
    """
    typedef struct ac_CUDAData
    {
        unsigned int dID;
    } ac_CUDAData;
    """

    _fields_ = [
        ("dID", ctypes.c_uint),
    ]


class ac_managerData(ctypes.Structure):
    """
    typedef struct ac_managerData
    {
        ac_OpenCLAnime4K09Data* OpenCLAnime4K09Data;
        ac_OpenCLACNetData* OpenCLACNetData;
        ac_CUDAData* CUDAData;
    } ac_managerData;
    """

    _fields_ = [
        ("OpenCLAnime4K09Data", ctypes.POINTER(ac_OpenCLAnime4K09Data)),
        ("OpenCLACNetData", ctypes.POINTER(ac_OpenCLACNetData)),
        ("CUDAData", ctypes.POINTER(ac_CUDAData)),
    ]


# ac_processType
(
    AC_CPU_Anime4K09,
    AC_CPU_ACNet,
    AC_OpenCL_Anime4K09,
    AC_OpenCL_ACNet,
    AC_Cuda_Anime4K09,
    AC_Cuda_ACNet,
) = (0, 1, 2, 3, 4, 5)


class ac_manager(object):
    AC_Manager_OpenCL_Anime4K09 = 1 << 0
    AC_Manager_OpenCL_ACNet = 1 << 1
    AC_Manager_Cuda = 1 << 2


# ac_bool
(AC_FALSE, AC_TRUE) = (0, 1)

# ac_error
(
    AC_OK,
    AC_ERROR_NULL_INSTANCE,
    AC_ERROR_NULL_PARAMETERS,
    AC_ERROR_NULL_Data,
    AC_ERROR_INIT_GPU,
    AC_ERROR_PORCESSOR_TYPE,
    AC_ERROR_LOAD_IMAGE,
    AC_ERROR_LOAD_VIDEO,
    AC_ERROR_INIT_VIDEO_WRITER,
    AC_ERROR_GPU_PROCESS,
    AC_ERROR_SAVE_TO_NULL_POINTER,
    AC_ERROR_NOT_YUV444,
    AC_ERROR_YUV444_AND_RGB32_AT_SAME_TIME,
    AC_ERROR_CUDA_NOT_SUPPORTED,
    AC_ERROR_VIDEO_MODE_UNINIT,
) = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

# ac_codec
(AC_OTHER, AC_MP4V, AC_DXVA, AC_AVC1, AC_VP09, AC_HEVC, AC_AV01) = (
    -1,
    0,
    1,
    2,
    3,
    4,
    5,
)

ac_instance = ctypes.c_void_p

ac_videoProcessor = ctypes.c_void_p

c_ac.acGetVersion.restype = ac_version

c_ac.acGetInstance2.restype = ac_instance

c_ac.acGetVideoProcessorFromInstance.restype = ac_videoProcessor

c_ac.acBenchmark2.restype = ctypes.c_double
