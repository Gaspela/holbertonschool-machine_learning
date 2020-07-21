#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

applebar = plt.bar(range(3), fruit[0, :], 0.5, color='red')
bananabar = plt.bar(range(3), fruit[1, :],
                    0.5, color='yellow', bottom=fruit[0, :])
orangebar = plt.bar(range(3), fruit[2, :], 0.5, color='#ff8000',
                    bottom=fruit[0, :] + fruit[1, :])
peachbar = plt.bar(range(3), fruit[3, :], 0.5, color='#ffe5b4',
                   bottom=fruit[0, :] + fruit[1, :] + fruit[2, :])


plt.xticks(range(3), ('Farrah', 'Fred', 'Felicia'))
plt.yticks(np.arange(0, 81, 10))
plt.ylabel("Quantity of Fruit")
plt.title("Number of Fruit per Person")
plt.legend((applebar[0], bananabar[0], orangebar[0], peachbar[0]),
           ('Apples', 'Bananas', 'Oranges', 'Peaches'))

plt.show()
