###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    dict_name2weight = {}
    with open(filename, 'r') as f:
        for line in f:
            name, weight = line.split(',')
            dict_name2weight[name] = int(weight)
    return dict_name2weight


# Problem 2
def getWeight(item):
    return item[1]

def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # sort cows names based on its weight from large to small
    cows_list = [(name, weight) for name, weight in cows.items()]
    cows_list = sorted(cows_list, key=getWeight, reverse=True)
    transported = []
    curr_trip_weight = 0
    ret = [[]]
    while curr_trip_weight < limit and len(transported) < len(cows_list):
        # try each cow
        for name, weight in cows_list:
            # ignore transported and over-weight cows
            if name in transported or curr_trip_weight + weight > limit: pass
            else: 
                curr_trip_weight += weight
                ret[-1].append(name)
                transported.append(name)
        # have cows to transport but even the lightest cow does not fit in the last trip
        if len(transported) < len(cows_list) and name == cows_list[-1][0]:
            # create a new trip
            ret.append([])
            curr_trip_weight = 0
    return ret

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    cow_names = cows.keys()
    ret, num_trips = [], len(cow_names)
    partitions = get_partitions(cow_names)
    for partition in partitions:
        # find weight of each trip
        for trip in partition:
            curr_trip_weight = 0
            for name in trip:
                curr_trip_weight += cows[name]
                if curr_trip_weight > limit: break
            if curr_trip_weight > limit: break
        if curr_trip_weight > limit: pass
        # all trips are within limit by this way of partition
        elif len(partition) >= num_trips: pass
        # else: update transport method and current best number of trips
        else: ret, num_trips = partition, len(partition)
    return ret

# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cows = load_cows("ps1_cow_data.txt")
    limit = 10

    start = time.time()
    method_greedy = greedy_cow_transport(cows, limit)
    end = time.time()
    time_greedy = end - start

    start = time.time()
    method_brute = brute_force_cow_transport(cows, limit)
    end = time.time()
    time_brute = end - start

    print(f'Greedy algorithm (# of trips, time)= ({len(method_greedy)}, {time_greedy})')
    print(f'Brute algorithm (# of trips, time) = ({len(method_brute)}, {time_brute})')

# Problem 5

# 1. Greedy algorithm (# of trips, time)= (6, 1.9311904907226562e-05)
# Brute algorithm (# of trips, time) = (5, 0.3817720413208008)
# Greedy algorithm ran faster
# 2. No, greedy algorithm did not return the optimal result
# 3. Yes, the brute force algorithm returned the optimal result
# because it has gone through every possible may of transporting cows



if __name__ == "__main__":
    compare_cow_transport_algorithms()