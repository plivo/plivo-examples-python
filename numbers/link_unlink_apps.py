import plivo

client = plivo.RestClient("YOUR_AUTH_ID","YOUR_AUTH_TOKEN")

# Link an application to a number
response = client.numbers.update(
    number="12143010249",
    app_id="16638156474000802", )
print(response)

# Sample successful output
# {
#   "message": "changed",
#   "api_id": "5a9fcb68-582d-11e1-86da-6ff39efcb949"
# }

# Unlink an application from an number
response = client.numbers.update(
    number="12143010249", # Number that has to be unlikned to an application
    app_id=""  # No app_id value to be passed.
)
print(response)

# Sample successful output
# {
#   "message": "changed",
#   "api_id": "5a9fcb68-582d-11e1-86da-6ff39efcb949"
# }
