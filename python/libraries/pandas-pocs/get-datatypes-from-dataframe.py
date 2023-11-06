import pandas
import numpy 

dataFrame = pandas.read_csv('online_shoppers_intention.csv')

data_types = dict(dataFrame.dtypes)


def get_dataTypes(dataFrame):
    data_types = dict(dataFrame.dtypes)
    numeric_columns = []
    categoric_columns = []
    
    for key,value in data_types.items():
        if value == numpy.float64:
            numeric_columns.append([key, 'Cuantitativa continua', dataFrame[key].mean(), dataFrame[key].min(), dataFrame[key].max(), dataFrame[key].median()])
        elif value == numpy.int64 or pandas.Int64Dtype.is_dtype(key):
            numeric_columns.append([key, 'Cuantitativa discreta', dataFrame[key].mean(), dataFrame[key].min(), dataFrame[key].max(), dataFrame[key].median()])
        elif value == numpy.bool_:
            categoric_columns.append([key, f'Cualitativa', dataFrame[key].nunique()])   
        else:
            categoric_columns.append([key, f'Cualitativa', dataFrame[key].nunique()])
    numeric = pandas.DataFrame(numeric_columns, columns=['Nombre', 'Tipo de variable', 'Media', 'Mínimo', 'Máximo', 'Mediana'])
    categoric = pandas.DataFrame(categoric_columns, columns=['Nombre', 'Tipo de variable', 'Número de clases'])
    return numeric, categoric

numeric_types, categoric_types = get_dataTypes(dataFrame)

print(numeric_types)

print (categoric_types)