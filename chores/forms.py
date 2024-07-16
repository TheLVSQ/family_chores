from django import forms
from .models import FamilyMember, Chore


class FamilyMemberForm(forms.ModelForm):
    class Meta:
        model = FamilyMember
        fields = ["member_type", "first_name", "last_name", "age", "email", "password"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "age": "Age",
            "username": "Username",
            "email": "Email Address",
            "password": "Password",
        }
        help_texts = {
            "first_name": "Enter the first name of the family member",
            "last_name": "Enter the last name of the family member",
            "username": "Create a username",
            "age": "Enter the age of the family member",
            "email": "Enter the email address of the family member (Only for Adults)",
            "password": "Create a password",
        }

    def __init__(self, *args, **kwargs):
        super(FamilyMemberForm, self).__init__(*args, **kwargs)
        self.fields["email"].required = False

    def clean(self):
        cleaned_data = super().clean()
        member_type = cleaned_data.get("member_type")
        email = cleaned_data.get("email")

        if member_type == FamilyMember.ADULT and not email:
            self.add_error("email", "Email is required for adults")

        return cleaned_data


class ChoreForm(forms.ModelForm):
    class Meta:
        model = Chore
        fields = [
            "title",
            "frequency",
            "assignee",
            "due_date",
            "priority",
            "category",
            "tags",
            "estimated_time",
            "description",
            "completed",
        ]
        widgets = {
            "due_date": forms.DateInput(attrs={"type": "date"}),
            "completed": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }
        help_texts = {
            "tags": "Enter tags separated by commas",
            "estimated_time": "Enter the estimated time in minutes",
        }
        labels = {
            "title": "Chore Name",
            "frequency": "How often should this chore be done?",
            "assignee": "Assigned to:",
            "due_date": "Due Date",
            "estimated_time": "Estimated Time (minutes)",
            "completed": "Completed",
        }
