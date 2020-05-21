# Simple Okta API Wrapper

### Requirements:

Set OKTA_DOMAIN and OKTA_API_TOKEN as environment variables

For macOS, edit ~/.bash_profile and reload terminal:
```
export OKTA_DOMAIN='your_domain.okta.com'
export OKTA_API_TOKEN='xxxxxxxxxxxxxxxxxxxxxxxxx'
```

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