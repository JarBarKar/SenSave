import serial
import csv
from currentTime import getTimeDict
import pandas as pd
import datetime

def startCSV():
    file0 = open('lastMovement.csv', 'a+')

    file1 = open('elderlyHabits.csv', 'a+')

    file2 = open('ownerVisitor.csv', 'a+')

    try:  
        df = pd.read_csv('lastMovement.csv')
    except pd.errors.EmptyDataError:
        df0 = pd.DataFrame({
            'year' : 0,
            'month' : 0,
            'day' : 0,
            'hour' : 0,
            'minute' : 0,
            'second' : 0,
            'location': ['living room']
            })
        df0.to_csv('lastMovement.csv', mode='a', index=False, header=True)

    try:  
        df = pd.read_csv('elderlyHabits.csv')
    except pd.errors.EmptyDataError:
        df1 = pd.DataFrame({
            'year' : 0,
            'month' : 0,
            'day' : 0,
            'hour' : 0,
            'minute' : 0,
            'second' : 0,
            'weekday' : 0,
            'duration': [1],
            'location' : ['living room']
            })
        df1.to_csv('elderlyHabits.csv', mode='a', index=False, header=True)

    try:  
        df = pd.read_csv('ownerVisitor.csv')
    except pd.errors.EmptyDataError:
        df2 = pd.DataFrame({
            'year' : 0,
            'month' : 0,
            'day' : 0,
            'hour' : 0,
            'minute' : 0,
            'second' : 0,
            'personCount': [1],
            'elderly' : [True]
            })
        df2.to_csv('ownerVisitor.csv', mode='a', index=False, header=True)

