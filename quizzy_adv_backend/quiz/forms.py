from django import forms
from django.forms.widgets import RadioSelect, Textarea
from django.contrib.auth.models import User
from quiz.models import QuizUser


class QuestionForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(QuestionForm, self).__init__(*args, **kwargs)
        choice_list = [x for x in question.get_answers_list()]
        self.fields["answers"] = forms.ChoiceField(choices=choice_list,
                                                   widget=RadioSelect)


class EssayForm(forms.Form):
    def __init__(self, question, *args, **kwargs):
        super(EssayForm, self).__init__(*args, **kwargs)
        self.fields["answers"] = forms.CharField(
            widget=Textarea(attrs={'style': 'width:100%'}))

class UserForm(forms.ModelForm):
	username = forms.CharField(help_text="Choose a username.")
	email = forms.CharField(help_text="Enter your email address.")
	password = forms.CharField(widget=forms.PasswordInput(),help_text="Enter your password.")
	class Meta:
		model = User
		fields = ('username','email','password')

class QuizUserForm(forms.ModelForm):
	picture = forms.ImageField(help_text="Select a profile picture to upload.",required=False)
	class Meta:
		model = QuizUser
		fields = ('picture',)
