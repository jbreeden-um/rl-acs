INCPATH := /home/jbreeden/libtorch/include #$(shell python -c "import torch.utils.cpp_extension as C; print('-I' + str.join(' -I', C.include_paths()))")

LIBPATH := -L/home/jbreeden/libtorch/lib #$(shell python -c "import torch.utils.cpp_extension as C; print(C.include_paths()[0] + '/../')")

#USE_CUDA := $(shell python -c "import torch; print(torch.cuda.is_available())")

TORCH_LIBS=-ltorch_cpu -lc10 #-lcaffe2_protos 
# MORE_LIBS = -lXNNPACK.a                 -ldnnl.a              -lkineto.a                   -lqnnpack.a
# -lasmjit.a                  libfbgemm.a            libnnapi_backend.so           libshm.so
# -lbackend_with_compiler.so  libfbjni.so            libnnpack.a                   libtensorpipe.a
# -lbenchmark.a               libfmt.a               libnnpack_reference_layers.a  libtensorpipe_uv.a
# -lbenchmark_main.a          libfoxi_loader.a       libonnx.a                     libtorch.so
# -lbreakpad.a                libgloo.a              libonnx_proto.a               libtorch_cpu.so
# -lbreakpad_common.a         libgmock.a             libprotobuf-lite.a            libtorch_global_deps.so
# -lc10.so                    libgmock_main.a        libprotobuf.a                 libtorch_python.so
# -lcaffe2_protos.a           libgomp-a34b3233.so.1  libprotoc.a                   libtorchbind_test.so
# -lclog.a                    libgtest.a             libpthreadpool.a
# libcpuinfo.a                 libgtest_main.a        libpytorch_jni.so
# libcpuinfo_internals.a       libjitbackend_test.so  libpytorch_qnnpack.a

INC = -I/home/jbreeden/libtorch/include -I/home/jbreeden/EECS598/acs-rl/load_torchscriptModel/callable2/

example: ../example_fast.cpp Makefile
	g++ ../example_fast.cpp -shared -fPIC -o libexample_fast.so $(INC) $(LIBPATH) $(TORCH_LIBS) -pthread -D_GLIBCXX_USE_CXX11_ABI=0 -std=c++14 -Wl,-rpath=/home/jbreeden/libtorch/lib