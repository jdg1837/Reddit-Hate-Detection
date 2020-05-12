import file_io
import sys
import os 

if len(sys.argv) < 2:
    print("Please include parameter file and API file")
param_file = sys.argv[1]

subreddits = file_io.read_parameters(param_file)[1]
src = file_io.read_parameters(param_file)[6]

subreddits = [x.lower() for x in subreddits]
subreddits.sort()
comment_count = {}

for sub in subreddits:
    word_count = {}
    input_file = src + '/' + sub.lower() + '_' + src + '.json'
    data = file_io.read(input_file)['data']
    count = len(data)
    #print(count)

    comment_count[sub] = count

with open(src + '/' + src + '_count.csv', 'w', encoding="utf8") as f:
    for sub in subreddits:
        f.write('{},{}\n'.format(sub,comment_count[sub]))