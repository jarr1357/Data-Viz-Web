# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:19:47 2020

@author: Mike
"""

from datetime import date
import time
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = "browser"

TotalHours = 24    #Used to determine how many charts will be created. 1 per hour

#Date format: YYYY-MM-DD
CurrentDay = str(date.today())

#This is a simple algorithm that caclculates the row number from today's date
Row = ((int(CurrentDay[8:])-1)*24)
Hour = Row

#Names of csv for data import are hardcoded.
CSVNames = ['ACData_Jan2019.csv','ACData_Feb2019.csv','ACData_Mar2019.csv', 
           'ACData_Apr2019.csv', 'ACData_May2019.csv', 'ACData_Jun2019.csv',
           'ACData_Jul2019.csv', 'ACData_Aug2019.csv', 'ACData_Sep2019.csv',
           'ACData_Oct2019.csv', 'ACData_Nov2019.csv', 'ACData_Dec2019.csv']
#ColumnNames
C_Name = ['BLD A (KW)', 'BLD A FITNESS ZONE (KW)', 'BLD B (KW)', 'BLD C (kW)',
          'BLD D (KW)', 'BLD E (KW)', 'BLD G (KW)', 'BLD H (KW)', 'BLD J (KW)',
          'BLD K (KW)', 'BLD M (KW)', 'BLD N (KW)', 'BLD P (KW)', 'BLD S (KW)',
          'BLD T (KW)', 'BLD V (KW)', 'BLD Z (KW)', 'RES PH 1 & 2 (KW)', 'RES PH 3 (KW)',
          'COGEN 1 (kW)', 'COGEN2 (kW)']

DataNames = []

MonthNumber = (int(CurrentDay[5:7])-1)

#Selects the appropriate file to import based on current month number
SensorData = pd.read_csv('%s' %CSVNames[MonthNumber])

#This for loop will generate a number of charts based on the given days
for i in range(TotalHours):    
  
  CurrentHour = SensorData.iloc[Hour,1]
  TotalPowerInput = (float(SensorData.loc[Hour,C_Name[19]]) + float(SensorData.loc[Hour,C_Name[20]]))
  TotalPowerOutput = (float(SensorData.loc[Hour,C_Name[0]]) + float(SensorData.loc[Hour,C_Name[1]]) + float(SensorData.loc[Hour,C_Name[2]]) + 
                      float(SensorData.loc[Hour,C_Name[3]]) + float(SensorData.loc[Hour,C_Name[4]]) + float(SensorData.loc[Hour,C_Name[5]]) +
                      float(SensorData.loc[Hour,C_Name[6]]) + float(SensorData.loc[Hour,C_Name[7]]) + float(SensorData.loc[Hour,C_Name[8]]) +
                      float(SensorData.loc[Hour,C_Name[9]]) + float(SensorData.loc[Hour,C_Name[10]]) + float(SensorData.loc[Hour,C_Name[11]]) +
                      float(SensorData.loc[Hour,C_Name[12]]) + float(SensorData.loc[Hour,C_Name[13]]) + float(SensorData.loc[Hour,C_Name[14]]) +
                      float(SensorData.loc[Hour,C_Name[15]]) + float(SensorData.loc[Hour,C_Name[16]]) + float(SensorData.loc[Hour,C_Name[17]]) +
                      float(SensorData.loc[Hour,C_Name[18]]))
  
#######  Debugging print statements  ############################################################
  
  #print("Chart #%d:" %(i+1))
  #print(CurrentHour)
  #print(TotalPowerInput)  
  #print(TotalPowerOutput)
  #print(PowerDifference)

  #print("A: %f" %float(SensorData.loc[Hour,C_Name[0]]))
  #print("A fit: %f" %float(SensorData.loc[Hour,C_Name[1]]))
  #print("B: %f" %float(SensorData.loc[Hour,C_Name[2]]))
  #print("C: %f" %float(SensorData.loc[Hour,C_Name[3]]))
  #print("D: %f" %float(SensorData.loc[Hour,C_Name[4]]))
  #print("E: %f" %float(SensorData.loc[Hour,C_Name[5]]))
  #print("G: %f" %float(SensorData.loc[Hour,C_Name[6]]))
  #print("H: %f" %float(SensorData.loc[Hour,C_Name[7]]))
  #print("J: %f" %float(SensorData.loc[Hour,C_Name[8]]))
  #print("K: %f" %float(SensorData.loc[Hour,C_Name[9]]))
  #print("M: %f" %float(SensorData.loc[Hour,C_Name[10]]))
  #print("N: %f" %float(SensorData.loc[Hour,C_Name[11]]))
  #print("P: %f" %float(SensorData.loc[Hour,C_Name[12]]))
  #print("S: %f" %float(SensorData.loc[Hour,C_Name[13]]))
  #print("T: %f" %float(SensorData.loc[Hour,C_Name[14]]))
  #print("V: %f" %float(SensorData.loc[Hour,C_Name[15]]))
  #print("Z: %f" %float(SensorData.loc[Hour,C_Name[16]]))
  #print("RES 1&2: %f" %float(SensorData.loc[Hour,C_Name[17]]))
  #print("RES 3: %f" %float(SensorData.loc[Hour,C_Name[18]]))
  #print("CG1: %f" %float(SensorData.loc[Hour,C_Name[19]]))
  #print("CG2: %f" %float(SensorData.loc[Hour,C_Name[20]]))
  
########## End of debigging print statements  ####################################################

  #This set of if statements accounts for the higher power usage of the two total power variables
  if TotalPowerOutput > TotalPowerInput:
    PowerDifference = TotalPowerOutput - TotalPowerInput
    TotalPower = TotalPowerOutput
    
  elif TotalPowerOutput < TotalPowerInput:
    PowerDifference = TotalPowerInput - TotalPowerOutput
    TotalPower = TotalPowerInput
    
  else:
    PowerDifference = TotalPowerInput - TotalPowerOutput
    TotalPower = TotalPowerInput



  fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      
      #label adds information to each node (data point) on the sankey diagram.
      label = ["Hydro Power (%.2fKW )" %float(PowerDifference), "COGEN 1 (%.2fKW)" %float(SensorData.loc[Hour,C_Name[19]]), 
               "COGEN 2 (%.2fKW)" %float(SensorData.loc[Hour,C_Name[20]]), "Solar 1 (KW)", "Solar 2 (KW)", 
               "Total Power (%.2fKW)" %float(TotalPower), "Building A (%.2fKW)" %float(SensorData.loc[Hour,C_Name[0]]), 
               "Building B (%.2fKW)" %float(SensorData.loc[Hour,C_Name[2]]), "Building C (%.2fKW)" %float(SensorData.loc[Hour,C_Name[3]]), 
               "Building D (%.2fKW)" %float(SensorData.loc[Hour,C_Name[4]]), "Building E (%.2fKW)" %float(SensorData.loc[Hour,C_Name[5]]), 
               "Building G (%.2fKW)" %float(SensorData.loc[Hour,C_Name[6]]), "Building H (%.2fKW)" %float(SensorData.loc[Hour,C_Name[7]]), 
               "Building J (%.2fKW)" %float(SensorData.loc[Hour,C_Name[8]]), "Building K (%.2fKW)" %float(SensorData.loc[Hour,C_Name[9]]), 
               "Building M (%.2fKW)" %float(SensorData.loc[Hour,C_Name[10]]), "Building N (%.2fKW)" %float(SensorData.loc[Hour,C_Name[11]]), 
               "Building P (%.2fKW)" %float(SensorData.loc[Hour,C_Name[12]]), "Building S (%.2fKW)" %float(SensorData.loc[Hour,C_Name[13]]), 
               "Building T (%.2fKW)" %float(SensorData.loc[Hour,C_Name[14]]), "Building V (%.2fKW)" %float(SensorData.loc[Hour,C_Name[15]]), 
               "Building Z (%.2fKW)" %float(SensorData.loc[Hour,C_Name[16]]), "Residence 1&2 (%.2fKW)" %float(SensorData.loc[Hour,C_Name[17]]), 
               "Residence 3 (%.2fKW)" %float(SensorData.loc[Hour,C_Name[18]])],
      
      #Used to select colours for the charts
      color = ["Seagreen", "Turquoise", "Teal", "Green", "Green", "Yellow", "Red", "Red", "Red", "Red", "Red", "Red", "Red", 
               "Red", "Red", "Red", "Red", "Red", "Red", "Red", "Red", "Red", "Red", "Red"]
    ),
    #This dictionary is used to specify the constraints of the sankey diagram
    link = dict(
      #source is used specifiy where each trace begins. Starts at 0
      source = [0, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,],
      #each of the values in the target list pairs to the corrosponding value in the start list to create the trace
      target = [5, 5, 5, 5, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,],
      #value assigns a number to each of the traces in the sankey diagram
      value = [PowerDifference, SensorData.loc[Hour,C_Name[19]], SensorData.loc[Hour,C_Name[20]],  0, 0, 
               (SensorData.loc[Hour,C_Name[0]] + SensorData.loc[Hour,C_Name[1]]), SensorData.loc[Hour,C_Name[2]], 
               SensorData.loc[Hour,C_Name[3]], SensorData.loc[Hour,C_Name[4]], SensorData.loc[Hour,C_Name[5]],
               SensorData.loc[Hour,C_Name[6]], SensorData.loc[Hour,C_Name[7]], SensorData.loc[Hour,C_Name[8]],
               SensorData.loc[Hour,C_Name[9]], SensorData.loc[Hour,C_Name[10]], SensorData.loc[Hour,C_Name[11]],
               SensorData.loc[Hour,C_Name[12]], SensorData.loc[Hour,C_Name[13]], SensorData.loc[Hour,C_Name[14]],
               SensorData.loc[Hour,C_Name[15]], SensorData.loc[Hour,C_Name[16]], SensorData.loc[Hour,C_Name[17]]]
  ))])

  #This block of code updates the title, font size and title offset of the chart.
  fig.update_layout(font_size=9)
  
  #Outputs the chart to the image files.
  FileName = ("SankeyFig%d.svg" %(i))
  fig.write_image(FileName)

  Hour += 1 #(Increments the hour)
  
  #time.sleep(0.5) #Adds a 500 millisecond delay to the for loop

