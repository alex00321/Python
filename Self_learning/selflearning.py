# sample_str = "today is sunday"
# i = []

# updated_str = sample_str.split(" ")
# for item in updated_str:
#     if len(item)>3:
#         i.append(item)

# print(i)
d = {"mike":10,"lucky":5,"bob":30}

updated_d = map(sorted(d.keys()))
print(updated_d)