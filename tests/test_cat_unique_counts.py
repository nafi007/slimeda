from slimeda.cat_unique_counts import cat_unique_counts

import pandas as pd
import numpy as np
import pytest

def test_cat_unique_counts():
    """Unit test for missing value counts."""
    df1 = pd.DataFrame(data = [['Jessica',10,"cook"],
                        ['Tom',12,"swim"],
                        ['Clarke',1,"football"]], 
                        columns=['Name','Age',"Hobby"])

    df2 = pd.DataFrame([['Alex', 10, '3'],["Marry", 19, '1'],['Clarke', 1, '4']], 
                           columns=['Name','Age',"Rate"])

    df3 = pd.DataFrame(columns=['Name','Age',"Hobby"])

    result1 = list(cat_unique_counts(df1).iloc[:, 0])
    result2 = list(cat_unique_counts(df2).iloc[:, 0])
    result3 = list(cat_unique_counts(df3).iloc[:, 0])

    assert result1 == ['Name', 'Hobby']
    assert result2 == ['Name']
    assert result3 == None

