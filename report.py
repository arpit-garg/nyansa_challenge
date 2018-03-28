from sys import argv
from time import localtime, strftime

from operator import itemgetter

'''
The complexity of the code wil be:
O(n) for reading and creating the mapping of dates and urls where n is length of file.
O(mlogm * klogk) where m is len of unique dates sorted and k is len of sorted url hits.
Since we are given that unique dates and hits are pretty low and unique urls fit into memory,
this code wouldn't take too long.
It uses dictionary(hashmap) for O(1) lookup.
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
            gmt = strftime('%m/%d/%Y', localtime(int(line[0])))

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
    for i in sorted(time_url_map.items(), key=itemgetter(0)):
        print(i[0] + ' GMT')
        sorted_urls_count = sorted(i[1].items(), key=itemgetter(1), reverse=True)
        for j in sorted_urls_count:
            print(j[0] + ' ' + str(j[1]))


def main(input_file):
    mapping = create_url_map(input_file)
    print_sorted_mapping(mapping)


if __name__ == '__main__':
    main(argv[1])
