//
//  example.cpp
//  
//
//  Created by Liliang Wang on 4/7/22.
//

// #include "example.hpp"
#include <torch/script.h> // One-stop header.

#include <iostream>
#include <memory>

void test(torch::jit::script::Module module){
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
    at::Tensor output = module(inputs).toTensor();
    std::cout << output[0]<<'\n';
}
int main(){//(int argc, const char* argv[]) {
    //torch::Tensor tensor = torch::eye(3);
    //std::cout << tensor <<std::endl;
    torch::jit::script::Module module;
    try {
      // Deserialize the ScriptModule from a file using torch::jit::load().
      module = torch::jit::load("/Users/liliang/Documents/example_folder/cqlDet.pt");
    }
    catch (const c10::Error& e) {
      std::cerr << "error loading the model\n";
      return -1;
    }

    std::cout << "ok\n";
    test(module);
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
