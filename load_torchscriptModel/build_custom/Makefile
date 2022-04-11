INCPATH := /home/jbreeden/libtorch/include #$(shell python -c "import torch.utils.cpp_extension as C; print('-I' + str.join(' -I', C.include_paths()))")

LIBPATH := -L/home/jbreeden/libtorch/lib #$(shell python -c "import torch.utils.cpp_extension as C; print(C.include_paths()[0] + '/../')")

#USE_CUDA := $(shell python -c "import torch; print(torch.cuda.is_available())")

TORCH_LIBS=-ltorch_cpu -lc10 #-lcaffe2_protos 

INC = -I/home/jbreeden/libtorch/include

example: ../example.cpp Makefile
	g++ ../example.cpp -o example $(INC) $(LIBPATH) $(TORCH_LIBS) -pthread -D_GLIBCXX_USE_CXX11_ABI=0 -std=c++14 -Wl,-rpath=/home/jbreeden/libtorch/lib
