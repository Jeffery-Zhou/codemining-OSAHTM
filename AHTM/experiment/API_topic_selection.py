# coding:utf-8
import random
import json

def produce_edges(n):
    edge_lst = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i <= j:
                temp_lst = []
                temp_lst.append(i)
                temp_lst.append(j)
                seed = random.randint(1, 10)
                if seed in [1]:
                    temp_lst.append(1)
                    temp_lst.append(0)
                    temp_lst.append(0)
                if seed in [2, 3]:
                    temp_lst.append(0)
                    temp_lst.append(1)
                    temp_lst.append(0)

                if seed in [4, 5, 6, 7]:
                    temp_lst.append(0)
                    temp_lst.append(2)
                    temp_lst.append(0)

                if seed in [8, 9, 10]:
                    temp_lst.append(0)
                    temp_lst.append(0)
                    temp_lst.append(1)
                print temp_lst

            edge_lst.append(temp_lst)
    return edge_lst

edge_lst =  produce_edges(8384)


with open('wordnet.json', 'w') as f:
    f.write(json.dumps(produce_edges(edge_lst)))
