import pandas
import numpy 


dataFrame = pandas.read_csv('online_shoppers_intention.csv')


numerical_columns = ['SpecialDay','Administrative','Administrative_Duration','Informational','Informational_Duration','ProductRelated','ProductRelated_Duration','BounceRates','ExitRates','PageValues']


Q1 = dataFrame[numerical_columns].quantile(0.25)

Q3 = dataFrame[numerical_columns].quantile(0.75)

print( "Q1 =   " , Q1)


print( "Q3 =   " , Q3)

IQR = Q3 - Q1

print("IQR =   " , IQR)

upper_limit = Q3 + 1.5 * IQR

lower_limit = Q1 - 1.5 * IQR


dataFrame_cleaned = dataFrame[~((dataFrame[numerical_columns] < (lower_limit)) | (dataFrame[numerical_columns] > (upper_limit))).any(axis=1)]

print(dataFrame_cleaned.head)


print(f'Número de filas (sin valores atípicos): {dataFrame_cleaned.shape[0]}')

