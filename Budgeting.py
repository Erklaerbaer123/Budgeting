
# Budgeting, 03.06.2019, Michael Moeck

# It should be a tool which imports CSV files and
# makes graphs and other stuff to have an continious
# overview over my finances. 

# ”Bring the whole tithe into the storehouse,
# that there may be food in my house. Test me in this,
# ’says the LORD Almighty, “and see if I will
#  not throw open the floodgates of heaven and pour
#  out so much blessing that you will not have
#  room enough for it.’” - 2.Malachi 3,10



# TODO:
# - MAKE CHART WHAT SHOULD BE DONE BY THE TOOL
# - Build a table where every transaction is sorted by the date and month
# - Table with all in and out comings per month
# - class for month in and outcome or first year and then month

import csv
import numpy

import dash
import dash_core_components as dcc
import dash_html_components as html

import plotly.graph_objs as go
from plotly.subplots import make_subplots



class Month:
    def __init__(self, name):
        self.name = name 
        self.incomes = []
        self.outgoings = []
        self.totalOut = 0
        self.totalIn = 0
        self.totalDiff = 0 

class Year:
    def __init__(self, name):
        self.name = name
        self.incomes = []
        self.outgoings = []
        self.totalOut = 0
        self.totalIn = 0
        self.totalDiff = 0     
        self.months = []
        self.months.append(Month('01')) 
        self.months.append(Month('02'))
        self.months.append(Month('03'))
        self.months.append(Month('04'))
        self.months.append(Month('05'))
        self.months.append(Month('06'))
        self.months.append(Month('07'))
        self.months.append(Month('08'))
        self.months.append(Month('09'))
        self.months.append(Month('10'))
        self.months.append(Month('11'))
        self.months.append(Month('12'))


    






# File include
umsatz1 = 'Budgeting\\umsatz_0818_0919.csv'

# Read CSV
with open(umsatz1) as umsatz:
    csv_umsatz1 = csv.reader(umsatz, delimiter=';' )
    data = []
    for row in csv_umsatz1:
        data.append(row)

numberOfYears = 5
yearNameDate = 17 
years = []

for i in range(numberOfYears):
    years.append(Year(yearNameDate)) 
    yearNameDate = yearNameDate + 1


## Preparing data

# Edit negative Values
for row in data[1:]:
    row[14] = row[14].replace("," , ".")
    if row[14][:1] == "-":
        row[14] = row[14].replace("-" , "")
        row[14] = float(row[14])
        row[14] = row[14] * (-1)
    else:
        row[14] = float(row[14])

# Seperate data per year
for row in data[1:]:
    for i in range(numberOfYears):
        if row[1][6:] == str(years[i].name):
            if row[14] > 0:
                years[i].incomes.append(row)
                years[i].totalIn = years[i].totalIn + row[14]
            else:
                years[i].outgoings.append(row)
                years[i].totalOut = years[i].totalOut + row[14]

# Seperate data per Month
for i in range(numberOfYears):
    for row in years[i].incomes:
        for monthIt in range(len(years[i].months)):
            if row[1][3:5] == str(years[i].months[monthIt].name):
                years[i].months[monthIt].incomes.append(row)
                years[i].months[monthIt].totalIn = years[i].months[monthIt].totalIn + row[14]
        
for i in range(numberOfYears):
    for row in years[i].outgoings:
        for monthIt in range(len(years[i].months)):
            if row[1][3:5] == str(years[i].months[monthIt].name):
                years[i].months[monthIt].outgoings.append(row)
                years[i].months[monthIt].totalOut = years[i].months[monthIt].totalOut + row[14]

# Calc TotalDifferene

for i in range(numberOfYears):
    years[i].totalDiff = years[i].totalIn + years[i].totalOut 
    for j in range(len(years[i].months)):
        years[i].months[j].totalDiff = years[i].months[j].totalIn + years[i].months[j].totalOut
        

# Data Clustering




# Pie Chart

labels = ['TotalIn','TotalOut']
values = [years[1].totalIn, -years[1].totalOut]

labels1 = ['TotalIn','TotalOut']
values1 = [years[2].totalIn, -years[2].totalOut]

fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
fig.add_trace(go.Pie(labels=labels, values=values, name='2018', hole=.3))
fig.add_trace(go.Pie(labels=labels1, values=values1, name='2019', hole=.3))



app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure= fig, id='figure')  
])

if __name__ == '__main__':
    app.run_server(debug=True)