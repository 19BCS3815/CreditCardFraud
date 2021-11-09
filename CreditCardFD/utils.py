import pandas as pd
import json
import pickle

def dataview1(name):
    df=pd.read_csv(name)
    df1=df.head(101)
    json_records = df1.reset_index().to_json(orient ='records')
    data = []
    data = json.loads(json_records)
    return data


def pred(name):
    df=pd.read_csv(name)
    datawithcol=df
    X = df
    # Getting the values of X and Y (Numpy array with no columns)
    xTest = X.values
    Modelname = 'C:/Users/hp/Documents/GitHub/CreditCardFraud/CreditCardFD/model.pkl'
    #Load the Model back from file
    with open(Modelname, 'rb') as file:
        rfc = pickle.load(file)
    #Predict the value of 'Class' using the reloaded Model
        yPred = rfc.predict(xTest)

    datawithcol.insert(1, "Predicted_Class", yPred, True)
    print(datawithcol.head(10))
    return datawithcol

def analysis(name):
     dfa=pred(name)  
     print(dfa)
     dshape=dfa.shape
     uniqueId = dfa["Predicted_Class"].unique() 
     totalrec=dfa["Predicted_Class"].count()
     fraud= dfa["Predicted_Class"].sum()
     fraudper = (fraud/totalrec) *100
     nonf= 100 - fraudper
     nonfcount= totalrec - fraud
     data=[dshape,uniqueId,totalrec,fraud,fraudper,nonf,nonfcount]
     return data