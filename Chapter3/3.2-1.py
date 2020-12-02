# -*- coding: utf-8 -*-
# @Time : 2020/12/2 14:49
# @Function :

if __name__ == "__main__":
    chile_rank = {'ghost': 1, 'habanero': 2, 'cayenne': 3}
    rank_dict = {rank: name for name, rank in chile_rank.items()}
    chile_len_set = {len(name) for name in rank_dict.values()}
    chile_len_list = [len(name) for name in rank_dict.values()]
    print(rank_dict)
    print(chile_len_set)
    print(chile_len_list)
