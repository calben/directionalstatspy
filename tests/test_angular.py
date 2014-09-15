from directional import *
import pandas as pd
import numpy as np

def test_col_names_from_sin_cos_matrix():
	df = pd.DataFrame(columns = ["N-CA-CB-CG--SIN", "CA-CB-CG-OD1--SIN", "CA-CB-CG-OD2--SIN", "N-CA-CB-CG--COS", "CA-CB-CG-OD1--COS", "CA-CB-CG-OD2--COS"])
	cols = col_names_from_sin_cos_matrix(df)
	assert cols == ["N-CA-CB-CG", "CA-CB-CG-OD1", "CA-CB-CG-OD2"]


