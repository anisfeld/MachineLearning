import pylab as pl
import seaborn as sns
import numpy as np
import pandas as pd


def summary_by_outcome(df, col, round_to=2):
	'''
	'''
	split_data = df.groupby(col)

	return round(split_data.describe(percentiles=[.5]),round_to).T



def correlation_plot(df):
	'''
	Makes a correlation plot of numeric columns in dataframe
	df (pd.DataFrame)
	Relied heavily on: http://seaborn.pydata.org/examples/many_pairwise_correlations.html
	'''
	sns.set(style="white")
	corr = df.corr()
	corr = corr.sort_index(axis=0).sort_index(axis=1)
	# Generate a mask for the upper triangle
	mask = np.zeros_like(corr, dtype=np.bool)
	mask[np.triu_indices_from(mask)] = True

	# Set up the matplotlib figure
	f, ax = pl.subplots(figsize=(20, 9))

	# Generate a custom diverging colormap
	cmap = sns.diverging_palette(220, 10, as_cmap=True)

	# Draw the heatmap with the mask and correct aspect ratio
	sns.heatmap(corr, mask=mask, cmap=cmap, vmax=1, square=True,
	            linewidths=.5, cbar_kws={"shrink": .7})

def print_null_freq(df):
    """
    for a given DataFrame, calculates how many values for 
    each variable is null and prints the resulting table to stdout
    Code from: https://github.com/yhat/DataGotham2013/blob/master/notebooks/3%20-%20Importing%20Data.ipynb
    """
    df_lng = pd.melt(df)
    null_variables = df_lng.value.isnull()
    return pd.crosstab(df_lng.variable, null_variables)

'''
Useful APIs:
seaborn.tsplot(data, time=None, unit=None, condition=None, 
			value=None, err_style='ci_band', ci=68, interpolate=True, 
			color=None, estimator=<function mean>, n_boot=5000, 
			err_palette=None, err_kws=None, legend=True, ax=None, 
			**kwargs)



'''





