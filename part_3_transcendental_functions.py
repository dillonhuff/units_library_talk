import pint
import math

ur = pint.UnitRegistry()

mass = 3.0 * ur.kilograms

print('mass:', mass)

this_value_makes_sense = math.sin(mass / mass)

print('sensible:', this_value_makes_sense)


this_value_is_nonsense = math.sin(mass)

print('nonsense value:', this_value_is_nonsense)

