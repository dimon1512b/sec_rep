"""
from django.db.models import *

min_value = Article.objects.aggregate(Min('field'))
max_value = Article.objects.aggregate(Max('field'))

>> min_max_value = Article.objects.aggregate(Min('field'), Max('field'))
{'field_min': 'value', 'field_max': value}

>> max_value = Article.objects.aggregate(max_value=Max('field'))
{'max_value': 'value'}

Можна використовувати разом з фільтрами

max_value = Article.objects.filter(pk=value).aggregate(max_value=Max('field'))

Group by

Можна виконати агрегації для груп данних. Наприклад:

Article.objects.values('cat').annotate(Count('id'))
#  SELECT count(id) FROM article GROUP BY cat

Наступний запрос поверне кількість записів по кожній категорії

Тому що метод values працює дещо інакше якщо він у поєднанні з методом
annotate

coll_orders = CollectionOrder.objects.filter(
    Q(closed_at__isnull=False) &
    (Q(collection_order_template__waste_stream__disposer=relation.id) |
    Q(collection_order_template__waste_stream__sender=relation.id))
)

coll_groups = coll_orders.values(
    'collection_order_template__collection_waste_group_id',
).annotate(
    group_id=F('collection_order_template__collection_waste_group_id'),
    count=Count('collection_order_template__collection_waste_group_id')
).values_list('group_id', flat=True)

"""