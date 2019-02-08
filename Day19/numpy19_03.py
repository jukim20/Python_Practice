import numpy as np
names = np.array(["철수", "명수", "길동", "명자", "철수"])
print(names)

data = np.random.rand(5, 3)
print(data)
print()
print(names == "철수")  # [ True False False False  True]
print(data[names == "철수", :])

print(data[(names == "명수") | (names == "명자"), :])

