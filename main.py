import Reddit
import file_io
import time
import sys

if len(sys.argv) < 2:
    print("Please include parameter file")
param_file = sys.argv[1]

method, subs, start, end, fields, k =  file_io.read_parameters(param_file)

program_start = int(time.time())

users = []
count = []

for sub in sub_list:
    sub_count = 0
    epoch = start
    output_file = sub.lower() + '_data.json'
    json_io.set_output_file(output_file)

    for round in range(k*2):
    while True:
        if (method=="count" and sub_count >= k*1000) or (method=="time" and epoch <= end):
            break

        epoch, count_curr = Reddit.request_data(sub,500,fields,epoch,round==0)

        if count_curr == -1:
            break
        else:
            sub_count += count_curr

    count.append(sub+','+str(sub_count))

file_io.write_to_txt(count,'comment_count.txt')
file_io.write_to_txt(users,'users.txt')

program_end = int(time.time())

print("%d\n", program_end - program_start)