import itertools
import math
import numpy as np
import subprocess
import os


CUR_DIR = os.getcwd()
TARGET_DIR = CUR_DIR + "/42"
RESULT_ORIGINAL_DIR = TARGET_DIR + "/InOut"
RESULT_DIR = CUR_DIR + "/collected_data"



    
def generate_samples(N,low,high,dist_type): #generate samples of a variable
    """
    N:number of samples
    low: lower bound of the variable
    high: upper bound of the variable
    """
    if dist_type=='UNIFORM':
        samples=np.random.uniform(low,high,N)
    return samples


def keep_comment_clean(new_value, original_line): #output value&origianl comment in input txt. files
    line_len = len(original_line)
    comment = "!" + original_line.split("!")[1]
    comment_len = len(comment)
    num_of_spaces = line_len - comment_len - len(str(new_value))

    return f"{str(new_value)}" + " " * num_of_spaces + comment

def simulation(value_107,value_AP,value_w0,value_w1,value_w2,path,path_wheel,line_107,line_AP, line_w0,line_w1,line_w2,rl_file):
    
    lines = list()
    # change F10.7 and AP
    with open(path,'r') as f:
        lines = f.readlines()

        index_107 = line_107 - 1
        lines[index_107] = keep_comment_clean(str(value_107), lines[index_107])

        index_AP = line_AP - 1
        lines[index_AP] = keep_comment_clean(str(value_AP), lines[index_AP])

    with open(path, "w+") as new_f:
        for line in lines:
            new_f.write(line)
            
    # change initial momentum
    with open(path_wheel,'r') as f:
        lines = f.readlines()

        index_w0 = line_w0 - 1
        lines[index_w0] = keep_comment_clean(str(value_w0), lines[index_w0])
        
        index_w1 = line_w1 - 1
        lines[index_w1] = keep_comment_clean(str(value_w1), lines[index_w1])
        
        index_w2 = line_w2 - 1
        lines[index_w2] = keep_comment_clean(str(value_w2), lines[index_w2])

    with open(path_wheel, "w+") as new_f:
        for line in lines:
            new_f.write(line)

    os.chdir(TARGET_DIR)
    # Run the 42 binary
    print(f"Running 42 under folder: {os.getcwd()}")
    args = ("./42")
    popen = subprocess.Popen(args, stdout=subprocess.PIPE)
    popen.wait()
    output = popen.stdout.read()
    print(f"Result is: {output}")
    os.chdir(CUR_DIR)

    # Gather result
    # Print metadata for time.42
#    with open(f"{RESULT_ORIGINAL_DIR}/time.42", "r") as result_time:
#        results = result_time.readlines()
#        time_file.write(f"Value F10.7 = {value_107}.\n")
#        time_file.write(f"Value AP = {value_AP}.\n")
#        time_file.write("=" * 30)
#        rl_file.write("\n")
#        for result in results:
#            time_file.write(result)
#        time_file.write("\n")

    # Print metadata for rl.42
    with open(f"{RESULT_ORIGINAL_DIR}/RL.42", "r") as result_time:
        results = result_time.readlines()
        rl_file.write(f"Value F10.7 = {value_107}.\n")
        rl_file.write(f"Value AP = {value_AP}.\n")
        rl_file.write(f"Value Wheel0 = {value_w0}.\n")
        rl_file.write(f"Value Wheel1 = {value_w1}.\n")
        rl_file.write(f"Value Wheel2 = {value_w2}.\n")
        rl_file.write("=" * 30)
        rl_file.write("\n")
        for result in results:
            rl_file.write(result)
        rl_file.write("\n")


if __name__ == "__main__":
    N_107=1 #number of samples of F10.7
    N_AP=1 #number of samples of AP
    N_W0=2 #number of samples of momentum of axis 0
    N_W1=1 #number of samples of momentum of axis 1
    N_W2=1 #number of samples of momentum of axis 2
    Low_107=100
    High_107=230
    Low_AP=50
    High_AP=100
    Low_W0=-0.05
    High_W0=0.05
    Low_W1=-0.01
    High_W1=0.01
    Low_W2=-0.01
    High_W2=0.01
    Dist_type_107='UNIFORM'
    Dist_type_AP='UNIFORM'
    Dist_type_W0='UNIFORM'
    Dist_type_W1='UNIFORM'
    Dist_type_W2='UNIFORM'
    
    Path_to_file='./42/InOut/Inp_Sim.txt'
    Path_to_file2='./42/InOut/RL_Spacecraft.txt'
    

    # Create result folder
    if (not os.path.isdir(RESULT_DIR)):
        print(f"{RESULT_DIR} doesn't exist, creating one...")
        os.mkdir(RESULT_DIR)
    
    Samples_107=generate_samples(N_107,Low_107,High_107,Dist_type_107)
    Samples_AP=generate_samples(N_AP,Low_AP,High_AP,Dist_type_AP)
    Samples_W0=generate_samples(N_W0,Low_W0,High_W0,Dist_type_W0)
    Samples_W1=generate_samples(N_W1,Low_W1,High_W1,Dist_type_W1)
    Samples_W2=generate_samples(N_W2,Low_W2,High_W2,Dist_type_W2)
    Samples =np.array(list(itertools.product(Samples_107,Samples_AP,Samples_W0,Samples_W1,Samples_W2)))

    #time_file = open(f"{RESULT_DIR}/time.txt", "w+")
    rl_file = open(f"{RESULT_DIR}/rl.txt", "w+")

    try:
        for ii in range(len(Samples)):
            Value_107=round(Samples[ii,0], 1)
            Value_AP=round(Samples[ii,1], 1)
            Value_W0=round(Samples[ii,2],4)
            Value_W1=round(Samples[ii,3],4)
            Value_W2=round(Samples[ii,4],4)
            simulation(Value_107, Value_AP, Value_W0,Value_W1,Value_W2,Path_to_file,Path_to_file2, 19, 20, 62, 71, 80, rl_file)
    except:
        print(f"Oops, something went wrong: {e}")
    finally:
        #time_file.close()
        rl_file.close()
