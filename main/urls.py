from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('all-news',views.all_news,name='all-news'),
    path('about',views.about,name='about'),
    path('detail/<int:id>',views.detail,name='detail'),
    path('all-category',views.all_category,name='all-category'),
    path('category/<int:id>',views.category,name='category'),
    path('learn',views.learn,name='learn'),
    path('guides',views.guide_category,name='guides'),
    path('jobs',views.jobs,name='jobs'),
    path('events',views.events,name='events'),
    path('press',views.press,name='press'),
    path('mine',views.mine,name='mine'),
    #path('user',views.app_user,name='user'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)