import pandas as pd
from sklearn.datasets import load_diabetes

diabetes_data = load_diabetes()

diabetes_data_return_X_y = load_diabetes(return_X_y=True)

print("diabetes_data_return_X_y:", diabetes_data_return_X_y)
print("diabetes_data_return_X_y[0]:" ,diabetes_data_return_X_y[0] )
print("diabettes_data_return_X_y[1]:" ,diabetes_data_return_X_y[1])

diabetes_data_as_frame = load_diabetes(as_frame=True)
print("diabetes_data_as_frame:", diabetes_data_as_frame)