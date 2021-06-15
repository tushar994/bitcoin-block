# BITCOIN-BLOCK

## To run

run

```shell
python main.py
```

## Problem

The problem here is to construct a bitcoin block by selecting a set of transactions from the mempool. The fee is to be maximised.

## Approach taken

We notice that ideally, we would include transactions with high fee and low weight. This is because we want to maximise our fee, while not exceeding the weight limit. 

This is why I chose to implement a greedy solution, where everytime I add a transaction, I add the transaction with the highest fee:weight ratio from my set of valid transactions (*transactions that can be added to the block considering the parent restraint*).

To do this I used the following method.

Firstly I stored all the transactions such that each transaction had with it a list of all of it's parents that have not been added to the block and a list of it's direct children.

Second, I had a max heap in which I'd store all the transactions that can be added to the block considering the parent restraint. The max heap is sorted according to the fee:weight ratio of the transactions. Initially this heap would only contain transactions with no parents. 

To construct the block I did the following.

Pop a transaction from the max heap. This transaction would have the maximum fee:weight ratio of all the valid transactions.

Everytime I'd add a new transaction (*say it's called transaction A*) to the block, I'd go through all the children of A, and for each child I'd remove A from theie parent list. I'd then check these children to see if any of them now had zero parents. If so I'd add them to the max heap.

I'd keep doing the above till the weight limit is reached or until I have no transactions left.

## Ways to improve this

One thing this algorithm does not consider is the following possibility. It might be such that one transaction has a very low fee:weight ratio, and is a horrible transaction, but its children are all execellent transactions with very high fee:weight ratios. In the above algorithm, we might not end up including the parent or the children, simply becuase this one parent wasnt good enough. This is not good cause we might end up missing out some very good transactions. 

Some ways in which we could account for this would be-

- add some factor the fee:weight ratio of a transaction based on how good its children are.
- instead of only considering individual transactions in the above algorithm, start considering sets of transactions (of variable length) too, and if a set is really good, just add the whole set at once.

## Design

There are many ways the design of this code can be made better.

For one, we dont need an array of transactions and then a dictionary which maps the ID to the index in the array. We could just use a dictionary whos key is the ID and which maps to the Transaction object.

Similary we could structure the classes,methods and variables used in a more refined way.

## Originality

For parsing the input I took some part of the code given in the question README.

Besides that, I wrote the code and I came up with the algorithm all on my own.

