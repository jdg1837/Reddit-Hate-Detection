sub_list = ['Gaming','LeagueOfLegends','Overwatch','Minecraft','Games','television','movies','rickandmorty','gameofthrones','freefolk','StarWars','comicbooks','marvelstudios','Marvel','DCcomics','batman','horror']

for sub in sub_list:
    with open('data/'+sub.lower()+'_data.json', 'r', encoding="utf8") as f:
        lines = f.readlines()
    print(len(lines))