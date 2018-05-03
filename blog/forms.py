from django import forms
from .models import Post


class PlatForm(forms.ModelsForm):


	class Meta:
		model = Post
		fields = ('title', 'text',)