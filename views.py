from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from pathlib import Path
import os
#importing all libraries i used in this project
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='sklearn')
file_path = os.path.join(settings.BASE_DIR, 'static', 'data_with_diseases.csv')
data=pd.read_csv(file_path)
data.drop(["Marraige Status (Yrs)","Fast food (Y/N)","Unnamed: 41","Sl. No","Patient File No."],axis=1,inplace=True)
for col in data.select_dtypes(include='int64'):
    data[col]=data[col].astype(float)
data["AMH(ng/mL)"] = pd.to_numeric(data["AMH(ng/mL)"], errors='coerce')
data.fillna({'AMH(ng/mL)' : data['AMH(ng/mL)'].median()} , inplace = True)
data['PCOS (Y/N)']=data['PCOS (Y/N)'].astype('int64')
y=data["PCOS (Y/N)"]
x=data.drop(["PCOS (Y/N)"],axis=1)
import sklearn
scaler=StandardScaler()
xscaler=scaler.fit_transform(x)
x_train,x_test,y_train,y_test=train_test_split(x ,y,test_size=0.30,random_state=42)
lr=LogisticRegression()
lr.fit(x_train,y_train)
acclogtrain=round(lr.score(x_train,y_train)*100,2)
acclogtest=round(lr.score(x_test,y_test)*100,2)
ypv=lr.predict(x_test)
# Create your views here.
def start(request):
    return render(request, 'start.html');
def home(request):
     return render(request,'home.html');
def add(request):
    val1=float(request.GET['age'])
    val2=float(request.GET['weight'])
    val3=float(request.GET['height'])
    val4=float(request.GET['bmi'])
    val5=float(request.GET['bloodgroup'])
    val6=float(request.GET['pulserate'])
    val7=float(request.GET['rr'])
    val8=float(request.GET['hb'])
    val9=float(request.GET['cycle'])
    val10=float(request.GET['cyclelength'])
    val11=float(request.GET['pregnancy'])
    val12=float(request.GET['noofabortions'])
    val13=float(request.GET['betahcg1'])
    val14=float(request.GET['betahcg2'])
    val15=float(request.GET['hip'])
    val16=float(request.GET['waist'])
    val17=float(request.GET['waisthip'])
    val18=float(request.GET['tsh'])
    val19=float(request.GET['amh'])
    val20=float(request.GET['prl'])
    val21=float(request.GET['vit'])
    val22=float(request.GET['prg'])
    val23=float(request.GET['rbs'])
    val24=float(request.GET['weightgain'])
    val25=float(request.GET['hairgrowth'])
    val26=float(request.GET['skindarkening'])
    val27=float(request.GET['hairloss'])
    val28=float(request.GET['pimples'])
    val29=float(request.GET['regularexercise'])
    val30=float(request.GET['bpsystolic'])
    val31=float(request.GET['bpdiastolic'])
    val32=float(request.GET['folliclel'])
    val33=float(request.GET['follicler'])
    val34=float(request.GET['avgfsizel'])
    val35=float(request.GET['avgfsizer'])
    val36=float(request.GET['endometrium'])
    val37=float(request.GET['diabetes'])
    val38=float(request.GET['hyperextension'])
    val39=float(request.GET['infertility'])
    val40=float(request.GET['stresslevels'])
    res=(val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,
          val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,
          val21,val22,val23,val24,val25,val26,val27,val28,val29,val30,
          val31,val32,val33,val34,val35,val36,val37,val38,val39,val40)
    new=[[val1,val2,val3,val4,val5,val6,val7,val8,val9,val10,
          val11,val12,val13,val14,val15,val16,val17,val18,val19,val20,
          val21,val22,val23,val24,val25,val26,val27,val28,val29,val30,
          val31,val32,val33,val34,val35,val36,val37,val38,val39,val40]]
    pred=lr.predict(new)
    if pred==[1]:
        Value="Yes The Person is Having PCOS"
    elif pred==[0]:
        Value="No The Person Doesn't Have PCOS"
    else:
        Value="None"
    if val11==0.0:
        val11a="No"
    elif val11==1.0:
        val11a="Yes"
    else:
        val11a="None"
    if val5==11.0:
        val5a="A+"
    elif val5==12.0:
        val5a="A-"
    elif val5==13.0:
        val5a="B+"
    elif val5==14.0:
        val5a="B-"
    elif val5==15.0:
        val5a="O+"
    elif val5==16.0:
        val5a="O-"
    elif val5==17.0:
        val5a="AB+"
    elif val5==18.0:
        val5a="AB-"
    else:
        val5a="None"
    if val24==0.0:
        val24a="No"
    elif val24==1.0:
        val24a="Yes"
    else:
        val24a="None"
    if val25==0.0:
        val25a="No"
    elif val25==1.0:
        val25a="Yes"
    else:
        val25a="None"
    if val26==0.0:
        val26a="No"
    elif val26==1.0:
        val26a="Yes"
    else:
        val26a="None"
    if val27==0.0:
        val27a="No"
    elif val27==1.0:
        val27a="Yes"
    else:
        val27a="None"
    if val28==0.0:
        val28a="No"
    elif val28==1.0:
        val28a="Yes"
    else:
        val28a="None"
    if val29==0.0:
        val29a="No"
    elif val29==1.0:
        val29a="Yes"
    else:
        val29a="None"
    if val37==0.0:
        val37a="No"
    elif val37==1.0:
        val37a="Yes"
    else:
        val37a="None"
    if val38==0.0:
        val38a="No"
    elif val38==1.0:
        val38a="Yes"
    else:
        val38a="None"
    if val39==0.0:
        val39a="No"
    elif val39==1.0:
        val39a="Yes"
    else:
        val39a="None"
    return render(request,'result.html',{'resultpred':Value,
                                         'age':val1,'weight':val2,'height':val3,'bmi':val4,'bloodgroup':val5a,
                                         'pulserate':val6,'rr':val7,'hb':val8,'cycle':val9,'cyclelength':val10,
                                         'pregnancy':val11a,'noofabortions':val12,'betahcg1':val13,'betahcg2':val14,'hip':val15,
                                         'waist':val16,'waisthip':val17,'tsh':val18,'amh':val19,'prl':val20,
                                         'vit':val21,'prg':val22,'rbs':val23,'weightgain':val24a,'hairgrowth':val25a,
                                         'skindarkening':val26a,'hairloss':val27a,'pimples':val28a,'regularexcercise':val29a,'bpsystolic':val30,
                                         'bpdiastolic':val31,'folliclel':val32,'follicler':val33,'avgfsizel':val34,'avgfsizer':val35,
                                         'endometrium':val36,'diabetes':val37a,'hyperextension':val38a,'infertility':val39a,'stresslevels':val40,
                                         'result':res});