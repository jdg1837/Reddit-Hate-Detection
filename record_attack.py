import language
import file_io
import time
import file_io
import json
import sys

if len(sys.argv) < 3:
    print("Please include parameter file and API file")
param_file = sys.argv[1]
key_file = sys.argv[2]

program_start = int(time.time())

subreddits =  file_io.read_parameters(param_file)[1]
src, dst = file_io.read_parameters(param_file)[6:8]
language.set_API_key(key_file)

for sub in subreddits:
    sub_data = []
    input_file = src + '/' + sub.lower() + '_' + src + '.json'
    comment_data = file_io.read(input_file)["data"]
    output_file = dst + '/' + sub.lower() + '_' + dst + '.json'
    file_io.set_output_file(output_file)

    c = 0 #number of api calls
    d = 0 #number of succesful api calls
    st = 0
    end = len(comment_data)

    t1 = int(time.time())

    for i in range(st,end):
        datum = comment_data[i]
        comment = datum['body']
        score = language.get_toxicity(comment, 'IDENTITY_ATTACK')
        c += 1

        if c == 600:
            t2 = int(time.time())
            t = t2 - t1
            if t < 60:
                time.sleep(60 - t)
            t1 = int(time.time())
            c = 0

        if score < 0:
            continue

        datum['identity'] = score
        sub_data.append(datum)

        d += 1

        if d % 1000 == 0:
            data = {'data': sub_data}
            file_io.write(data)

    data = {'data': sub_data}
    file_io.write(data)

program_end = int(time.time())

print(program_end - program_start)