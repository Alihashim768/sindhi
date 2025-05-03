import platform
import importlib.util
import os

def load_pk_module():
    arch = platform.architecture()[0]

    if arch == '64bit':
        lib_path = os.path.join(os.getcwd(), "64bit.cpython-312.so")
    elif arch == '32bit':
        lib_path = os.path.join(os.getcwd(), "32bit.cpython-312.so")
    else:
        raise RuntimeError("Unknown architecture: " + arch)

    spec = importlib.util.spec_from_file_location("pk", lib_path)
    pk = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(pk)
    return pk

if __name__ == "__main__":
    pk = load_pk_module()
    pk.main()