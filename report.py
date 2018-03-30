from sys import argv
from time import localtime, strftime, strptime

from operator import itemgetter

'''
The complexity of the code wil be:
O(n+ mlogm * klogk) where n is number of lines in input file, m is number of
unique dates sorted and k is len of sorted url hits.
Since we are given that unique dates and hits are pretty low (n >> k),
essentially the complexity should be O(n) as it will take most of the time.
'''


def in_dict(_dict, key):
    """
    Returns True if key is present in dictionary else return False if not
    present.
    :param _dict: dictionary
    :param key: key
    :rtype : bool
    """
    return True if key in _dict else False


def create_url_map(input_file):
    """
    This function takes in the input text file with unix time(epochs) and urls
    separated by a pipe(|) and returns the mapping of date to map of unique
    urls and number of hits on that date.
    :param input txt file:
    :rtype : dictionary
    """
    time_url_map = {}

    with open(input_file) as _file:
        for line in _file:
            line = line.split('|')
            gmt = strftime('%Y/%m/%d', localtime(int(line[0])))
            # gmt = line[0][:10]
            if not in_dict(time_url_map, gmt):
                time_url_map[gmt] = {}
            url = line[1].strip('\n')
            time_url_map[gmt][url] = 1 if not in_dict(time_url_map[gmt], url) \
                else time_url_map[gmt][url] + 1

    return time_url_map


def print_sorted_mapping(time_url_map):
    """
    This function takes in the mapping from create_url_map() and prints out
    daily summarized report on url hit count, organized daily(GMT) with the
    earliest date appearing first and for each day, displays the number of
    times each url is visited in the order of highest hit count to lowest count.
    :param dictionary:
    """

    # with open('sorted_output.txt','w') as sortf:
    for i in sorted(time_url_map.items(), key=itemgetter(0)):
        new_date = strftime('%m/%d/%Y', strptime(i[0], '%Y/%m/%d'))
        print(new_date + ' GMT')
        # sortf.write(str(new_date) + ' GMT' + '\n')
        sorted_urls_count = sorted(i[1].items(), key=itemgetter(1), reverse=True)
        for j in sorted_urls_count:
            # sortf.write(j[0] + ' ' + str(j[1]) + '\n')
            print(j[0] + ' ' + str(j[1]))
            # sortf.write('------------------------------------------------------------------------------------\n')


def main(input_file):
    mapping = create_url_map(input_file)
    print_sorted_mapping(mapping)


if __name__ == '__main__':
    main(argv[1])
