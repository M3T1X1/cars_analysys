import random
from openpyxl import load_workbook

id = ''.join(random.choice('QWERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(11))
file = 'Cars.xlsx'
data = [[id]]
wb = load_workbook(file)
ws = wb["Customers"] #Just change the name from 'Sellers' to 'Customers' to insert values to proper worksheet
for customer_id in data: # as above
    ws.append(customer_id)
    wb.save(file)
