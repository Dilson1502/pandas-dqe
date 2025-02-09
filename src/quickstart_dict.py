import pandas as pd  # type:ignore

from decorators import ValidateSchema

# 📌 Sample schemas
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

# 📊 Test Data


data = {
    "id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "age": [25, 30, 35]
}

df_input = pd.DataFrame(data)

# 🔄 Execute
df_output = transform_data(df_input)
print(df_output)
