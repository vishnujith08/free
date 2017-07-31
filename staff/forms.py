from django import forms


from staff.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','password']
class EditForm(forms.ModelForm):
    email = forms.CharField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name','address','image','mobile','password2','password1')

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        print "password1",password1
        print "password2",password2

        if password1 and password2 and password1 == password2:
            return password2
        else:
            raise forms.ValidationError('password_mismatch')

    def save(self, commit=True):
        form = super(EditForm, self).save(commit=False)
        if commit:
            form.set_password(self.cleaned_data["password2"])
            form.save()

        return form

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(max_length=18, widget=forms.PasswordInput)
    email = forms.CharField(required=True)
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password','password1','address','image','mobile']

    def clean_password1(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')
        if not password1:
            raise forms.ValidationError("You must confirm your password")
        if password != password1:
            raise forms.ValidationError("Your passwords do not match")
        return password1

    def save(self, commit=True):
        form = super(RegistrationForm, self).save(commit=False)
        if commit:
            form.set_password(self.cleaned_data["password"])
            form.save()
        return form