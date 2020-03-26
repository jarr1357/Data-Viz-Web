# Data-Viz-Web

All webpage commenting in SankeyWeb/index.html. Each webpage index.html is identical aside from refrencing 
different charts.

This set of programs is run on an ubuntu EC2 AWS machine. 

Cronjobs execute the programs at 12:15am to produce new graphs.
Website includes javascript that forces a reboot at 1am
  -keeps websites synchronized
  -updates graphics to include the newly generated images

Requires python and various dependancies.
Orca is difficult to install. If it is installed and cronjob isn't running, $cp your 
orca install to default folder listed in error.
