from heapq import heapify, heappush, heappop


# this class is used to store the data of every transaction in way thats easy to access
class Transaction:
    # each transaction has its ID, fee, weight, a list of its parents and a list of its direct children
    def __init__(self, id, fee,weight, parents,children):
        self.id = id
        self.fee = fee
        self.weight = weight
        self.parents = parents
        self.children = children


class Transaction_tracker:
    # here we get the input from the file, and store it in certain ways
    def __init__(self, input_array):
        # self.nodes is just an array of transaction objects.
        self.nodes = []
        # This dictionary maps the transaction id to the index it is in of the self.nodes
        self.dict = {}
        # this is a min heap that will be used when making a block. We will keep all the valid transactions
        # that is, transactions which can be added to the blockk considering the restraint that all their parents 
        # must already be in the block
        self.queue = []
        heapify(self.queue)
        # we pop the first line of input from the file because it was just the labels.
        input_array.pop(0)

        # here we store all the info on the transactions in the self.nodes array and the dictionary
        for index,transaction in enumerate(input_array):
            new_trans = Transaction(transaction[0],float(transaction[1]),float(transaction[2]),transaction[3],[])
            self.nodes.append(new_trans)
            self.dict[transaction[0]] = index
        for index,transaction in enumerate(self.nodes):
            for parent in transaction.parents:
                self.nodes[self.dict[parent]].children.append(transaction.id)
        # if a transaction has no parents, we add it to the priority queue, as it is a transaction that can be added
        for transaction in self.nodes:
            if transaction.parents == []:
                heappush(self.queue, [ -1*(transaction.fee/transaction.weight)  , transaction.id])
        
    # here we generate the block
    def generate_block(self):
        total_weight = 0
        block_list = []
    
        # we keep addding transactions till either there are no transactions or the ttal weight has been reached
        while total_weight<4000000 and len(self.queue)>0:
            # we get the transaction with the best fee:weight ratio from the heap.
            transaction = heappop(self.queue)
            index_present = self.dict[transaction[1]]
            transaction = self.nodes[index_present]
            if(total_weight + transaction.weight > 4000000):
                break
            # we add this transaction to the block, and add any of its children to the heap if they are now valid transactions
            block_list.append(transaction.id)
            total_weight += transaction.weight
            for children in transaction.children:
                child_index = self.dict[children]
                if transaction.id in self.nodes[child_index].parents:
                    self.nodes[child_index].parents.remove(transaction.id)
                if(len(self.nodes[child_index].parents) == 0):
                    # we use -1*(fee/weight) because this is really a min heap, but by multiplying with 
                    # -1 we emulate a max heap where we just put fee/weight
                    heappush(self.queue, [ -1*(self.nodes[child_index].fee/self.nodes[child_index].weight)  , self.nodes[child_index].id])

        return block_list
    
    def tell_weight(self, block):
        weight = 0
        for transaction in block:
            weight += self.nodes[self.dict[transaction]].weight
        return weight
    
    def tell_fee(self, block):
        fee = 0
        for transaction in block:
            fee += self.nodes[self.dict[transaction]].fee
        return fee
        
        
        

