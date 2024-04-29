from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from django.shortcuts import get_object_or_404, reverse

choices = Category.objects.all().values_list("name_1", "name_1")

choice_list = []
for item in choices:
    choice_list.append(item)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "slug",
            "author",
            "category",
            "featured_image",
            "content",
        )

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "slug": forms.TextInput(attrs={"class": "form-control", "hidden": "hidden", "value": "0"}),
            "author": forms.TextInput(
             attrs={"class": "form-control", "hidden": "hidden", "value": "0",}
            ),
            "category": forms.Select(
                choices=choice_list, attrs={"class": "form-control"}
            ),
            "featured_image": forms.ClearableFileInput
            (attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": "form-control"}),
        }
        # Remove labels for hidden fields
        for field_name, widget in widgets.items():
            if "hidden" in widget.attrs and widget.attrs["hidden"] == "hidden":
                widget.attrs["label"] = ""

        title = forms.CharField(widget=widgets["title"])
        slug = forms.CharField(widget=widgets["slug"])
        author = forms.CharField(widget=widgets["author"])
        category = forms.ChoiceField(choices=choice_list, widget=widgets["category"])
        featured_image = forms.FileField(widget=widgets["featured_image"])
        content = forms.CharField(widget=widgets["content"])
        