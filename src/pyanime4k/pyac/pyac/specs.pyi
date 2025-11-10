from __future__ import annotations
__all__: list[str] = ['ModelDescriptionList', 'ModelNameList', 'ProcessorDescriptionList', 'ProcessorNameList']
ModelDescriptionList: tuple = ('Lightweight CNN, detail enhancement.', 'Lightweight CNN, mild denoising.', 'Lightweight CNN, moderate denoising.', 'Lightweight CNN, heavy denoising.', 'Lightweight CNN, extreme denoising.', 'Lightweight ResNet, mild denoising.')
ModelNameList: tuple = ('acnet-gan', 'acnet-hdn0', 'acnet-hdn1', 'acnet-hdn2', 'acnet-hdn3', 'arnet-hdn')
ProcessorDescriptionList: tuple = ('General-purpose CPU processing with optional SIMD acceleration.', 'Cross-platform acceleration requiring OpenCL 1.2+ compliant devices.', 'NVIDIA GPU acceleration requiring Compute Capability 5.0+.')
ProcessorNameList: tuple = ('cpu', 'opencl', 'cuda')
