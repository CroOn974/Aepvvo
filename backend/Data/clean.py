import pandas as pd
import numpy as np
from sqlalchemy import create_engine

conn= 'postgresql://postgres:0000@localhost:5432/aepvvo'
engine=create_engine(conn)

df = pd.read_csv('car_price_prediction.csv')

def cleanData(df) :
    # df.info()
    # print(df.describe())

    # print levy avec '-'  total: 5819 lignes
    # print(df[df['Levy'] == '-'])
    #### Remplace '-' en null
    df['Levy'].replace({'-':np.nan}, inplace = True)
    ####  Levy en float
    df['Levy'] = df['Levy'].astype('float64')
    # df.info()
    #check dupp
    # dupp = df[df['ID'].duplicated() == True]
    
    df.drop_duplicates(subset=['ID'], keep='first',inplace=True)
    
    # df = df.drop_duplicates(subset=['ID'], keep='first')
    
    ## datetime
    df['Prod. year'] = pd.to_datetime(df['Prod. year'],format='%Y')
    
    ####transforme leather interior en bool
    df['Leather interior'].replace({'Yes': True, 'No':False}, inplace=True)
    
    ###uppercase nom model  ex:Cayenne S et s
    df['Model'] = df['Model'].str.upper()
    ####lowercase turbo
    df['Engine volume'] = df['Engine volume'].str.lower()
    ####lignes avec turbo
    df['Turbo'] = df['Engine volume'].str.contains('turbo')
    #### slice turbo puis conversion en float
    df['Engine volume'] = df['Engine volume'].str.slice(0,3)
    df['Engine volume'] = df['Engine volume'].astype('float64')

    ####supp km puis conversion en int
    df['Mileage'] = df['Mileage'].str.strip('km')
    df['Mileage'] = df['Mileage'].astype('int64')

    #### nettoyage portes
    df['Doors'].replace({'04-May':'4-5', '02-Mar':'2-3', '>5':'4-5'}, inplace=True)

    #### converison cylindre en int 
    df['Cylinders'] = df['Cylinders'].astype(int)

    #### suppr prix anormaux
    # print(df[df.Price == df.Price.max()])
    # print(df[df.Price < 1000])
    df = df[df['Price'] > 1000]
    # print(df[df.Price > 100000])
    df = df[df['Price'] < 100000]

    #### remplis les null par median
    df['Levy'] = df['Levy'].fillna(df['Levy'].median())

    df.to_csv('cleanData.csv',index=False)

    # print(df.nlargest(10, 'Price'))

    return df

cleanDf=cleanData(df)
# print(cleanDf)

def manufacturerDf(df):
    df = df.iloc[:, [3]]
    df = df.drop_duplicates(subset=['Manufacturer'], keep='first')
    df.rename(columns={'Manufacturer': 'manufacturer_libele'}, inplace=True)
    return df

manufacturerTable=manufacturerDf(cleanDf)   
    

def modelDf(df):
    df = df.iloc[:, [3,4]]
    df = df.drop_duplicates(subset=['Model'], keep='first')
    df.rename(columns={'Manufacturer': 'manufacturer_libele',"Model":"model_libele"},inplace = True)
    ##PRIUS 2014
    return df

modelTable=modelDf(cleanDf)
# print(modelTable)

def doorDf(df):
    df = df.iloc[:, [14]]
    df = df.drop_duplicates(subset=['Doors'], keep='first')
    df.rename(columns={'Doors': 'door_number'},inplace = True)
    return df

doorTable=doorDf(cleanDf)

def gearboxDf(df):
    df = df.iloc[:, [12]]
    df = df.drop_duplicates(subset=['Gear box type'], keep='first')
    df.rename(columns={'Gear box type': 'gearbox_type'},inplace = True)
    return df

gearboxTable=gearboxDf(cleanDf)

def drivewheelsDf(df):
    df = df.iloc[:, [13]]
    df = df.drop_duplicates(subset=['Drive wheels'], keep='first')
    df.rename(columns={'Drive wheels': 'drivewheels_type'},inplace = True)
    return df

drivewheelsTable=drivewheelsDf(cleanDf)

def fuelDf(df):
    df = df.iloc[:, [8]]
    df = df.drop_duplicates(subset=['Fuel type'], keep='first')
    df.rename(columns={'Fuel type': 'fuel_type'},inplace = True)
    return df
    
fuelTable=fuelDf(cleanDf)

def cylindersDf(df):
    df = df.iloc[:, [11]]
    df = df.drop_duplicates(subset=['Cylinders'], keep='first')
    df.rename(columns={'Cylinders': 'cylenders_number'},inplace = True)
    return df    

cylindersTable=cylindersDf(cleanDf)

def categoryDf(df):
    df = df.iloc[:, [6]]
    df = df.drop_duplicates(subset=['Category'], keep='first')
    df.rename(columns={'Category': 'category_libele'},inplace = True)
    return df        

categoryTable=categoryDf(cleanDf)

def carDf(df):
    df = df.drop_duplicates(subset=['ID'], keep='first')
    df.rename(columns={'ID': 'car_id','Price':'car_price','Levy':'car_levy','Prod. year':'car_year','Leather interior':'car_leather','Engine volume':'car_engine_volume','Mileage':'car_mileage','Airbags':'car_airbags','Turbo':'car_turbo','Cylinders':'cylenders_number','Drive wheels':'drivewheels_type','Doors':'door_number','Gear box type':'gearbox_type','Model':'model_libele','Fuel type':'fuel_type','Category':'category_libele'},inplace = True)
    df.drop(['Manufacturer','Wheel','Color'], inplace=True, axis=1)
    return df

carTable=carDf(cleanDf)
    

#### import vers BDD

manufacturerTable.to_sql('manufacturer',engine, if_exists='append',index= False)

modelTable.to_sql('model',engine, if_exists='append',index= False)

doorTable.to_sql('door',engine, if_exists='append',index= False)

gearboxTable.to_sql('gearbox',engine, if_exists='append',index= False)

drivewheelsTable.to_sql('drivewheels',engine, if_exists='append',index= False)

fuelTable.to_sql('fuel',engine, if_exists='append',index= False)

cylindersTable.to_sql('cylinders',engine, if_exists='append',index= False)

categoryTable.to_sql('category',engine, if_exists='append',index= False)

carTable.to_sql('car',engine, if_exists='append',index= False)













