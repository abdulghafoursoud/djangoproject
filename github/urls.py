from django.urls import path
from crsapp import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns =[
    #login
    path("login/",TokenObtainPairView.as_view()),
    path("token/refresh/",TokenObtainPairView.as_view()),


#urls for student
    path('Student/',views.manage_Student),
    path('Student/<int:id>/',views.manage_Student),

#urls for Admin
    path('Admin/',views.manage_Admin),
    path('Admin/<int:id>/',views.manage_Admin),

#urls for instructor
    path('Instructor/',views.manage_Instructor),
    path('Instructor/<int:id>/',views.manage_Instructor),

#urls for project
    path('Project/',views.manage_Project),
    path('Project/<int:id>/',views.manage_Project),


]