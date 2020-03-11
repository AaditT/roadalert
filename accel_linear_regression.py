import pandas as pd
import numpy as np
from sklearn import linear_model

df = pd.read_csv("pothole_data.csv")
reg = linear_model.LinearRegression()
reg.fit(df[['x','y','z']],df.pothole_severity)
