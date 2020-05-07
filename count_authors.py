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
    author_count = {}
    input_file = src + '/' + sub.lower() + '_' + src + '.json'
    output_file = src + '/' + sub.lower() + '_' + src + '_authors.txt'
    data = file_io.read(input_file)['data']
    for datum in data:
        author = datum['author']
        if author in author_count:
            author_count[author] += 1
        else:
            author_count[author] = 1

    with open(output_file, 'w', encoding="utf8") as f:
        for author in sorted(author_count, key=author_count.get, reverse=True):
            f.write("{},{}\n".format(author,author_count[author]))