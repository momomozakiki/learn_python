letters = ["a", "b", "c", "y"]
it = iter(letters)
while True:
    try:
        letter = next(it)
    except StopIteration:
        break
    print(letter)
