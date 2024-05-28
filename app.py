import streamlit as st
import pickle 
import numpy as np

#import model
pipe=pickle.load(open('pipe.pkl','rb'))
laptop=pickle.load(open('laptop.pkl','rb'))



st.title("Laptop Predictor")

#brand
company = st.selectbox('Brand',laptop['Company'].unique())

#type of laptop
type = st.selectbox('Type',laptop['TypeName'].unique())

#Ram
Ram = st.selectbox('RAM(in GB)',[2,4,6,8,12,16,24,32,64])

#weight

weight = st.number_input("Weight of the Laptop")

#TouchScreen
touchscreen = st.selectbox('TouchScreen',['NO','YES'])

#IPS

ips =st.selectbox('IPS',['NO','YES'])

#screen size
screen_size = st.number_input('Screen Size')

#resolution

resolution = st.selectbox('Screen Resolution',['1920x1080','1366x768','1600x900','3840x2160','3200x1800','2880x1800','2560x1600','2560x1440','2304x1440'])

#cpu

cpu = st.selectbox('Processor',laptop['Cpu_Processor'].unique())

hdd = st.selectbox('HDD(in GB)',[0,128,256,500,1024,2048])

sdd = st.selectbox('SDD(in GB)',[0,128,256,500,1024])

gpu = st.selectbox('Gpu',laptop['Gpu_brand'].unique())

os = st.selectbox('Operating System',laptop['Os'].unique())

if st.button('Predict Price'):
    #querry point
    ppi=None
    if touchscreen =='YES':
        touchscreen=1
    else:
        touchscreen=0
    
    if ips == 'YES':
        ips = 1
    else:
        ips = 0


    X_res=int(resolution.split('x')[0])
    Y_res =int(resolution.split('x')[1])
    ppi = ((X_res**2) + (Y_res**2))**0.5/screen_size 
    querry = np.array([company,type,Ram,weight,touchscreen,ips,ppi,cpu,hdd,sdd,gpu,os])

    querry=querry.reshape(1,12)

    st.title("The predicated price is :" + str(int(np.exp(pipe.predict(querry)[0]))))