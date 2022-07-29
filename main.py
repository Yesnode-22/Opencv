# pip install matplotlib

import matplotlib.pyplot as plt
partition = 'Python', 'Javascript', 'C++', 'C', 'PHP', 'HTML & CSS'
sizes = [350, 250, 150, 10,50, 150]
fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=partition, autopct='%1.1f%%', shadow=True)
ax1.axis('equal')
plt.show()