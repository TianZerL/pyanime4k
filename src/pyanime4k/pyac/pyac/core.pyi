from __future__ import annotations
import numpy
import numpy.typing
import typing
__all__: list[str] = ['IMREAD_COLOR', 'IMREAD_GRAYSCALE', 'IMREAD_RGB', 'IMREAD_RGBA', 'IMREAD_UNCHANGED', 'ImreadModes', 'Processor', 'RESIZE_BICUBIC_0_100', 'RESIZE_BICUBIC_0_60', 'RESIZE_BICUBIC_0_75', 'RESIZE_BICUBIC_20_50', 'RESIZE_BILINEAR', 'RESIZE_CATMULL_ROM', 'RESIZE_LANCZOS2', 'RESIZE_LANCZOS3', 'RESIZE_LANCZOS4', 'RESIZE_MITCHELL_NETRAVALI', 'RESIZE_POINT', 'RESIZE_SOFTCUBIC100', 'RESIZE_SOFTCUBIC50', 'RESIZE_SOFTCUBIC75', 'RESIZE_SPLINE16', 'RESIZE_SPLINE36', 'RESIZE_SPLINE64', 'ResizeModes', 'imread', 'imwrite', 'resize']
class ImreadModes:
    """
    Members:
    
      IMREAD_UNCHANGED
    
      IMREAD_GRAYSCALE
    
      IMREAD_COLOR
    
      IMREAD_RGB
    
      IMREAD_RGBA
    """
    IMREAD_COLOR: typing.ClassVar[ImreadModes]  # value = <ImreadModes.IMREAD_COLOR: 3>
    IMREAD_GRAYSCALE: typing.ClassVar[ImreadModes]  # value = <ImreadModes.IMREAD_GRAYSCALE: 1>
    IMREAD_RGB: typing.ClassVar[ImreadModes]  # value = <ImreadModes.IMREAD_COLOR: 3>
    IMREAD_RGBA: typing.ClassVar[ImreadModes]  # value = <ImreadModes.IMREAD_RGBA: 4>
    IMREAD_UNCHANGED: typing.ClassVar[ImreadModes]  # value = <ImreadModes.IMREAD_UNCHANGED: 0>
    __members__: typing.ClassVar[dict[str, ImreadModes]]  # value = {'IMREAD_UNCHANGED': <ImreadModes.IMREAD_UNCHANGED: 0>, 'IMREAD_GRAYSCALE': <ImreadModes.IMREAD_GRAYSCALE: 1>, 'IMREAD_COLOR': <ImreadModes.IMREAD_COLOR: 3>, 'IMREAD_RGB': <ImreadModes.IMREAD_COLOR: 3>, 'IMREAD_RGBA': <ImreadModes.IMREAD_RGBA: 4>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Processor:
    CPU: typing.ClassVar[int] = 0
    CUDA: typing.ClassVar[int] = 2
    OpenCL: typing.ClassVar[int] = 1
    InfoList: typing.ClassVar[tuple[str, ...]]
    def __call__(self, src: numpy.ndarray, factor: typing.SupportsFloat = 2.0) -> numpy.ndarray:
        ...
    @typing.overload
    def __init__(self, processor_type: typing.SupportsInt = 0, device: typing.SupportsInt = 0, model: str = 'acnet-gan') -> None:
        ...
    @typing.overload
    def __init__(self, processor_type: str, device: typing.SupportsInt = 0, model: str = 'acnet-gan') -> None:
        ...
    def __str__(self) -> str:
        ...
    def error(self) -> str:
        ...
    def name(self) -> str:
        ...
    def ok(self) -> bool:
        ...
    def process(self, src: numpy.ndarray, factor: typing.SupportsFloat = 2.0) -> numpy.ndarray:
        ...
class ResizeModes:
    """
    Members:
    
      RESIZE_POINT
    
      RESIZE_CATMULL_ROM
    
      RESIZE_MITCHELL_NETRAVALI
    
      RESIZE_BICUBIC_0_60
    
      RESIZE_BICUBIC_0_75
    
      RESIZE_BICUBIC_0_100
    
      RESIZE_BICUBIC_20_50
    
      RESIZE_SOFTCUBIC50
    
      RESIZE_SOFTCUBIC75
    
      RESIZE_SOFTCUBIC100
    
      RESIZE_LANCZOS2
    
      RESIZE_LANCZOS3
    
      RESIZE_LANCZOS4
    
      RESIZE_SPLINE16
    
      RESIZE_SPLINE36
    
      RESIZE_SPLINE64
    
      RESIZE_BILINEAR
    """
    RESIZE_BICUBIC_0_100: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_BICUBIC_0_100: 5>
    RESIZE_BICUBIC_0_60: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_BICUBIC_0_60: 3>
    RESIZE_BICUBIC_0_75: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_BICUBIC_0_75: 4>
    RESIZE_BICUBIC_20_50: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_BICUBIC_20_50: 6>
    RESIZE_BILINEAR: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_BILINEAR: 16>
    RESIZE_CATMULL_ROM: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_CATMULL_ROM: 1>
    RESIZE_LANCZOS2: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_LANCZOS2: 10>
    RESIZE_LANCZOS3: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_LANCZOS3: 11>
    RESIZE_LANCZOS4: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_LANCZOS4: 12>
    RESIZE_MITCHELL_NETRAVALI: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_MITCHELL_NETRAVALI: 2>
    RESIZE_POINT: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_POINT: 0>
    RESIZE_SOFTCUBIC100: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_SOFTCUBIC100: 9>
    RESIZE_SOFTCUBIC50: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_SOFTCUBIC50: 7>
    RESIZE_SOFTCUBIC75: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_SOFTCUBIC75: 8>
    RESIZE_SPLINE16: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_SPLINE16: 13>
    RESIZE_SPLINE36: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_SPLINE36: 14>
    RESIZE_SPLINE64: typing.ClassVar[ResizeModes]  # value = <ResizeModes.RESIZE_SPLINE64: 15>
    __members__: typing.ClassVar[dict[str, ResizeModes]]  # value = {'RESIZE_POINT': <ResizeModes.RESIZE_POINT: 0>, 'RESIZE_CATMULL_ROM': <ResizeModes.RESIZE_CATMULL_ROM: 1>, 'RESIZE_MITCHELL_NETRAVALI': <ResizeModes.RESIZE_MITCHELL_NETRAVALI: 2>, 'RESIZE_BICUBIC_0_60': <ResizeModes.RESIZE_BICUBIC_0_60: 3>, 'RESIZE_BICUBIC_0_75': <ResizeModes.RESIZE_BICUBIC_0_75: 4>, 'RESIZE_BICUBIC_0_100': <ResizeModes.RESIZE_BICUBIC_0_100: 5>, 'RESIZE_BICUBIC_20_50': <ResizeModes.RESIZE_BICUBIC_20_50: 6>, 'RESIZE_SOFTCUBIC50': <ResizeModes.RESIZE_SOFTCUBIC50: 7>, 'RESIZE_SOFTCUBIC75': <ResizeModes.RESIZE_SOFTCUBIC75: 8>, 'RESIZE_SOFTCUBIC100': <ResizeModes.RESIZE_SOFTCUBIC100: 9>, 'RESIZE_LANCZOS2': <ResizeModes.RESIZE_LANCZOS2: 10>, 'RESIZE_LANCZOS3': <ResizeModes.RESIZE_LANCZOS3: 11>, 'RESIZE_LANCZOS4': <ResizeModes.RESIZE_LANCZOS4: 12>, 'RESIZE_SPLINE16': <ResizeModes.RESIZE_SPLINE16: 13>, 'RESIZE_SPLINE36': <ResizeModes.RESIZE_SPLINE36: 14>, 'RESIZE_SPLINE64': <ResizeModes.RESIZE_SPLINE64: 15>, 'RESIZE_BILINEAR': <ResizeModes.RESIZE_BILINEAR: 16>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: typing.SupportsInt) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: typing.SupportsInt) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
def imread(filename: str, mode: ImreadModes = ...) -> numpy.typing.NDArray[numpy.uint8]:
    ...
def imwrite(filename: str, image: typing.Annotated[numpy.typing.ArrayLike, numpy.uint8]) -> bool:
    ...
def resize(src: numpy.ndarray, dsize: tuple, fx: typing.SupportsFloat = 0.0, fy: typing.SupportsFloat = 0.0, mode: ResizeModes = ...) -> numpy.ndarray:
    ...
IMREAD_COLOR: ImreadModes  # value = <ImreadModes.IMREAD_COLOR: 3>
IMREAD_GRAYSCALE: ImreadModes  # value = <ImreadModes.IMREAD_GRAYSCALE: 1>
IMREAD_RGB: ImreadModes  # value = <ImreadModes.IMREAD_COLOR: 3>
IMREAD_RGBA: ImreadModes  # value = <ImreadModes.IMREAD_RGBA: 4>
IMREAD_UNCHANGED: ImreadModes  # value = <ImreadModes.IMREAD_UNCHANGED: 0>
RESIZE_BICUBIC_0_100: ResizeModes  # value = <ResizeModes.RESIZE_BICUBIC_0_100: 5>
RESIZE_BICUBIC_0_60: ResizeModes  # value = <ResizeModes.RESIZE_BICUBIC_0_60: 3>
RESIZE_BICUBIC_0_75: ResizeModes  # value = <ResizeModes.RESIZE_BICUBIC_0_75: 4>
RESIZE_BICUBIC_20_50: ResizeModes  # value = <ResizeModes.RESIZE_BICUBIC_20_50: 6>
RESIZE_BILINEAR: ResizeModes  # value = <ResizeModes.RESIZE_BILINEAR: 16>
RESIZE_CATMULL_ROM: ResizeModes  # value = <ResizeModes.RESIZE_CATMULL_ROM: 1>
RESIZE_LANCZOS2: ResizeModes  # value = <ResizeModes.RESIZE_LANCZOS2: 10>
RESIZE_LANCZOS3: ResizeModes  # value = <ResizeModes.RESIZE_LANCZOS3: 11>
RESIZE_LANCZOS4: ResizeModes  # value = <ResizeModes.RESIZE_LANCZOS4: 12>
RESIZE_MITCHELL_NETRAVALI: ResizeModes  # value = <ResizeModes.RESIZE_MITCHELL_NETRAVALI: 2>
RESIZE_POINT: ResizeModes  # value = <ResizeModes.RESIZE_POINT: 0>
RESIZE_SOFTCUBIC100: ResizeModes  # value = <ResizeModes.RESIZE_SOFTCUBIC100: 9>
RESIZE_SOFTCUBIC50: ResizeModes  # value = <ResizeModes.RESIZE_SOFTCUBIC50: 7>
RESIZE_SOFTCUBIC75: ResizeModes  # value = <ResizeModes.RESIZE_SOFTCUBIC75: 8>
RESIZE_SPLINE16: ResizeModes  # value = <ResizeModes.RESIZE_SPLINE16: 13>
RESIZE_SPLINE36: ResizeModes  # value = <ResizeModes.RESIZE_SPLINE36: 14>
RESIZE_SPLINE64: ResizeModes  # value = <ResizeModes.RESIZE_SPLINE64: 15>
