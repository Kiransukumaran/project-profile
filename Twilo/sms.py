from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC74064c6679bbed6c5e57a5d21a47ea57"
# Your Auth Token from twilio.com/console
auth_token  = "4c8cc0a9165fe4f1c7d5efc8cfcc7a04"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="9567464915", 
   # from_="9567464915",
    body="Hello from Python!")

print(message.sid)
