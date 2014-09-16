from directional import *
import pandas as pd
import numpy as np

demo_sin_cos_matrix = pd.read_csv("sample_data/sin-cos.csv")
demo_sin_cos_mean = pd.read_csv("sample_data/sin-cos-mean.csv")
demo_angle_matrix = pd.read_csv("sample_data/degrees.csv")
demo_radian_matrix = pd.read_csv("sample_data/radians.csv")
demo_radian_mean = pd.read_csv("sample_data/radians-mean.csv")
demo_radian_std = pd.read_csv("sample_data/radians-std.csv")



def test_col_names_from_sin_cos_matrix():
	df = pd.DataFrame(columns = ["N-CA-CB-CG--SIN", "CA-CB-CG-OD1--SIN", "CA-CB-CG-OD2--SIN", "N-CA-CB-CG--COS", "CA-CB-CG-OD1--COS", "CA-CB-CG-OD2--COS"])
	cols = col_names_from_sin_cos_matrix(df)
	assert cols == ["N-CA-CB-CG", "CA-CB-CG-OD1", "CA-CB-CG-OD2"]


def test_sin_cos_matrix_to_radian_matrix():
	result = sin_cos_matrix_to_radian_matrix(demo_sin_cos_matrix.applymap(np.radians)).values
	result = np.around(result, decimals = 2)
	comparison = np.around(demo_radian_matrix.values, decimals = 2)
	assert np.array_equal(comparison, result) 


def test_radian_matrix_to_sin_cos_matrix():
	result = radian_matrix_to_sin_cos_matrix(demo_radian_matrix)
	result = np.around(result, decimals = 2)
	comparison = np.around(demo_sin_cos_matrix.values, decimals = 2)
	assert np.array_equal(comparison, result) 


def test_sin_cos_matrix_to_degrees_matrix():
	result = sin_cos_matrix_to_degrees_matrix(demo_sin_cos_matrix).values
	result = np.around(result, decimals = 2)
	comparison = np.around(demo_angle_matrix.values, decimals = 2)
	assert np.array_equal(comparison, result) 


def test_sin_cos_matrix_mean():
	result = sin_cos_matrix_mean(demo_sin_cos_matrix).values
	result = np.around(result, decimals = 2)
	comparison = np.around(demo_sin_cos_mean.values, decimals = 2)
	assert np.array_equal(comparison[0], result)


def test_sin_cos_matrix_to_radians_mean():
	result = sin_cos_matrix_to_radians_mean(demo_sin_cos_matrix).values
	result = np.around(result, decimals = 2)
	comparison = np.around(demo_radian_mean.values, decimals = 2)
	assert np.array_equal(comparison[0], result)


def test_sin_cos_matrix_to_radian_std():
	result = sin_cos_matrix_to_radian_std(demo_sin_cos_matrix).values
	result = np.around(result, decimals = 2)
	comparison = np.around(demo_radian_std.values, decimals = 2)
	assert np.array_equal(comparison[0], result)


def test_radian_matrix_std():
	result = radian_matrix_std(demo_radian_matrix).values
	result = np.around(result, decimals = 2)
	comparison = np.around(demo_radian_std.values, decimals = 2)
	assert np.array_equal(comparison[0], result)

