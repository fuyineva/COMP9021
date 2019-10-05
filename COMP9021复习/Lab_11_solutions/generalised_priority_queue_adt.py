# Written by Eric Martin for COMP9021


'''
A max priority queue abstract data type to insert pairs of the form (datum, priority).
If a pair is inserted with a datum that already occurs in the priority queue, then
the priority is (possibly) changed to the (possibly) new value.
'''


class EmptyPriorityQueueError(Exception):
    def __init__(self, message):
        self.message = message


class PriorityQueue():
    min_capacity = 10

    def __init__(self, capacity = min_capacity):
        self.min_capacity = capacity
        self._data = [None] * capacity
        self._length = 0
        self._locations = {}
        
    def __len__(self):
        '''
        >>> len(PriorityQueue(100))
        0
        '''
        return self._length

    def is_empty(self):
        return self._length == 0

    def insert(self, element):
        '''
        >>> pq = PriorityQueue(4)
        >>> L = [('A', 13), ('B', 13), ('C', 4), ('D', 15), ('E', 9), ('F', 4), ('G', 5),\
                 ('H', 14), ('A', 4), ('B', 11), ('C', 15), ('D', 2), ('E', 17),\
                 ('A', 8), ('B', 14), ('C',12), ('D', 9), ('E', 5),\
                 ('A', 6), ('B', 16)\
                ]
        >>> for e in L: pq.insert(e); print(f'{pq._data[: len(pq) + 1]}    {len(pq._data)}')
        [None, ['A', 13]]    4
        [None, ['A', 13], ['B', 13]]    4
        [None, ['A', 13], ['B', 13], ['C', 4]]    4
        [None, ['D', 15], ['A', 13], ['C', 4], ['B', 13]]    8
        [None, ['D', 15], ['A', 13], ['C', 4], ['B', 13], ['E', 9]]    8
        [None, ['D', 15], ['A', 13], ['C', 4], ['B', 13], ['E', 9], ['F', 4]]    8
        [None, ['D', 15], ['A', 13], ['G', 5], ['B', 13], ['E', 9], ['F', 4], ['C', 4]]    8
        [None, ['D', 15], ['H', 14], ['G', 5], ['A', 13], ['E', 9], ['F', 4], ['C', 4], ['B', 13]]    16
        [None, ['D', 15], ['H', 14], ['G', 5], ['B', 13], ['E', 9], ['F', 4], ['C', 4], ['A', 4]]    16
        [None, ['D', 15], ['H', 14], ['G', 5], ['B', 11], ['E', 9], ['F', 4], ['C', 4], ['A', 4]]    16
        [None, ['D', 15], ['H', 14], ['C', 15], ['B', 11], ['E', 9], ['F', 4], ['G', 5], ['A', 4]]    16
        [None, ['C', 15], ['H', 14], ['G', 5], ['B', 11], ['E', 9], ['F', 4], ['D', 2], ['A', 4]]    16
        [None, ['E', 17], ['C', 15], ['G', 5], ['B', 11], ['H', 14], ['F', 4], ['D', 2], ['A', 4]]    16
        [None, ['E', 17], ['C', 15], ['G', 5], ['B', 11], ['H', 14], ['F', 4], ['D', 2], ['A', 8]]    16
        [None, ['E', 17], ['C', 15], ['G', 5], ['B', 14], ['H', 14], ['F', 4], ['D', 2], ['A', 8]]    16
        [None, ['E', 17], ['B', 14], ['G', 5], ['C', 12], ['H', 14], ['F', 4], ['D', 2], ['A', 8]]    16
        [None, ['E', 17], ['B', 14], ['D', 9], ['C', 12], ['H', 14], ['F', 4], ['G', 5], ['A', 8]]    16
        [None, ['B', 14], ['H', 14], ['D', 9], ['C', 12], ['E', 5], ['F', 4], ['G', 5], ['A', 8]]    16
        [None, ['B', 14], ['H', 14], ['D', 9], ['C', 12], ['E', 5], ['F', 4], ['G', 5], ['A', 6]]    16
        [None, ['B', 16], ['H', 14], ['D', 9], ['C', 12], ['E', 5], ['F', 4], ['G', 5], ['A', 6]]    16
        '''
        datum = element[0]
        priority = element[1]
        if datum in self._locations:
            self._change_priority(datum, priority)
            return
        if self._length + 1 == len(self._data):
            self._resize(2 * len(self._data))
        self._length += 1
        self._data[self._length] = [datum, priority]
        self._locations[datum] = self._length
        self._bubble_up(self._length)

    def delete(self):
        '''
        >>> pq = PriorityQueue(4)
        >>> L = [('A', 13), ('B', 13), ('C', 4), ('D', 15), ('E', 9), ('F', 4), ('G', 5),\
                 ('H', 14), ('A', 4), ('B', 11), ('C', 15), ('D', 2), ('E', 17),\
                 ('A', 8), ('B', 14), ('C',12), ('D', 9), ('E', 5),\
                 ('A', 6), ('B', 16)\
                ]
        >>> for e in L: pq.insert(e)
        >>> for _ in range(len(pq)):
        ...     print(f'{pq.delete():2} {pq._data[: len(pq) + 1]}    {len(pq._data)}')
        B  [None, ['H', 14], ['C', 12], ['D', 9], ['A', 6], ['E', 5], ['F', 4], ['G', 5]]    16
        H  [None, ['C', 12], ['A', 6], ['D', 9], ['G', 5], ['E', 5], ['F', 4]]    16
        C  [None, ['D', 9], ['A', 6], ['F', 4], ['G', 5], ['E', 5]]    16
        D  [None, ['A', 6], ['E', 5], ['F', 4], ['G', 5]]    8
        A  [None, ['G', 5], ['E', 5], ['F', 4]]    8
        G  [None, ['E', 5], ['F', 4]]    8
        E  [None, ['F', 4]]    8
        F  [None]    8
        >>> pq.delete()
        Traceback (most recent call last):
        ...
        EmptyPriorityQueueError: Cannot delete element from empty priority queue
        '''
        if self.is_empty():
            raise EmptyPriorityQueueError('Cannot delete element from empty priority queue')
        top_datum = self._data[1][0]
        del self._locations[top_datum]        
        self._data[1], self._data[self._length] = self._data[self._length], self._data[1]
        self._length -= 1
        if self.min_capacity <= self._length <= len(self._data) // 4:
            self._resize(len(self._data) // 2)
        self._bubble_down(1)
        return top_datum

    def _change_priority(self, datum, priority):
        i = self._locations[datum]
        if priority > self._data[i][1]:
            self._data[i][1] = priority
            self._bubble_up(i)
        elif priority < self._data[i][1]:
            self._data[i][1] = priority
            self._bubble_down(i)
        
    def _bubble_up(self, i):
        if i > 1 and self._data[i][1] > self._data[i // 2][1]:
            self._data[i // 2], self._data[i] = self._data[i], self._data[i // 2]
            self._locations[self._data[i // 2][0]] = i // 2
            self._locations[self._data[i][0]] = i
            self._bubble_up(i // 2)

    def _bubble_down(self, i):
        child = 2 * i
        if child < self._length and self._data[child + 1][1] > self._data[child][1]:
            child += 1
        if child <= self._length and self._data[child][1] > self._data[i][1]:
            self._data[child], self._data[i] = self._data[i], self._data[child]
            self._locations[self._data[child][0]] = child
            self._locations[self._data[i][0]] = i
            self._bubble_down(child)

    def _resize(self, new_size):
        self._data = list(self._data[ : self._length + 1]) + [None] * (new_size - self._length - 1)
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()    
   
            
