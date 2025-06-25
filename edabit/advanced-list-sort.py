# available at: https://edabit.com/challenge/6vSZmN66xhMRDX8YT

def advanced_sort(sequence):

    '''given a list of items, groups equivalent items in maintaining order of appearence
    and returns a list of sublist clusters'''
    
    clustered_sequence = []

  # create clusters of matching items, maintaining order of precedence
    for item in sequence:
        if item not in clustered_sequence:
            clustered_sequence.append(item)
        else:
            clustered_sequence.insert(clustered_sequence.index(item), item)

    clustered_sequence.append('dummy')
    incumbent_item = clustered_sequence[0]
    count = 0
    sorted_sequence = []

  # organise into sublists
    for item in clustered_sequence:
        if incumbent_item == item:
            count += 1
        else:
            sorted_sequence.append([incumbent_item for _ in range(count)])
            count = 1
            incumbent_item = item

    return sorted_sequence

assert advanced_sort([1,2,1,2]) == [[1,1],[2,2]]
assert advanced_sort([2,1,2,1]) == [[2,2],[1,1]]
assert advanced_sort([3,2,1,3,2,1]) == [[3,3],[2,2],[1,1]]
assert advanced_sort([5,5,4,3,4,4]) == [[5,5],[4,4,4],[3]]
assert advanced_sort([80,80,4,60,60,3]) ==[[80,80],[4],[60,60],[3]]
assert advanced_sort(['c','c','b','c','b',1,1]) == [['c','c','c'],['b','b'],[1,1]]
assert advanced_sort([1234, 1235, 1234, 1235, 1236, 1235]) == [[1234, 1234],[1235, 1235, 1235],[1236]]
assert advanced_sort(['1234', '1235', '1234', '1235', '1236', '1235']) == [['1234', '1234'],['1235', '1235', '1235'],['1236']]
