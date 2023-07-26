# Combo Finder Program 
# PRactical Use : Its based on Selection Program problem and is used practically by E commerce websites to make a good combination of 
# products for people to buy.
import random as rp

prod_details = {'p1': 10, 'p2': 15, 'p3': 20, 'p4': 25, 'p5': 30, 'p6': 35, 'p7': 50,
            'p8': 40, 'p9': 55, 'p10': 60, 'p11': 65, 'p12': 75, 'p13': 70,
            'p14': 45}

min = 290
max = 310
result = set()  
iterations = 1000    

def combinations(iterations, product_list, lb, ub):
    for int in range(iterations):
        combo_size = rp.randint(2, len(product_list) - 1)
        combo_list = rp.sample(list(product_list.keys()), combo_size)
        combo_list.sort()
        combo_sum = sum([product_list[i] for i in combo_list])
        
        if lb <= combo_sum <= ub:
            result.add(tuple(combo_list))

combinations(iterations, prod_details, min, max)

for r in result:
    print(r)

print("\nTotal Combo Stes are:", len(result), "\n")