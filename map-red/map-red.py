from sys import argv
from operator import itemgetter

'''
Key-Value Transformations

To solve this problem, we will use multiple pass map reduce jobs.

The map reduce jobs will be chained/cascaded together to get the final answer.
Initially we will have our data as list of data points read from an input file.

The 1st mapper will get the id as key and score and device type as values.
It will return the count of each id as 1.

The 1st reducer will get these key value pairs with 1 count and reduce them
for each unique id type(key) and avg the score(values).

The 2nd mapper will get these transformed values and then for each device(key)
type it will assign it as poor or not poor(values).

The 2nd reducer will reduce the data to for each device type(key) to find
the poor-ratio(values).
'''

def map_first_pass(data_points):
    """
    :param data_points: list of input data
    :return: list of key value pairs with 1 count
    """
    return data_points[0], data_points[1], data_points[2], 1


def reduce_first_pass(dev_cnt_list):
    """
    :param dev_cnt_list: list of all values for each unique key
    :rtype : list of device type and average value for each key
    """
    _sum = 0
    for i in dev_cnt_list:
        _sum += int(i[1])
    return dev_cnt_list[0][0], _sum // len(dev_cnt_list)


def map_second_pass(dev_scores):
    """
    :param dev_scores: list of key value pais of device type and avg scores
    :return: list of device type and poor/not poor mapping
    """
    return dev_scores[0], 'Poor' if dev_scores[1] <= 50 else 'Not Poor'


def reduce_second_pass(poor_vals):
    """
    :param poor_vals: list of poor value for each device
    :return: float val poor-ratio for each device
    """
    return float(poor_vals.count('Poor')) / len(poor_vals)


def main(data):

    # First Map Pass
    first_map_output = map(map_first_pass, data)

    # Grouping and Shuffling with key as Device ID
    id_count_map = {}
    for data_point in first_map_output:
        if data_point[0] not in id_count_map:
            id_count_map[data_point[0]] = []
            id_count_map[data_point[0]].append((data_point[1], data_point[2], data_point[3]))
        else:
            id_count_map[data_point[0]].append((data_point[1], data_point[2], data_point[3]))

    # First Reduce Pass
    device_avg_list = []
    for _id in id_count_map:
        device_avg_list.append(reduce_first_pass(id_count_map[_id]))

    # Second Map Pass
    dev_poor_list = map(map_second_pass, device_avg_list)

    # Grouping and Shuffling with key as Device Type
    dev_poor_map = {}
    for dev in dev_poor_list:
        if dev[0] not in dev_poor_map:
            dev_poor_map[dev[0]] = []
            dev_poor_map[dev[0]].append(dev[1])
        else:
            dev_poor_map[dev[0]].append(dev[1])

    # Second Reduce Pass
    for dev in dev_poor_map:
        dev_poor_map[dev] = reduce_second_pass(dev_poor_map[dev])

    # Final Answer
    sorted_ratio = sorted(dev_poor_map.items(), key=itemgetter(1), reverse=True)
    highest_poor_ratio = sorted_ratio[0][1]

    for ratio in sorted_ratio:
        if ratio[1] == highest_poor_ratio:
            print(ratio[0])

if __name__ == '__main__':

    input_file = argv[1]
    input_data = []

    with open(input_file) as f:
        for line in f:
            line = line.strip('\n')
            _id, device, score = line.split(',')
            input_data.append([_id, device, score])

    main(input_data)

