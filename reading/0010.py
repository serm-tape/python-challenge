'''
CSV file is a file that represent table as a text.
Each line is a row and seperated each column with comma (,)
A function below will read any file and return as
a list of dictionary which contains data for each column

input file:
id,local_currency,local_amount,usd_amount
10,USD,30.0,30.0
11,CNY,200,15.0
12,THB,312,10.4

output:
[
    {id:10, local_currency:'USD', local_amount:30.0, usd_amount:30.0},
    {id:11, local_currency:'CNY', local_amount:200.0, usd_amount:15.0},
    {id:12, local_currency:'THB', local_amount:312.0, usd_amount:10.4},
]
'''
def readCsv(filename):
    with open(filename) as f:
        lines = f.readlines()

    table = {}
    header = lines[0].split():
    for line in lines:
        cells = line.split():
        row = {}
        for ci in range(cells):
            row[ci] = cells[ci]
        table.append(row)

    return table
