import pandas as pd
def miss_counts(df, keyword=None, sparse=False, ascending=False):
    """
    Return the number of missing values and coresponding percentages for each column in the df. 
    Users can also define a single number or word like "missing" as NaN in this function.
    Parameters
    ----------
    df: pd.DataFrame
        pandas dataframe
    keyword: string or int or float
             Default is None, a single number or string that users want to define
             as NaN along with original NaNs
    sparse: Boolen
            Default is False, meaning don't show columns without null values.
    Ascending: Boolen
            Default is False, to sort the counts ascending or decending.
    Returns
    -------
    pd.DataFrame
    Examples
    --------
    >>>from slimeda import miss_counts
    >>>miss_counts(df,keyword="Missing")
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError(" df should be of type dataframe.")
    if not isinstance(keyword,(float,int,str)):
        raise TypeError(" keyword should be a number or a string.")
    a = []
    for i in df.columns.values.tolist():
        a.append([i,df[i].isna().sum()+len(df.loc[df[i]==keyword])])
    results = pd.DataFrame(a,columns=["Columns","Counts"])
    results["percentage"] = results["Counts"]/len(df)
    results["percentage"] = results["percentage"].apply(lambda x: format(x,".2%"))
    results = results.sort_values(by=["Counts"],ascending=True).set_index("Columns")
    if sparse == False:
        results = results.loc[results["Counts"]!=0]
    if ascending == True:
        results = results.sort_values(by=["Counts"],ascending=True)
    if len(results) == 0:
        return "Congratulations! There is no null value in this dataframe"
    return results