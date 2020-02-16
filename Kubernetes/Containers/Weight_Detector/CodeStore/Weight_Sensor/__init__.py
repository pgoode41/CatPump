import serial
import time

#port level = ~750 ml
#empty res level = 1000ml





def Percentage(full_connected, empty_connected):
    delta = full_connected - empty_connected
    percent_100 = delta
    percent_90 = delta * 0.90
    percent_80 = delta * 0.80
    percent_70 = delta * 0.70
    percent_60 = delta * 0.60
    percent_50 = delta * 0.50
    percent_40 = delta * 0.40
    percent_30 = delta * 0.30
    percent_20 = delta * 0.20
    percent_10 = delta * 0.10
    percent_0 = delta * 0.05

    percentage_Data = [
        percent_100,
        percent_90,
        percent_80,
        percent_70,
        percent_60,
        percent_50,
        percent_40,
        percent_30,
        percent_20,
        percent_10,
        percent_0
    ]
    #print(percentage_Data)
    return percentage_Data

def Weight_Test_Loop():
    empty_disconnected = 0.76
    #empty_connected = 1.12
    empty_connected = 0.74
    full_connected = 3.0
    ser = serial.Serial('/dev/ttyACM0', 9600)
    count = 0
    while count < 10: 
        if(ser.in_waiting >0):
            line = ser.readline()
            weight_in_kilos = float(str(line).replace('''\\r\\n''', "").replace("b'", "").replace("'", ""))
            fluid_weight_in_kilos = weight_in_kilos - empty_connected
            PercentageList = Percentage(full_connected, empty_connected)
            #closest_num = min(PercentageList, key=lambda x=float(fluid_weight_in_kilos))
            closest_num_idx = min(range(len(PercentageList)), key=lambda i: abs(float(PercentageList[i]) - float(fluid_weight_in_kilos)))



            if closest_num_idx == 0:
                percentage = 100.00
            elif closest_num_idx == 1:
                percentage = 90.00
            elif closest_num_idx == 2:
                percentage = 80.00
            elif closest_num_idx == 3:
                percentage = 70.00
            elif closest_num_idx == 4:
                percentage = 60.00
            elif closest_num_idx == 5:
                percentage = 50.00
            elif closest_num_idx == 6:
                percentage = 40.00
            elif closest_num_idx == 7:
                percentage = 30.00
            elif closest_num_idx == 8:
                percentage = 20.00
            elif closest_num_idx == 9:
                percentage = 10.00      
            elif closest_num_idx == 10:
                percentage = 0.00  
            weightData = {
                "fluid_weight_in_kilos": fluid_weight_in_kilos,
                "total_weight_in_kilos": weight_in_kilos,
                "fluid_percentage_full": percentage,
                "fluid_percentage_full_message": "Reservoir is "+str(percentage)+ "% full."

            }
            print(weightData)
            count+=1
            return weightData


def Weight_Test_Single():
    empty_disconnected = 0.76
    #empty_connected = 1.12
    empty_connected = 0.74
    full_connected = 3.0
    ser = serial.Serial('/dev/ttyACM0', 9600)
    while 1: 
        if(ser.in_waiting >0):
            line = ser.readline()
            weight_in_kilos = float(str(line).replace('''\\r\\n''', "").replace("b'", "").replace("'", ""))
            fluid_weight_in_kilos = weight_in_kilos - empty_connected
            PercentageList = Percentage(full_connected, empty_connected)
            #closest_num = min(PercentageList, key=lambda x=float(fluid_weight_in_kilos))
            closest_num_idx = min(range(len(PercentageList)), key=lambda i: abs(float(PercentageList[i]) - float(fluid_weight_in_kilos)))



            if closest_num_idx == 0:
                percentage = 100.00
            elif closest_num_idx == 1:
                percentage = 90.00
            elif closest_num_idx == 2:
                percentage = 80.00
            elif closest_num_idx == 3:
                percentage = 70.00
            elif closest_num_idx == 4:
                percentage = 60.00
            elif closest_num_idx == 5:
                percentage = 50.00
            elif closest_num_idx == 6:
                percentage = 40.00
            elif closest_num_idx == 7:
                percentage = 30.00
            elif closest_num_idx == 8:
                percentage = 20.00
            elif closest_num_idx == 9:
                percentage = 10.00      
            elif closest_num_idx == 10:
                percentage = 0.00  

            weightData = {
                "fluid_weight_in_kilos": fluid_weight_in_kilos,
                "total_weight_in_kilos": weight_in_kilos,
                "fluid_percentage_full": percentage,
                "fluid_percentage_full_message": "Reservoir is "+str(percentage)+ "% full."

            }
            print(weightData)
            return weightData
            break
            #print(str(line).replace('''\\r\\n''', "").replace("b'", "").replace("'", ""))