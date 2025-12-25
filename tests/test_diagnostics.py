from ngpu import to_dataframe
from ngpu.ml.diagnostics import CoverageReport


def test_missing_rate_bounds():
    df = to_dataframe()
    report = CoverageReport(df)
    rate = report.missing_rate()
    assert 0.0 <= rate <= 1.0