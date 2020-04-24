import language
import file_io
import json
import sys

if len(sys.argv) < 2:
    print("Please include parameter file")
param_file = sys.argv[1]

subreddits =  file_io.read_parameters(param_file)[1]
k, src, dst = file_io.read_parameters(param_file)[5:8]
k = k*1000

for sub in subreddits:
    sub_data = []
    input_file = src + '/' + sub.lower() + '_' + src + '.json'
    comment_data = file_io.read(input_file)["data"]
    output_file = dst + '/' + sub.lower() + '_' + dst + '.json'
    file_io.set_output_file(output_file)

    for datum in comment_data:
        comment = datum['body']
        if comment == '[removed]' or not language.is_english(comment):
            continue
        score = language.get_toxicity(comment)
        datum['toxicity'] = score
        sub_data.append(datum)
        if len(sub_data) >= k:
            break

    data = {'data': sub_data}
    file_io.write(data)