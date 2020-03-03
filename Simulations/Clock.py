"""
In this is a simple simulation of a clock in different
environments.
"""

from simpy import Environment


# This is a type of function to deploy envs in the module simpy


def clock(env, name, tick):
    while True:
        print(name, env.now)
        yield env.timeout(tick)


# Execution the process in the evironment determined for simpy

if __name__ == '__main__':
    env = Environment()
    # In this lines we determine the process:
    env.process(clock(env, 'fast', 0.5))
    env.process(clock(env, 'slow', 2))
    # Finally we run them in a lapse: The number of pulses:
    env.run(until=10)
