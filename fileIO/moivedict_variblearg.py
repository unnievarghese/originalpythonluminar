f=open('movies.csv')
movie={}
for line in f:
    words=list(line.rstrip('\n').split(','))
    if words[1] not in movie:
        movie[words[1]]={'name':words[1],'year':words[2],'rating':words[3],'no.of votes':words[4]}
def func(**arg):
    mov_name=arg.get('name')
    mov_detail=arg.get('detail')
    if mov_name in movie and mov_detail not in movie[mov_name]:
        print(movie[mov_name])
    if mov_name in movie and mov_detail in movie[mov_name]:
        print(movie[mov_name][mov_detail])

#a=input('Enter the movie name:')
#b=input('enter specific moive detail:')
func(name=input(),detail=input())
