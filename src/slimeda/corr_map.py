

def corr_map(df, columns, path=""):
    """
    Creates correlation map chart object for specific columns in a data frame
    
    Parameters
    ----------
    df: pd.DataFrame
        pandas dataframe
    columns: list
        list of columns to create the correlation map for
    path: string [default value of ""]
        the file path indicating where the image is stored
        by default it would store at the current working directory
    
    Returns
    -------
    Chart

    Examples
    --------
    >>>from slimeda import corr_map
    >>>corr_map(df, ['age', 'income'])
    """