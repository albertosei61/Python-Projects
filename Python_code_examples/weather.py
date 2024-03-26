import csv


with open('weather.csv', 'r') as file:
    weatherData = list(csv.reader(file))
    print(weatherData)
city = str(input('Enter station: '))
for row in weatherData:
    if row[0] == city:
        print(f'The temperature is {row[1]} degrees Fahrenheit')
