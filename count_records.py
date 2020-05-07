import file_io
import sys
import os 

if len(sys.argv) < 2:
    print("Please include parameter file and API file")
param_file = sys.argv[1]

subreddits = file_io.read_parameters(param_file)[1]
src = file_io.read_parameters(param_file)[6]

comment_count = []

for sub in subreddits:
    word_count = {}
    input_file = src + '/' + sub.lower() + '_' + src + '_comments.txt'
    with open(input_file, 'r', encoding="utf8") as f:
        lines = f.readlines()
        count = int((len(lines)))

    comment_count.append("{:15s}{:10,d}\n".format(sub,count))
    
with open(src + '/' + src + '_count.txt', 'w', encoding="utf8") as f:
    f.writelines(comment_count)