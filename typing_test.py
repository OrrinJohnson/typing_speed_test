import random
from clock import Clock


random_words = ['hello', 'australia', 'hippo', 'walkabout']
clock = Clock(10)


def get_random_word():
    return random.choice(random_words)


def main():
    clock.countdown()


if __name__ == "__main__":
    main()
