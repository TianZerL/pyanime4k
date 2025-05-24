import numpy

from . import pyac

class Processor:
    def __init__(self, processor_name: str = "cpu", device_id:int = 0, model_name: str = "acnet-hdn0"):
        self.processor_name = processor_name.lower()
        if self.processor_name == "opencl" :
            processor_type = pyac.core.Processor.OpenCL
        if self.processor_name == "cuda":
            processor_type = pyac.core.Processor.CUDA
        else:
            self.processor_name = "cpu"
            processor_type = pyac.core.Processor.CPU

        self.processor = pyac.core.Processor(processor_type = processor_type, device = device_id, model = model_name)
        if not self.processor.ok():
            raise RuntimeError(self.processor.error())
    
    def __call__(self, src: numpy.ndarray, factor: float = 2.0) -> numpy.ndarray:
        dst = self.processor.process(src = src, factor = factor)
        if not self.processor.ok():
            raise RuntimeError(self.processor.error())
        return dst

    def __str__(self):
        return f"{self.processor_nam}: {self.processor.name()}"
