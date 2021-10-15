from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views, user_views

urlpatterns = [
    url(r'^$', views.index, name ="index"),
    # teacher
    # url(r"^create-teacher$", views.CreateTeacher.as_view(), name="create_teacher"),
    # url(r"^list-teacher$", views.ListTeacher.as_view(), name="list_teacher"),
    # url(r"^update-teacher/(?P<pk>[0-9]+)$", views.UpdateTeacher.as_view(), name="update_teacher"),
    # url(r"^delete-teacher/(?P<pk>[0-9]+)$", views.DeleteTeacher.as_view(), name="delete_teacher"),
    # course
    # url(r"^create-course$", views.CreateCourse.as_view(), name="create_course"),
    # url(r"^list-course$", views.ListCourse.as_view(), name="list_course"),
    # url(r"^update-course/(?P<pk>[0-9]+)$", views.UpdateCourse.as_view(), name="update_course"),
    # url(r"^delete-course/(?P<pk>[0-9]+)$", views.DeleteCourse.as_view(), name="delete_course"),
    # document
    # url(r"^create-document$", views.CreateDocument.as_view(), name="create_document"),
    # url(r"^list-document$", views.ListDocument.as_view(), name="list_document"),
    # url(r"^update-document/(?P<pk>[0-9]+)$", views.UpdateDocument.as_view(), name="update_document"),
    # url(r"^delete-document/(?P<pk>[0-9]+)$", views.DeleteDocument.as_view(), name="delete_document"),
    # # news
    # url(r"^create-news$", views.CreateNews.as_view(), name="create_newst"),
    # url(r"^list-news$", views.ListNews.as_view(), name="list_news"),
    # url(r"^update-news/(?P<pk>[0-9]+)$", views.UpdateNews.as_view(), name="update_news"),
    # url(r"^delete-news/(?P<pk>[0-9]+)$", views.DeleteNews.as_view(), name="delete_news"),
    
    # # user
    # url(r"^register$",user_views.register_user, name="register_user"),
	url(r"^login$",user_views.login_user, name="login_user"),
	url(r"^logout$",auth_views.LogoutView.as_view(next_page="/"), name="logout_user"),
	
    # url(r"^signup-course$",views.Signup_Course.as_view(), name="signup_course"),
    url(r"^signup-course/(?P<course_id>[0-9]+)$",views.RegisterCourse, name="signup_course"),
    url(r"^document-detail/(?P<document_id>[0-9]+)$",views.DocumentDetail, name="document_detail"),

    url(r"^course$",views.Courses, name="course"),
    url(r"^documents$",views.Documents, name="documents"),
    url(r"^about$",views.About, name="about"),
    url(r"^contact$",views.Contact, name="contact"),
    url(r"^news$",views.New, name="news"),
    url(r"^news-detail/(?P<news_id>[0-9]+)$",views.NewDetail, name="news-detail"),


]