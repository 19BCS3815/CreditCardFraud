from django.shortcuts import redirect, render, HttpResponse
#from creditcardfd.models import Contact
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import uploadForm
from .models import upload1
import pandas as pd
import json
import pickle
import matplotlib.pyplot as plt
import numpy as np


# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
#     # return HttpResponse("this is aboutpage")
def signin(request):
      if request.method == "POST":
          user=request.POST["username"]
          pass1=request.POST["pass1"]
          user = authenticate(username=user, password=pass1)
        
          if user is not None:
              login(request, user)
              messages.success(request, "Logged In Sucessfully!!")
              return redirect('home1')
          else:
              messages.error(request, "Bad Credentials!!")
              return redirect('home')
    

      return render(request, 'signin.html')
#     # return HttpResponse("this is service page")
def home1(request):
    if request.method == 'POST':
        form = uploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = uploadForm()
    return render(request, 'index1.html', {
        'form': form
    })
def dashboard(request):
    uploads=upload1.objects.all()
    return render(request,'dasboard.html',{'uploads':uploads})
def deleteupload(request,pk):
    if request.method == "POST":
        upload =upload1.objects.get(pk=pk)
        upload.delete()
    return redirect('dashboard')


def dataview(request,pk):
    if request.method == "POST":
        upload =upload1.objects.get(pk=pk)
        name=upload.uploadfile
        print(name)
        global df
        df= pd.read_csv(name)
        df1=df.head(101)
        data1=df1.to_html()
        context = {'d': data1,'upload':upload}

                # Load the dataset from the csv file using pandas
        
        global data
        data=df
        global datawithcol
        datawithcol=df
        # Splitting the data into Independent (X) and Dependent (Y) data sets
       
        pred()
        analysis()
        
    return render(request, 'dataview.html', context,)


    
def pred():
       
        # Splitting the data into Independent (X) and Dependent (Y) data sets
        X = data

        # Getting the values of X and Y (Numpy array with no columns)
        xTest = X.values
    
       
        Modelname = "D:/CreditCardFraud/CreditCardFD/model.pkl"
                
        #Load the Model back from file
        with open(Modelname, 'rb') as file:
            rfc = pickle.load(file)

        #Predict the value of 'Class' using the reloaded Model
        yPred = rfc.predict(xTest)

        datawithcol.insert(1, "Predicted Class", yPred, True)
        print(yPred)
        print(datawithcol.head(10))
        



def analysis():

     dfa=datawithcol   
     dshape=dfa.shape
     uniqueId = dfa["Predicted Class"].unique() 
     totalrec=dfa["Predicted Class"].count()
     fraud= dfa["Predicted Class"].sum()
     fraudper = (fraud/totalrec) *100
     nonf= 100 - fraudper
     nonfcount= totalrec - fraud
     print(dshape)
     print(uniqueId)
     print(totalrec)
     print(fraud)
     print(fraudper)
     print(nonf )
     print(nonfcount)



     y = np.array([fraud, nonfcount])
     mylabels = ["Fraudulent Cases", "Non-Fraudulent Cases"]
     myexplode = [0.2, 0]

     plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
     
    


def easyCproject(request):
    return render(request,'easyCproject.html')
def intmCproject(request):
    return render(request,'intmCproject.html')
def advCproject(request):
    return render(request,'advCproject.html')
def easyJproject(request):
    return render(request,'easyJproject.html')
def intmJproject(request):
    return render(request,'intmJproject.html')
def advJproject(request):
    return render(request,'advJproject.html')
def contact(request):
   # if request.method == "POST":
       # name = request.POST['name']
       # email = request.POST['email']
       # phone = request.POST['phone']
        #desc = request.POST['desc']
        #C1 = Contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
       # C1.save()
       # messages.success(request, 'Profile Successfuly Saved')
    return render(request,'contact.html')

