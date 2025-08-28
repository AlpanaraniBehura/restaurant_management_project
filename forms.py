from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'cols': 40, 'placeholder': 'Enter your feedback here....'})
class ContactForm(forms.Form):
        name = forms.CharField(max_length=100, required=True)
        email = forms.EmailField(required=True) # Built-in email validation
        message = forms.CharField(widget=forms.Textarea, required=True)

        def clean_message(self):
            message = self.cleaned_data.get("message", "")
            if len(message.strip()) < 10: # ensure message is meanigful
               raise forms.ValidationError("Message must be at least 10 characters long.")
            return message 
               
