from random import randint, sample
from oop import Player, Vector2D
from solid import Car


def is_impaired(number):
    return number % 2 != 0

numbers = [ 1, 3, 4, 5, 6, 7, 8, 9, 1 ,2 ,3]
impaired_numbers = filter(is_impaired, numbers)
impaired_numbers = list(impaired_numbers)
multi_numbers = []
one_to_undred = []
random_tab = []
random_sample = []

print(sum(numbers))
print(impaired_numbers)

for number in numbers:
    multi_numbers.append(number*2)

print(multi_numbers)

for i in range(1, 101):
    one_to_undred.append(i)

print(one_to_undred)

for i in range(1, 101):
    random_tab.append(randint(0, 100))

print(random_tab)

random_sample = sample(range(100), 10)
print(random_sample)

#les Sets

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}


print(a)
a.add(8)
a.remove(2)
print(a)
print(3 in a)

print(a.symmetric_difference(b))

numbers_b = [1, 3, 4, 5, 6, 7, 8, 9, 1 ,2 ,3]
numbers_b_set = set()

for number in numbers_b:
    if number not in numbers_b_set:
        numbers_b_set.add(number)

print(numbers_b_set)

#Les dicos

prices = {"apple": 1.5, "banana": 1.2, "orange": 2.0}
cart = {"apple": 2, "banana": 3, "orange": 1}
sentence = "apple banana apple orange banana apple"

for key, value in prices.items():
    print(key, value)

prices.update({"pineapple": 1.1})

print(prices)

print(sum(prices.values()))

total_price = 0
for key, value in cart.items():
    total_price += value * prices.get(key)

print(total_price)

sentence_tab = sentence.split(" ")
sentense_dict = {}

for word in sentence_tab:
    if (word not in sentense_dict):
        sentense_dict[word] = 1
    else:
        sentense_dict[word] += 1

print(sentense_dict)

#Les fonctions

def is_palindrome(word):
    return word == word[::-1]

print(is_palindrome("hello"))

def get_fibonnaci(number :int) -> list[int]:
    result :list[int] = [0, 1]

    for i in range(number -2):
        result.append(result[-1] + result[-2])

    return result

print(get_fibonnaci(10))

player1 = Player("Bob", Vector2D(5, 0), Vector2D(2, 3), 6)
player2 = Player("Patrick", Vector2D(0, 5), Vector2D(2, 3), 10)
player3 = Player("Sandy", Vector2D(-4, -6), Vector2D(2, 3), 10)
player4 = Player("Plancton", Vector2D(10, 3), Vector2D(2, 3), 10)
player5 = Player("MrCrabe", Vector2D(-10, 5), Vector2D(2, 3), 10)


print("Player is visible" if player1.is_visible(player2) else "Player is not visible")

player_visible = player1.area_visible([player2, player3, player4, player5])
for player in player_visible:
    print(player.name)

print("With FOV")
player_visible = player1.area_fov_visible([player2, player3, player4, player5])
for player in player_visible:
    print(player.name)

car = Car()