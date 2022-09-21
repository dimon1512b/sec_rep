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

Настпний запрос поверне кількість записів по кожній категорії

Тому що метод values працює дещо інакше якщо він у поєднанні з методом
annotate
"""