"""
Table.objects.filter(foreignkey_field__field=value)

Через __ можна указати поле вже в іншій таблиція до якої ми відносимось через
foreignkey

exem = Table.objects.get(pk=value)

exem.foreignkey_field == exemplar of related table with all fields

class RelatedManager:

c = Category.objects.get(pk=value)
c.article_set == RelatedManager
c.article_set.all() == Article.objects.filter(cat=c)

Щоб не прибігати до конструкції типу article_set, ми можемо указати
related_name

class Article(models.Model):
    cat = models.ForeignKey(
        'Category',
        on_delete=models.PROTECT,
        related_name='articles'
    )

c = Category.objects.get(pk=value)
c.articles.all() == Article.objects.filter(cat=c)

Можна фільтрувати мій об'єкт по полям foreignkey таблиці:

obj = Article.objects.filter(cat__field=value) -> Article object
obj = Article.objects.filter(cat__field__contains=value) -> Article object

"""