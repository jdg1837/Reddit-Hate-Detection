import file_io
import sys
import os 

if len(sys.argv) < 2:
    print("Please include parameter file")
param_file = sys.argv[1]

subreddits = file_io.read_parameters(param_file)[1]
src = file_io.read_parameters(param_file)[6]
count = []

subreddits = [x.lower() for x in subreddits]
subreddits.sort()

for sub in subreddits:
    del_count = 0
    input_file = src + '/' + sub.lower() + '_' + src + '.json'
    data = file_io.read(input_file)['data']

    for datum in data:
        if datum['body'] == '[removed]' in datum['body']:
            del_count += 1

    count.append("{:15s}{:10,d}\n".format(sub,del_count))
    
with open(src + '/' + src + '_rem_count.txt', 'w', encoding="utf8") as f:
    f.writelines(count)