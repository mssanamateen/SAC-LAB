cent=float(input("enter the temperature in degree centigrade:"))
# Why do we multiply by 9/5?

# On Celsius scale: 0°C = freezing, 100°C = boiling → difference = 100 units
# On Fahrenheit scale: 32°F = freezing, 212°F = boiling → difference = 180 units
# So, 100°C change = 180°F change
# Therefore, 1°C = 180/100 = 9/5 °F
#
# Then we add 32 because 0°C corresponds to 32°F (offset adjustment).


# Apply the conversion formula
# Formula: F = (C × 9/5) + 32
fahrenheit=9/5*cent+32

print("The converted temperature is", fahrenheit)