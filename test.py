__author__ = 'arpitgarg'
import re
import time
datetime_pattern = '%Y-%m-%d %H:%M:%S'
def preprocessing():
    regex = '([a-z0-9.\-]+[.][a-z]{1,10}/)'
    count = 0
    with open('sample_test_data1.txt') as readf, open('input_data2', 'w') as writef:
        for n, line in enumerate(readf):
            try:

                line = line.split('|')
                epoch = int(time.mktime(time.strptime(line[0], datetime_pattern)))
                url = re.search(regex, line[1]).group(1)
                url = url.strip('/')
                writef.write(str(epoch) + '|' + url + '\n')
            except AttributeError as e:
                count += 1
                # print(n)
                # print(line)
                continue
    print(count)

preprocessing()
