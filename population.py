import random
from joshua import target
from joshua import random_casualties

# British Cities
if target == "London":
    random_casualties = (random.randint(10, 130) / 10)
elif target == "Birmingham":
    random_casualties = (random.randint(10, 36) / 10)
elif target == "Manchester":
    random_casualties = (random.randint(10, 25) / 10)
elif target == "Leeds":
    random_casualties = (random.randint(10, 23) / 10)
elif target == "Liverpool":
    random_casualties = (random.randint(10, 22) / 10)