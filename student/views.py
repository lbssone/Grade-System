from django.shortcuts import render, reverse, redirect, get_object_or_404
from django.db.models import Q, Value
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.http import JsonResponse
from django.db.models.functions import Concat
from django.core.paginator import Paginator
from student.models import Student, Grade
from student.HelperFunction import *
from .forms import CUStudentForm, CUGradeForm
from student.Exceptions import GradeExistedError


class StudentList(ListView):
    model = Student
    template_name = "student/StudentList.html"
    context_object_name = "students"
    paginate_by = 5

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.GET.get("name")
        if name:
            result = searchStudent(name)
            if result:
                return result
            else:
                return []
        else:
            return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        context["name"] = name
        return context


class StudentDetail(DetailView):
    model = Student
    template_name = "student/StudentDetail.html"
    context_object_name = "student"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["grades"] = self.object.getGrades()
        context["paginator"] = Paginator(context["grades"], 5)
        return context


class StudentCreate(CreateView):
    model = Student
    form_class = CUStudentForm
    context_object_name = "form"
    template_name = "student/Form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Add a Student"
        return context


class StudentUpdate(UpdateView):
    model = Student
    form_class = CUStudentForm
    context_object_name = "form"
    template_name = "student/Form.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Update {self.object.fullName}'s information"
        return context


class StudentDelete(DeleteView):
    model = Student
    success_url = reverse_lazy("student:list")


class GradeCreate(View):
    def get(self, request, pk):
        form = CUGradeForm()
        student = get_object_or_404(Student, pk=pk)
        title = f"Add Grade for {student.fullName}"
        return render(request, "student/Form.html", {"form": form, "title": title})

    def post(self, request, pk):
        form = CUGradeForm(request.POST)
        student = get_object_or_404(Student, pk=pk)
        title = f"Add Grade for {student.fullName}"
        if form.is_valid():
            testNo, chinese, english, math = form.cleaned_data.values()
            try:
                grade, _ = student.addGrade(testNo, chinese, english, math)
                return redirect(grade)
            except GradeExistedError as e:
                errorMessage = str(e)
                return render(request, "student/Form.html", {"form": form, "title": title, "errorMessage": errorMessage})
        return render(request, "student/Form.html", {"form": form, "title": title})


class GradeUpdate(UpdateView):
    model = Grade
    form_class = CUGradeForm
    template_name = "student/Form.html"
    context_object_name = "form"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = f"Update Test {self.object.testNo} of {self.object.student.fullName}"
        return context


class GradeDelete(DeleteView):
    model = Grade
    def get_success_url(self):
        return reverse('student:detail', kwargs={"pk": self.object.student.pk})

    # def post(self, request, pk, testNo):
    #     student = get_object_or_404(Student, pk=pk)
    #     student.deleteGrade(testNo)
    #     return redirect('student:detail', pk=pk)


class StudentsGrades(TemplateView):
    template_name = "student/StudentsGrades.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testNumbers'] = getAllTestNumbers()
        context['grades'] = Grade.objects.all()
        return context


class StudentsRank(TemplateView):
    template_name = "student/StudentsRank.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testsRank'] = getTestsRank()
        return context

class SubjectScores(TemplateView):
    template_name = "student/SubjectScores.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['subjectsScores'] = getSubjectsScores()
        return context

def searchAutocomplete(request):
    name = request.GET.get("q")
    if name:
        students = searchStudent(name)
        result = [student.fullName for student in students]
        return JsonResponse(result, safe=False)
    else:
        return JsonResponse([], safe=False)
