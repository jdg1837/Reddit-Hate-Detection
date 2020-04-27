import sys
import os 

if len(sys.argv) < 3:
    print("Please include directory name and size of packets")
directory = sys.argv[1]
n = sys.argv[2]

comment_count = []

for filename in os.listdir(directory):
    if filename == directory + '_count.txt':
        continue
    with open(directory + '/' + filename, 'r', encoding="utf8") as f:
        lines = f.readlines()
        count = int((len(lines)-4)/n)

    sub = filename.split('_')[0]

    comment_count.append(sub+'\t\t'+str(count)+'\n')
    
with open(directory + '/' + directory + '_count.txt', 'w', encoding="utf8") as f:
    f.writelines(comment_count)