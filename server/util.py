import json
import pickle
import numpy as np
import os
os.chdir(r'C:\Users\CHRISTY HARSHITHA\OneDrive\Desktop\ML\hhp\server')
__locations=None
__data_columns=None
__model=None

def get_estimated_price(area,bhk,resale,intercom,vaastu,ppa,location,connectivity,societies,apartment):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = 101
    tx=np.zeros(len(__data_columns))
    tx[0]=area
    tx[1]=bhk
    tx[2]=resale
    tx[3]=intercom
    tx[4]=vaastu
    tx[5]=ppa
    tx[6]=area/bhk
    tx[7]=societies
    tx[8]=connectivity
    tx[9]=apartment
    if loc_index>=0:
        tx[loc_index]=1
    
    return round(__model.predict([tx])[0],2)




def load_saved_artifacts():
    print("loading saved artifacts")
    global __data_columns
    global __locations
    

    with open('./artifacts/columns.json','r') as f:    
        __data_columns=json.load(f)['data_columns']
        
        __locations=__data_columns[10:]
        #print(__locations)
    global __model
    with open('./artifacts/hyd_pred_model.pickle','rb') as f:
        __model=pickle.load(f)
    print("loading saved artifacts is done")
def get_locations():
    return __locations


if __name__=="__main__":
    load_saved_artifacts()
    print(get_locations())
    print(get_estimated_price(1170,2,0,0,0,6949,'Boduppal',0,0,0))
    print(get_estimated_price(1170,2,0,0,0,6949,'Alugaddabhavi',0,0,0))
    print(get_estimated_price(1431,3,0,1,1,22000,'Boduppal',1,1,1))