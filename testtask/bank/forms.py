from django import forms

class TransForm():
	email = forms.EmailField(required=True)
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')
	
	def save(self, commit=True):
		user = super(MyRegistrationForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.email = self.cleaned_data['password1']
		
		if commit:
			user.save()
			
		return user
