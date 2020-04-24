import Reddit
import file_io
import time
import sys

if len(sys.argv) < 2:
    print("Please include parameter file")
param_file = sys.argv[1]

method, subreddits, start, end, fields, k, src, dst, extend =  file_io.read_parameters(param_file)

program_start = int(time.time())

for sub in subreddits:
    sub_count = 0
    epoch = start
    output_file = dst + '/' + sub.lower() + '_' + dst + '.json'
    file_io.set_output_file(output_file)

    if extend:
        epoch, sub_count = file_io.extract_data(sub,src)

    while True:
        if (method=="count" and sub_count >= k*1000) or (method=="time" and epoch <= end):
            break

        epoch, count_curr = Reddit.request_data(sub,500,fields,epoch,sub_count==0)

        if count_curr == -1:
            break
        else:
            sub_count += count_curr

program_end = int(time.time())

print(program_end - program_start)