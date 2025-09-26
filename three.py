from enum import Enum


class State(Enum):
    INACTIVE = 0  # State.INACTIVE = 0
    ACTIVE = 1  # State.ACTIVE = 1


print(State.ACTIVE)  # State.ACTIVE
print(State.ACTIVE.value) # 1
print(State.INACTIVE.value) # 0
print(State(1))  # Will return State.ACTIVE
print(State['ACTIVE']) # Will return State.ACTIVE

print(list(State)) # [<State.INACTIVE: 0>, <State.ACTIVE: 1>]

# This is the only way to Create to constant(a value that can never be changed or reassigned)  in python
