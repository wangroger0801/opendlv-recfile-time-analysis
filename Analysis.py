import csv
import sys
import os
import numpy as np

#####
# Function defs for Jitter and latency analysis
# sample of usage shown in python notebooks 
# Naichen Wang @CFSD19
# Jan 2019
#####


def showFolderContent(data_folder_path):
    print(data_folder_path)
    for root, dirs, files in os.walk(data_folder_path):
        for name in files:
            data_path = os.path.join(data_folder_path,name)
            with open(data_path) as csvfile:
                reader = csv.DictReader(csvfile,delimiter=";")
                print("reading file: ", name)
                for row in reader: 
                    print(list(row.keys()))
                    break
                print("")

def data_summary(data_raw_list):
    for data_dic in (data_raw_list):
        print(data_dic['name'])
        for i in range(0,1):
            print(i,data_dic['time'][i])

def read_data(data_folder_path):
    print("reading from: ",data_folder_path)
    data_raw_list = list()
    for root, dirs, files in os.walk(data_folder_path):
        for name in files:
            data_path = os.path.join(data_folder_path,name)
            with open(data_path) as csvfile:
                reader = csv.DictReader(csvfile,delimiter=";",)
                time_dict_list = list()
                for row in reader:
                    time_dict_list.append(dict((k,int(row[k])) for k in list(row.keys())[0:6]))
                data_raw_list.append({"name" : name , "time" : time_dict_list})
                print("readed " , name , "total rows: ", len(time_dict_list))
    return data_raw_list


def Latecy_analysis(data_list):
    data_sub = np.zeros(len(data_list))
    for i in range(len(data_list)):
        end   = data_list[i]['received.seconds'] + data_list[i]['received.microseconds']/1000000
        start = data_list[i]['sent.seconds'] + data_list[i]['sent.microseconds']/1000000
        data_sub[i] = end-start

    latency_avg = np.average(data_sub)
    latency_max = np.max(data_sub)
    latency_min = np.min(data_sub)
    latency_std = np.std(data_sub)
    return (latency_avg,latency_max,latency_min,latency_std,data_sub)


def Jitter_analysis(data_list):
    data_sub = np.zeros(len(data_list)-1)
    for i in range(len(data_list)-1):
        end   = data_list[i+1]['sampleTimeStamp.seconds'] + data_list[i+1]['sampleTimeStamp.microseconds']/1000000
        start = data_list[i]['sampleTimeStamp.seconds'] + data_list[i]['sampleTimeStamp.microseconds']/1000000
        data_sub[i] = end-start
    jitter_avg = np.average(data_sub)
    jitter_max = np.max(data_sub)
    jitter_min = np.min(data_sub)
    jitter_std = np.std(data_sub)
    return (jitter_avg,jitter_max,jitter_min,jitter_std,data_sub)
