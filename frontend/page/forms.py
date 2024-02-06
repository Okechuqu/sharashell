from django import forms
from backend.authuser.models.students import Student


class StudentRegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Student
        exclude = ['username']
        widgets = {
            'fullName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Phone Number', 'required': True}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': True}),
            'confirm_password': forms.PasswordInput(attrs={'class': 'form-control', 'required': True}),
            'dob': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'occupation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Occupation'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your State of Origin'}),
            'careerPath': forms.Select(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': '2',  'placeholder': 'Your Address'}),
        }

    def clean(self):
        cleaned_data = super(StudentRegisterForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password:
            if len(password) < 8:  
                self.add_error('password', "Must be at least 8 characters")
            if password != confirm_password:
                self.add_error('confirm_password', "Password does not match")
        else:
            raise forms.ValidationError(
                "Both password and confirm password fields are required.")

        return cleaned_data

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        # Convert the date to Django date format
        if dob:
            self.cleaned_data['dob'] = dob.strftime('%Y-%m-%d')
        return self.cleaned_data['dob']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
