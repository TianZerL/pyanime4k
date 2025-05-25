import numpy

from . import pyac

def imread(filename: str) -> numpy.ndarray:
    return pyac.core.imread(filename, pyac.core.IMREAD_UNCHANGED)

def imwrite(filename: str, image: numpy.ndarray) -> bool:
    return pyac.core.imwrite(filename, image)
