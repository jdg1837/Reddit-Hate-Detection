import sys
import json
import file_io

if len(sys.argv) < 2:
    print("Please include parameter file and API file")
param_file = sys.argv[1]

subreddits = file_io.read_parameters(param_file)[1]
src = file_io.read_parameters(param_file)[6]

for sub in subreddits:
    sub_data = []
    input_file = src + '/' + sub.lower() + '_' + src + '.json'
    comment_data = file_io.read(input_file)["data"]
    output_file = src + '/' + sub.lower() + '_' + src + '_comments.txt'
    file_io.set_output_file(output_file)

    for datum in comment_data:
        comment = datum['body'].replace('\n','')
        sub_data.append(comment)

    with open(output_file,'w',encoding='utf-8') as f:
        for comment in sub_data:
            f.write(comment + '\n')