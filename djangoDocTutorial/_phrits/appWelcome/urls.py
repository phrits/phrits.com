from django.urls import path

from . import views


"""
'index' is also returned for '' in the project urls.py.
"""
urlpatterns = [
    path('', views.index, name='index'),
    
# *****************************************************************************

    # ex: /appWelcome/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /appWelcome/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /appWelcome/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]