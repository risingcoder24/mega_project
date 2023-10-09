"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path


from . import admin_views, views

urlpatterns = [
    path("", views.login_page, name='login_page'),
    path("firebase-messaging-sw.js", views.showFirebaseJS, name='showFirebaseJS'),
    path("doLogin/", views.doLogin, name='user_login'),
    path("logout_user/", views.logout_user, name='user_logout'),
    path("admin/home/", admin_views.admin_home, name='admin_home'),
    path("staff/add", admin_views.add_staff, name='add_staff'),
    path("post/add", admin_views.add_post, name='add_post'),
    path("staff/manage/", admin_views.manage_staff, name='manage_staff'),


    path("admin_view_profile", admin_views.admin_view_profile,
         name='admin_view_profile'),
    path("check_email_availability", admin_views.check_email_availability,
         name="check_email_availability"),

    path("post/manage/", admin_views.manage_post, name='manage_post'),
    path("staff/edit/<int:staff_id>", admin_views.edit_staff, name='edit_staff'),
    path("staff/delete/<int:staff_id>",
         admin_views.delete_staff, name='delete_staff'),

    path("post/delete/<int:post_id>",
         admin_views.delete_post, name='delete_post'),

    path("post/edit/<int:post_id>",
         admin_views.edit_post, name='edit_post'),

    # Staff
    # path("staff/home/", staff_views.staff_home, name='staff_home'),

    # path("staff/view/profile/", staff_views.staff_view_profile,
    #      name='staff_view_profile'),
]

