#Create a list for each item below that contains the given information:
fav_colours = ['brown', 'yellow', 'red']
age = ['5', '1', '10']
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
    'Evgenia': 35,
    'Danile': 7,
    'Sofia': 5
}


# age.append(0)

# print(name_siblings)
# print(coin)
# print(fav_colours[0])
# print('Sorted list:', name_siblings)
# print(fav_movie['Titanic'])

# print(fav_colours[-1])
# three_cities.update({'Brampton': 3})
# coin.reverse()
# print(coin)
# print(three_cities['Toronto'])


# for name in artist:
#     print(f"I think {name} is great!")
# #3.1
# print(artist[0])
# #3.2
# for pizza, pasta in fav_movie.items():
#     print(f"{pizza} came out {pasta}")
# #3.3
# age.sort(reverse=True)
# print(age)

# #3.4
# fav_movie['Beauty and the Beast'] = 1991, 2017 
# print(fav_movie)

# #4.1
# for nameage in age:
#     if nameage < 30:
#         print (nameage) 

# #4.2
# print(max(name_siblings))
# #4.3
# count = coin.count('heads')
# print(count)
# #4.4
# del artist[1]
# print(artist)
# #4.5
#three_cities.update({'Toronto': '10'})
#print(three_cities)
# #5.1
#print(sum(three_cities.values()))
# #5.2
#for key, value in name_siblings.items():
#    if value < 30:
#        print(f"{key} is young")
#    else:
#        print(f"{key} is old")
# #5.3
#print(fav_colours[1:3])
# #5.4 
# +enumerate
#for index, a in enumerate(age):
#    aa = int(a)
#    age[index] = aa + 1
#print(age)
# # 5.4
# new_ages = []
# for a in age:
#     aa = int(a)
#     aa += 1
#     new_ages.append(aa)
# print(new_ages)
# #5.5
#fav_colours.append('black')
#fav_colours.append('white')
#print(fav_colours)
# #6.1
# movies = {
#     1999: ["The Matrix", "Star Wars: Episode 1", "The Mummy"], 2009: ["Avatar", "Star Trek", "District 9"], 2019: ["How to Train Your Dragon 3", "Toy Story 4", "Star Wars: Episode 9"]
# }
# phone_buttons = {
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     ['*', 0, '#']
# }
countries = [
  {'country': 'Canada', 'continent': 'North America', 'island': False},
  {'country': 'Russia', 'continent': 'Europe', 'island': False},
  {'country': 'Japan', 'island': 'Oceania', 'island': True}
]
# #7.1
# for i in range(20):
#     print ("I will not skateboard in the halls")
# #7.2
# list = []
# for i in range(20):
#     list.append("I will not skateboard in the halls")
# print(list)
# #7.3
# list = range(1, 51)
# print(list(numbers))
# # #7.4

# total = 0
# for num in list:
#     total += num
# print(total)

# #7.5
# new_list = []
# for i in range(1,50):
#     new_list.append(i)
#     new_list.append(i)
#     new_list.append(i)
# print(new_list)
# #7.6
# non_island_countries = []
# for country in countries:
#     if country['island'] == False:
#         non_island_countries.append(country)
# print(countries)
# print(non_island_countries)

# #8
  
expense = [250, 5, 1, 2, 9, 4]
expensea = [350, 15, 41, 22, 19, 34]
print(sum(expense))
print(sum(expensea))

def expense_total(l):
    return sum(l)

print(expense_total(expense))
print(expense_total(expensea))   
