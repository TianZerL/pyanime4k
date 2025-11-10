import os
from pathlib import Path
from setuptools import find_packages
from skbuild import setup

def is_python_extension(file_path):
    exts = [".dll", ".pyd", ".dylib", ".so"]
    for ext in exts:
        if ext in file_path:
            return True
    return False

def check_cuda():
    cuda_path = os.environ.get("CUDA_HOME") or os.environ.get("CUDA_PATH")
    if cuda_path:
        cuda_bin = Path(cuda_path) / "bin"
        cuda_include = Path(cuda_path) / "include"
        if cuda_bin.exists() and cuda_include.exists():
            return True
    return False

def main():
    pyac_cmake_args = ["-DAC_CORE_WITH_OPENCL=ON", "-DAC_CORE_WITH_EIGEN3=ON", "-DAC_BUILD_BINDING_PYTHON=ON", "-DAC_BUILD_CLI=OFF"]

    if os.name == 'nt':
        pyac_cmake_args.append("-DAC_ENABLE_STATIC_CRT=ON")

    if check_cuda():
        pyac_cmake_args.append("-DAC_CORE_WITH_CUDA=ON")

    setup(
        packages=find_packages(where='src'),
        package_dir={'': 'src'},
        package_data={'pyanime4k.pyac': ['**/*.pyi']},
        cmake_args=pyac_cmake_args,
        cmake_source_dir="src/Anime4KCPP",
        cmake_process_manifest_hook = lambda manifest : list(filter(lambda name: is_python_extension(name), manifest))
    )

if __name__ == "__main__":
    main()
