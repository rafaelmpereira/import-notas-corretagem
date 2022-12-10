import os
import extractEasynvest
from extractEasynvest import main

c = 0
for filename in os.listdir("C:/Users/rafae/Desktop/python/Nova Pasta/Easy/"):
     c += 1
     main("C:/Users/rafae/Desktop/python/Nova Pasta/Easy/"+filename)
#     if c ==20:
#          break
