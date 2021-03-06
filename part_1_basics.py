# Import the units of measurement library
import pint

# Initialize the data structure that 
# stores units
ur = pint.UnitRegistry()

print('------ CPU energy efficiency')
# The throughput of the CPU measured in pixels of
# input processed per second
throughput = (1.35133e+10 * ur.pixels / ur.seconds)
print('CPU throughput:', throughput)

print()

# Define the power consumption of the design in Watts
power = 122 * ur.watts
print('CPU power:', power)

print()

# Compute energy efficiency and print it out
ppf = (throughput / power)
print('CPU energy efficiency (original) :', ppf)

# Convert to gigapixels per joule
ppf = ppf.to(ur.gigapixels / ur.joules)
print('CPU energy efficiency (converted):', ppf)
print()

