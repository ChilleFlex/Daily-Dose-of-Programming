# country = []
# capital = []
# with open('data/country_capital.txt','r',encoding='utf-8') as infile:
#     content = infile.readlines()

# for rows in content:
#     #print(rows.strip())
    
#     temp = rows.strip()
#     a, b = temp.split('\t')
#     country.append(a)
#     capital.append(b)
# print(country,capital)

    
# div = []
# dist = []
# with open('data/div_dist.txt','r',encoding='utf-8') as infile:
#     content = infile.readlines()

# for rows in content:
#     #print(rows.strip())
    
#     temp = rows.strip()
#     a, b = temp.split('\t')
#     div.append(a)
#     dist.extend(b.split(', '))
# print(div,dist)

# upo = []
# with open('data/upozilla.txt','r',encoding='utf-8') as infile:
#     content = infile.readlines()

# for rows in content:
#     a = rows.strip()
#     upo.append(a)
# print(upo,len(upo))

# union = []
# with open('data/union_list.txt','r',encoding='utf-8') as infile:
#     content = infile.readlines()

# for rows in content:
#     #print(rows.strip())
    
#     temp = rows.strip()
#     a, b = temp.split('\t')
#     union.extend(b.split(', '))
# print(union, len(union))

# thana = []
# with open('data/thana.txt','r',encoding='utf-8') as infile:
#     content = infile.readlines()

# for rows in content:
#     a = rows.strip()
#     thana.append(a)
# print(thana,len(thana))

big_city = []
with open('data/big_city.txt','r',encoding='utf-8') as infile:
    content = infile.readlines()

for rows in content:
    a = rows.strip()
    big_city.append(a)
print(big_city,len(big_city))