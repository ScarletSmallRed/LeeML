import matplotlib.pyplot as plt

movie_name = ["The Wandering Earth", "Avengers: Endgame", "Crazy Alien", "Pegasus", "Spider-Man: Far From Home", "Bumblebee", "The White Storm 2 - Drug Lords", "Captain Marvel", "More than Blue", "Godzilla: King of the Monsters", "Alita: Battle Angel", "P Storm", "Boonie Bears: Blast into the Past", "Pokémon Detective Pikachu", "The New King of Comedy", "The Lion King", "Spirited Away", "Green Book", "White Snake", "With You"]

movie_total_box_office = [46.81, 42.05, 21.83, 17.03, 13.46, 11.38, 10.78, 10.25, 9.46, 9.26, 8.88, 7.88, 7.09, 6.34, 6.19, 5.27, 4.79, 4.73, 4.55, 4.08]

plt.figure(figsize=(22, 8), dpi = 80)

plt.barh(range(len(movie_name)),movie_total_box_office, height = 0.5, color = 'orange')  
plt.yticks(range(len(movie_name)), movie_name)
step = []  
for i in range(0, 50, 2):  
    step.append(i)
plt.xticks(step)
plt.grid(alpha=0.3)
plt.title('2019 Movie Box Office Ranking')
plt.xlabel('Box Office')
plt.ylabel('Movie')

plt.savefig("./Movie.png")
plt.show()