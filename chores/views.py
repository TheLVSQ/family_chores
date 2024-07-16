from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import FamilyMember, Chore
from .serializers import FamilyMemberSerializer, ChoreSerializer
from .forms import FamilyMemberForm, ChoreForm
from datetime import date

# Create your views here.


class FamilyMemberViewSet(viewsets.ModelViewSet):
    queryset = FamilyMember.objects.all()
    serializer_class = FamilyMemberSerializer


class ChoreViewSet(viewsets.ModelViewSet):
    queryset = Chore.objects.all()
    serializer_class = ChoreSerializer


def home(request):
    today = date.today()
    tasks_due_today = Chore.objects.filter(due_date=today)

    # Group tasks by assignee
    tasks_by_assignee = {}
    for chore in tasks_due_today:
        if chore.assignee in tasks_by_assignee:
            tasks_by_assignee[chore.assignee].append(chore)
        else:
            tasks_by_assignee[chore.assignee] = [chore]

    context = {
        "tasks_by_assignee": tasks_by_assignee,
    }
    return render(request, "chores/family_overview.html", context)


def add_family_member(request):
    if request.method == "POST":
        form = FamilyMemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = FamilyMemberForm()
    return render(request, "chores/add_family_member.html", {"form": form})


def add_chore(request):
    if request.method == "POST":
        form = ChoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ChoreForm()
    return render(request, "chores/add_chore.html", {"form": form})
