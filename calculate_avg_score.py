import file_io
import sys
import os 

if len(sys.argv) < 2:
    print("Please include parameter file")
param_file = sys.argv[1]

subreddits = file_io.read_parameters(param_file)[1]
src = file_io.read_parameters(param_file)[6]
count = []

for sub in subreddits:
    score = 0
    c = 0
    input_file = src + '/' + sub.lower() + '_' + src + '.json'
    data = file_io.read(input_file)['data']

    for datum in data:
        score += datum['score']
        c += 1

    score = score/c

    count.append("{:15s}{:10,f}\n".format(sub,score))
    
with open(src + '/' + src + 'avg_score.txt', 'w', encoding="utf8") as f:
    f.writelines(count)