import itertools
import math
import numpy as np
import subprocess
import os


CUR_DIR = os.getcwd()
TARGET_DIR = CUR_DIR + "/42"
RESULT_ORIGINAL_DIR = TARGET_DIR + "/InOut"
RESULT_DIR = CUR_DIR + "/collected_data"



def sample_F107_AP(N_107,N_AP,low_107,high_107,low_AP,high_AP,dist_type_107,dist_type_AP):
    if dist_type_107=='UNIFORM':
        samples_107=np.random.uniform(low_107,high_107,N_107)
    if dist_type_AP=='UNIFORM':
        samples_AP=np.random.uniform(low_AP, high_AP, N_AP)
    out=np.array(list(itertools.product(samples_107,samples_AP)))
    return out

def keep_comment_clean(new_value, original_line):
    line_len = len(original_line)
    comment = "!" + original_line.split("!")[1]
    comment_len = len(comment)
    num_of_spaces = line_len - comment_len - len(str(new_value))

    return f"{str(new_value)}" + " " * num_of_spaces + comment

def simulation(value_107,value_AP,path,line_107,line_AP, time_file, rl_file):
    lines = list()
    with open(path,'r') as f:
        lines = f.readlines()

        index_107 = line_107 - 1
        lines[index_107] = keep_comment_clean(str(value_107), lines[index_107])

        index_AP = line_AP - 1
        lines[index_AP] = keep_comment_clean(str(value_AP), lines[index_AP])

    with open(path, "w+") as new_f:
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
    with open(f"{RESULT_ORIGINAL_DIR}/time.42", "r") as result_time:
        results = result_time.readlines()
        time_file.write(f"Value F10.7 = {value_107}.\n")
        time_file.write(f"Value AP = {value_AP}.\n")
        time_file.write("=" * 30)
        rl_file.write("\n")
        for result in results:
            time_file.write(result)
        time_file.write("\n")

    # Print metadata for rl.42
    with open(f"{RESULT_ORIGINAL_DIR}/RL.42", "r") as result_time:
        results = result_time.readlines()
        rl_file.write(f"Value F10.7 = {value_107}.\n")
        rl_file.write(f"Value AP = {value_AP}.\n")
        rl_file.write("=" * 30)
        rl_file.write("\n")
        for result in results:
            rl_file.write(result)
        rl_file.write("\n")


if __name__ == "__main__":
    N_107=5
    N_AP=5
    Low_107=100
    High_107=230
    Low_AP=50
    High_AP=100
    Dist_type_107='UNIFORM'
    Dist_type_AP='UNIFORM'
    Path_to_file='./42/InOut/Inp_Sim.txt'

    # Create result folder
    if (not os.path.isdir(RESULT_DIR)):
        print(f"{RESULT_DIR} doesn't exist, creating one...")
        os.mkdir(RESULT_DIR)

    Samples = sample_F107_AP(N_107,N_AP,Low_107,High_107,Low_AP,High_AP,Dist_type_107,Dist_type_AP)

    time_file = open(f"{RESULT_DIR}/time.txt", "w+")
    rl_file = open(f"{RESULT_DIR}/rl.txt", "w+")

    try:
        for ii in range(len(Samples)):
            Value_107=round(Samples[ii,0], 1)
            Value_AP=round(Samples[ii,1], 1)
            simulation(Value_107, Value_AP, Path_to_file, 19, 20, time_file, rl_file)
    except:
        print(f"Oops, something went wrong: {e}")
    finally:
        time_file.close()
        rl_file.close()
