from pandas import read_csv
from matplotlib import pyplot


file_name = "/Users/ramideltoro/ml/diabetes.csv"
raw_data = open(file_name, 'rt')
names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
data = read_csv(file_name,names=names)

data.plot(kind='box', subplots=True,layout=(3,3,), sharex=False)

pyplot.show()
