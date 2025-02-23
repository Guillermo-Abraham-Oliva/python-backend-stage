import os
os.system('clear' if os.name == 'posix' else 'cls')

import time
import itertools
relojillo = itertools.cycle(['-', '\\', '|', '/'])

for _ in range(7):
    print(f"{next(relojillo)}", end="\r")
    time.sleep(0.1)
print('\r                                                                                ')

for _ in range(7):
    print(f" {next(relojillo)}", end="\r")
    time.sleep(0.1)
print('\r                                                                                ')

for _ in range(7):
    print(f"  {next(relojillo)}", end="\r")
    time.sleep(0.1)
print('\r                                                                                ')

for _ in range(7):
    print(f"   {next(relojillo)}", end="\r")
    time.sleep(0.1)
print('\r                                                                                ')

for _ in range(7):
    print(f"    {next(relojillo)}", end="\r")
    time.sleep(0.1)
print('\r                                                                                ')

for _ in range(7):
    print(f"     {next(relojillo)}", end="\r")
    time.sleep(0.1)
print('\r                                                                                ')

for _ in range(7):
    print(f"      {next(relojillo)}", end="\r")
    time.sleep(0.1)
print('\r                                                                                ')

for _ in range(7):
    print(f"       {next(relojillo)}", end="\r")
    time.sleep(0.1)
print('\r                                                                                ')

print('''
\n\n==========================
    Proceso completado
==========================
''')
