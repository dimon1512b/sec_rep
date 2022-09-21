"""
Лукапи пишуться через field__lookup

objs = Table.objects.filter(field__gte=10)
objs = Table.objects.filter(field__contains='keyword')

Popular lookups

contains - same as sql LIKE %%
icontains - same as sql LIKE %% not depends of register
in - working with iterable objects and QuerySets
gt
gte
lt
lte 
"""