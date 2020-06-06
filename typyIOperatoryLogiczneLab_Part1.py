isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRain = False
turnLightsOn  = isAutomaticMode and (not is80PercentLight or isDirectLight or isRain)
print("case 1")
print("Automatic mode: ",isAutomaticMode)

print("Is the light good: ",is80PercentLight)

print("Is sun low: ", isDirectLight)

print("Is it rainy: ",isRain)

print()

print("TURN LIGHTS ON", turnLightsOn)
print()

print("case 2")
isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRain = False
turnLightsOn  = isAutomaticMode and (not is80PercentLight or isDirectLight or isRain)

print("Automatic mode: ",isAutomaticMode)

print("Is the light good: ",is80PercentLight)

print("Is sun low: ", isDirectLight)

print("Is it rainy: ",isRain)

print()

print("TURN LIGHTS ON", turnLightsOn)
print()

print("case 3")
isAutomaticMode = True
is80PercentLight = True
isDirectLight = False
isRain = True
turnLightsOn  = isAutomaticMode and (not is80PercentLight or isDirectLight or isRain)

print("Automatic mode: ",isAutomaticMode)

print("Is the light good: ",is80PercentLight)

print("Is sun low: ", isDirectLight)

print("Is it rainy: ",isRain)

print()

print("TURN LIGHTS ON", turnLightsOn)
print()

print("case 4")
isAutomaticMode = True
is80PercentLight = True
isDirectLight = True
isRain = False
turnLightsOn  = isAutomaticMode and (not is80PercentLight or isDirectLight or isRain)

print("Automatic mode: ",isAutomaticMode)

print("Is the light good: ",is80PercentLight)

print("Is sun low: ", isDirectLight)

print("Is it rainy: ",isRain)

print()

print("TURN LIGHTS ON", turnLightsOn)
print()

print("case 5")
isAutomaticMode = True
is80PercentLight = False
isDirectLight = False
isRain = True
turnLightsOn  = isAutomaticMode and (not is80PercentLight or isDirectLight or isRain)

print("Automatic mode: ",isAutomaticMode)

print("Is the light good: ",is80PercentLight)

print("Is sun low: ", isDirectLight)

print("Is it rainy: ",isRain)

print()

print("TURN LIGHTS ON", turnLightsOn)
print()

print("case 6")
isAutomaticMode = False
is80PercentLight = True
isDirectLight = False
isRain = True
turnLightsOn  = isAutomaticMode and (not is80PercentLight or isDirectLight or isRain)

print("Automatic mode: ",isAutomaticMode)

print("Is the light good: ",is80PercentLight)

print("Is sun low: ", isDirectLight)

print("Is it rainy: ",isRain)

print()

print("TURN LIGHTS ON", turnLightsOn)