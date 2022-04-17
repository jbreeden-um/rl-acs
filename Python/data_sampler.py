import numpy as np
import torch
import random
import pandas
  
class DataSampler:
    def __init__(self, path_to_data="../collected_data/rl_deterministic.txt"):
        self.path_to_data = path_to_data
        self.chunk_length = 27771
        self.max_chunk = 1e4
        self.bytes_per_chunk = 11664000
        self.bytes_offset = 10000
        self.skip_header = 6
        self.skip_footer = 1
        self.num_chunks_read = 0
        self.data = None
        
    def setting(self, setting):
        if setting == "original":
            self.chunk_length = 27771
            self.max_chunk = 1e4
            self.bytes_per_chunk = 11664000
            self.bytes_offset = 10000
            self.skip_header = 4
            self.skip_footer = 1
        elif setting == "coarse":
            self.chunk_length = 1111
            self.max_chunk = 4999
            self.bytes_per_chunk = 444700
            self.bytes_offset = 1000
            self.skip_header = 4
            self.skip_footer = 1
        
    def use_file(self, filename):
        self.path_to_data = filename
        
    def use_chunk(self, num):
        self.num_chunks_read = num
        
    def read_chunk(self):
        if self.num_chunks_read >= self.max_chunk:
            return None
        
        # lines_per_chunk = self.chunk_length + self.skip_header + self.skip_footer
        # current_line = self.num_chunks_read*lines_per_chunk + self.skip_header
        
        # print("is anything happening?")
        with open(self.path_to_data, "r") as input:
            input.seek(max(self.bytes_per_chunk*self.num_chunks_read - self.bytes_offset, 0))
            count = 0
            print("start")
            line = input.readline()
            # print("finish")
            while line[0:12] != "Value Wheel0":
                line = input.readline()
                count += 1
                # print(line[:-1])
                # rint(line[0:11])
            # print("Skipped: ", count)
            
            for i in range(self.skip_header-1):
                input.readline()
              
            self.data = pandas.read_csv(input, header=None, skiprows=0, usecols=range(11), dtype=np.float64, nrows=self.chunk_length).to_numpy()
            
            self.num_chunks_read += 1
            print(self.data[0])
            
            print("Read chunk #", self.num_chunks_read, "out of", int(self.max_chunk))
        
    def get_batch(self, batch_size):
        if batch_size > self.chunk_length-1:
            batch_size = self.chunk_length-1
        
        
        #batch = random.sample(range(self.chunk_length-1), batch_size)
        batch = [i for i in range(batch_size)]
        # print(self.data[batch])
        
        state_batch = torch.Tensor(self.data[batch,2:8])
        next_state_batch = torch.Tensor(self.data[[x+1 for x in batch],2:8])
        action_batch = torch.Tensor(self.data[batch,8:11])
        
        # Reward is negative of the cost
        # Cost is the wheel momentum after the action is applied
        # Should we instead make the reward the change in momentum between steps?
        reward_batch = torch.Tensor(np.vstack([y for y in -np.linalg.norm(self.data[[x+1 for x in batch],2:4], axis=1)]))
        
        return state_batch, action_batch, reward_batch, next_state_batch
        
# random.seed(0)
# samples = DataSampler()
# samples.setting("coarse")
# print(samples.chunk_length)
# samples.use_chunk(9999)
# samples.read_chunk()
# [states, actions, rewards, next_states] = samples.get_batch(5)
# print(states)
# print(actions)
# print(rewards)
# print(next_states)
