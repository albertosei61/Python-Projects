def get_frequency(text, word):
    words = text.strip(" ")
    count = text.count(word)
    frequency = count / len(words) * 100
    return frequency

frequency = get_frequency("I love Sun", "love")
if frequency > 5:
    print("High frequency")
else:
    print("Low frequency")

