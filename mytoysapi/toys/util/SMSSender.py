#/usr/bin/python
#coding:utf-8
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid

REGION = "cn-hangzhou"
ACCESS_KEY_ID = "x"
ACCESS_KEY_SECRET = "x"
SMS_TEMPLATE_CODE = "SMS_105020035"
SMS_PARAM_KEY = "code"
SMS_SIGN_NAME = ""

acs_client = AcsClient(ACCESS_KEY_ID, ACCESS_KEY_SECRET, REGION)

def send_sms(num, code):
	smsRequest = SendSmsRequest.SendSmsRequest()
	smsRequest.set_TemplateCode(SMS_TEMPLATE_CODE)
	smsRequest.set_TemplateParam({SMS_PARAM_KEY: code})
	smsRequest.set_OutId(uuid.uuid1())
	smsRequest.set_SignName(SMS_SIGN_NAME);
	smsRequest.set_PhoneNumbers(num)
	smsResponse = acs_client.do_action_with_exception(smsRequest)
	print smsResponse
	pass


