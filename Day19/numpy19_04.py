import numpy as np
data = np.loadtxt("movielens-1m/ratings.dat", delimiter="::", dtype=np.int64)
# print(data)
print(data.shape)  # (1000209, 4)  # 세로는 백만줄, 가로는 4줄
print(data[:5, 1])  # [1193  661  914 3408 2355]

mean_rating_total = data[:, 2].mean()  # 평가 백만개의 평균
print(mean_rating_total)  # 3.581564453029317

user_ids = np.unique(data[:, 0])  # 겹치는 숫자 제거
print(user_ids)  # 사람 수  # 6040

user_list = []

for user_id in user_ids:
    data_for_user = data[data[:, 0] == user_id, :]  # 데이터의 0번이 유저아이디와 같고 그에 해당되는 점수
    mean_rating = data_for_user[:, 2].mean()
    user_list.append([user_id, mean_rating])
print(user_list)

mean_rating_by_user_array = np.array(user_list, dtype=np.float)
np.savetxt("mean_rating_by_user.csv", mean_rating_by_user_array, fmt="%.2f", delimiter=",")
