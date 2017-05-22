import ops
import iopc

def MAIN_ENV(args):
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    return False

def MAIN_EXTRACT(args):
    pkg_dir = args["pkg_path"]
    output_dir = args["output_path"]

    src_lib = iopc.getBaseRootFile("/lib/arm-linux-gnueabihf/libjson-c.so.2.0.0")
    ops.copyto(src_lib, output_dir)

    ops.ln(output_dir, "libjson-c.so.2.0.0", "libjson-c.so.2")
    ops.ln(output_dir, "libjson-c.so.2.0.0", "libjson-c.so")
    return False

def MAIN_CONFIGURE(args):
    output_dir = args["output_path"]
    return False

def MAIN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN_INSTALL(args):
    output_dir = args["output_path"]

    src_includes = iopc.getBaseRootFile("/usr/include/json-c/.")
    dst_includes = ops.path_join("include",args["pkg_name"])
    iopc.installBin(args["pkg_name"], src_includes, dst_includes)

    src_lib = ops.path_join(output_dir, ".")
    iopc.installBin(args["pkg_name"], src_lib, "usr/lib")
    return False

def MAIN_CLEAN_BUILD(args):
    output_dir = args["output_path"]
    return False

def MAIN(args):
    output_dir = args["output_path"]

