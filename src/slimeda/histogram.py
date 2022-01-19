import altair as alt

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

    charts = []
    for col in columns:
        current_chart = alt.Chart(df).mark_bar().encode(
            x=alt.X(col, bin=True),
            y="count()"
        )
        charts.append(current_chart)
    return charts