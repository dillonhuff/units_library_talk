import pint
import math

ur = pint.UnitRegistry()

mass = 3.0 * ur.kilograms

print('mass:', mass)

this_value_makes_sense = math.sin(mass / mass)

print('sensible:', this_value_makes_sense)


this_value_is_nonsense = math.sin(mass)

print('nonsense value:', this_value_is_nonsense)

# Some links discussing this problem of transcendentals:
# - https://pubs.acs.org/doi/abs/10.1021/ed1000476?casa_token=lxqvMHb8e9IAAAAA:HXgKk3vgOaPNs9Q_5Unl8TfsQQy3MpW4T4urEhmS-wxqc4K2uc6N4XFuCEuetkbdX6pTujIZ3QiirLo
# - https://idp.springer.com/authorize/casa?redirect_uri=https://link.springer.com/article/10.1023/A:1019102415633&casa_token=SCgq7aPJymAAAAAA:h3nr_mp0vbVZ8jk35cgwDSe4MUpB1li-gBw3CEmKryF0ev0Y9Z0CJC0IGqEtRwMcjO7GN6np0KvSCIo3 
