import pandas as pd

# Helper Functions
def check_nulls(df, col):
    '''
    returns df with NaN in specified column(s)
    '''
    return df.ix[df.ix[:,col].isnull()]

def get_notnulls(df, col):
    '''
    returns df without NaN in specified column(s)
    '''
    return df.ix[df.ix[:,col].notnull()]



def clean_data(df, cleaning_tuples):
    '''
    replace a string in a column (pat) with a clean string (repl):
    e.g. cleaning_tuples = [(col, pat, repl)]
    '''
    for col, pat, repl in cleaning_tuples:
        df.ix[:,col] = df.ix[:,col].str.replace(pat, repl)
        
def clean_grouped_data(grouped_df,col=0):
    '''
    returns df with counts that result from groupby
    '''
    counts = pd.DataFrame(grouped_df.count().ix[:,col])
    counts = counts.unstack()
    counts.columns = counts.columns.droplevel()
    counts.columns.name = None
    counts.index.name = None
    counts.fillna(0, inplace=True)
    return counts


def camel_to_snake(column_name):
    """
    converts a string that is camelCase into snake_case
    Example:
        print camel_to_snake("javaLovesCamelCase")
        > java_loves_camel_case
    See Also:
        http://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-camel-case
    """
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', column_name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()