from pyanime4k.anime4k.anime4kcpp import Anime4K
from pyanime4k import ffmpeg
import os


def showImg2X(src, *args):
    r"""Quickly show a image which be processed by anime4k
    :param src: Path of input file.
    :param args: If you want to specify the prcessing arguments, put it here.
    
    Default args:
    int passes=2, double strengthColor=0.3, double strengthGradient=1.0, 
    double zoomFactor=2.0, bool fastMode=False, bool videoMode=False(do not change it), 
    unsigned int maxThreads=std::thread::hardware_concurrency()) 
    """
    
    tmpImg = Anime4K(*args)
    tmpImg.loadImage(src)
    tmpImg.process()
    tmpImg.showImage()


def cvtImg2X(srcList, dstSuffix="_output", dstPath=None, *args):
    r"""Convert images by anime4k
    :param srcList: String list of Path of input files.
    :param dstSuffix: Add a suffix of output files.
    :param dstPath: Specify a path for output files, should be str.
    :param args: If you want to specify the prcessing arguments, put it here.
    
    Default args:
    int passes=2, double strengthColor=0.3, double strengthGradient=1.0, 
    double zoomFactor=2.0, bool fastMode=False, bool videoMode=False(do not change it), 
    unsigned int maxThreads=std::thread::hardware_concurrency()) 
    """

    if isinstance(srcList, str):
        srcList = [srcList]
    if dstPath is None:
        dstPath = os.path.split(srcList[0])[0]
        if dstPath == "":
            dstPath = "."
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)
    tmpImg = Anime4K(*args)
    for src in srcList:
        tmpImg.loadImage(src)
        tmpImg.process()
        dstName = os.path.splitext(os.path.split(src)[1])
        print(dstPath + "/" + dstName[0] + dstSuffix + dstName[1])
        tmpImg.saveImage(dstPath + "/" + dstName[0] + dstSuffix + dstName[1])


def cvtVideo2X(srcList, dstSuffix="_output", dstPath=None, *args):
    r"""Convert videos by anime4k
    :param srcList: String list of Path of input files.
    :param dstSuffix: Add a suffix of output files.
    :param dstPath: Specify a path for output files, should be str.
    args: If you want to specify the prcessing arguments, put it here.
    
    Default args:
    int passes=1, double strengthColor=0.3, double strengthGradient=1.0, 
    double zoomFactor=2.0, bool fastMode=False, bool videoMode=True(do not change it), 
    unsigned int maxThreads=std::thread::hardware_concurrency()) 
    """

    if isinstance(srcList, str):
        srcList = [srcList]
    if not dstPath:
        dstPath = os.path.split(srcList[0])[0]
        if not dstPath:
            dstPath = "."
    if not os.path.exists(dstPath):
        os.makedirs(dstPath)
    if not args:
        args = (1, 0.3, 1.0, 2.0, False, True)
    tmpVideo = Anime4K(*args)
    for src in srcList:
        tmpVideo.loadVideo(src)
        dstName = os.path.splitext(os.path.split(src)[1])
        tmpVideo.setVideoSaveInfo("tmp_out.mp4")
        tmpVideo.process()
        tmpVideo.saveVideo()
        ffmpeg.mergeAudio(
            "tmp_out.mp4", src, dstPath + "/" + dstName[0] + dstSuffix + dstName[1]
        )
        os.remove("tmp_out.mp4")
