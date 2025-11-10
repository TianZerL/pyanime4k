from itertools import zip_longest, islice
from pathlib import Path

from .pyac import pyac

def upscale_images(
    inputs: list,
    outputs: list = [],
    output_suffix: str = "_output",
    factor: float = 2.0,
    processor_type: str = "cpu",
    device_id:int = 0,
    model_name: str = "acnet-hdn0"
):
    if isinstance(inputs, str):
        inputs = [inputs]

    processor = pyac.core.Processor(processor_type, device_id, model_name)

    for input, output in islice(zip_longest(inputs, outputs, fillvalue=None), len(inputs)):
        if output is None:
            input_path = Path(input)
            output = input_path.with_stem(input_path.stem + output_suffix)

        src = pyac.core.imread(str(input))
        dst = processor(src, factor)
        if not pyac.core.imwrite(str(output), dst):
            raise IOError(f"Failed to save image to {output}")
