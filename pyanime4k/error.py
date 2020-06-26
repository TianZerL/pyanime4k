#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: PyAnime4K error
Author: TianZerL
Editor: TianZerL
"""

from pyanime4k.wrapper import *

'''
	typedef enum ac_error
	{
		AC_OK = 0,
		AC_ERROR_NULL_INSTANCE,
		AC_ERROR_NULL_PARAMETERS,
		AC_ERROR_INIT_GPU,
		AC_ERROR_PORCESSOR_TYPE,
		AC_ERROR_LOAD_IMAGE,
		AC_ERROR_LOAD_VIDEO,
		AC_ERROR_INIT_VIDEO_WRITER,
		AC_ERROR_GPU_PROCESS,
		AC_ERROR_SAVE_TO_NULL_POINTER,
		AC_ERROR_NOT_YUV444
	} ac_error;
'''

error_code_str = {
    AC_OK: "AC_OK",
    AC_ERROR_NULL_INSTANCE: "AC_ERROR_NULL_INSTANCE",
    AC_ERROR_NULL_PARAMETERS: "AC_ERROR_NULL_PARAMETERS",
    AC_ERROR_INIT_GPU: "AC_ERROR_INIT_GPU",
    AC_ERROR_PORCESSOR_TYPE: "AC_ERROR_PORCESSOR_TYPE",
    AC_ERROR_LOAD_IMAGE: "AC_ERROR_LOAD_IMAGE",
    AC_ERROR_LOAD_VIDEO: "AC_ERROR_LOAD_VIDEO",
    AC_ERROR_INIT_VIDEO_WRITER: "AC_ERROR_INIT_VIDEO_WRITER",
    AC_ERROR_GPU_PROCESS: "AC_ERROR_GPU_PROCESS",
    AC_ERROR_SAVE_TO_NULL_POINTER: "AC_ERROR_SAVE_TO_NULL_POINTER",
    AC_ERROR_NOT_YUV444: "AC_ERROR_NOT_YUV444",
    AC_ERROR_VIDEO_MODE_UNINIT: "AC_ERROR_VIDEO_MODE_UNINIT",
}


class ACError(Exception):
    def __init__(self, code, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.msg = error_code_str[code]

    def __str__(self):
        return "AC error: %s" % (self.msg)
