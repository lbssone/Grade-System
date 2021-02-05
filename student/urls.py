from django.urls import path

from .views import StudentList, StudentDetail, StudentCreate, StudentUpdate, StudentDelete, StudentsGrades, \
    StudentsRank, SubjectScores, GradeCreate, GradeUpdate, GradeDelete, searchAutocomplete

app_name = "student"

urlpatterns = [
    path('', StudentList.as_view(), name='list'),
    path('<int:pk>', StudentDetail.as_view(), name='detail'),
    path('create', StudentCreate.as_view(), name='create'),
    path('<int:pk>/update', StudentUpdate.as_view(), name='update'),
    path('<int:pk>/delete', StudentDelete.as_view(), name='delete'),
    path('<int:pk>/grade/create', GradeCreate.as_view(), name='create_grade'),
    path('<int:studentId>/grade/<int:pk>/update', GradeUpdate.as_view(), name='update_grade'),
    path('<int:studentId>/grade/<int:pk>/delete', GradeDelete.as_view(), name='delete_grade'),
    path('grades', StudentsGrades.as_view(), name='grades'),
    path('rank', StudentsRank.as_view(), name='rank'),
    path('subjects', SubjectScores.as_view(), name='subjects'),
    path('autoComplete', searchAutocomplete, name='autoComplete')
]