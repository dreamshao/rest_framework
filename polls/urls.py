from django.urls import path
from .apiviews import PollList,PollDetail,ChoiceList,CreateVote,UserCreate
from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet,ChoiceList,CreateVote,UserCreate,LoginView
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('polls',PollViewSet,basename='polis')
urlpatterns=[
     path("polls/",PollList.as_view(),name="polls_list"),
     path("polls/<int:pk>/",PollDetail.as_view(),name="polls_detail"),
     path("choices/",ChoiceList.as_view(),name="choice_list"),
     path("vote/",CreateVote.as_view(),name="create_vote"),
     path("polls/<int:pk>/choices/",ChoiceList.as_view(),name="choice_list"),
     path("polls/<int:pk>/choices/<int:choices_pk>/vote/",CreateVote.as_view(),name="create_vote"),
     path("users/",UserCreate.as_view(),name="user_create"),
     path("login/",views.obtain_auth_token,name="login")
]

urlpatterns += router.urls