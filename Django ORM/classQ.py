"""
class Q need for 'and/or/not' operators
| - or
& - and
~ - not

from django.db.models import Q

objects = Table.objects.filter(pk__gt=10, cat_id__in=[1,2,3]) - simple
objects = Table.objects.filter(Q(pk__gt=10) | Q(cat_id__in=[1,2,3])) - with or
objects = Table.objects.filter(~Q(pk__gt=10) & Q(cat_id__in=[1,2,3]))

"""