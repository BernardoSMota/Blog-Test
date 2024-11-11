from twilio.rest import Client
from django.core.cache import cache
from decouple import config


def TFA(code):
    account_sid = config('TWILIO_ACCOUNT_SID')
    auth_token = config('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    print('aaa')
    message = client.messages.create(
    from_='whatsapp:+14155238886',
    content_sid='HX229f5a04fd0510ce1b071852155d3e75',
    content_variables='{"1":' + f'"{str(code)}"' + '}',
    to=config('TWILIO_TO_NUMBER'),
    )
    
    return message


