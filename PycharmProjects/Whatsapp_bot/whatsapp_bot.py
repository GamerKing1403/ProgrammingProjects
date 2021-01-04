import os
from twilio.rest import Client

client = Client()
from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:+918420596897'
client.messages.create("Ahoy World",
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
