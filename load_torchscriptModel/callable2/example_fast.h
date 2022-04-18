#ifndef EXAMPLE_FAST
#define EXAMPLE_FAST

#ifdef __cplusplus
void cpp_get_torch_control(double States[6], double Actions[3]);
void cpp_get_torch_control7(double States[7], double Actions[3]);
void cpp_mytorch_init(char filename[200]);
extern "C" {
#endif
	void get_torch_control(double States[6], double Actions[3]);
	void get_torch_control7(double States[7], double Actions[3]);
	void mytorch_init(char filename[200]);
#ifdef __cplusplus
}
#endif

#endif
