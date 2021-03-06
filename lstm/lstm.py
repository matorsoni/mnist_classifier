from lstm_block import *


class LSTM:
	def __init__(self, inp_size: int, out_size: int, y_activation = 'sigmoid'):
		'''
		
		
		
		
		T = total number of timestamps 
		'''
		self.inp_size = inp_size
		self.out_size = out_size
		self.block = LSTM_Block(1, inp_size, out_size)
		self.Y, self.d_Y = choose(y_activation)
		
		self.w_hy = np.random.randn(out_size, out_size) # weighted output y_t
		self.b_y = np.random.randn(out_size, 1) # biased output y_t
	
	def initialize(self):
		self.block.compute(np.zeros([self.inp_size, 1]))
		
	def single_forward_pass(self, x_t):
		self.block.compute(x_t)
		y = self.Y(self.b_y + np.dot(self.w_hy, self.block.get_h(-1))) # Y(y), Y=sigmoid -> can be changed
		return y
		
	def forward_pass(self, x_inputs:list):
		# input = list[x_0, x_1, x_2, ...], x_i = column np.array
		output_list = []
		for t in range(len(x_inputs)):
			y = self.single_forward_pass(x_inputs[t])
			output_list.append(deepcopy(y))  
		
		return output_list
	
	def reset_block(self):
		self.block.reset()