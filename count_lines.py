import sys
import os 

if len(sys.argv) < 2:
    print("Please include directory name and file suffix")
directory = sys.argv[1]

comment_count = []

for filename in os.listdir(directory):
    if filename == directory + '_count.txt':
        continue
    with open(directory + '/' + filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        count = int((len(lines)-4)/7)

    sub = filename.split('_')[0]

    comment_count.append(sub+', '+str(count)+'\n')
    
with open(directory + '/' + directory + '_count.txt', 'w', encoding="utf8") as f:
    f.writelines(comment_count)