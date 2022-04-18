//
//  example.cpp
//  
//
//  Created by Liliang Wang on 4/7/22.
//

// #include "example.hpp"
#include <torch/script.h> // One-stop header.

#include <iostream>
#include <fstream>
#include <memory>
#include <string>
#include "example_fast.h"
using namespace std;

torch::jit::script::Module torch_module;
torch::Device torch_device(torch::kCPU);

void cpp_get_torch_control(double States[6], double Actions[3]){
    std::vector<torch::jit::IValue> inputs;
    // double States[6];
    int i;
    // double ini_state[6]={-1.180891077077e-01,-1.719999530800e-02,-7.300013419836e-03,0.000000000000e+00,-5.334234891820e+00,-1.570916181701e+00};
    // for(i=0;i<6;i++) {
       // States[i]=ini_state[i];
    // }
    //double array[1][6] = {{-1.180891077077e-01,-1.719999530800e-02,-7.300013419836e-03,0.000000000000e+00,-5.334234891820e+00,-1.570916181701e+00}};
    //auto tharray = torch::zeros({1,6},torch::kFloat32); //or use kF64
    //std::memcpy(tharray.data_ptr(),array,sizeof(double)*tharray.numel());
    torch::Tensor tharray = torch::tensor({{States[0],States[1],States[2],States[3],States[4],States[5]}}, {torch::kFloat32});
    inputs.push_back(tharray);//-1.0*torch::rand({1, 6}));
    //std::cout << "hi\n";

    // Execute the model and turn its output into a tensor.
    at::Tensor output = torch_module(inputs).toTensor();
    //std::cout << output[0]<<'\n';
	for (i=0; i<3;i++) Actions[i] = (double)output[0][i].item<float>();
}
void cpp_get_torch_control7(double States[7], double Actions[3]){
    std::vector<torch::jit::IValue> inputs;
    // double States[6];
    int i;
    // double ini_state[6]={-1.180891077077e-01,-1.719999530800e-02,-7.300013419836e-03,0.000000000000e+00,-5.334234891820e+00,-1.570916181701e+00};
    // for(i=0;i<6;i++) {
       // States[i]=ini_state[i];
    // }
    //double array[1][6] = {{-1.180891077077e-01,-1.719999530800e-02,-7.300013419836e-03,0.000000000000e+00,-5.334234891820e+00,-1.570916181701e+00}};
    //auto tharray = torch::zeros({1,6},torch::kFloat32); //or use kF64
    //std::memcpy(tharray.data_ptr(),array,sizeof(double)*tharray.numel());
    torch::Tensor tharray = torch::tensor({{States[0],States[1],States[2],States[3],States[4],States[5],States[6]}}, {torch::kFloat32});
    inputs.push_back(tharray);//-1.0*torch::rand({1, 6}));
    //std::cout << "hi\n";

    // Execute the model and turn its output into a tensor.
    at::Tensor output = torch_module(inputs).toTensor();
    //std::cout << output[0]<<'\n';
	for (i=0; i<3;i++) Actions[i] = (double)output[0][i].item<float>();
}
void cpp_mytorch_init(char filename[200]){//(int argc, const char* argv[]) {
    //torch::Tensor tensor = torch::eye(3);
    //std::cout << tensor <<std::endl;<<<<<<< HEAD
    // ifstream indata;
    // ofstream outdata;
    // indata.open("input.dat");
    // double States[6];
    // for (int i=0; i<6; i++){
        // indata >> States[i];
        // cout << States[i] <<'\n';
    // }
	 try {
      // Deserialize the ScriptModule from a file using torch::jit::load().
	std::cout << "started torch model import\n";
      torch_module = torch::jit::load(filename, c10::DeviceType::CPU);
	std::cout << "filename is valid\n";
      torch_module.to(at::kCPU);
	std::cout << "file works in CPU\n";
//      torch_module.cpu();
//	std::cout << "successfully moved to CPU\n";
    }
    catch (const c10::Error& e) {
      std::cerr << "error loading the model\n";
	std::cout << e.what() << "\n";
      return;
    }
	std::cout << "Torch model loaded\n";
    return;
    
	
    // std::vector<torch::jit::IValue> inputs;
    // torch::Tensor tharray = torch::tensor({{States[0],States[1],States[2],States[3],States[4],States[5]}}, {torch::kFloat32});
    // inputs.push_back(tharray);

    // Execute the model and turn its output into a tensor.
    
	// at::Tensor output = module(inputs).toTensor();
    // outdata.open("output.dat", ofstream::out | ofstream::trunc);
    // string output1(to_string(output[0][0].item<float>()));
    // string output2(to_string(output[0][1].item<float>()));
    // string output3(to_string(output[0][2].item<float>()));
    // outdata << output1 << " ";
    // outdata << output2 << " ";
    // outdata << output3;
    // outdata.close();
    
    /*
    int i;
    for(i=0;i<27770;i++){
        std::cout << i <<'\n'; //hi
        torch::jit::script::Module module;
        try {
          // Deserialize the ScriptModule from a file using torch::jit::load().
          module = torch::jit::load("/Users/liliang/Documents/example_folder/cqlDet.pt");
        }
        catch (const c10::Error& e) {
          std::cerr << "error loading the model\n";
          return -1;
        }

        //std::cout << "ok\n";
        test(module);
    }//*/
    /*
    // Create a vector of inputs.
    std::vector<torch::jit::IValue> inputs;
    double States[6];
    int i;
    double ini_state[6]={-1.180891077077e-01,-1.719999530800e-02,-7.300013419836e-03,0.000000000000e+00,-5.334234891820e+00,-1.570916181701e+00};
    for(i=0;i<6;i++) {
       States[i]=ini_state[i];
    }
    //double array[1][6] = {{-1.180891077077e-01,-1.719999530800e-02,-7.300013419836e-03,0.000000000000e+00,-5.334234891820e+00,-1.570916181701e+00}};
    //auto tharray = torch::zeros({1,6},torch::kFloat32); //or use kF64
    //std::memcpy(tharray.data_ptr(),array,sizeof(double)*tharray.numel());
    torch::Tensor tharray = torch::tensor({{States[0],States[1],States[2],States[3],States[4],States[5]}}, {torch::kFloat32});
    inputs.push_back(tharray);//-1.0*torch::rand({1, 6}));
    std::cout << "hi\n";

    // Execute the model and turn its output into a tensor.
    at::Tensor output = module(inputs).toTensor(); //*/
    //std::cout << output[0]<<'\n';//.slice(/*dim=*/1, /*start=*/0, /*end=*/2) << '\n';
    
}
//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

void get_torch_control(double States[6], double Actions[3]){
    cpp_get_torch_control(States, Actions);
	return;
}
void get_torch_control7(double States[7], double Actions[3]){
    cpp_get_torch_control7(States, Actions);
	return;
}
void mytorch_init(char filename[200]){
	cpp_mytorch_init(filename);
	return;
}
