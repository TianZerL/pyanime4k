#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: PyAnime4K ac
Author: TianZerL
Editor: K4YT3X
"""

from pyanime4k.wrapper import *
from pyanime4k.error import ACError
import numpy as np
import multiprocessing


(AC_INPUT_BGR, AC_INPUT_RGB, AC_INPUT_YUV444, AC_INPUT_RGB32, AC_INPUT_BGR32) = (
    0,
    1,
    2,
    3,
    4,
)
(AC_PROCESS_PAUSED, AC_PROCESS_STOP, AC_PROCESS_RUNNING) = (0, 1, 2)


class Version(object):
    pyanime4k = "2.5.1"

    def __init__(self):
        ac_version = c_ac.acGetVersion()
        self.core = str(ac_version.coreVersion, "utf-8")
        self.wrapper = str(ac_version.wrapperVersion, "utf-8")

    def __str__(self):
        return (
            f"Version information:\n"
            f"  pyanime4k: {self.pyanime4k}\n"
            f"  core:      {self.core}\n"
            f"  C wrapper: {self.wrapper}"
        )


class Parameters(object):
    def __init__(self):
        self.passes = 2
        self.pushColorCount = 2
        self.strengthColor = 0.3
        self.strengthGradient = 1.0
        self.zoomFactor = 2.0
        self.fastMode = False
        self.videoMode = False
        self.preprocessing = False
        self.postprocessing = False
        self.preFilters = 4
        self.postFilters = 40
        self.maxThreads = multiprocessing.cpu_count()
        self.HDN = False
        self.HDNLevel = 1
        self.alpha = False

    def reset(self):
        self.passes = 2
        self.pushColorCount = 2
        self.strengthColor = 0.3
        self.strengthGradient = 1.0
        self.zoomFactor = 2.0
        self.fastMode = False
        self.videoMode = False
        self.preprocessing = False
        self.postprocessing = False
        self.preFilters = 4
        self.postFilters = 40
        self.maxThreads = multiprocessing.cpu_count()
        self.HDN = False
        self.HDNLevel = 1
        self.alpha = False

    def print_info(self):
        print(
            "passes:            %d\n"
            "pushColorCount:    %d\n"
            "strengthColor:     %.2f\n"
            "strengthGradient:  %.2f\n"
            "zoomFactor:        %.2f\n"
            "fastMode:          %r\n"
            "videoMode:         %r\n"
            "preprocessing:     %r\n"
            "postprocessing:    %r\n"
            "preFilters:        %d\n"
            "postFilters:       %d\n"
            "maxThreads:        %d\n"
            "HDN:               %r\n"
            "HDNLevel           %r\n"
            "alpha              %r"
            % (
                self.passes,
                self.pushColorCount,
                self.strengthColor,
                self.strengthGradient,
                self.zoomFactor,
                self.fastMode,
                self.videoMode,
                self.preprocessing,
                self.postprocessing,
                self.preFilters,
                self.postFilters,
                self.maxThreads,
                self.HDN,
                self.HDNLevel,
                self.alpha,
            )
        )


class ProcessorType(object):
    """
    processor type of AC

    AUTO will AC set to GPUCNN and initialize GPUCNN if available, otherwise set it to CPUCNN
    """

    CPU_Anime4K09 = AC_CPU_Anime4K09
    CPU_ACNet = AC_CPU_ACNet
    OpenCL_Anime4K09 = AC_OpenCL_Anime4K09
    OpenCL_ACNet = AC_OpenCL_ACNet
    Cuda_Anime4K09 = AC_Cuda_Anime4K09
    Cuda_ACNet = AC_Cuda_ACNet

    type_code_str = {
        CPU_Anime4K09: " CPU_Anime4K09",
        CPU_ACNet: "CPU_ACNet",
        OpenCL_Anime4K09: "OpenCL_Anime4K09",
        OpenCL_ACNet: "OpenCL_ACNet",
        Cuda_Anime4K09: "Cuda_Anime4K09",
        Cuda_ACNet: "Cuda_ACNet",
    }


class Codec(object):
    OTHER = AC_OTHER
    MP4V = AC_MP4V
    DXVA = AC_DXVA
    AVC1 = AC_AVC1
    VP09 = AC_VP09
    HEVC = AC_HEVC
    AV01 = AC_AV01


class CNNType(object):
    AC_Default = 0
    AC_ACNetHDNL0 = 1
    AC_ACNetHDNL1 = 2
    AC_ACNetHDNL2 = 3
    AC_ACNetHDNL3 = 4


class GPGPUModel(object):
    AC_CUDA = 0
    AC_OpenCL = 1


class OpenCLAnime4K09Manager(object):
    def __init__(
        self,
        pID: int = 0,
        dID: int = 0,
        OpenCLQueueNum: int = 4,
        OpenCLParallelIO: bool = False,
    ):
        self.pID = pID
        self.dID = dID
        self.OpenCLQueueNum = OpenCLQueueNum
        self.OpenCLParallelIO = OpenCLParallelIO

    def _get_manager_data(self):
        manager_data = ac_OpenCLAnime4K09Data()
        manager_data.pID = ctypes.c_uint(self.pID)
        manager_data.dID = ctypes.c_uint(self.dID)
        manager_data.OpenCLQueueNum = ctypes.c_int(self.OpenCLQueueNum)
        manager_data.OpenCLParallelIO = ctypes.c_int(self.OpenCLParallelIO)
        return manager_data


class OpenCLACNetManager(object):
    def __init__(
        self,
        pID: int = 0,
        dID: int = 0,
        CNN: int = CNNType.AC_Default,
        OpenCLQueueNum: int = 4,
        OpenCLParallelIO: bool = False,
    ):
        self.pID = pID
        self.dID = dID
        self.CNNType = CNN
        self.OpenCLQueueNum = OpenCLQueueNum
        self.OpenCLParallelIO = OpenCLParallelIO

    def _get_manager_data(self):
        manager_data = ac_OpenCLACNetData()
        manager_data.pID = ctypes.c_uint(self.pID)
        manager_data.dID = ctypes.c_uint(self.dID)
        manager_data.OpenCLQueueNum = ctypes.c_int(self.OpenCLQueueNum)
        manager_data.OpenCLParallelIO = ctypes.c_int(self.OpenCLParallelIO)
        manager_data.CNNType = ctypes.c_int(self.CNNType)
        return manager_data


class CUDAManager(object):
    def __init__(self, dID: int = 0):
        self.dID = dID

    def _get_manager_data(self):
        manager_data = ac_CUDAData()
        manager_data.dID = ctypes.c_uint(self.dID)
        return manager_data


class ManagerList(object):
    def __init__(self, managerList: list):
        self._manager_data = ac_managerData()
        self._manager_mask = 0
        for manager in managerList:
            if isinstance(manager, OpenCLAnime4K09Manager):
                self._manager_mask |= ac_manager.AC_Manager_OpenCL_Anime4K09
                self._manager_data.OpenCLAnime4K09Data = ctypes.pointer(
                    manager._get_manager_data()
                )
            elif isinstance(manager, OpenCLACNetManager):
                self._manager_mask |= ac_manager.AC_Manager_OpenCL_ACNet
                self._manager_data.OpenCLACNetData = ctypes.pointer(
                    manager._get_manager_data()
                )
            elif isinstance(manager, CUDAManager):
                self._manager_mask |= ac_manager.AC_Manager_Cuda
                self._manager_data.CUDAData = ctypes.pointer(
                    manager._get_manager_data()
                )

    def get_managers(self):
        return self._manager_mask

    def get_manager_data(self):
        return self._manager_data


class AC(object):
    """
    Anime4KCPP core in python
    """

    def __get_c_parameters(self, parameters):
        c_struct = ac_parameters()
        c_struct.passes = ctypes.c_int(parameters.passes)
        c_struct.pushColorCount = ctypes.c_int(parameters.pushColorCount)
        c_struct.strengthColor = ctypes.c_double(parameters.strengthColor)
        c_struct.strengthGradient = ctypes.c_double(parameters.strengthGradient)
        c_struct.zoomFactor = ctypes.c_double(parameters.zoomFactor)
        c_struct.fastMode = ctypes.c_int(parameters.fastMode)
        c_struct.videoMode = ctypes.c_int(parameters.videoMode)
        c_struct.preprocessing = ctypes.c_int(parameters.preprocessing)
        c_struct.postprocessing = ctypes.c_int(parameters.postprocessing)
        c_struct.preFilters = ctypes.c_uint8(parameters.preFilters)
        c_struct.postFilters = ctypes.c_uint8(parameters.postFilters)
        c_struct.maxThreads = ctypes.c_uint(parameters.maxThreads)
        c_struct.HDN = ctypes.c_int(parameters.HDN)
        c_struct.HDNLevel = ctypes.c_int(parameters.HDNLevel)
        c_struct.alpha = ctypes.c_int(parameters.alpha)
        return c_struct

    def __init__(
        self,
        managerList: ManagerList = None,
        parameters: Parameters = Parameters(),
        type: ProcessorType = ProcessorType.CPU_ACNet,
    ):
        err = ctypes.c_int(AC_OK)
        self.ac_object = c_ac.acGetInstance2(
            ctypes.c_uint(managerList.get_managers() if managerList is not None else 0),
            ctypes.byref(managerList.get_manager_data())
            if managerList is not None
            else None,
            ctypes.byref(self.__get_c_parameters(parameters)),
            ctypes.c_int(type),
            ctypes.pointer(err),
        )
        if err.value != AC_OK:
            raise ACError(err.value)

        self.parameters = parameters
        self.ac_object = ctypes.c_void_p(self.ac_object)

        self.input_type = AC_INPUT_BGR
        self.processor_type = type

        self.process_status = AC_PROCESS_STOP

    def __del__(self):
        c_ac.acFreeInstance2(self.ac_object)

    @staticmethod
    def get_version() -> Version:
        """
        return the version of Anime4kCPP core and pyanime4k
        """
        return Version()

    def get_processor_type(self) -> str:
        """
        return the processor type string
        """
        return ProcessorType.type_code_str[self.processor_type]

    def set_video_mode(self, flag: bool = True):
        err = c_ac.acSetVideoMode(self.ac_object, ctypes.c_int(flag))
        if err != AC_OK:
            raise ACError(err)
        self.parameters.videoMode = flag

    def set_arguments(self, parameters: Parameters):
        err = c_ac.acSetArguments(
            self.ac_object, ctypes.byref(self.__get_c_parameters(parameters))
        )
        if err != AC_OK:
            raise ACError(err)

        self.parameters = parameters

    def load_image(self, src_path: str):
        """
        load an image from disk
        """
        err = c_ac.acLoadImage(self.ac_object, ctypes.c_char_p(src_path.encode('utf-8')))
        if err != AC_OK:
            raise ACError(err)

    def load_video(self, src_path: str):
        """
        load a video from disk
        """
        if self.parameters.videoMode is False:
            raise ACError(AC_ERROR_VIDEO_MODE_UNINIT)
        err = c_ac.acLoadVideo(self.ac_object, ctypes.c_char_p(src_path.encode('utf-8')))
        if err != AC_OK:
            raise ACError(err)

    def set_save_video_info(
        self, dst_path: str, codec: Codec = Codec.MP4V, fps: float = 0
    ):
        """
        set output video saving path and codec, should be called before calling process

        set fps to 0 for automatic detection
        """
        err = c_ac.acSetSaveVideoInfo(
            self.ac_object,
            ctypes.c_char_p(dst_path.encode('utf-8')),
            ctypes.c_int(codec),
            ctypes.c_double(fps),
        )
        if err != AC_OK:
            raise ACError(err)

    def process(self):
        """
        process image or video
        """
        self.process_status = AC_PROCESS_RUNNING

        err = c_ac.acProcess(self.ac_object)
        if err != AC_OK:
            raise ACError(err)

        self.process_status = AC_PROCESS_STOP

    def process_with_progress(self):
        """
        process video with progress displaying
        """
        self.process_status = AC_PROCESS_RUNNING

        err = c_ac.acProcessWithPrintProgress(self.ac_object)
        if err != AC_OK:
            raise ACError(err)

        self.process_status = AC_PROCESS_STOP

    def process_with_progress_callback(self, func):
        """
        process video with callback function:

        func(v :float) -> None

        v: progress value (0 to 1)
        """
        self.process_status = AC_PROCESS_RUNNING

        c_callback = ctypes.CFUNCTYPE(None, ctypes.c_double)
        err = c_ac.acProcessWithProgress(self.ac_object, c_callback(func))
        if err != AC_OK:
            raise ACError(err)

        self.process_status = AC_PROCESS_STOP

    def process_with_progress_time_callback(self, func):
        """
        process video with callback function:

        func(v :float, t: float) -> None

        v: progress value (0 to 1)

        t: time used
        """
        self.process_status = AC_PROCESS_RUNNING

        c_callback = ctypes.CFUNCTYPE(None, ctypes.c_double, ctypes.c_double)
        err = c_ac.acProcessWithProgressTime(self.ac_object, c_callback(func))
        if err != AC_OK:
            raise ACError(err)

        self.process_status = AC_PROCESS_STOP

    def pause_video_process(self):
        """
        pause video processing
        """
        err = c_ac.acPauseVideoProcess(self.ac_object)
        if err != AC_OK:
            raise ACError(err)

        self.process_status = AC_PROCESS_PAUSED

    def continue_video_process(self):
        """
        continue video processing
        """
        err = c_ac.acContinueVideoProcess(self.ac_object)
        if err != AC_OK:
            raise ACError(err)

        self.process_status = AC_PROCESS_RUNNING

    def stop_video_process(self):
        """
        stop video processing
        """
        err = c_ac.acStopVideoProcess(self.ac_object)
        if err != AC_OK:
            raise ACError(err)

        self.process_status = AC_PROCESS_STOP

    def get_process_status(self) -> int:
        return self.process_status

    def save_image(self, dst_path: str):
        """
        save image to disk
        """
        err = c_ac.acSaveImage(self.ac_object, ctypes.c_char_p(dst_path.encode('utf-8')))
        if err != AC_OK:
            raise ACError(err)

    def save_video(self):
        """
        compete output video, should be called after calling process
        """
        err = c_ac.acSaveVideo(self.ac_object)
        if err != AC_OK:
            raise ACError(err)

    def show_image(self):
        """
        quickly show image which has been inputted
        """
        err = c_ac.acShowImage(self.ac_object, ctypes.c_int(self.input_type))
        if err != AC_OK:
            raise ACError(err)

    def init_GPU(self):
        """
        initialize GPU for GPU mode
        """
        err = c_ac.acInitGPU()
        if err != AC_OK:
            raise ACError(err)

    def release_GPU(self):
        """
        release GPU for GPU mode
        """
        c_ac.acReleaseGPU()

    def is_initialized_GPU(self) -> bool:
        """
        check is initialized GPU for GPU mode
        """
        flag = c_ac.acIsInitializedGPU()
        return bool(flag)

    def init_GPUCNN(self):
        """
        initialize GPU for GPUCNN mode
        """
        err = c_ac.acInitGPUCNN()
        if err != AC_OK:
            raise ACError(err)

    def release_GPUCNN(self):
        """
        release GPU for GPUCNN mode
        """
        c_ac.acReleaseGPUCNN()

    def is_initialized_GPUCNN(self) -> bool:
        """
        check is initialized GPU for GPUCNN mode
        """
        flag = c_ac.acIsInitializedGPUCNN()
        return bool(flag)

    @staticmethod
    def list_GPUs():
        """
        print platforms and GPUs info
        """
        c_length = ctypes.c_size_t()
        c_ac.acListGPUs(None, ctypes.pointer(c_length), None, None)
        length = c_length.value
        info = (ctypes.c_char * length)()
        c_ac.acListGPUs(info, None, None, None)
        print(ctypes.string_at(info).decode())

    @staticmethod
    def check_GPU_support(GPGPU: GPGPUModel, pID: int = 0, dID: int = 0) -> (bool, str):
        """
        check the specified GPU and return info
        """
        c_length = ctypes.c_size_t()
        c_ac.acCheckGPUSupport2(
            ctypes.c_int(GPGPU),
            ctypes.c_uint(pID),
            ctypes.c_uint(dID),
            None,
            ctypes.pointer(c_length),
        )
        length = c_length.value
        info = (ctypes.c_char * length)()
        flag = c_ac.acCheckGPUSupport2(
            ctypes.c_int(GPGPU), ctypes.c_uint(pID), ctypes.c_uint(dID), info, None
        )
        return bool(flag), ctypes.string_at(info).decode()

    @staticmethod
    def get_GPU_list() -> (str, int, list):
        """
        return GPU info string, platforms, and a list of devices of each platform
        """
        c_length = ctypes.c_size_t()
        c_platforms = ctypes.c_size_t()
        c_ac.acListGPUs(
            None, ctypes.pointer(c_length), ctypes.pointer(c_platforms), None
        )
        length = c_length.value
        platforms = c_platforms.value
        info = (ctypes.c_char * length)()
        devices = (ctypes.c_size_t * length)()
        c_ac.acListGPUs(info, None, None, devices)
        return (
            ctypes.string_at(info).decode(),
            platforms,
            [devices[i] for i in range(platforms)],
        )

    def get_processor_info(self) -> str:
        """
        return the current processor infomation
        """
        c_length = ctypes.c_size_t()
        c_ac.acGetProcessorInfo(self.ac_object ,None, ctypes.pointer(c_length))
        length = c_length.value
        info = (ctypes.c_char * length)()
        c_ac.acGetProcessorInfo(self.ac_object ,info, None)
        return ctypes.string_at(info).decode()

    def load_image_from_numpy(self, np_array: np.array, input_type: int = AC_INPUT_RGB):
        """
        load an image from numpy array, supported type is RGB and YUV444
        """

        input_as_yuv444 = input_type == AC_INPUT_YUV444

        input_as_rgb32 = input_type == AC_INPUT_RGB32 or input_type == AC_INPUT_BGR32

        if input_type == AC_INPUT_RGB or input_type == AC_INPUT_RGB32:
            self.input_type = AC_INPUT_RGB

        rows, cols, _ = np_array.shape
        data = np_array.ctypes.data_as(ctypes.POINTER(ctypes.c_ubyte))
        err = c_ac.acLoadImageRGBPackedB(
            self.ac_object,
            ctypes.c_int(rows),
            ctypes.c_int(cols),
            data,
            ctypes.c_int64(0),
            ctypes.c_int(input_as_yuv444),
            ctypes.c_int(input_as_rgb32),
        )
        if err != AC_OK:
            raise ACError(err)

    def save_image_to_numpy(self) -> np.array:
        """
        save image to a numpy array and return it
        """
        err = ctypes.c_int(AC_OK)
        size = c_ac.acGetResultDataLength(self.ac_object, ctypes.pointer(err))
        if err.value != AC_OK:
            raise ACError(err.value)

        data = (ctypes.c_ubyte * size)()

        err = c_ac.acSaveImageRGBPackedB(self.ac_object, ctypes.pointer(data))
        if err != AC_OK:
            raise ACError(err)

        np_array = np.ctypeslib.as_array(data)

        shape = (ctypes.c_int * 3)()
        err = c_ac.acGetResultShape(self.ac_object, ctypes.pointer(shape))
        if err != AC_OK:
            raise ACError(err)

        np_array = np_array.reshape((shape[0], shape[1], shape[2]))
        return np_array

    def proccess_image_with_numpy(
        self, np_array: np.array, input_type: int = AC_INPUT_BGR
    ) -> np.array:
        """
        For quickly process image with OpenCV

        same with:

        load_image_from_numpy(img, AC_INPUT_BGR)

        process()

        img = save_image_to_numpy()

        """
        self.load_image_from_numpy(np_array, input_type)
        self.process()
        return self.save_image_to_numpy()

    @staticmethod
    def do_benchmark(processType: ProcessorType, pID: int = 0, dID: int = 0) -> float:
        """
        Do benchmark and return score
        """
        return c_ac.acBenchmark2(
            ctypes.c_int(processType), ctypes.c_uint(pID), ctypes.c_uint(dID)
        )
