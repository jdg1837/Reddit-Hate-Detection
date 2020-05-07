import file_io
import sys

if len(sys.argv) < 4:
    print("Please include parameter file, treshold value, and toxicity type: 1 for regular, 2 for identity")
param_file = sys.argv[1]
z = float(sys.argv[2])

toxicity_type = 'toxicity'
if int(sys.argv[3]) == 2:
    toxicity_type = 'identity'
if int(sys.argv[3]) == 3:
    toxicity_type = 'identities'


subreddits =  file_io.read_parameters(param_file)[1]
src = file_io.read_parameters(param_file)[6]
dst = file_io.read_parameters(param_file)[7]

for sub in subreddits:
    input_file = src + '/' + sub.lower() + '_' + src + '_attack.json'
    comment_data = file_io.read(input_file)["data"]
    output_file = dst + '/' + sub.lower() + '_' + dst + '.json'
    file_io.set_output_file(output_file)

    old_data = file_io.read(input_file)
    sub_data = old_data['data']
    filtered_data = []

    for datum in sub_data:
        if toxicity_type == 'identities':
            if len(datum[toxicity_type]) == 0:
                filtered_data.append(datum)
        elif datum[toxicity_type] >= z:
            filtered_data.append(datum)

    data = {'data': filtered_data}
    file_io.write(data)