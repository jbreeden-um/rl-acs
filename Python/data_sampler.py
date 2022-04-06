import numpy as np
import torch
import random
import pandas

class data_sampler:
	def __init__(self):
		self.path_to_data = "D:/Joseph/Dropbox (University of Michigan)/EECS598/rl_deterministic.txt"
		self.chunk_length = 55550
		self.max_chunk = 1e4
		self.num_rows_to_skip = 10
		self.num_chunks_read = 0
		self.data = None
		
	def use_chunk(self, num)
		self.num_chunks_read = num
		
	def read_chunk(self):
		self.data = pandas.read_csv(self.path_to_data, skiprows=10, nrows=self.chunk_length)
		
	def get_batch(self, batch_size):