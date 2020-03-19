import sys

fileName = sys.argv[1]
minsup = float(sys.argv[2])
minconf = float(sys.argv[3])

file = open(fileName, mode='rt')
contents = file.readlines()

transactions = []
for content in contents:
    temp = content.split(',')
    temp[-1] = temp[-1][:-1]
    transactions.append(temp[1:])
size = len(transactions)


# Step 1: Find frequent 1-itemsets
c1 = {}
for i in range(0, 100):
    c1[str(i)] = 0

for transaction in transactions:
    for item in transaction:
        c1[item] += 1
c1_keys = list(c1.keys())

f1 = {}
for item in c1_keys:
    if c1[item] >= (minsup*size):
        f1[item] = c1[item]
f1_keys = list(f1.keys())


# Step 2: Generate candidate 2-itemsets
c2 = {}
for i in range(0, len(f1_keys)-1):
    for j in range(i+1, len(f1_keys)):
        c2[(f1_keys[i], f1_keys[j])] = 0
c2_keys = list(c2.keys())

for transaction in transactions:
    for i in range(0, len(transaction)-1):
        for j in range(i+1, len(transaction)):
            temp = (transaction[i], transaction[j])
            if temp in c2:
                c2[temp] += 1


# Step 3: Find frequent 2-itemsets
f2 = {}
for item in c2_keys:
    if c2[item] >= (minsup*size):
        f2[item] = c2[item]
f2_keys = list(f2.keys())


# Step 4: Generate association rules
print("Association rules found:")
for items in f2_keys:
    if f2[items] > (minconf*c1[items[0]]):
        print("{0} -> {1} (support = {2}, confidence = {3})".format(items[0], items[1], f2[items]/size, f2[items]/c1[items[0]]))
    if f2[items] > (minconf*c1[items[1]]):
        print("{0} -> {1} (support = {2}, confidence = {3})".format(items[1], items[0], f2[items]/size, f2[items]/c1[items[1]]))
