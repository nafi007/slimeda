

def histogram(df, columns, path=""):
    """
    Creates histogram chart objects for specific columns in a data frame
    Parameters
    ----------
    df: pd.DataFrame
        pandas dataframe
    columns: list
        list of columns to create histograms for
    Returns
    -------
    Chart[]
    Examples
    --------
    >>>from slimeda import histogram
    >>>histogram(df, ['age', 'income'])
    """