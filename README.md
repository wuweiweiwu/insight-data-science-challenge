# insight_data_science_challenge
This is the solution to the Insight Data Science Challenge implemented in python 3

##task

Our task is to represent the 'Paymo' friend network in a way that is easy to and fast to see the relationship between users. If one user pays another user then that establishes them as 'friends'. The different features is simply testing if users are within specified friend "levels" of each other.

The first feature of the coding challenge is to test if two users have ever made transactions with each other and print 'trusted' if they have or print 'unverified' if not. Simply put, they are within 1 level of each other

The second feature of the coding challenge is to test if two users have ever made transactions with a mutual user or 'friend of a friend' and print 'trusted' if they have or print 'unverified' if not. Simply put, they are within 2 levels of each other

The third feature of the coding challenge is to test if two users are within 4 levels of each other and print 'trusted' if they have or print 'unverified' if not

We are given two input files: `batch_payment.txt` which is used to construct the social network and `stream_payment.txt` which is read line by line to see if the transaction will print 'trusted' or 'unverified' when it is analyzed. We will print the results for each feature in the specified output files

##solution

My solution is based on representing the friend network as a  graph with each node being one user and each node has a direct path to another node if they are 'friends'

I represented the graph using an adjacency list using python dictionaries and sets. All transactions from `batch_payment.txt` are used to construct this initial graph

I then implemented an iterative breadth first search algorithm to find two nodes and how many degrees/levels separate them. It also takes in a `level` parameter that specifies how many levels to search

For each feature, we can then use the breadth first search algorithm and specify a specific level to search. For example: feature one would specify `level=1` and feature two would specify `level=2` and feature three would specify `level=4`

##additional features

Since I implemented the social network graph using an adjacency list, there was no use for edges. However, edges in the graph are useful to represent each transaction. Even though the 'friend' relationship in the graph is undirected, the transactions are directed from one user to another. Thus, I created a `Edge` class to represent a transaction and stored all the transactions in the `Graph` class as a dictionary with a tuple of the source and destination node as the keys Ex: `(src_node,des_node)` and a list of `Edge` elements as the values representing transactions

I also implemented some functions in the `Graph` class that mimics functionality from Venmo such as find transactions between two users, find outgoing transactions, and find incoming transactions

##running digital wallet

I use a python dict to implement the adjacency list where the key is a `Node` and the value is a `Set` of nodes. So the neighbors for a node can be access in time proportional to the degree of the node or __O(n)__ where __n__ is # of neighbors. The space complexity of the adjacency list is also __O(n)__. My implementation of the breadth first search limits how many degrees from a node it will search. The maximum level that it will search is 4. Thus it will operate in __O(n)__ for sparse graphs but it will operate in __O(n^2)__ for dense graphs where users make transactions with a lot of other users.

## run programs

__Digital Wallet__ is run using the __run.sh__ Bash script:

    ./run.sh

The results will be available in the __paymo_output__ directory

## tests

Tests are in the __insight_testsuite__ directory. To run them:

    cd insight_testsuite
    ./run_tests.sh
