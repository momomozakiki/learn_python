# https://gist.github.com/Zearin/2f40b7b9cfc51132851a

def shout(word='yes'):
    return word.capitalize() + '!'


print('shout', shout())

scream = shout

print('scream', scream())

del shout
try:
    print(shout())
except NameError as e:
    print('Error', e)


print(scream)