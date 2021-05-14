class Queue:
    """
    Class for Queue DS
    """
    def __init__(self, size=10):
        """
        Initializing 2 counters.
        i for pop, j for push

        :param size: size of queue (list) for initializing
        """
        self.i = 0
        self.j = 0
        self.size = size
        self.q = [str(False) for x in range(self.size)]

    def push(self, data):
        """
        Push elements to the queue (list)

        :param data: element to be pushed in queue
        :return:
        """
        # if insert push index less than the size of list
        # push the data and increment the push counter
        if self.j < self.size:
            self.q[self.j] = data
            print("Push: " + str(data))
            self.j += 1
        # if insert counter is greater than or equal to the size of list, size = 3, j=3 or j=4
        else:
            # if number of elements in the list should are less than size
            if (self.j - self.i) < self.size:
                # add next element at remainder of j % size
                nxt_idx = self.j % self.size
                self.q[nxt_idx] = data
                print("Push: " + str(data))
                self.j += 1
            else:
                print("Queue is full")

    def pop(self):
        """
        Pop elements from the queue (list)

        :return:
        """
        # if pop index is less than the size of list
        # pop the element at i index and i++
        if self.i < self.size:
            data = self.q[self.i]
            print("Pop: " + str(data))
            self.q[self.i] = str(False)
            self.i += 1
        # if pop counter is greater than equal to size, size=4, i=4 or i=5
        else:
            # if pop counter is less than push counter
            # means there are elements in the queue to pop
            if self.i < self.j:
                # get the remainder of i % size and pop
                nxt_idx = self.i % self.size
                data = self.q[nxt_idx]
                self.q[nxt_idx] = str(False)
                print("Pop: " + str(data))
                self.i += 1
            # No element to pop
            else:
                print("No element to Pop")

    def __repr__(self):
        return str(self.q)

