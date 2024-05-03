from .get_data import get_historical_price

class HistoricalPrice:
	
    def __init__(self, ticker='VCB', start_date='2018-01-01'):
	
        """ Generic distribution class for calculating and 
        visualizing a probability distribution.

        Attributes:
            mean (float) representing the mean value of the distribution
            stdev (float) representing the standard deviation of the distribution
            data_list (list of floats) a list of floats extracted from the data file
            """
        
        self.ticker = ticker
        self.start_date = start_date
        self.data = self.get_data(ticker, start_date)
    
    def get_data(self, ticker, start_date):
        data = get_historical_price(self.ticker, self.start_date)
        data = data.droplevel("Symbols", axis=1)
        return data

