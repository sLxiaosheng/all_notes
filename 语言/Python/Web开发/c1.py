
import pickle

list1 = [1,2,3,4]
f1 = file('Hello.txt',wb)

pickle.dump(list1,True)

print(pickle.load(list1))
