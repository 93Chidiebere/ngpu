# Nigerian Polling Units

**ngpu** is a Python and R programming library that provides hierarchical intelligence over
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

For R Users: Run in terminal or Anaconda Prompt
```bash
conda create -n ngpu-r -c conda-forge python=3.10 ngpu r-base r-reticulate pandas scikit-learn
```
This installs:

Python
ngpu
R
reticulate
ML dependencies


## Quick Start

```python
from ngpu import Index, to_dataframe

states = Index.states()
lgas = Index.lgas("Lagos")

df = to_dataframe()
```

## Connecting R to ngpu

Open R or RStudio.
```r
library(reticulate)

use_condaenv("ngpu-r", required = TRUE)

ngpu <- import("ngpu")
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

```r
states <- ngpu$Index$states()
print(states)
```
Validate state names in a dataset before analysis.

```r
lgas <- ngpu$Index$lgas("Lagos")
print(lgas)
```
Fill missing LGAs when only state information exists.

```r
df <- ngpu$to_dataframe()
df_r <- py_to_r(df)

head(df_r)
```
Join ngpu data with survey, transaction, or demographic datasets.

### Problem

You have a dataset with:
state
missing lga, ward, polling_unit

### Solution (in R)
```r
library(dplyr)

data <- data.frame(
  state = c("Lagos", "Kano")
)

ngpu_df <- py_to_r(ngpu$to_dataframe())

enriched <- data %>%
  left_join(ngpu_df, by = "state")

head(enriched)
```
Dataset is automatically expanded with valid LGAs, wards, and polling units.

### Machine Learning Usage
```r
encoder <- ngpu$PollingUnitEncoder()

encoded <- encoder$fit_transform(
  state = "Lagos",
  lga = "Ikeja",
  ward = "Ward 1",
  polling_unit = "PU 001"
)

print(encoded)
```
Convert categorical hierarchy into numeric ML-ready features
Used in regression, classification, clustering

### Use with caret/tidymodels
```r
library(caret)

ml_df <- ngpu_df %>%
  select(state, lga, ward) %>%
  mutate(across(everything(), as.factor))

model <- train(
  ward ~ .,
  data = ml_df,
  method = "rf"
)
```
Predict missing administrative attributes
Learn regional patterns
### Data Validation & Diagnotstics
```r
diag <- ngpu$HierarchyDiagnostics()

diag$validate(
  state = "Lagos",
  lga = "Gwale"
)
```
Returns

TRUE → valid
FALSE → impossible combination

Use case:
Catch data errors before modeling
Prevent garbage-in-garbage-out ML


## Common Errors & Fixes

#### Error: ModuleNotFoundError
```r
use_condaenv("ngpu-r", required = TRUE)
```
#### Error: Wrong Python
```r
py_config()
```
Ensure it points to ngpu-r.


## LICENSE

MIT

## Test execution

```bash
pip install -e .[dev]
pytest
```


