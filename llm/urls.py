from django.urls import path
from .views import upload_file,edite_file,delete_file


app_name="llm"

urlpatterns = [
    path("",upload_file, name="upload_file"),
    path("<int:id>/",edite_file, name="edite_file"),
    path("delete/<int:id>/",delete_file,name="delete_file"),
    # path("update/<int:id>/",update_blog,name="update_blog"),
    
]
