from django.contrib import admin
from django.urls import path
from employee.views import(
    emp,
    emp_show,
    emp_update,
    emp_delete,
    loop,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('emp', emp, name='emp'),
    path('show/<int:page>', emp_show, name='show_name'),
    path('update/<int:id>/<int:page>', emp_update, name='update'),
    path('delete/<int:id>/<int:page>', emp_delete, name='delete'),
    path('loop', loop, name='loop'),
]
