"""food_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from food_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # this is data_dodel home page url path
    path('', views.index, name='home'),
    # this is LearningActiviies page url path
    path('list/', views.list, name='list'),
    # this is Detail page url path
    path('detail/', views.detail, name='detail', ),
    path('detail/<int:item_id>/', views.detail,name='detail2'),
    
        
    # 4 path under LearningActivites
    path('info/', views.info, name='info'),
    path('strategies/', views.strategies, name='strategies'),
    path('donation/', views.donation, name='donation'),
    path('tracker/', views.problem, name='problem'),
      
    # this is data_dodel page url path
    path('data_model/', views.data_model, name='data_model'),  
]