from typing import Any, Callable, Dict, Union

import pandas as pd  # type: ignore


class ValidateSchema:
    """
    Pandas DataFrame Schema Validator.

    Validate the schema of a Pandas DataFrame before and after a function execution.

    Args:
        input_schema: expected schema of the input DataFrame.
        output_schema: expected schema of the output DataFrame.

    Returns:
        pd.DataFrame: output DataFrame after transformation.
    """

    def __init__(self, input_schema: Union[Any, Dict[str, Any]], output_schema: Union[Any, Dict[str, Any]]) -> None:
        self.input_schema = input_schema
        self.output_schema = output_schema

    def _validate_schema(self, df: pd.DataFrame, expected_schema: Union[Any, Dict[str, Any]], stage: str) -> None:
        """
        Validate DataFrame schema versus expected one.

        Args:
            df (pd.DataFrame): input or Output Pandas DataFrame to validate.
            expected_schema (Union[Any, Dict[str, Any]]): expected schema for the DataFrame.
            stage (str): validation stage ("input" or "output").

        Returns:
            None

        Raises:
            ValueError: if there are missing columns in the DataFrame.
            TypeError: if the DataFrame columns have unexpected types.
        """

        missing_columns = set(expected_schema.keys()) - set(df.columns)
        if missing_columns:
            raise ValueError(f"""❌ [Error in {stage}] the following columns are missing in the DataFrame:
                              {missing_columns}""")

        for column, expected_type in expected_schema.items():
            if column in df.columns:
                actual_types = df[column].dropna().map(type).unique()
                if not all(issubclass(t, expected_type) for t in actual_types):
                    raise TypeError(
                        f"""❌ [Error in {stage}] Column '{column}':
                        expect {expected_type}, got {actual_types}"""
                    )

    def __call__(self, func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> pd.DataFrame:
            """Validate DataFrame schema before and after function execution.

            Raises:
                TypeError: if the function does not return a Pandas DataFrame.

            Returns:
                pd.DataFrame: output DataFrame after transformation.
            """
            df_input = args[0]

            # 🔍 Validate input DataFrame
            self._validate_schema(df_input, self.input_schema, "input")

            # 🔄 Execute transformation
            df_output = func(*args, **kwargs)

            if not isinstance(df_output, pd.DataFrame):
                raise TypeError("Funtion must return a Pandas DataFrame.")

            # 🔍 Validate output DataFrame
            self._validate_schema(df_output, self.output_schema, "output")

            return df_output

        return wrapper
