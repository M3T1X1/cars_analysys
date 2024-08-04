import string
import random

vin = ''.join(random.choice('WERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(17))
print('VIN: ',vin)