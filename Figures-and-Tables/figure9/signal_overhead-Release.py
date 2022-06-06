import numpy as np 
import math
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy.io as scio
import sys

## single_upbound:The maximum number of users allowed to access a single satellite
##modify gs_type, label, constellation

path="/media/files/workplaces/cym/midata/Seafile/星座数据/"#"/Users/liulixin/Desktop/Tsinghua/Seafile/网元功能划分与路由/data/星座数据/"#" 


R=6371
lat=110.95
long=111.314

constellation=sys.argv[1]
cycle=100
single_upbound=int(sys.argv[2])

gs_type = "opt_handover/distributed"#new_sp #opt_handover
label = "distributed"  # distributed,single
name_s=['a','b','c','d']

# total_ue=7568902783
# ratio=10000/total_ue


policy="P_OPT"  

if constellation=="starlink":
    sat_diameter=1874.2664448706144
    node_num=1584
    orbit_num=72
    sat_per_orbit=22
    generatrix=1123.27700157791
    inclination=53.0
    path+="starlink_72_22/oneweek_interval60/"
elif constellation=="kuiper":
    sat_diameter=2480.5271244802866
    node_num=1156
    orbit_num=34
    sat_per_orbit=34
    generatrix=1450.37612078939
    inclination=51.9
    path+="kuiper/"
elif constellation=="oneweb":
    sat_diameter=3362.458672391004  # 3362.458672391004 1362.9519523964689
    node_num=720
    orbit_num=18
    sat_per_orbit=40
    generatrix=2204.43292594425 # 2204.43292594425 1411.90309481454
    inclination=87.9
    path+="OneWeb-1week/"
elif constellation=="iridium":
    sat_diameter=4079.1391091351293  
    node_num=66
    orbit_num=6
    sat_per_orbit=11
    generatrix=2324.58930012188 
    inclination=86.4
    path+="Iridium_1week/"

ue_access_file=path+constellation+"_ue_access_"+policy+".npy"
ue_access=np.array(np.load(ue_access_file,allow_pickle=True))
print(type(ue_access[0][0]))
print(np.shape(ue_access))

gs_access_file=path+constellation+"_fac_access_"+policy+".npy"
gs_access=np.array(np.load(gs_access_file,allow_pickle=True))
print(type(gs_access[0][0]))
print(np.shape(gs_access))

old_end_sp=np.array(np.load(path+gs_type+"_"+"old-end"+"_SP_delay_hop.npy",allow_pickle=True))  # ground的access sat
print(np.shape(old_end_sp))
old_new_sp=np.array(np.load(path+gs_type+"_"+"old-new"+"_SP_delay_hop.npy",allow_pickle=True))  # ground的access sat
print(np.shape(old_new_sp))
new_end_sp=np.array(np.load(path+gs_type+"_"+"new-end"+"_SP_delay_hop.npy",allow_pickle=True))  # ground的access sat
print(np.shape(new_end_sp))
print(new_end_sp[0][0])

def cal_selected_ue():
    cal_sue=[]
    for c in range(cycle):
        tmp=[0]*node_num
        for i in range(len(ue_access)):
                tmp[int(ue_access[i][c])-1]+=1
        cal_sue.append(tmp)
    return cal_sue
sue=cal_selected_ue()
print(np.shape(sue))
print(max(sue[0]))

'''
    Calculate the percentage of deflation per user
    ratio: [cycle,node_num]
'''
def ratio():
    result=[]
    l=[]
    for c in range(cycle):
        tmp=[]
        for s in range(node_num):
            if sue[c][s] < single_upbound:
                if sue[c][s] != 0 :
                    r = single_upbound // sue[c][s]
                    left = single_upbound - sue[c][s] * r
                    tmp.append(r)
                    l.append(left)
                else:
                    tmp.append(1)
            else:
                tmp.append(1)
        result.append(tmp)
    return result,l
                    
rat,left=ratio()
print(np.shape(rat))

def cal_handover():
    r=[]
    for t in range(1,cycle):
        r_in=[]
        for i in range( len(ue_access)):
            if ue_access[i][t-1] != ue_access[i][t]:
                r_in.append(i)
        r.append(r_in)
    return r
ho=cal_handover()
print(np.shape(ho))
print(ho[0])

def cal_frequency():
    count=[]
    for c in range(len(old_new_sp[0])):
        co=0
        for i in range(len(old_new_sp)):
            if old_new_sp[i][c][3] > 1:
                co+=1
        count.append(co)
    return count
hopp=cal_frequency()
ue_count=len(old_new_sp)
print(np.mean(hopp)/ue_count,max(hopp)/ue_count,min(hopp)/ue_count)
# 3386.0 6576 53

def read_pos(label,cal_location_file):
    if cal_location_file[-3:] == "csv":
        df=pd.read_csv(cal_location_file,header=None,sep='\t')
        if label:
            df.drop(labels=None,axis=0, index=0, columns=None, inplace=True)
        cal_pos=df[0].str.split(',').values.tolist()    
    elif cal_location_file[-3:] == "npy":
        cal_pos=np.load(cal_location_file,allow_pickle=True).tolist()

    print(np.shape(cal_pos))
    return cal_pos

node_type="ue"  # fac,ue
ue_location_file="../data/ue_pos.csv"  #13_root_server.csv
ue_pos=read_pos(False,ue_location_file)
ue_length=len(ue_pos)
print(ue_pos[0])

gs_location_file="../data/oneweb.csv"  #13_root_server.csv
gs_pos=read_pos(False,gs_location_file)
gs_length=len(gs_pos)
print(gs_pos[0])

dataFile = path + "position.mat" 
data = scio.loadmat(dataFile)
pos_all=data['position']
pos_cbf=data['position_cbf'] 
print(np.shape(pos_cbf))

def to_cbf(lat_long,length):
    cbf=[]
    radius=6371
    for num in range(0,length):
        cbf_in=[]
        z=radius*math.sin(math.radians(float(lat_long[num][0])))
        x=radius*math.cos(math.radians(float(lat_long[num][0])))*math.cos(math.radians(float(lat_long[num][1])))
        y=radius*math.cos(math.radians(float(lat_long[num][0])))*math.sin(math.radians(float(lat_long[num][1])))
        cbf_in.append(x)
        cbf_in.append(y)
        cbf_in.append(z)
        cbf.append(cbf_in)
    return cbf
ue_cbf=to_cbf(ue_pos,ue_length)
print(np.shape(ue_cbf))
gs_cbf=to_cbf(gs_pos,gs_length)
print(np.shape(gs_cbf))

def cal_pairs(flag):
    print(flag)
    p=[]
    if flag == "single":
        gs_index=3
        for i in range(len(ue_access)):
            tmp=[]
            for t in range(cycle):
                tmp.append([int(ue_access[i][t]),int(gs_access[gs_index][t])])
            p.append(tmp)
    elif flag == "distributed":
        mapping=np.array(np.load("../data/pairs.npy",allow_pickle=True))
        for i in range(len(ue_access)):
            tmp=[]
            for t in range(cycle):
                tmp.append([int(ue_access[i][t]),int(gs_access[mapping[i]][t])]) 
            p.append(tmp)
            
    return p
pairs=cal_pairs(label)
print(np.shape(pairs))

def cal_gsl():
    print(label)
    v=300
    r=[]
    for t in range(cycle):
        r_in=[]
        for i in range(len(ue_cbf)):
            x1=ue_cbf[i][0]
            y1=ue_cbf[i][1]
            z1=ue_cbf[i][2]
            x2=pos_cbf[pairs[i][t][0]-1][0][0][t]/1000
            y2=pos_cbf[pairs[i][t][0]-1][0][1][t]/1000
            z2=pos_cbf[pairs[i][t][0]-1][0][2][t]/1000
            dist1=np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
            delay1=dist1/v
            if label == "single":
                gs_index=3
                x3=gs_cbf[gs_index][0]
                y3=gs_cbf[gs_index][1]
                z3=gs_cbf[gs_index][2]
            elif label == "distributed":
                mapping=np.array(np.load("../data/pairs.npy",allow_pickle=True))
                x3=gs_cbf[mapping[i]][0]
                y3=gs_cbf[mapping[i]][1]
                z3=gs_cbf[mapping[i]][2]
            x4=pos_cbf[pairs[i][t][1]-1][0][0][t]/1000
            y4=pos_cbf[pairs[i][t][1]-1][0][1][t]/1000
            z4=pos_cbf[pairs[i][t][1]-1][0][2][t]/1000
            dist2=np.sqrt((x3-x4)**2+(y3-y4)**2+(z3-z4)**2)
            delay2=dist2/v
            r_in.append([delay1,delay2])
        r.append(r_in)
        print(t)
    return r
gsl_delay=cal_gsl()
print(np.shape(gsl_delay),gsl_delay[0][0])

## Modify s_index and r_flag to get RTT for different procedure

'''
     In the 4 scenarios, the 4 processes correspond to the RTT of each user
    [cycle,10000,4]
'''
tau_rtt={'UE-RAN':1, 'RAN-new AMF':1, 'new AMF-old AMF':2, 'new AMF-UDM':5, 'old AMF-UDM':1, 'UE-new AMF':2}
ho_rtt={'UE-old gNB':2, 'old gNB-new gNB':3, 'UE-new gNB':1, 'new gNB-AMF':1}
reallocation_rtt={'new gNB-AMF':2, 'AMF-source I-SMF':4, 'source I-SMF-SMF':2, 'AMF-target I-SMF':2, 'target I-SMF-source I-SMF':2, 'target I-SMF-target I-UPF':2, 'target I-SMF-SMF':2, 'SMF-UPF':2, 'source I-SMF-source I-UPF':2, 'old gNB-new gNB':1}
pdu_rtt={'UE-RAN':1, 'UE-AMF':1, 'AMF-SMF':6, 'UPF-SMF':4, 'AMF-RAN':2}

rtt=[{'ho':{'UE-RAN':2,'RAN-core':[2,1],'RAN-RAN':4},'tau':{'UE-RAN':0,'RAN-core':[0,0],'RAN-RAN':0},'re':{'UE-RAN':0,'RAN-core':[0,0],'RAN-RAN':0},'pdu':{'UE-RAN':2,'RAN-core':[3,0],'RAN-RAN':0}},
     {'ho':{'UE-RAN':2,'RAN-core':[4,2],'RAN-RAN':6},'tau':{'UE-RAN':0,'RAN-core':[0,0],'RAN-RAN':0},'re':{'UE-RAN':0,'RAN-core':[0,0],'RAN-RAN':0},'pdu':{'UE-RAN':2,'RAN-core':[8,0],'RAN-RAN':0}},
     {'ho':{'UE-RAN':5,'RAN-core':[5,1],'RAN-RAN':10},'tau':{'UE-RAN':0,'RAN-core':[0,0],'RAN-RAN':0},'re':{'UE-RAN':0,'RAN-core':[0,0],'RAN-RAN':0},'pdu':{'UE-RAN':2,'RAN-core':[0,0],'RAN-RAN':0}},
     {'ho':{'UE-RAN':5,'RAN-core':[0,0],'RAN-RAN':10},'tau':{'UE-RAN':0,'RAN-core':[0,0],'RAN-RAN':0},'re':{'UE-RAN':0,'RAN-core':[0,0],'RAN-RAN':0},'pdu':{'UE-RAN':2,'RAN-core':[0,0],'RAN-RAN':0}}]
# not includes pdu

def cal_rtt(ho,s_index,flag):
    tau_flag,re_flag=False,False
    if s_index == 1:
        re_flag=True
    elif s_index == 2 or s_index == 3:
        re_flag=True
        tau_flag=True
    
    r=[]
    for t in range(len(old_end_sp[0])):
        if flag == "pdu": # [cycle,10000,1]
            real_t=t+1
            # if t%2 == 0:
            r_in=[]
            for ue in range(len(ue_access)):
                tmp=rtt[s_index]['pdu']['UE-RAN']*gsl_delay[real_t][ue][0] + rtt[s_index]['pdu']['RAN-RAN']*old_new_sp[ue][t][2] + rtt[s_index]['pdu']['RAN-core'][0]*(new_end_sp[ue][t][2]+gsl_delay[real_t][ue][1]) + rtt[s_index]['pdu']['RAN-core'][1]*(old_end_sp[ue][t][2]+gsl_delay[real_t][ue][1])
                r_in.append(tmp)
                
        else: # [cycle,,3]
            real_t=t+1
            r_in=[]
            for ue in ho[t]:
                tmp=[0]*3  # handover,re,tau
                tmp[0]=rtt[s_index]['ho']['UE-RAN']*gsl_delay[real_t][ue][0] + rtt[s_index]['ho']['RAN-RAN']*old_new_sp[ue][t][2] + rtt[s_index]['ho']['RAN-core'][0]*(new_end_sp[ue][t][2]+gsl_delay[real_t][ue][1]) + rtt[s_index]['ho']['RAN-core'][1]*(old_end_sp[ue][t][2]+gsl_delay[real_t][ue][1])
                if re_flag:
                    tmp[1]=tmp[0] + rtt[s_index]['re']['UE-RAN']*gsl_delay[real_t][ue][0] + rtt[s_index]['re']['RAN-RAN']*old_new_sp[ue][t][2] + rtt[s_index]['re']['RAN-core'][0]*(new_end_sp[ue][t][2]+gsl_delay[real_t][ue][1]) + rtt[s_index]['re']['RAN-core'][1]*(old_end_sp[ue][t][2]+gsl_delay[real_t][ue][1])
                if tau_flag:
                    tmp[2]=rtt[s_index]['tau']['UE-RAN']*gsl_delay[real_t][ue][0] + rtt[s_index]['tau']['RAN-RAN']*old_new_sp[ue][t][2] + rtt[s_index]['tau']['RAN-core'][0]*(new_end_sp[ue][t][2]+gsl_delay[real_t][ue][1]) + rtt[s_index]['tau']['RAN-core'][1]*(old_end_sp[ue][t][2]+gsl_delay[real_t][ue][1])
                r_in.append(tmp)
            
        r.append(r_in)
    return r

for s_index in range(len(name_s)):
    for r_flag in ["pdu","other"]:
        rtt_result=cal_rtt(ho,s_index,r_flag)
        print(np.shape(rtt_result))
        name_s=['a','b','c','d']
        np.save(path+"opt_handover/rtt/"+label+"_scenario_"+name_s[s_index]+"_"+r_flag+"_rtt.npy",rtt_result)



## inter_satellite：calculate state migration of per satellite

SMF_UPF_allocation={'gNB-gNB':[326.5,19], 'gNB-AMF':[83,20], 'AMF- source I-SMF':[41.5,15],'source I-SMF-SMF':[33,15], 'AMF-target I-SMF':[99.5,18], 'source I-SMF-target I-SMF':[47,24], 'SMF-target I-SMF':[83.5,18], 'SMF-UPF':[107,8], 'target I-SMF-target I-UPF':[232,13]}
UPF_allocation={'gNB-gNB':[37,7], 'gNB-AMF':[68,9], 'source I-SMF-SMF': [32,8], 'SMF-UPF':[65,3], 'SMF-target I-UPF':[205,13]}
basic_ho={'gNB-gNB':[326.5,19], 'gNB-AMF': [199,20], 'AMF-SMF':[33,13], 'SMF-UPF': [107,8]}
tau={'UE-RAN': [109.5,19], 'RAN-new AMF':[111,12], 'new AMF-old AMF':[219.9,61], 'new AMF-PCF': [7.5+46.5,3+7]}
pdu={'UE-RAN':[111.4,26], 'RAN-AMF':[205.4,40], 'AMF-SMF':[300.4,58], 'SMF-UPF':[290,15]}

pdu_state={'RAN-core':[[[3,40],[8,90],[0,0],[0,0]],[[0,0],[0,0],[0,0],[0,0]]], 'RAN-RAN':[[0,0],[0,0],[0,0],[0,0]]}
state_num={'RAN-core':[[[2,17],[4,39],[5,7],[0,0]],[[1,0],[2,2],[1,1],[0,0]]], 'RAN-RAN':[[4,23],[6,40],[10,111],[10,111]]}
# 'RAN-core': the first part is new to end,the second part is old to end
'''
    oh:[cycle,node_num]
'''
def cal_overhead(ho,s_index):
    oh=[]
    oh_session=[]
    for t in range(len(ho)): 
        real_t=t
        d=[[0,0] for _ in range(node_num)] # bytes, number
        d2=[[0,0] for _ in range(node_num)]
        for ue in ho[t]:
            for sat in new_end_sp[ue][real_t][-1]:
                sat=sat.replace('\'','')
                d[int(sat)-1][0] += state_num['RAN-core'][0][s_index][0]*rat[t][int(old_end_sp[ue][t][0])-1]
                d[int(sat)-1][1] += state_num['RAN-core'][0][s_index][1]*rat[t][int(old_end_sp[ue][t][0])-1]
            for sat in old_end_sp[ue][real_t][-1]:
                sat=sat.replace('\'','')
                d[int(sat)-1][0] += state_num['RAN-core'][1][s_index][0]*rat[t][int(old_end_sp[ue][t][0])-1]
                d[int(sat)-1][1] += state_num['RAN-core'][1][s_index][1]*rat[t][int(old_end_sp[ue][t][0])-1]
            for sat in old_new_sp[ue][real_t][-1]:
                sat=sat.replace('\'','')
                d[int(sat)-1][0] += state_num['RAN-RAN'][s_index][0]*rat[t][int(old_end_sp[ue][t][0])-1]
                d[int(sat)-1][1] += state_num['RAN-RAN'][s_index][1]*rat[t][int(old_end_sp[ue][t][0])-1]
        if t%2 ==0:
            for ue in range(len(ue_access)): # all ue
                for sat in new_end_sp[ue][real_t][-1]:
                    sat=sat.replace('\'','')
                    d2[int(sat)-1][0] += pdu_state['RAN-core'][0][s_index][0]*rat[t][int(old_end_sp[ue][t][0])-1]
                    d2[int(sat)-1][1] += pdu_state['RAN-core'][0][s_index][1]*rat[t][int(old_end_sp[ue][t][0])-1]
                for sat in old_end_sp[ue][real_t][-1]:
                    sat=sat.replace('\'','')
                    d2[int(sat)-1][0] += pdu_state['RAN-core'][1][s_index][0]*rat[t][int(old_end_sp[ue][t][0])-1]
                    d2[int(sat)-1][1] += pdu_state['RAN-core'][1][s_index][1]*rat[t][int(old_end_sp[ue][t][0])-1]
                for sat in old_new_sp[ue][real_t][-1]:
                    sat=sat.replace('\'','')
                    d2[int(sat)-1][0] += pdu_state['RAN-RAN'][s_index][0]*rat[t][int(old_end_sp[ue][t][0])-1]
                    d2[int(sat)-1][1] += pdu_state['RAN-RAN'][s_index][1]*rat[t][int(old_end_sp[ue][t][0])-1]
        oh.append(d)
        oh_session.append(d2)
        #print(t)
    oh=np.array(oh)
    oh_session=np.array(oh_session)
    return oh,oh_session
                
for s_index in [0,1,2,3]:
    overhead_mobility,overhead_pdu=cal_overhead(ho,s_index)
#     print(np.shape(overhead))
    name_s=['a','b','c','d']
    np.save(path+"opt_handover/satellite/"+label+"scenario_"+name_s[s_index]+"_"+str(single_upbound)+"_mobility.npy",overhead_mobility)
    np.save(path+"opt_handover/satellite/"+label+"scenario_"+name_s[s_index]+"_"+str(single_upbound)+"_session.npy",overhead_pdu)
