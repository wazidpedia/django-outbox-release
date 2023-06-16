_a='address'
_Z='whatsapp'
_Y='is_external'
_X='is_visibled'
_W='order_menu'
_V='file_path_doc'
_U='designation'
_T='sub_title'
_S='location'
_R='email'
_Q='kind'
_P='description'
_O='embed'
_N='order_item'
_M='site_id'
_L='priority'
_K='is_header_text'
_J='icon'
_I='link'
_H='tags'
_G='categories'
_F='content'
_E='name'
_D='title'
_C='post'
_B='status'
_A='form-group col-md-12 mb-0'
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column,Layout,Row
from django import forms
from django.forms import ModelForm
from menu.models import Menu
from parler.forms import TranslatableModelForm
from core.models import *
from education.models import *
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
class TagsForm(TranslatableModelForm):
	class Meta:model=Tags;fields=[_E,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_E,css_class=_A),Column(_B,css_class=_A)))
class WhyUsForm(TranslatableModelForm):
	class Meta:model=WhyUs;fields=[_D,_J,_P,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_P,css_class=_A),Column(_J,css_class=_A),Column(_B,css_class=_A)))
class LogoForm(ModelForm):
	dim_w=forms.CharField(widget=forms.HiddenInput(),initial=300);dim_h=forms.CharField(widget=forms.HiddenInput(),initial=48);save_as_png=forms.CharField(widget=forms.HiddenInput(),initial=1)
	class Meta:model=Logo;fields=[_E]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_E,css_class=_A)))
class AnnouncementForm(TranslatableModelForm):
	dim_w=forms.CharField(widget=forms.HiddenInput(),initial=870);dim_h=forms.CharField(widget=forms.HiddenInput(),initial=500)
	class Meta:model=Announcement;fields=[_D,_F,_G,_H,_L,_B]
	def __init__(self,*args,**kwargs):
		site_id=kwargs.pop(_M);super().__init__(*(args),**kwargs)
		if site_id:self.fields[_H].queryset=Tags.objects.filter(site_id=site_id);self.fields[_G].queryset=Categories.objects.filter(site_id=site_id)
		self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_F,css_class=_A),Column(_G,css_class=_A),Column(_L,css_class=_A),Column(_H,css_class=_A),Column(_B,css_class=_A)))
class FasilitiesForm(TranslatableModelForm):
	dim_w=forms.CharField(widget=forms.HiddenInput(),initial=870);dim_h=forms.CharField(widget=forms.HiddenInput(),initial=500)
	class Meta:model=Fasilities;fields=[_D,_F,_N,_K,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_F,css_class=_A),Column(_K,css_class=_A),Column(_B,css_class=_A)))
class NewsForm(TranslatableModelForm):
	dim_w=forms.CharField(widget=forms.HiddenInput(),initial=870);dim_h=forms.CharField(widget=forms.HiddenInput(),initial=500)
	class Meta:model=News;fields=[_D,_F,_G,_H,_B]
	def __init__(self,*args,**kwargs):
		site_id=kwargs.pop(_M);super().__init__(*(args),**kwargs)
		if site_id:self.fields[_H].queryset=Tags.objects.filter(site_id=site_id);self.fields[_G].queryset=Categories.objects.filter(site_id=site_id)
		self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_F,css_class=_A),Column(_G,css_class=_A),Column(_H,css_class=_A),Column(_B,css_class=_A)))
class ArticleForm(TranslatableModelForm):
	dim_w=forms.CharField(widget=forms.HiddenInput(),initial=870);dim_h=forms.CharField(widget=forms.HiddenInput(),initial=500)
	class Meta:model=Article;fields=[_D,_F,_G,_H,_K,_B]
	def __init__(self,*args,**kwargs):
		site_id=kwargs.pop(_M);super().__init__(*(args),**kwargs)
		if site_id:self.fields[_H].queryset=Tags.objects.filter(site_id=site_id);self.fields[_G].queryset=Categories.objects.filter(site_id=site_id)
		self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_F,css_class=_A),Column(_G,css_class=_A),Column(_H,css_class=_A),Column(_B,css_class=_A)))
class EventsForm(TranslatableModelForm):
	dim_w=forms.CharField(widget=forms.HiddenInput(),initial=870);dim_h=forms.CharField(widget=forms.HiddenInput(),initial=500)
	class Meta:model=Events;fields=[_D,_S,'date','time',_F,_G,_H,_B]
	def __init__(self,*args,**kwargs):
		site_id=kwargs.pop(_M);super().__init__(*(args),**kwargs)
		if site_id:self.fields[_H].queryset=Tags.objects.filter(site_id=site_id);self.fields[_G].queryset=Categories.objects.filter(site_id=site_id)
		self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_S,css_class=_A),Column('date',css_class=_A),Column('time',css_class=_A),Column(_F,css_class=_A),Column(_G,css_class=_A),Column(_H,css_class=_A),Column(_B,css_class=_A)))
class SlideShowForm(TranslatableModelForm):
	dim_w=forms.CharField(widget=forms.HiddenInput(),initial=873);dim_h=forms.CharField(widget=forms.HiddenInput(),initial=424)
	class Meta:model=SlideShow;fields=[_D,_T,_F,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_T,css_class=_A),Column(_F,css_class=_A),Column(_B,css_class=_A)))
class DailyAlertForm(TranslatableModelForm):
	class Meta:model=DailyAlert;fields=['alert',_I,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column('alert',css_class=_A),Column(_I,css_class=_A),Column(_B,css_class=_A)))
class GreetingForm(TranslatableModelForm):
	dim_w=forms.CharField(widget=forms.HiddenInput(),initial=164);dim_h=forms.CharField(widget=forms.HiddenInput(),initial=201)
	class Meta:model=Greeting;fields=[_D,_E,_U,_F,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_E,css_class=_A),Column(_U,css_class=_A),Column(_F,css_class=_A),Column(_B,css_class=_A)))
class PagesForm(TranslatableModelForm):
	dim_w=forms.CharField(widget=forms.HiddenInput(),initial=870);dim_h=forms.CharField(widget=forms.HiddenInput(),initial=500)
	class Meta:model=Pages;fields=[_D,_F,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_F,css_class=_A),Column(_B,css_class=_A)))
class SocialMediaForm(ModelForm):
	class Meta:model=SocialMedia;fields=[_Q,_I,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_Q,css_class=_A),Column(_I,css_class=_A),Column(_B,css_class=_A)))
class HowItWorksForm(TranslatableModelForm):
	class Meta:model=HowItWorks;fields=[_D,_F,_J,_N,_K,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_F,css_class=_A),Column(_J,css_class=_A),Column(_N,css_class=_A),Column(_K,css_class=_A),Column(_B,css_class=_A)))
class PhotoGalleryForm(TranslatableModelForm):
	dim_w=forms.CharField(widget=forms.HiddenInput(),initial=1000);dim_h=forms.CharField(widget=forms.HiddenInput(),initial=496)
	class Meta:model=PhotoGallery;fields=[_D,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_B,css_class=_A)))
class VideoGalleryForm(TranslatableModelForm):
	class Meta:model=VideoGallery;fields=[_D,_O,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_O,css_class=_A),Column(_B,css_class=_A)))
class RelatedLinkForm(TranslatableModelForm):
	class Meta:model=RelatedLink;fields=[_E,_I,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_E,css_class=_A),Column(_I,css_class=_A),Column(_B,css_class=_A)))
class DocumentForm(TranslatableModelForm):
	class Meta:model=Document;fields=[_E,_F,_V,_G,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_E,css_class=_A),Column(_F,css_class=_A),Column(_V,css_class=_A),Column(_G,css_class=_A),Column(_B,css_class=_A)))
class MenuForm(TranslatableModelForm):
	class Meta:model=Menu;fields=[_E,_I,_W,_J,_X,_Y]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_E,css_class=_A),Column(_I,css_class=_A),Column(_W,css_class=_A),Column(_J,css_class=_A),Column(_X,css_class=_A),Column(_Y,css_class=_A)))
class AgencyForm(TranslatableModelForm):
	class Meta:model=Agency;fields=[_E,_R,'phone','fax',_Z,_a,'notes']
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_E,css_class=_A),Column(_R,css_class=_A),Column('phone',css_class=_A),Column('fax',css_class=_A),Column(_Z,css_class=_A),Column(_a,css_class=_A),Column('notes',css_class=_A)))
class CategoriesForm(TranslatableModelForm):
	class Meta:model=Categories;fields=[_E,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_E,css_class=_A),Column(_B,css_class=_A)))
class ProductForm(TranslatableModelForm):
	dim_w=forms.CharField(widget=forms.HiddenInput(),initial=870);dim_h=forms.CharField(widget=forms.HiddenInput(),initial=500)
	class Meta:model=Product;fields=[_E,_D,_F,_N,_K,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C
class TemplateOwnerForm(ModelForm):
	class Meta:model=TemplateOwner;fields=[_E]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_E,css_class=_A)))
class ModelListForm(ModelForm):
	class Meta:model=ModelList;fields=[_E,_P,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_E,css_class=_A)))
class ServiceForm(ModelForm):
	class Meta:model=Service;fields=['site',_Q,'agency','is_active','expired_date']
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_E,css_class=_A)))
class TemplateForm(ModelForm):
	class Meta:model=Template;fields=[_E,'rel_path','template_owner','is_frontend']
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_E,css_class=_A)))
class BannerForm(ModelForm):
	dim_w=forms.CharField(widget=forms.HiddenInput(),initial=267);dim_h=forms.CharField(widget=forms.HiddenInput(),initial=417)
	class Meta:model=Banner;fields=[_L,_I]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_L,css_class=_A),Column(_I,css_class=_A)))
class LocationForm(TranslatableModelForm):
	class Meta:model=Location;fields=[_D,_O,_B]
	def __init__(self,*args,**kwargs):super().__init__(*(args),**kwargs);self.helper=FormHelper();self.helper.form_method=_C;self.helper.layout=Layout(Row(Column(_D,css_class=_A),Column(_O,css_class=_A),Column(_B,css_class=_A)))
class CustomUserCreationForm(UserCreationForm):
	is_accept_terms=forms.BooleanField(required=True)
	class Meta(UserCreationForm.Meta):model=get_user_model();fields=_R,_E,'is_accept_terms'