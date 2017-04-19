import pylab as pl
import seaborn as sns
import numpy as np


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