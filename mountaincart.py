# pip install gym==0.17.3

import gym

env = gym.make("MountainCar-v0")
state = env.reset()

done = False
while not done:
    # 1 = left, 2 = right
    action = 2  # always go right!
    env.step(action)
    env.render(mode="human")
env.close()