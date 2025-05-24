from . import pyac

def print_model_list():
    for name, description in zip(pyac.specs.ModelNameList, pyac.specs.ModelDescriptionList):
        print(f"{name}\t\t{description}")

def print_processor_list():
    for name, description in zip(pyac.specs.ProcessorNameList, pyac.specs.ProcessorDescriptionList):
        print(f"{name}\t\t{description}")

def print_device_list():
    for info in pyac.core.Processor.InfoList:
        print(info, end="")
