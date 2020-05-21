# Simple Okta API Wrapper

### Requirements:

Set the following as environment variables:

OKTA_DOMAIN
OKTA_API_TOKEN

### Examples:

Get single user and pretty print:
```
import okta

print(okta.getUser('example.user', pretty_print=True))
```

Get all users and print:
```
import okta

users = okta.getUsers()
for user in users:
    firstName = user['profile']['firstName']
    lastName = user['profile']['lastName']
    email = user['profile']['email']
    print(f'{firstName}, {lastName}, {email}')
```

Update a users security question:
```
import okta

okta.updateUserSecurityQuestion('example.user', 'New security question', 'New answer')
```