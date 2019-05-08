#Create a list for each item below that contains the given information:
fav_colours = ['brown', 'yellow', 'red']
age = ['five', 'one', 'ten']
coin = ['heads', 'tails', 'heads', 'heads']
artist= ['Ricky Martin', 'Betman', 'Sher'] 

#Create a dictionary for each item below that contains the given information:

three_words = {
    'Ironman': 'strong',
    'Betman': 'respectful',
    'Spiderman': 'thinkful' 
}
fav_movie = {
    'Back to the Future': '1985',
    'Titanic': '2000'
}
three_cities = {
    'Toronto': 3,
    'Oakville': 1,
    'Bloomfield': 1
}
name_siblings = {
    'Danile': 7,
    'Sofia': 5,
    'Evgenia': 35
}


age.append(0)

print(name_siblings)
print(coin)
print(fav_colours[0])
print('Sorted list:', name_siblings)
print(fav_movie['Titanic'])

print(fav_colours[-1])
three_cities.update({'Brampton': 3})
coin.reverse()
print(coin)
print(three_cities['Toronto'])


for name in artist:
    print(f"I think {name} is great!")

    
