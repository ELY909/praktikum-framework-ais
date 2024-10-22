from django.urls import path, include
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from . import views
from .views import StudentsViewSet

# Create router and register viewset
router = DefaultRouter()
router.register(r'students', StudentsViewSet, basename='students')

urlpatterns = [ 
    path('about/', views.about, name='about'),
    path('', views.homepage, name='homepage'),
    path('student/', views.student_index, name='student_index'),
    path('student/create/', views.student_create, name='student_create'),
    path('student/update/<int:student_id>/', views.student_update, name='student_update'),
    path('student/delete/<int:student_id>/', views.student_delete, name='student_delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/admin/', views.dashboard_admin, name='dashboard_admin'),
    path('dashboard/student/', views.dashboard_student, name='dashboard_student'),
    path('dashboard/teacher/', views.dashboard_teacher, name='dashboard_teacher'),
    
    # API URLs
    path('api/', include(router.urls)),
]