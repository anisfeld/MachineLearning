# mess with data creat features


def fill_with_mean(df, col,round_to):
	''' 
	Fill missing values in column(s) with mean
		Inputs: df (dataFrame)
				col (string or list of strings)
	'''
	# check dtype to ensure only numeric columns pass, remove non-numeric values
	if isinstance(col, str):
		col = [col]
	
	numeric_cols = df.select_dtypes(include=["int64","float64"]).columns
	clean_col = [c for c in col if c in numeric_cols]

	if clean_col != col:
		#better: figure out how to do Warning
		diff = set(clean_col).diff(col)
		print("Mean is meaningless for columns {}".format(diff))
	
	mean = df[clean_col].mean()
	df[clean_col].fillna(round(mean,round_to), inplace=True)
    # Question: Is it better to return a new variable or fillna(mean, inplace=True)?
	return df

# get schema from csv header

# make table ?

# Put CSV into postgresdb


