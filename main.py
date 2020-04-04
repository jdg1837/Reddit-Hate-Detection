import pushshift
import json_io
import time

sub_list = ['Gaming','LeagueOfLegends','Overwatch','Minecraft','Games','television','movies','rickandmorty','gameofthrones','freefolk','StarWars','comicbooks','marvelstudios','Marvel','DCcomics','batman','horror']
#sub_list = ['comicbooks','marvelstudios','Marvel','DCcomics','batman','horror']
size = 2
epoch = int(time.time())
fields = "body,author,score,permalink,created_utc"
k = 100

start = epoch

for sub in sub_list:
    output_file = sub.lower() + '_data.json'
    json_io.set_output_file(output_file)

    for round in range(k*2):
        epoch = pushshift.request_data(sub,500,fields,epoch,round==0)

end = int(time.time())

print("%d\n", end - start)