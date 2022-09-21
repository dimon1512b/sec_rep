"""
Table.objects.get(uniq_field=value) - один об'єкт

Table.objects.all() - квері сет. Iterable object

Table.objects.all()[:5] - не просто слайс як у списка, а цілий sql запрос

Table.objects.order_by('pk') - сортує по первинному ключу не залежно від того
як цей первинний ключ називається

Table.objects.order_by('-field') - зворотній порядок сортування по полю

Table.objects.all().reverse() - зворотній порядок дефолтного сортування

"""