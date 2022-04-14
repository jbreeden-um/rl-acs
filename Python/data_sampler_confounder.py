import numpy as np
import torch
import random
import pandas

class DataSampler:
    def __init__(self, path_to_data="../collected_data/rl_deterministic.txt"):
        self.path_to_data = path_to_data
        self.chunk_length = 27771
        self.max_chunk = 1e4
        self.skip_header = 6
        self.skip_footer = 1
        self.num_chunks_read = 0
        self.data = None
        
    def use_file(self, filename):
        self.path_to_data = filename
        
    def use_chunk(self, num):
        self.num_chunks_read = num
        
    def read_chunk(self):
        if self.num_chunks_read >= self.max_chunk:
            return None
        
        # lines_per_chunk = self.chunk_length + self.skip_header + self.skip_footer
        # current_line = self.num_chunks_read*lines_per_chunk + self.skip_header
        
        with open(self.path_to_data, "r") as input:
            input.seek(max(11664000*self.num_chunks_read - 10000, 0))
            count = 0
            line = input.readline()
            while line[0:11] != "Value F10.7":
                line = input.readline()
                count += 1
                # print(line[:-1])
            # print("Skipped: ", count)
            
            for i in range(self.skip_header-1):
                input.readline()
              
            self.data = pandas.read_csv(input, header=None, skiprows=0, usecols=range(21), dtype=np.float64, nrows=self.chunk_length).to_numpy()
            
            self.num_chunks_read += 1
            # print(self.data[0])
            
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
        
        position = self.data[batch,14:17];
        hparallel = np.vstack([np.cross(position[0:-5,:], position[5:,:]), np.cross(position[-10:-5,:], position[-5:,:])]);
        hhat = hparallel / np.linalg.norm(hparallel, axis=1)[:, None];
        
        States = self.data[batch,2:5];
        Actions = self.data[batch,8:11];
        MagField = self.data[batch,18:21];
        dt = self.data[1,0];
        mu = 398600e9;
        a = 6778e3;
        H_expected = States + dt*(np.cross(Actions, MagField) - np.sqrt(mu/a**3)*np.cross(hhat, States));
        Tdist = np.vstack([States[1:,:] - H_expected[:-1,:], [0, 0, 0]])
        Tdist[-1,:] = Tdist[-2,:]
        # print(Tdist)
        metric = np.linalg.norm(Tdist, axis=1);
        
        # Reward is negative of the cost
        # Cost is the wheel momentum after the action is applied
        # Should we instead make the reward the change in momentum between steps?
        reward_batch = torch.Tensor(np.vstack([y for y in -np.linalg.norm(self.data[[x+1 for x in batch],2:4], axis=1)]))
        
        return state_batch, action_batch, reward_batch, next_state_batch, metric
        
# random.seed(0)
# samples = DataSampler()
# samples.use_file("RL.42")
# samples.use_chunk(9999)
# samples.read_chunk()
# [states, actions, rewards, next_states, metric] = samples.get_batch(15)
# print(states)
# print(actions)
# print(rewards)
# print(next_states)
# print(metric)