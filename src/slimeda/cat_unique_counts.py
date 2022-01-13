import pandas as pd
from dateutil.parser import parse

value_counts = []
VALID_TYPES = [pd.DataFrame]

def cat_unique_counts(df):
    """
    Return unique value count of categorical features
    Parameters
    ----------
    df: pd.DataFrame
        pandas dataframe
    Returns
    -------
    pd.DataFrame
    Examples
    --------
    >>>from slimeda import cat_unique_counts
    >>>cat_unique_counts(df)
    """
    
    