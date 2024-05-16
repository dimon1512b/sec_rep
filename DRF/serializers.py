"""
Серіалайзери потрібні щоб валідувати та конвертувати данні.
Найчастіший варіант конвертування це із джанго моделей у джейсон

Серіалізатори в основному побудовані на serializers.Serializer
Всі інші представляють собою лише додаткові автоматичні валідації
Наприклад

The ModelSerializer class provides a shortcut that lets you automatically
create a Serializer class with fields that correspond to the Model fields.

The ModelSerializer class is the same as a regular Serializer class, except that:

- It will automatically generate a set of fields for you, based on the model.
- It will automatically generate validators for the serializer, such as unique_together validators.
- It includes simple default implementations of .create() and .update().


"""