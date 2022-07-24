import time
from threading import Timer


def test():
    for _ in range(5):
        print('?')
        time.sleep(2)

# Timer(5, test).start()
