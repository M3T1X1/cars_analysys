import random
from openpyxl import load_workbook

id = ''.join(random.choice('QWERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(11))
file = 'Cars.xlsx'
data = [[id]]

wb = load_workbook(file)
ws = wb["Sellers"]

for seller_id in data:
    ws.append(seller_id)

wb.save(file)
