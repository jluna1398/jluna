from collections import defaultdict, Counter

users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

## Creates a dictionary with id and empty araay for each user

frienship = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    frienship[i].append(j)
    frienship[j].append(i)

print(frienship)


def number_of_friedns(user):
    user_id = user["id"]
    friends_ids = frienship[user_id]
    return len(friends_ids)


total_connections = sum(number_of_friedns(user) for user in users)

# total average of connections
num_users = len(users)
avg_connections = total_connections / num_users

print(avg_connections)

# Creates a list of (user_id, number of friends)
num_friends_by_id = [(user["id"], number_of_friedns(user)) for user in users]

# sort the dic from largest to smallest base on number of friends
num_friends_by_id.sort(
    key=lambda id_and_friends: id_and_friends[1],
    reverse=True)


def foaf_ids_bad(user):
    """foaf is short for "friend of a friend" """
    return [foaf_id
            for friend_id in frienship[user["id"]]
            for foaf_id in frienship[friend_id]]


print(foaf_ids_bad(users[0]))

# Strings
name = "Jose"
last_name = "Luna"
full_name = f"{name} {last_name}"
print(full_name)

# Reverse Indexing
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
five_to_three = x[5:2 - 1]

# Dictionaries
# Check for an existing key inside a dictionary:
grades = {"Joel": 80, "Tim": 95}
print("Joel" in grades)

# Dictioanires return defaul value if not found
joels_grade = grades.get("Joel", 0)

# when to use set instead of dictionaries
# the In function is super fast on set operations
# also its easy to find distinct values in the collection
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list)
item_set = set(item_list)

# While loop
x = 0
while x < 10:
    print(f"{x} is less than 10")
    x += 1

lista = []
for x in range(5):
    if x % 2 == 0:
        lista.append(x)
print(lista)

# a better way to write this is
even_numbers = [x for x in range(5) if x % 2 == 0]
print(even_numbers)

# turning list to dictionaries
dico = {}
for x in range(5):
    dico[x] = x
print(dico)
# A better way to do this is
square_dict = {x: x for x in range(5)}
print(square_dict)


#####   Classes   #####
class CountingClicker:
    def __init__(self, count=0):
        self.count = count

    def __repr__(self):
        return f"CounterClicker(count={self.count})"

    def click(self, num_times=1):
        self.count += num_times

    def read(self):
        return self.count

    def reset(self):
        self.count = 0


clicker = CountingClicker()
assert clicker.read() == 0, "clicker should start with count 0"
clicker.click()
clicker.click()
assert clicker.read() == 2, "after two clicks, clicker should have count 2"
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"

# Iterators
#
# data = natural_numbers()
# evens = (x for x in data if x % 2 == 0)
# even_squares = (x ** 2 for x in evens)
# even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
import random

# Creates random numbers array with the _ alternatives

four_uniform_randoms = [random.random() for _ in range(4)]

from typing import List


def total(xs: List[float]) -> float:
    return sum(total)

# optional variables annotations

from typing import Optional
values: List[int] = []
# This allows the varable to be float or none

best_so_far: Optional[float] = None

from typing import Dict, Iterable, Tuple
counts: Dict[str, int] = {"data":1, "science":2}

triple: Tuple[int, float, int] = (10, 2.3, 5)



