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

'nested lists'
complete_movies = [['Titanic', 1970], ['The Spiderman', 2012], ['Avengers', 2021]]
print(complete_movies[1][1])

for each_movie in complete_movies:
    if isinstance(each_movie, list):
        print("this is a list", each_movie)
    print(each_movie, type(each_movie))

'built-in functions'
built_ins = dir(__builtins__)
print(len(built_ins))
for item in built_ins:
    print(item)


def process_nested_list(items):
    """
    This function prints the nested list of items
    """
    for list_item in items:
        if isinstance(list_item, list):
            process_nested_list(list_item)
        else:
            print(list_item)


process_nested_list(movies)
