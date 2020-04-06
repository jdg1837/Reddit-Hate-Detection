import Reddit
import json_io
import time

sub_list = ['Gaming','LeagueOfLegends','Overwatch','Minecraft','Games','television','movies','rickandmorty','gameofthrones','freefolk','StarWars','comicbooks','marvelstudios','Marvel','DCcomics','batman','horror']
#sub_list = ['comicbooks','marvelstudios','Marvel','DCcomics','batman','horror']
size = 2
epoch = 1585717199 #March 31st, 11:59 PM
final_epoch = 1577858400
fields = "body,author,score,permalink,created_utc"
users = {}
k = 100

sub = sub_list[0]
output_file = sub.lower() + '_data.json'
json_io.set_output_file(output_file)

count = 0
while epoch > final_epoch:
    epoch, count_curr = Reddit.request_data(sub,500,fields,epoch,count==0,users)
    count += count_curr

for sub in sub_list[1:]:
    sub_count = 0
    output_file = sub.lower() + '_data.json'
    json_io.set_output_file(output_file)

    while sub_count < count:
        epoch, count_curr = Reddit.request_data(sub,500,fields,epoch,sub_count==0,users)
        if count_curr == -1:
            break
        else:
            sub_count += count_curr