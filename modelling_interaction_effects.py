import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

X = pd.Dataframe()

#generating interaction terms
x_interaction = PolynomialFeatures(2, interaction_only=True, include_bias=False).fit_transform(X)

#creating a new dataframe with the interaction terms included
interaction_df = pd.DataFrame(x_interaction, 
                                columns = ['cylinders','displacement','horsepower','weight','acceleration','year','origin',
                                            'cylinders:displacement','cylinders:horsepower','cylinders:weight','cylinders:acceleration',
                                            'cylinders:year','cylinders:origin','displacement:horsepower','displacement:weight',
                                            'displacement:acceleration','displacement:year','displacement:origin','horsepower:weight',
                                            'horsepower:acceleration','horsepower:year','horsepower:origin','weight:acceleration',
                                            'weight:year','weight:origin','acceleration:year','acceleration:origin','year:origin'])