import collections
import itertools
import operator
import random


# Math = M
# Computer = C
# Industrial Engineering = IE
# Electrical Engineering = EE

expert_List1 = [("Ali", "Ahmadi", "M", 35), ("Sima", "Sadri", "C", 39),
                ("Ahmad", "Moradi", "M", 30), ("Ftemeh", "Majd", "C", 29),
                ("Sara", "Biglar", "IE", 27), ("Reza", "Rahnama", "EE", 45)]

expert_List2 = [("Mina", "Gohari", "EE", 40), ("Iman", "Shams", "M", 26),
                ("Farzad", "Yeganeh", "M", 41), ("Ali", "Imani", "C", 33),
                ("Aref", "Alameh", "M", 32), ("Narges", "Sohrabi", "C", 35)]


# union_list = [expert_List1,expert_List2]
# union_list = list(itertools.chain.from_iterable(union_list))
union_list = collections.ChainMap(expert_List1,expert_List2)

union_list = sorted(union_list,key=operator.itemgetter(2))

chosen_people = list(itertools.islice(union_list,7,12))

grouping = list(itertools.combinations(chosen_people,3))

[print(i) for i in random.choice(grouping)]