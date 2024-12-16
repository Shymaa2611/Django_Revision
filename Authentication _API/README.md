# Django Rest Framework Authentication 

## Session Authentication
This is the default authentication class used by DRF. It relies on Django's built-in session authentication, where the client sends a session ID to the server for authentication.
## Endpoint 
- Signup (http://127.0.0.1:8000/signup/)

POST METHOD 
{
    "username":"<your-username>",
    "email":"<your-email>"
    "password":"<your-password>"
}
- Login  (http://127.0.0.1:8000/login/)

POST METHOD 
{
    "username":"<your-username>",
    "password":"<your-password>"
}

- Rest Password  (http://127.0.0.1:8000/password-reset/)

POST METHOD
{
    "email":"<your-email>"
}

- Complete Rest Password  (http://127.0.0.1:8000/complete-reset/token/user_id/)

POST METHOD
{
    "new_password":"<your-new-password>"
}

- Logout (http://127.0.0.1:8000/logout/)

## Basic Authentication
Basic authentication sends the username and password in the HTTP request headers. It’s simple and works across many different platforms.

## Token Authentication
Token-based authentication involves the client sending an authorization token (usually a JWT or a custom token) in the request header. It's commonly used for mobile or single-page applications .

## Endpoint 
- Signup (http://127.0.0.1:8000/signup/)

POST METHOD 
{
    "username":"<your-username>",
    "email":"<your-email>"
    "password":"<your-password>"
}
- Login  (http://127.0.0.1:8000/login/)
Header 
key                   value
Authorization         <token>

POST METHOD 
{
    "username":"<your-username>",
    "password":"<your-password>"
}

- Rest Password  (http://127.0.0.1:8000/password-reset/)

POST METHOD
{
    "email":"<your-email>"
}

- Complete Rest Password  (http://127.0.0.1:8000/complete-reset/token/user_id/)

POST METHOD
{
    "new_password":"<your-new-password>"
}

- Logout (http://127.0.0.1:8000/logout/)
Header
key                                value
Authorization                     Token<token>


## Jwt Authenication
JWT is widely used for stateless authentication in web and mobile applications. It allows secure transmission of information as a JSON object.

## Endpoint 
- Signup (http://127.0.0.1:8000/signup/)

POST METHOD 
{
    "username":"<your-username>",
    "email":"<your-email>"
    "password":"<your-password>"
}
- Login  (http://127.0.0.1:8000/login/)

POST METHOD 
{
    "username":"<your-username>",
    "password":"<your-password>"
}

- Rest Password  (http://127.0.0.1:8000/password-reset/)

POST METHOD
{
    "email":"<your-email>"
}

- Complete Rest Password  (http://127.0.0.1:8000/complete-reset/token/user_id/)

POST METHOD
{
    "new_password":"<your-new-password>"
}

- Logout (http://127.0.0.1:8000/logout/)
{
"refresh_token":"your-refresh_token"
}

## OAuth2 Authentication
OAuth2 is a widely adopted protocol that allows third-party applications to access a user's resources without exposing their credentials. It is highly flexible and secure.

## Endpoint 
- Signup (http://127.0.0.1:8000/signup/)

POST METHOD 
{
    "username":"<your-username>",
    "email":"<your-email>"
    "password":"<your-password>"
}
- Login  (http://127.0.0.1:8000/login/)

POST METHOD 
{
    "username":"<your-username>",
    "password":"<your-password>"
}

- Rest Password  (http://127.0.0.1:8000/password-reset/)

POST METHOD
{
    "email":"<your-email>"
}

- Complete Rest Password  (http://127.0.0.1:8000/complete-reset/token/user_id/)

POST METHOD
{
    "new_password":"<your-new-password>"
}

- Logout (http://127.0.0.1:8000/logout/)
{
"refresh_token":"your-refresh_token"
}

