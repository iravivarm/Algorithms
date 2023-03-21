price_list=[3,5,1,-3]

price_list.sort(reverse=True)
print(price_list)
min_cost=0
for price in range(len(price_list)):
    min_cost += (price+1) * price_list[price]
print(min_cost)