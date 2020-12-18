import pandas as pd
import pickle
df = pd.read_csv('students.csv',delimiter=';')
df['Возраст'] = pd.to_numeric(df['Возраст'])

def getMore22():
    print(df.loc[df['Возраст'] > 22])

def sortFamilie():
    print(df.sort_values('ФИО'))

def writeToCSV():
    df.to_csv('test.csv', encoding='utf-8', index=False)

def appenStudent():
    df.append({'No': '11', 'ФИО': 'Рудак Алан Денисович', 'Возраст': '19', 'Группа': 'БО-111222'}, ignore_index=True)

def saveStudentsCSV():
    df.to_csv('students_changed.csv', encoding='utf-8', index=False)

def saveToPickle():
    df.to_pickle("dummy.pkl")

def readFromPickle():
    unpickled_df = pd.read_pickle("dummy.pkl")

class LabFour():
    fl = 'students.csv'
    def getCSV(self,fl):
        df = pd.read_csv(fl, delimiter=';')
        df['Возраст'] = pd.to_numeric(df['Возраст'])

    def saveStudentsCSV(self, df):
        df.loc[df['Возраст'] > 22]
        df.sort_values('ФИО')
        df.append({'No': '11', 'ФИО': 'Рудак Алан Денисович', 'Возраст': '19', 'Группа': 'БО-111222'}, ignore_index=True)
        df.to_csv('students_changed.csv', encoding='utf-8', index=False)

    def readFromPickle(self):
        unpickled_df = pd.read_pickle("dummy.pkl")

    def saveToPickle(self,df):
        df.to_pickle("dummy.pkl")

