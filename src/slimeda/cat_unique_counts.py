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
    


# Helper function
def _is_date(string):
    """
    Check if a string can be parsed as a date
    Parameters
    ----------
    string : str
            string value
    Returns
    -------
    bool
    Examples
    --------
    >>>_is_date('2022-01-13')
    """
    try:
        parse(string)
        return True
    except ValueError:
        return False