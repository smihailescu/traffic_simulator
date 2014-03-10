#keeping track of elements moving in a list
a, b, c, d, e, f, g = [object() for i in range(7)]
lst = [a, b, c, d, e, f, g]

objid_to_idx = {id(obj): idx for idx, obj in enumerate(lst)} # <---
# {
#     id(a): 0,
#     id(b): 1,
#     ...
#     id(g): 6,
# }

[objid_to_idx[id(obj)] for obj in lst]
[0, 1, 2, 3, 4, 5, 6]

lst = [a, d, b, c, e, f, g]
[objid_to_idx[id(obj)] for obj in lst]
[0, 3, 1, 2, 4, 5, 6]

lst = [a, d, b, a, c, e, e, f, g]
[objid_to_idx[id(obj)] for obj in lst]
[0, 3, 1, 0, 2, 4, 4, 5, 6]