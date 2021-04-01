from twilio.rest import Client
import config

client = Client(config.sid, config.auth_token)


message = client.messages.create(
    to="+17067161091",
    from_="+18588791597",
    body="This is a test message"
)
