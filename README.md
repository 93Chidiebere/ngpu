# Nigerian Polling Units

**ngpu** is a Python library that provides hierarchical intelligence over
Nigeria’s polling unit administrative structure, designed specifically
for machine learning, analytics, and research workflows.

## Features

- Programmatic access to States, LGAs, Wards, and Polling Units
- ML-ready DataFrame export
- Hierarchical categorical encoders
- Coverage and bias diagnostics
- Fuzzy search for noisy text inputs

## Installation

```bash
pip install ngpu
```

## Quick Start

```python
from ngpu import Index, to_dataframe

states = Index.states()
lgas = Index.lgas("Lagos")

df = to_dataframe()
```

## Machine Learning Usgae

```python
from ngpu.ml.encoder import PollingUnitEncoder

encoder = PollingUnitEncoder(level="ward")
X = encoder.fit_transform(df)
```

## Coverage Diagnostics

```python
from ngpu.ml.diagnostics import CoverageReport

report = CoverageReport(df)
report.coverage_by_state()
```

## Use Cases

Regional ML feature engineering

Bias and coverage analysis

Socio-economic modeling

Civic tech and policy research

Any domain requiring stable Nigerian administrative anchors

## LICENSE

MIT

## Test execution

```bash
pip install -e .[dev]
pytest
```


