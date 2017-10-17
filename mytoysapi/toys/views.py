from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from util import SMSSender
import phonenumbers
import random
# Create your views here.
class RegView(View):
	def post(self, request):
		short_num = request.POST['number']
		long_num = short_num
		if not num.startsWith('+'):
			long_num = '+86'.short_num
		if not phonenumbers.is_valid_number(phonenumbers.parse(long_num)):
			return JsonResponse({'valid': False})
		else:
			digit = random.randint(100000, 999999)
			SMSSender.send_sms(long_num, digit)
			return JsonResponse({'valid': True})	
		pass
	pass
pass


SMSSender.send_sms('13681977706',random.randint(100000, 999999)) 