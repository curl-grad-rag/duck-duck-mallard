
# Singleton Pattern
from tigger import *

a = tigger()
b = tigger()
print(f'ID(a) = {id(a)}')
print(f'ID(b) = {id(b)}')
print(f'Are they the same? {a is b}')

c = tigger2()
d = tigger2()
print(f'ID(c) = {id(d)}')
print(f'ID(d) = {id(c)}')
print(f'Are they the same? {c is d}')