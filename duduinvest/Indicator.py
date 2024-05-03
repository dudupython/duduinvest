from .General import HistoricalPrice

class BBand(HistoricalPrice):
	""" Gaussian distribution class for calculating and 
	visualizing a Gaussian distribution.
	
	Attributes:
		mean (float) representing the mean value of the distribution
		stdev (float) representing the standard deviation of the distribution
		data_list (list of floats) a list of floats extracted from the data file
			
	"""
	def __init__(self, ticker='VCB', start_date='2018-01-01'):
		
		HistoricalPrice.__init__(self, ticker, start_date)
	
		
	
	def calculate_mean_return(self):
	
		"""Function to calculate the mean of the data set.
		
		Args: 
			None
		
		Returns: 
			float: mean of the data set
	
		"""
					
		avg = self.data.close.mean()
		
		self.mean = avg
		
		return self.mean
