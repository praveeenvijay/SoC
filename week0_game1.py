import numpy as np
capital = 10


def game_A(cap):
    num = np.random.randint(0, 1001)

    if num <= 505:
        cap = cap - 1
    else:
        cap = cap+1

    return cap


def game_B(cap):

    if cap % 3 == 0:
        num_b = np.random.randint(0, 101)

        if num_b <= 90:
            cap = cap - 1
        else:
            cap = cap + 1
    else:
        num_b = np.random.randint(0, 101)

        if num_b <= 75:
            cap = cap + 1
        else:
            cap = cap-1

    return cap


for i in range(10):
    print("what game do you want to play: ")
    choice = input("")
    if choice == 'a' or choice == "A":
        capital = game_A(capital)
    elif choice == 'b' or choice == "B":
        capital = game_B(capital)
    else:
        print("choice is invalid")
        i = i-1
    print(f"your current captial is {capital}")
