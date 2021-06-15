import gym
import gym_chrome_dino
from gym_chrome_dino.utils.wrappers import make_dino
env = gym.make('ChromeDino-v0')
env = make_dino(env, timer=True, frame_stack=True)
done = True
# while True:
if done:
    env.reset()
#     action = env.action_space.sample()
action = 2
print (action)
observation, reward, done, info = env.step(action)

input()