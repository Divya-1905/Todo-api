from.models import Todo
queryset1= Todo.objects.all()
for x in queryset1:
           print(x)