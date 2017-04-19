from pipeline.util import map_camel_to_snake
import pandas as pd
import re

def read_csv(file, parse_zipcodes=None, **kwargs):
	'''

	'''
	### parse dates ... 
	# parse zipcodes ... future question 'object' or 'categorical'
	if isinstance(parse_zipcodes, list):
		dtype = {zc: 'str' for zc in parse_zipcodes}
		if kwargs.get("dtype", False):
			kwargs['dtype'] = {**kwargs['dtype'],**dtype}
		else:
			kwargs['dtype'] = dtype



	df = pd.read_csv(file, **kwargs)
	df.columns = map_camel_to_snake(df.columns)
	return df