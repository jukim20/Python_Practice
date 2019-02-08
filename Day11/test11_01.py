# 문제 1)
"""
$$$$$
$$$$$
$$$$$
"""

for i in range(3):  # 세로
    for j in range(5):  # 가로
        print("$", end="")
    print()

"""
#
##
###
####
"""
# 3, 33, 333, 3333

for i in range(4):
    for j in range(i+1):
        print("#", end="")
    print()

"""
   &
  &&
 &&&
&&&&
"""
#   &,   &&,  &&&, &&&&

for i in range(4):
    for j in range(i+1):
        print("&", end="")
    print()