import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def gaussian_arm():
    value = np.random.normal(2, 1)
    return value


def fair_arm():
    x = np.random.randint(0, 2)
    if x == 0:
        return +5
    else:
        return -6


def poisson_arm():
    return np.random.poisson(2)


def exp_arm():
    return np.random.exponential(3)


def random_arm():
    x = np.random.randint(0, 4)
    if x == 0:
        return gaussian_arm()
    elif x == 1:
        return fair_arm()
    elif x == 2:
        return poisson_arm()
    elif x == 3:
        return exp_arm()
    else:
        print("there is a problem in random_arm")


# expected_value = [ exp_gaus, exp_exp, exp_poisson, exp_fair, exp_random]


def episode(epi=0):
    gaus_step = 1
    exp_step = 1
    fair_step = 1
    random_step = 1
    pois_step = 1
    reward = 0
    total_reward = 0
    for i in range(100):
        x = np.random.randint(0, 101)
        if x >= epi * 100:
            action = np.argmax(expected_value)
        else:
            action = np.random.randint(0, 5)
            while action == np.argmax(expected_value):
                action = np.random.randint(0, 5)

        if action == 0:
            reward = gaussian_arm()
            expected_value[0] = (
                expected_value[0] + (reward - expected_value[0]) / gaus_step
            )
            gaus_step = gaus_step + 1
        elif action == 1:
            reward = exp_arm()
            expected_value[1] = (
                expected_value[1] + (reward - expected_value[1]) / exp_step
            )
            exp_step = exp_step + 1

        elif action == 2:
            reward = poisson_arm()
            expected_value[2] = (
                expected_value[2] + (reward - expected_value[2]) / pois_step
            )
            pois_step = pois_step + 1

        elif action == 3:
            reward = fair_arm()
            expected_value[3] = (
                expected_value[3] + (reward - expected_value[3]) / fair_step
            )
            fair_step = fair_step + 1

        elif action == 4:
            reward = random_arm()
            expected_value[4] = (
                expected_value[4] + (reward - expected_value[4]) / random_step
            )
            random_step = random_step + 1

        else:
            print("there is a problem with action allocation")
        total_reward = total_reward + reward
    average = total_reward / 100
    return average


reward_history_epi = []
expected_value = [0, 0, 0, 0, 0]
for i in range(1000):
    reward = episode(0.1)
    reward_history_epi.append(reward)


reward_history = []
expected_value = [0, 0, 0, 0, 0]
for i in range(1000):
    reward = episode(0)
    reward_history.append(reward)


expected_value = [0, 0, 0, 0, 0]
reward_history_epsilon = []
for i in range(1000):
    reward = episode(0.1)
    reward_history_epsilon.append(reward)


fig, ax = plt.subplots()

ax.plot(np.arange(1, 1001), reward_history_epi, label="epi_01")

fig, ax = plt.subplots()

ax.plot(np.arange(1, 1001), reward_history, label="epi_0")
fig, ax = plt.subplots()
ax.plot(np.arange(1, 1001), reward_history_epsilon, label="epi_001")
ax.set_xlabel("episode")
ax.set_ylabel("reward")
ax.set_title("reward vs episode")
ax.legend()
plt.show()
