import pandas as pd
import numpy as np

# mess with data create features
def fill_with(df, col, group=None,round_to=2):
	''' 
	Fill missing values in column(s) with mean or median of column dependant on type
	columns in col should be numeric (int64 or float64)
		Inputs: df (dataFrame)
				col (string or list of strings)
	'''
	if isinstance(col, str):
		col = [col]
	
	# check dtype to ensure only numeric columns pass, remove non-numeric values
	num_cols = df.select_dtypes(include=["int64","float64"]).columns
	
	clean_col = [c for c in col if c in num_cols]

	if clean_col != col:
		#better: figure out how to do Warning
		diff = set(col).difference(set(clean_col))
		print("Mean/Median is meaningless for columns {}".format(diff))
	
	# 
	float_cols = df[clean_col].select_dtypes(include=["float64"]).columns
	int_cols = df[clean_col].select_dtypes(include=["int64"]).columns

	#if group use group level mean/median
	if group:
		df[float_cols] = df.groupby(group)[float_cols].transform(lambda x: x.fillna(x.mean()))
		df[int_cols] = df.groupby(group)[int_cols].transform(lambda x: x.fillna(x.median()))

	else:
		mean = df[float_cols].mean()
		df[float_cols] = df[float_cols].fillna(round(mean,round_to))

		median = df[int_cols].median()
		df[int_cols] = df[int_cols].fillna(round(median,round_to))

	return df[clean_col]



def cap_values(x, cap, kill = False):
	"""	
	x (numeric)
	cap (numeric)
	kill (boolean) If true, return NaN for all values above the threshold.

	ex:
		df[col] = df.col.apply(lambda x: cap_values(x, 15000))
	credit: 
		https://github.com/yhat/DataGotham2013/blob/master/notebooks/7%20-%20Feature%20Engineering.ipynb
	"""
	if x > cap:
		if kill:
			return np.nan
		return cap
	else:
		return x


def floor_values(x, floor, kill = False):
	"""	
	x (numeric)
	floor (numeric)
	kill (boolean) If true, return NaN for all values below the threshold.

	ex:
		df[col] = df.col.apply(lambda x: floor_values(x, 15000))
	inspired by cap at: 
		https://github.com/yhat/DataGotham2013/blob/master/notebooks/7%20-%20Feature%20Engineering.ipynb
	"""
	if x < floor:
		if kill:
			return np.nan
		return floor
	else:
		return x
# get schema from csv header

# make table ?

# Put CSV into postgresdb

def cut(x, bins=4, method=pd.qcut, labels=None, cap=None, floor=None, **kwargs):
    '''
    convert real values to categorical data
    
    inputs:
        x (array-like)
        bins (int or list) 
        method (e.g. pd.cut for fixed width cuts, pd.qcut for distribution-based cuts) 
        labels (list or keyword "auto") (if "auto", generate integer labels; if None, return range for group)
        cap (numeric) sets all values above a threshold to the cap value
        floor (numeric) sets all values below a threshold to the floor
        **kwargs (built on top of pandas cut/qcut see pandas docummentation for more detail)
    
    returns:
        array-like object
    '''

    # Check for caps and floors prior to cutting.
    if isinstance(cap, (int,float)):
	    x = x.apply(lambda z: cap_values(z, cap))
    
    if isinstance(floor, (int,float)):
	    x = x.apply(lambda z: floor_values(z, floor))
    
    # If generating ordered labels automatically
    if labels=="auto":
    	try:
    		labels = range(bins)
    	except:
	    	labels = range(len(bins)-1)
    return method(x,bins, labels=labels, **kwargs)


def convert_bools(df, bool_cols):
    for col in bool_cols:
        df[col] = df[col].astype(np.bool)

def get_dummies(data,auxdf=None, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=False):
	'''
	convert categorical values (set of k) to dummy variables (in k columns)

	inputs:
	    data (array-like)
	    auxdf (dataFrame)
	    other args (built on top of pandas get_dummies see pandas docummentation for more detail)

	returns:
	    array-like object
	'''

	dummies = pd.get_dummies(data, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=False).astype(np.int8)
	if isinstance(auxdf, pd.DataFrame):
		df = pd.concat([auxdf, dummies],axis=1)
		return df
	return dummies








'''
SNIPPETS FOR FUTURE WORK PLEASE IGNORE
	out = pd.DataFrame(index=data.index)
	for col in columns:
		for item in data[col].unique():
			out[item] = 0
			out.ix[out.[col]==item,item] = 1
	return out
'''




