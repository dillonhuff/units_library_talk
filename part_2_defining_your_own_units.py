# Import the units of measurement library
import pint

# Initialize the data structure that 
# stores units
ur = pint.UnitRegistry()

print('------ CPU Throughput In Ops Per Second')
# The throughput of the CPU measured in pixels of
# input processed per second
throughput = (1.35133e+10 * ur.pixels / ur.seconds)
print('CPU throughput:', throughput)

print()

pixel_size = 2 * ur.bytes / ur.pixel
print('Bytes per pixel:', pixel_size)
print()

# Define a new unit: "op", a unit of
# computation
ur.define('op = [computation]')

arithmetic_intensity = 4 * ur.ops / ur.byte

print('Arithmetic intensity:', arithmetic_intensity)
print()

throughput_in_ops_per_sec = (throughput * pixel_size * arithmetic_intensity).to(ur.gigaops / ur.seconds)

print('CPU throughput:', throughput_in_ops_per_sec)
print()



