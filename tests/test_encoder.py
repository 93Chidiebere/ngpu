from ngpu import to_dataframe
from ngpu.ml.encoder import PollingUnitEncoder


def test_encoder_output_shape():
    df = to_dataframe().head(100)
    enc = PollingUnitEncoder(level="ward")
    X = enc.fit_transform(df)
    assert X.shape[0] == len(df)
    assert X.shape[1] == 1