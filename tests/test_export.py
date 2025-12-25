from ngpu import to_dataframe


def test_dataframe_structure():
    df = to_dataframe()
    assert {"state", "lga", "ward", "polling_unit"}.issubset(df.columns)
    assert len(df) > 0