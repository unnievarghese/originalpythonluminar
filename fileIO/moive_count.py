f=open("movies.csv")
movie_dict={}
for lines in f:
    words=list(lines.rstrip('\n').split(','))

    if words[2] not in movie_dict:
        movie_dict[words[2]]=[words[1]]
    else:
        movie_dict[words[2]].append(words[1])
print('Total number of movies:','\n')
for year in sorted(movie_dict):
    print(year,':',len(movie_dict[year]))