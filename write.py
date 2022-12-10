import os
import test
from test import main

c = 0
for filename in os.listdir("C:/Users/rafae/Downloads/Notas julho/"):
     c += 1
     main("C:/Users/rafae/Downloads/Notas julho/"+filename)
#     if c ==20:
#          break
