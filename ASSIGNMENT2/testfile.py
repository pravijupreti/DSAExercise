from firstExercise import IntArray

array = IntArray()
for i in range(6):
    array.append(i)
val = array.remove(3)
print(val, array)