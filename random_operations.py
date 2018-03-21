import pandas as pd


def float_sum(value_1: float, value_2: float) -> float:
    return value_1 + value_2


def sum_columns(matrix: pd.DataFrame) -> pd.Series:
    return matrix.sum(0)
