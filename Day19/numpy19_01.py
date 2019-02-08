import numpy as np  # as ==> numpy 를 앞으로 np 로 부르겠다 (다섯글자가 너무 기니 두글자로 줄임)

"""
list()
dict()

보다 상위호환
"""

data1 = [6, 7, 8, 9, 10]  # 리스트를 만들어서 넘파이 배열에 집어넣음
arr1 = np.array(data1)  # 넘파이 배열에 집어넣음
print(arr1)  # [ 6  7  8  9 10]
print(arr1.shape)

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(data2)
arr2 = np.array(data2)
print(arr2)  # 보기 편하게 두줄로 뽑아준다

print(np.arange(15))
print(arr1.dtype)  # 중요!  # int32 ==> 0이 32개 ==> +- 20억까지 밖에 못 씀
arr3 = np.array([1, 2, 3, 4, 5], dtype=np.int64)  # 데이터 저장 크기; 2배가 아니라 어마어마한 숫자; 0이 64개
print(arr3)

float_arr1 = arr3.astype(np.float64)  # 정수뿐이 아닌 실수로도 표현 가능
print(float_arr1)
print(float_arr1.dtype)  # 데이터 타입 확인

arr4 = np.array(([1, 3, 4], [2, 4, 6]))
print(arr4)

arr5 = np.array(([11, 33, 55], [44, 66, 22]))
print(arr5)