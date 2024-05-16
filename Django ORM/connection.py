# from django.db import connection
# from django.http import JsonResponse
# from .models import YourModel  # Import your model
#
# def your_view(request):
#     # Your logic here
#     queryset = YourModel.objects.all()  # Or any other queryset
#     count = queryset.count()
#
#     # Get the count of database queries executed
#     query_count = len(connection.queries)
#
#     # Prepare response data
#     response_data = {
#         'count': count,
#         'query_count': query_count,
#         'queries': [query['sql'] for query in connection.queries]
#     }
#
#     return JsonResponse(response_data)
