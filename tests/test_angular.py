from directional import *
import pandas as pd
import numpy as np

demo_sin_cos_matrix = pd.read_csv("sample_data/sin-cos.csv")
demo_angle_matrix = pd.read_csv("sample_data/degrees.csv")

def test_col_names_from_sin_cos_matrix():
	df = pd.DataFrame(columns = ["N-CA-CB-CG--SIN", "CA-CB-CG-OD1--SIN", "CA-CB-CG-OD2--SIN", "N-CA-CB-CG--COS", "CA-CB-CG-OD1--COS", "CA-CB-CG-OD2--COS"])
	cols = col_names_from_sin_cos_matrix(df)
	assert cols == ["N-CA-CB-CG", "CA-CB-CG-OD1", "CA-CB-CG-OD2"]


def test_sin_cos_matrix_to_degrees_matrix():
	assert demo_angle_matrix.values == sin_cos_matrix_to_degrees_matrix(demo_sin_cos_matrix).values
