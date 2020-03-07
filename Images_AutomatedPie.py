# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 15:19:47 2020

@author: Mike
"""

from datetime import date
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
          'BLD T (KW)', 'BLD V (KW)', 'BLD Z (KW)', 'RES PH 1 & 2 (KW)', 'RES PH 3 (KW)']

DataNames = []

MonthNumber = (int(CurrentDay[5:7])-1)

#Selects the appropriate file to import based on current month number
SensorData = pd.read_csv('csv/%s' %CSVNames[MonthNumber])

#This for loop will generate a number of charts based on the given days
for i in range(TotalHours):    
  
  CurrentHour = SensorData.iloc[Hour,1]

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

  #This list is referenced later to set the colours used in the chart. uses CSS colours
  colors = ["Salmon", "LightSalmon", "Aquamarine", "Mediumaquamarine", "Lightskyblue", "Deepskyblue", "moccasin", "paleturquoise", 
            "Orange", "Darkorange", "Khaki", "Darkkhaki", "Palegreen", "Springgreen", "Lightgreen", "cornflowerblue", "Plum", "Orchid"]

  fig = go.Figure(data=[go.Pie(labels=["Building A (%.2fKW)" %float(SensorData.loc[Hour,C_Name[0]]), "Building B (%.2fKW)" %float(SensorData.loc[Hour,C_Name[2]]), 
                                       "Building C (%.2fKW)" %float(SensorData.loc[Hour,C_Name[3]]), "Building D (%.2fKW)" %float(SensorData.loc[Hour,C_Name[4]]), 
                                       "Building E (%.2fKW)" %float(SensorData.loc[Hour,C_Name[5]]), "Building G (%.2fKW)" %float(SensorData.loc[Hour,C_Name[6]]), 
                                       "Building H (%.2fKW)" %float(SensorData.loc[Hour,C_Name[7]]), "Building J (%.2fKW)" %float(SensorData.loc[Hour,C_Name[8]]), 
                                       "Building K (%.2fKW)" %float(SensorData.loc[Hour,C_Name[9]]), "Building M (%.2fKW)" %float(SensorData.loc[Hour,C_Name[10]]), 
                                       "Building N (%.2fKW)" %float(SensorData.loc[Hour,C_Name[11]]), "Building P (%.2fKW)" %float(SensorData.loc[Hour,C_Name[12]]), 
                                       "Building S (%.2fKW)" %float(SensorData.loc[Hour,C_Name[13]]), "Building T (%.2fKW)" %float(SensorData.loc[Hour,C_Name[14]]), 
                                       "Building V (%.2fKW)" %float(SensorData.loc[Hour,C_Name[15]]), "Building Z (%.2fKW)" %float(SensorData.loc[Hour,C_Name[16]]), 
                                       "Residence 1&2 (%.2fKW)" %float(SensorData.loc[Hour,C_Name[17]]), "Residence 3 (%.2fKW)" %float(SensorData.loc[Hour,C_Name[18]])
                                       ],
                                                                      
                             values=[SensorData.loc[Hour,C_Name[0]] + SensorData.loc[Hour,C_Name[1]], SensorData.loc[Hour,C_Name[2]], 
                                     SensorData.loc[Hour,C_Name[3]], SensorData.loc[Hour,C_Name[4]], SensorData.loc[Hour,C_Name[5]],
                                     SensorData.loc[Hour,C_Name[6]], SensorData.loc[Hour,C_Name[7]], SensorData.loc[Hour,C_Name[8]],
                                     SensorData.loc[Hour,C_Name[9]], SensorData.loc[Hour,C_Name[10]], SensorData.loc[Hour,C_Name[11]],
                                     SensorData.loc[Hour,C_Name[12]], SensorData.loc[Hour,C_Name[13]], SensorData.loc[Hour,C_Name[14]],
                                     SensorData.loc[Hour,C_Name[15]], SensorData.loc[Hour,C_Name[16]], SensorData.loc[Hour,C_Name[17]]
                                     ])])

  fig.update_traces(hoverinfo='label+percent', textinfo='label', textfont_size=8,
                    marker=dict(colors=colors, line=dict(color='#000000', width=0)))                                  
   
  #This block of code updates the title, font size and title offset of the chart.
  fig.update_layout(font_size=9,
                    showlegend=False)
  
  #Outputs the chart to the image files.
  FileName = ("PieWeb/charts/PieChartFig%d.svg" %(i))
  fig.write_image(FileName)

  Hour += 1 #(Increments the hour)
  print ("chart %s" %i)
  
  
  #time.sleep(0.5) #Adds a 500 millisecond delay to the for loop

