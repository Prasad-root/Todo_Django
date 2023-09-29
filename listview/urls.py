from django.urls import path
from . import views

urlpatterns = [
    path('',views.dashboard,name = 'dashboard'),
    path('changestatus/<int:changestate_id>',views.changeStatus,name = "changestate"),
    path('delete/<int:delete_id>',views.delete,name = "delete"),
    path("update/<int:_update_id>",views.update_load,name = "update"),
    path("addtask/",views.addTask,name = "addtask"),
    path("loadupdate/<int:update_id>",views.update_task,name = "updateTask")
]
