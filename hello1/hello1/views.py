from django.shortcuts import  render,HttpResponse
from . import test_model
from . import ML_Model
def index(request):
    return render(request,'index.html')
def Result(request):
    pclass=int(request.GET['pclass'])
    sex= int(request.GET['sex'])
    age = int(request.GET['age'])
    sibsp = int(request.GET['sibsp'])
    parch = int(request.GET['parch'])
    fare = int(request.GET['fare'])
    ebarked= int(request.GET['ebarked'])
    title= int(request.GET['title'])

    prediction= ML_Model.predict_Model(pclass,sex,age,sibsp,parch,fare,ebarked,title)
    return render(request,'Result.html',{'result':prediction})