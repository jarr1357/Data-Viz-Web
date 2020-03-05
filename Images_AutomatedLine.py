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

TotalHours = 23    #Used to determine how many charts will be created. 1 per hour

#Date format: YYYY-MM-DD
CurrentDay = str(date.today())

#This is a simple algorithm that caclculates the row number from today's date
Row = ((int(CurrentDay[8:])-1)*24)

#This will be used to reference a row in the .csv. Hours are all sequential so hours can be used to designate for the whole month
StartHour = Row 
EndHour = StartHour + TotalHours
Hour = Row

HydroPower = []

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

MonthNumber = (int(CurrentDay[5:7])-1)

#Selects the appropriate file to import based on current month number
SensorData = pd.read_csv('%s' %CSVNames[MonthNumber])

for i in range(TotalHours+1):    
  
  CurrentHour = SensorData.iloc[Hour,1]
  TotalPowerInput = (float(SensorData.loc[Hour,C_Name[19]]) + float(SensorData.loc[Hour,C_Name[20]]))
  TotalPowerOutput = (float(SensorData.loc[Hour,C_Name[0]]) + float(SensorData.loc[Hour,C_Name[1]]) + float(SensorData.loc[Hour,C_Name[2]]) + 
                      float(SensorData.loc[Hour,C_Name[3]]) + float(SensorData.loc[Hour,C_Name[4]]) + float(SensorData.loc[Hour,C_Name[5]]) +
                      float(SensorData.loc[Hour,C_Name[6]]) + float(SensorData.loc[Hour,C_Name[7]]) + float(SensorData.loc[Hour,C_Name[8]]) +
                      float(SensorData.loc[Hour,C_Name[9]]) + float(SensorData.loc[Hour,C_Name[10]]) + float(SensorData.loc[Hour,C_Name[11]]) +
                      float(SensorData.loc[Hour,C_Name[12]]) + float(SensorData.loc[Hour,C_Name[13]]) + float(SensorData.loc[Hour,C_Name[14]]) +
                      float(SensorData.loc[Hour,C_Name[15]]) + float(SensorData.loc[Hour,C_Name[16]]) + float(SensorData.loc[Hour,C_Name[17]]) +
                      float(SensorData.loc[Hour,C_Name[18]]))
  
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

  HydroPower.append(PowerDifference)
  Hour += 1




for j in range(TotalHours+1): 
    
  #This list is referenced later to set the colours used in the chart. uses CSS colours
  colors = []

  #Set up the first figure

  fig = go.Figure()
  fig.add_trace(go.Scatter(x=SensorData.loc[StartHour:EndHour,"TIME"],
                         y=HydroPower,
                         name='Hydro Power',
                         line=dict(color='seagreen', width=4)))

  fig.add_trace(go.Scatter(x=SensorData.loc[StartHour:EndHour,"TIME"], 
                         y=SensorData.loc[StartHour:EndHour,C_Name[19]],
                         name='CoGen 1',
                         line=dict(color='turquoise', width=4)))

  fig.add_trace(go.Scatter(x=SensorData.loc[StartHour:EndHour,"TIME"], 
                         y=SensorData.loc[StartHour:EndHour,C_Name[20]],
                         name='CoGen 2',
                         line=dict(color='teal', width=4)))
  fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0=j,
            y0=0,
            x1=j,
            y1=TotalPower,
            line=dict(
                color="Red",
                width=3
            )))
  #The (title_x = 0.5) argument allows for orientation of the title. This can be any number from 0-1.
  fig.update_layout(font_size=12,
                  showlegend=True)
    
    

            
  #Outputs the chart to the image files.
  FileName = ("StackedLineFig%d.svg" %j)
  fig.write_image(FileName)