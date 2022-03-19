from socket import herror
from turtle import title

from random import choice


fname = input("Enter the File name: ")
f = open('D:\\vscode files\\python\\file handaling_files\\' + fname, 'a+')


class movie:
    """Movie class developed by Ashutosh for python practice"""

    def __init__(self, num, title, hero, heroine):
        self.num = num
        self.title = title
        self.hero = hero
        self.heroine = heroine

    def info(self):
        f.write("File number:" + str(self.num)+'\n')
        f.write("Movie name:" + self.title+'\n')
        f.write("Hero name:" + self.hero+'\n')
        f.write("Heroine name:" + self.heroine+'\n')
        f.write('\n')
        print("File number ", self.num)
        print('Movie name:', self.title)
        print('Hero name:', self.hero)
        print('Heroine name:', self.heroine)
        print('\n')


num = 1
list_of_movies = []
while True:

    title = input("Enter Movie name: ")
    hero = input("Enter Hero name: ")
    heroine = input("Enter Heroine name: ")
    m = movie(num, title, hero, heroine)
    list_of_movies.append(m)
    print("Movie add to the list successfully! ")
    # f.write("The movie is added to the list successfully")
    option = input("Do you want to add more Movies in the list [yes| no]! :")
    num = num+1
    if option.lower() == "no":
        break
print("\n\n")

f.write("#"*50+"\n")
f.write("All Movies information...." + "\n")
f.write("#"*50+"\n")

print("#"*50)
print("All Movies information....")
print("#"*50)
for movie in list_of_movies:
    movie.info()
