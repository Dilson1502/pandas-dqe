# pandas-dqe

Pandas DataFrame Data Quality Engine, decorators to enhace function schema validation before and after transformation execution.

## Authors

- [@dilson1502](https://www.github.com/dilson1502)

## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
![python3.9](https://img.shields.io/badge/Python-3.9-blue)

## Run Locally

Clone the project

```bash
  git clone https://github.com/Dilson1502/pandas-dqe.git
```

Go to the project directory

```bash
  cd ./src/
```

Create a virtual env

```bash
  python -m <env name> venv
```

Install dependencies

```bash
  pip install -r requirements-devel.txt
```

You can define schemas as dictionaries, see example running:

```bash
  python src/quickstart_dictionaries.py
```

You can define schemas as dataclasses, see example running:

```bash
  python src/quickstart_dataclasses.py
```

Example usage using dictionaries as input.

Define input and output schemas.

```python
INPUT_SCHEMA = {
    "id": int,
    "name": str,
    "age": int
}

OUTPUT_SCHEMA = {
    "user_id": int,
    "full_name": str,
    "age_in_10_years": float
}
```

Add the decorator to your transformation function.

```python
@ValidateSchema(input_schema=INPUT_SCHEMA, output_schema=OUTPUT_SCHEMA)
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """Transforms a DataFrame by renaming columns and adding a new column.

    Args:
        df (pd.DataFrame): input DataFrame.

    Returns:
        pd.DataFrame: transformed DataFrame.
    """
    df = df.rename(columns={"id": "user_id", "name": "full_name"})
    df["age_in_10_years"] = df["age"] + 10
    df["age_in_10_years"] = df["age_in_10_years"].astype(float)
    df = df.drop(columns=["age"])
    return df
```

Execute your function.

```python.
data = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
}

df_input = pd.DataFrame(data)

transform_data(df_input)
```

Errors will arise otherwise your transformation will continue as expected!
