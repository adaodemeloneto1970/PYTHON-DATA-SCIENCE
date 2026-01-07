import numpy as np
import sys
import pandas as pd
import matplotlib.pyplot as plt

gas= pd.read_csv('gas_prices.csv')

#print(gas)

plt.title('Valores do combustível')
plt.xlabel('Years')
plt.ylabel('US$')
plt.plot(gas['Year'],gas['Australia'],label=['Australia'])
plt.plot(gas['Year'],gas['USA'],label='USA')
plt.plot(gas['Year'],gas['Germany'],label=['Alemanha'])
plt.plot(gas['Year'],gas['France'],label=['França'])


plt.show()


list_country=['Australia','USA','Germany']

for country in gas:
    if country in list_country:
        plt.plot(gas['Year'],gas[country])

plt.savefig('country.png')
plt.show()