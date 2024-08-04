import string
import random

id = ''.join(random.choice('QWERTYUIOPASDFGHJKLZXCVBNM1234567890') for i in range(11))
print('ID:',id)