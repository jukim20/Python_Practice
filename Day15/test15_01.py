# 문제 1  다이아 12345678910111213
# 문제 1  하트 12345678910111213
# 문제 1  클로버 12345678910111213
# 문제 1  스페이드 12345678910111213
# 문제 2) 섞는거
# 문제 3) 플레이어 2명 두장씩 나눠가저서 두장을 더한값이 높은사람이 승리
card_shape = ["◆", "♠", "♥", "♣"]
card_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
deck = []
for i in range(40):
    temp = []  # 임시로 한장씩 만든다음 deck 에 추가
    # if i % 4 == 0:
    #     temp.append(card_shape[0])
    # elif i % 4 == 1:
    #     temp.append(card_shape[1])
    # elif i % 4 == 2:
    #     temp.append(card_shape[2])
    # elif i % 4 == 3:
    #     temp.append(card_shape[3])
    temp.append(card_shape[i % 4])
    temp.append(card_num[i // 4])  # 나누기 종류 ==> / (나누기) ,  // (몫)  ,  % (나머지)
    deck.append(temp)

for i in range(40):
    print(deck[i], end=" ")
    if i % 4 == 3:
        print()
print("====================================")
import random
for i in range(100):
    rand = random.randint(0, 39)
    temp = deck[rand]
    deck[rand] = deck[0]
    deck[0] = temp

# deck.sort()  # 섞은 걸 다시 원상태로 복귀

for i in range(40):
    print(deck[i], end=" ")
    if i % 10 == 9:
        print()
p1 = deck[0][1] + deck[1][1]
p2 = deck[2][1] + deck[3][1]
print(deck[0][1], ",", deck[1][1])
print(deck[2][1], ",", deck[3][1])
index = 0
for i in range(10):
    p1 = deck[index][1] + deck[index+1][1]
    p2 = deck[index+2][1] + deck[index+3][1]
    index += 4
