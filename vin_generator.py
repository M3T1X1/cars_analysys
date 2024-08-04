import random
from openpyxl import load_workbook

vin = ''.join(random.choice('WERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(17))
file = 'Cars.xlsx'
data = [[vin]]

wb = load_workbook(file)
ws = wb.active

for vin in data:
    ws.append(vin)

wb.save(file)
