import random
from openpyxl import load_workbook

name_random = ''.join(random.choice(['ADAM','AARON','ANAKIN','ANDY','DANIEL','JACKOB','KYLE','WALTER','SKYLER','TED','JESSIE','BOB','GRACE','OLIVIA','ANGELA','VICTOR','VALERIE','VINCENT','OSWALD','SLADE']))
surname_random = ''.join(random.choice(['SMIT','JOHNSON','WILLIAMS','JONES','DAVIS','TAYLOR','MILLER','THOMAS','HARRIS','MARTINEZ','CLARK','WAYNE','COBBLEPOT','WILLSON','KOWALSKI','STARK','BJORNSON','WELLS']))
file = 'Cars.xlsx'
data_name = [[name_random]]
data_surname = [[surname_random]]
wb = load_workbook(file)
ws = wb['Sellers']

for name in data_name:
    ws.append(name)
    wb.save(file)

for surname in data_surname:
    ws.append(surname)
    wb.save(file)