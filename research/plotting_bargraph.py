import numpy as np 
import matplotlib.pyplot as plt 

objects = ('Logistic Regression', 'SGD', 'SVM', 'Random Forests', 'Keras Sequential')
y_pos = np.arange(len(objects))
performance = [88.3, 97.1, 97.6, 99.7, 94.7]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.ylim(82,100)

plt.text(1,1,str(5))
#plt.xticks(y_pos, objects)
plt.ylabel('Accuracy')
plt.show()
