import os
import sys

for filename in os.listdir(sys.argv[1]):
    with open("{}/{}".format(sys.argv[1], filename), 'r') as txtfile:
        lines = txtfile.readlines()
        print(' '.join(line.strip() for line in lines))
