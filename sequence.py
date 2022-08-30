import random as rand
import time

names = ['Alden', 'Elan', 'Luke', 'Grantly', 'Grant', 'Grayson', 'Willow']

def sequence(names, minTime, maxTime, seed=69):
    while 1:
        dur = rand.randint(minTime, maxTime)
        print(f'\nSpeaker: {rand.choice(names)}\nDuration: {dur} seconds')
        time.sleep(2)
        
        for i in reversed(list(range(dur + 1))):
            print(f'{i} ...')
            time.sleep(1)

sequence(names, 5, 10)
