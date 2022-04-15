sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# Dictionary comprehension
result = {word: len(word) for word in sentence.split()}

print(result)
