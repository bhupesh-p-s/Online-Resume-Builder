from django import forms
from .models import Post
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from crispy_forms.layout import Column
from crispy_forms.layout import Row


# class SkillWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput(),
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','','','','','',''])

# class SkillsField(forms.MultiValueField):
# 	widget=SkillWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),
# 			forms.CharField(),
# 			forms.CharField(),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			forms.CharField(required=False),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]} {data_list[3]} {data_list[4]} {data_list[5]} {data_list[6]}'


# class ExpWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput()#,
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','',''])

# class ExpField(forms.MultiValueField):
# 	widget=ExpWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),#validators can be added
# 			forms.CharField(),
# 			forms.CharField(),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]}'

# class EduWidget(forms.MultiWidget):
# 	def __init__(self,attrs=None):
# 		super().__init__([
# 			forms.TextInput(),
# 			forms.TextInput(),
# 			forms.TextInput()#,
# 		],attrs)

# 	def decompress(self,value):
# 		if value:
# 			return value.split(' ')
# 		return(['','',''])

# class EduField(forms.MultiValueField):
# 	widget=EduWidget
# 	def __init__(self,*args,**kwargs):
# 		fields=(forms.CharField(),#validators can be added
# 			forms.CharField(),
# 			forms.CharField(),
# 			)
# 		super().__init__(fields,*args,**kwargs)

# 	def compress(self,data_list):
# 		return f'{data_list[0]} {data_list[1]} {data_list[2]}'


class ContactForm(forms.ModelForm):
    name=forms.CharField()#required=False
    email=forms.EmailField(label='E-Mail')
    field=forms.CharField()
    mobile=forms.CharField(max_length=10)
    address=forms.CharField()
    skills_1=forms.CharField()
    skills_2=forms.CharField()
    skills_3=forms.CharField(required=False)
    skills_4=forms.CharField(required=False)

    experience_1_title=forms.CharField()
    experience_1_dur=forms.CharField()
    experience_1_desc=forms.CharField()

    experience_2_title=forms.CharField(required=False)
    experience_2_dur=forms.CharField(required=False)
    experience_2_desc=forms.CharField(required=False)

    education_1=forms.CharField()
    education_1_dur=forms.CharField()
    education1_score=forms.CharField()

    education_2=forms.CharField()
    education_2_dur=forms.CharField()
    education2_score=forms.CharField()


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.helper=FormHelper
        self.helper.form_class = ' container justify-content-center '
        # self.helper.label_class = ''
        # self.helper.field_class = 'col-md-6 col-xs-9'
        self.helper.form_method="post"
        self.helper.layout=Layout(
            Row(
                Column('name', css_class='form-group col-md-5  mb-10'),
                Column('email', css_class='form-group col-md-7 mb-10'),
                Column('field', css_class='form-group col-md-7 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('mobile', css_class='form-group col-md-5  mb-10'),
                Column('address', css_class='form-group col-md-7 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('skills_1', css_class='form-group col-md-6  mb-10'),
                Column('skills_2', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('skills_3', css_class='form-group col-md-6  mb-10'),
                Column('skills_4', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
            Row(
                Column('experience_1_title', css_class='form-group col-md-7  mb-10'),
                Column('experience_1_dur', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
            'experience_1_desc',
            Row(
                Column('experience_2_title', css_class='form-group col-md-7  mb-10'),
                Column('experience_2_dur', css_class='form-group col-md-5 mb-10'),
                css_class='form-row  center'
            ),
            'experience_2_desc',
            'education_1',
            Row(
                Column('education_1_dur', css_class='form-group col-md-6 mb-10'),
                Column('education1_score', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
            'education_2',
            Row(
                Column('education_2_dur', css_class='form-group col-md-6  mb-10'),
                Column('education2_score', css_class='form-group col-md-6 mb-10'),
                css_class='form-row  center'
            ),
        
            Submit('submit','Submit',css_class="btn-success")
            )
    
    class Meta:
        model = Post
        fields =['name','email','field','mobile','address','skills_1','skills_2','skills_3','skills_4','experience_1_title','experience_1_dur','experience_1_desc','experience_2_title','experience_2_dur','experience_2_desc','education_1','education_1_dur','education1_score','education_2','education_2_dur','education2_score']
        labels = {'name':"Name",'email':"Email",'field':"Field",'mobile':"Mobile",'address':"Address",'skills_1':"Skills1",'skills_2':"Skills2",'skills_3':"Skills3",'skills_4':"Skills4",'experience_1_title':"Experience1",'experience_1_dur':"Experience1dur",'experience_1_desc':"Experience1desc",'experience_2_title':"Experience2",'experience_2_dur':"Experience2dur",'experience_2_desc':"Experience2desc",'education_1':"Education1",'education_1_dur':"Education1dur",'education1_score':"Education1score",'education_2':"Education2",'education_2_dur':"Education2dur",'education2_score':"Education2score"}