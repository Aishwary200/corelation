import csv
import pandas as pd
import plotly_express as px
import numpy as np

def  main(data_path):
    with open(data_path) as f:
        reader=csv.DictReader(f)
        fig=px.scatter(reader,x='Temperature',y='Ice-cream Sales')
        fig.show()
def getData(data_path):
    icecrame_sales = []
    colddrink_sales = []
    with open(data_path) as f:
        df = csv.DictReader(f)
        for row in df:
            icecrame_sales.append(float(row['Temperature']))
            colddrink_sales.append(float(row['Ice-cream Sales']))
        return {'x': icecrame_sales, 'y': colddrink_sales}


def findCoRelation(datasource):
    corelation = np.corrcoef(datasource['x'], datasource['y'])
    print(corelation[0,1])


def setup():
    data_path = './sales.csv'
    data_source = getData(data_path)
    findCoRelation(data_source)
    main(data_path)

setup()
