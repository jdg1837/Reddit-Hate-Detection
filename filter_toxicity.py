import file_io
import sys

if len(sys.argv) < 3:
    print("Please include parameter file and treshold value")
param_file = sys.argv[1]
z = float(sys.argv[2])

subreddits =  file_io.read_parameters(param_file)[1]
src = file_io.read_parameters(param_file)[6]

for sub in subreddits:
    input_file = src + '/' + sub.lower() + '_' + src + '.json'
    comment_data = file_io.read(input_file)["data"]
    output_file = src + '/' + sub.lower() + '_' + src + '_' + 'filtered' + '_' + str(z) + '.json'
    file_io.set_output_file(output_file)

    old_data = file_io.read(input_file)
    sub_data = old_data['data']
    filtered_data = []

    for datum in sub_data:
        if datum['toxicity'] >= z:
            filtered_data.append(datum)

    data = {'data': filtered_data}
    file_io.write(data)