from sys import argv
from operator import itemgetter


def map_first_pass(data_points):
    """

    :param data_points:
    :return:
    """
    return data_points[0], data_points[1], data_points[2], 1


def reduce_first_pass(dev_cnt_list):
    """

    :param dev_cnt_list:
    :rtype : object
    """
    _sum = 0
    for i in dev_cnt_list:
        _sum += int(i[1])
    return dev_cnt_list[0][0], _sum // len(dev_cnt_list)


def map_second_pass(dev_scores):
    """

    :param dev_scores:
    :return:
    """
    return dev_scores[0], 'Poor' if dev_scores[1] <= 50 else 'Not Poor'


def reduce_second_pass(poor_vals):
    """

    :param poor_vals:
    :return:
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

