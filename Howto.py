import numpy as np
import random


Persons = np.array(["Max", "Chef", "Mia", "Tomas", "Bram", "Thomas", "HJ"])
Money_owed = np.array([45.08,22.69,-27.39,-0.26,3.61,-34.67,-9.06])


if round(np.sum(Money_owed),2) != 0:
	print("Sum of the total is not 0")
	exit()


Money = np.copy(Money_owed)


count = 0

while (np.count_nonzero(Money) != 0) and (count < 20):
	Index_max = int(random.choice(np.where(Money == np.amax(Money))[0]))
	Index_min = int(random.choice(np.where(Money == np.amin(Money))[0]))

	#print(Money)

	if Money[Index_max] >= abs(Money[Index_min]):
		Money[Index_max] = Money[Index_max] + Money[Index_min]
		print(Persons[Index_max] + " gets " + str(round(Money[Index_min], 2)) + " from " + Persons[Index_min])
		Money[Index_min] = 0

	elif Money[Index_max] < abs(Money[Index_min]):
		Money[Index_min] = Money[Index_min] + Money[Index_max]
		print(Persons[Index_max] + " gets " + str(round(Money[Index_max], 2)) + " from " + Persons[Index_min])
		Money[Index_max] = 0
	
	Money = np.around(Money, decimals=2)

	count = count + 1
	
print('done')




