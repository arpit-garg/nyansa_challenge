__author__ = 'arpitgarg'
import re
import time

def preprocessing():
    datetime_pattern = '%Y-%m-%d %H:%M:%S'
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
            except AttributeError:
                count += 1
                continue
    print(count)

preprocessing()
