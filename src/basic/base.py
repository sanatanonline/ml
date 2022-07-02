"""list fundamentalls"""
movies = ['The Holy Grail', 'The Spy Who Loved Me', 'Paddington', 10]
print(type(movies[3]))
print(len(movies))
print(movies)
'This only replaces the item at index 2'
movies[2] = 'Titanic'
print(type(movies[3]))
print(len(movies))
print(movies)
'append item at the last'
movies.append('The Golden Eye')
print(type(movies[3]))
print(len(movies))
print(movies)
'remove one item from top'
movies.pop()
print(type(movies[3]))
print(len(movies))
print(movies)
'remove one item from an index location'
movies.pop(2)
print(type(movies[1]))
print(len(movies))
print(movies)

recent_movies = ['The Spiderman', 'The Batman']
movies.extend(recent_movies)
print(movies)
movies.insert(0, 'Avengers')
print(movies)
'iterate through list using for loop'
for movie in movies:
    print(movie)

'iterate through list using while loop'
count = 0
while count < len(movies):
    print(movies[count])
    count += 1
