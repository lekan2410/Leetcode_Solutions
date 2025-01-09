strs = ["Jesus","eat","tea","tan","ate","nat","bat"]

listdict = defaultdict(list)

for str in strs:
    
    new_string = ''.join(sorted(str))
    
    listdict[new_string].append(str)

print(list(listdict.values()))
