from itertools import zip_longest, islice
from pathlib import Path

from .image_io import imread, imwrite
from .processor import Processor

def upscale_images(
    inputs: list,
    outputs: list = [],
    output_suffix: str = "_output",
    factor: float = 2.0,
    processor_name: str = "cpu",
    device_id:int = 0,
    model_name: str = "acnet-hdn0"
):
    if isinstance(inputs, str):
        inputs = [inputs]

    processor = Processor(processor_name, device_id, model_name)

    for input, output in islice(zip_longest(inputs, outputs, fillvalue=None), len(inputs)):
        if output is None:
            input_path = Path(input)
            output = str(input_path.with_stem(input_path.stem + output_suffix))

        src = imread(input)
        dst = processor(src, factor)
        if not imwrite(output, dst):
            raise IOError(f"Failed to save image to {output}")
