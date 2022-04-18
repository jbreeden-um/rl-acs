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

#def simulation(value_107,value_AP,value_w0,value_w1,value_w2,path,path_wheel,line_107,line_AP, line_w0,line_w1,line_w2,rl_file):
def set_outputInterval(value, path, line_number):
    lines = list()
    # change Output Interval
    with open(path,'r') as f:
        lines = f.readlines()

        index = line_number - 1
        lines[index] = keep_comment_clean(str(value), lines[index])

    with open(path, "w+") as new_f:
        for line in lines:
            new_f.write(line)
    
def simulation(value_w0,value_w1,value_w2,value_RAAN,path_wheel,path_RAAN,line_w0,line_w1,line_w2,line_RAAN,rl_file,vary_RAAN):   
    lines = list()
            
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
 
    if (vary_RAAN):
        with open(path_RAAN,'r') as f:
            lines = f.readlines()

            index = line_RAAN - 1
            lines[index] = keep_comment_clean(str(value_RAAN), lines[index])
        
        with open(path_RAAN, "w+") as new_f:
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
        #rl_file.write(f"Value F10.7 = {value_107}.\n")
        #rl_file.write(f"Value AP = {value_AP}.\n")
        rl_file.write(f"Value Wheel0 = {value_w0}.\n")
        rl_file.write(f"Value Wheel1 = {value_w1}.\n")
        rl_file.write(f"Value Wheel2 = {value_w2}.\n")
        if (vary_RAAN):
            rl_file.write(f"Value RAAN = {value_RAAN}.\n")
        rl_file.write("=" * 30)
        rl_file.write("\n")
        for result in results:
            rl_file.write(result)
        rl_file.write("\n")

def record_F10p7_AP(value_file,SimNum):
    with open(f"{RESULT_ORIGINAL_DIR}/Values_10p7_AP.txt", "r") as result_time:
        results = result_time.readlines()
        value_file.write(f"Simulation No. {SimNum}.\n")
        value_file.write("=" * 30)
        value_file.write("\n")
        for result in results:
            value_file.write(result)
        value_file.write("\n")


if __name__ == "__main__":
    #N_107=1 #number of samples of F10.7
    #N_AP=1 #number of samples of AP
    Value_OutputInterval=5.0
    N_W0=2 #number of samples of momentum of axis 0
    N_W1=2 #number of samples of momentum of axis 1
    N_W2=2 #number of samples of momentum of axis 2
    N_RAAN=2 #number of samples of RAAN
    Low_W0=-0.15
    High_W0=0.15
    Low_W1=-0.03
    High_W1=0.03
    Low_W2=-0.03
    High_W2=0.03
    Low_RAAN=-180.0
    High_RAAN=180.0
    Dist_type_W0='UNIFORM'
    Dist_type_W1='UNIFORM'
    Dist_type_W2='UNIFORM'
    Dist_type_RAAN='UNIFORM'
    Record_10p7_AP=True #set this to 0 if we don't want values of F10.7 and AP be stored
    Vary_RAAN=False #set this to 0 if we don't want vary RAAN
    
    Path_to_file='./42/InOut/Inp_Sim.txt'
    Path_to_file2='./42/InOut/RL_Spacecraft.txt'
    Path_to_file3='./42/InOut/RL_Orbit.txt'
    

    # Create result folder
    if (not os.path.isdir(RESULT_DIR)):
        print(f"{RESULT_DIR} doesn't exist, creating one...")
        os.mkdir(RESULT_DIR)

    #time_file = open(f"{RESULT_DIR}/time.txt", "w+")
    if (Record_10p7_AP):
        value_file = open(f"{RESULT_DIR}/F10p7_AP.txt", "w+")
    rl_file = open(f"{RESULT_DIR}/new_rl.txt", "w+")

    Samples_W0=generate_samples(N_W0,Low_W0,High_W0,Dist_type_W0)
    Samples_W1=generate_samples(N_W1,Low_W1,High_W1,Dist_type_W1)
    Samples_W2=generate_samples(N_W2,Low_W2,High_W2,Dist_type_W2)
    Samples_RAAN=generate_samples(N_RAAN,Low_RAAN,High_RAAN,Dist_type_RAAN)
    Samples =np.array(list(itertools.product(Samples_W0,Samples_W1,Samples_W2)))

    try:
        set_outputInterval(Value_OutputInterval, Path_to_file, 5)
        if False:
            if (Vary_RAAN):
                Samples =np.array(list(itertools.product(Samples_W0,Samples_W1,Samples_W2,Samples_RAAN)))
            for ii in range(len(Samples)):
                Value_W0=round(Samples[ii,0],4)
                Value_W1=round(Samples[ii,1],4)
                Value_W2=round(Samples[ii,2],4)
                Value_RAAN=round(Samples[ii,2+Vary_RAAN],1)
                simulation(Value_W0,Value_W1,Value_W2,Value_RAAN,Path_to_file2,Path_to_file3, 62, 71, 80,18, rl_file,Vary_RAAN)
                if (Record_10p7_AP):
                    record_F10p7_AP(value_file,ii+1)
        else:
        
            for ii in range(5000):
                Value_W0=round(generate_samples(1,Low_W0,High_W0,Dist_type_W0)[0],4)
                Value_W1=round(generate_samples(1,Low_W1,High_W1,Dist_type_W1)[0],4)
                Value_W2=round(generate_samples(1,Low_W2,High_W2,Dist_type_W2)[0],4)
                Value_RAAN=round(generate_samples(1,Low_RAAN,High_RAAN,Dist_type_RAAN)[0],1)
                simulation(Value_W0,Value_W1,Value_W2,Value_RAAN,Path_to_file2,Path_to_file3, 62, 71, 80,18, rl_file,Vary_RAAN)
                if (Record_10p7_AP):
                    record_F10p7_AP(value_file,ii+1)
                #simulation(Value_W0,Value_W1,Value_W2,Path_to_file2, 62, 71, 80, rl_file)
    except Exception as e:
        print(f"Oops, something went wrong: {e}")
    finally:
        #time_file.close()
        # print("Done, closing file")
        rl_file.close()
