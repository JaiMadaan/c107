import csv
import plotly_express as px
import numpy as np

def getDataSource(data_path):
    marks=[]
    daysinpresent=[]
    with open(data_path) as csv_file :
        reader=csv.DictReader(csv_file)
        for row in reader:
            marks.append(float(row['Marks In Percentage']))
            daysinpresent.append(float(row['Days Present']))

    return{'x':marks,'y':daysinpresent}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])

    print('correlation between marks and number of days present',correlation)

def setup():
    data_path="Student Marks vs Days Present.csv"
    dataSource=getDataSource(data_path)
    findCorrelation(dataSource)


setup()
