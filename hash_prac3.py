poem_dict = {}
with open('data/poem.txt','r') as infile:
    for line in infile:
        # line = line.strip()
        tokens = line.split()
        for token in tokens:
            if token in poem_dict:
                poem_dict[token] += 1
            else:
                poem_dict[token] = 1
                
print(poem_dict)
        