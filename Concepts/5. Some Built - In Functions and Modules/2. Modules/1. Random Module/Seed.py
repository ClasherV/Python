import random

def with_seed():
    random.seed(10)
    print(random.randint(0,100))

def without_seed():
    print(random.randint(0,100))

# without_seed()
with_seed()