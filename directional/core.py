import numpy as np 
import scipy as sp 
import pandas as pd 


###########################
# PANDAS MATRIX CONVERSIONS
###########################


def sin_cos_matrix_to_radian_matrix(sin_cos_matrix):
  radian_matrix = pd.DataFrame(index = sin_cos_matrix.index)
  for name in [col[:-5] for col in sin_cos_matrix.columns]:
    radian_matrix[name] = np.arctan2(sin_cos_matrix[name + "--SIN"].values, sin_cos_matrix[name + "--COS"].values)
  return radian_matrix


def radian_matrix_to_sin_cos_matrix(radian_matrix):
  sin_matrix = radian_matrix.apply(np.sin)
  sin_matrix.columns = map(lambda x : x + "--SIN", radian_matrix.columns)
  cos_matrix = radian_matrix.apply(np.cos)
  cos_matrix.columns = map(lambda x : x + "--COS", radian_matrix.columns)
  return pd.concat([sin_matrix, cos_matrix], axis=1, join='outer', join_axes=None, ignore_index=False, keys=None, levels=None, names=None, verify_integrity=True)


def sin_cos_matrix_to_degrees_matrix(sin_cos_matrix):
  return sin_cos_matrix_to_radian_matrix(sin_cos_matrix).applymap(np.degrees)


def sin_cos_pair_std(sin_cos_matrix):
	mean = sin_cos_pair_mean(sin_cos_matrix)
	mean.apply(lambda x : np.sqrt())


def sin_cos_pair_mean(sin_cos_matrix):
	return sin_cos_matrix.mean()


