import numpy as np
import pandas as pd
from slimeda.histogram import histogram

def test_histogram_single_chart():
    rng = np.random.default_rng()

    # create a dummy date frame with four columns for testing
    df = pd.DataFrame(rng.integers(0, 100, size=(100, 4)), columns=list('ABCD'))
    charts = histogram(df, "A")
    assert charts != None
    assert len(charts) == 1
    assert charts[0] != None
    assert charts[0].data.equals(df)
    assert charts[0].mark == "bar"

def test_histogram_multiple_charts():
    rng = np.random.default_rng()

    # create a dummy date frame with four columns for testing
    df = pd.DataFrame(rng.integers(0, 100, size=(100, 4)), columns=list('ABCD'))
    charts = histogram(df, ["A", "B", "C"])
    assert charts != None
    assert len(charts) == 3
    for chart in charts:
        assert chart != None
        assert chart.data.equals(df)
        assert chart.mark == "bar"