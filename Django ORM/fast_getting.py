"""
Залежно від сортування

Article.objects.filter(cat=c).order_by(field).first()
Article.objects.filter(cat=c).last()

Не залежно від сортування

Article.objects.filter(cat=c).latest('datetime_field')
Article.objects.filter(cat=c).earliest('datetime_field')

Також запрос буде швидше відпрацьовувати якщо робити виборку не всіх полів, а
лише необхідних:

obj = Article.objects.values('title', 'cat_id').filter(cat=c)
obj = Article.objects.values('title', 'cat__name').filter(cat=c)

Отримання наступного або попереднього об'єкта відносно данного об'єкта

obj = Article.objects.filter(cat=c).order_by(field).first()
next_obj = obj.get_next_by_field()
previous_obj = obj.get_previous_by_field()

"""