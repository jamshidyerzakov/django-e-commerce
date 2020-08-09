# E-commerce in Django

API for a online shop where orders will be delivered with the help of drivers or
customers will take their orders from sellers.

# About project

Soon!

# Setup

Create virtual environment and clone this repository:

<code>>>> python -m venv .</code>

<code>>>> cd Scripts\activate</code>

<code>>>> git clone https://github.com/jamshidyerzakov/django-e-commerce.git</code>

Install all packages from <strong> requirements.txt. </strong> :

<code>>>> pip install -r requirements.py</code>

Make migrations and migrate:

<code>>>> cd django-e-commerce</code>

<code>>>> python manage.py makemigrations</code>

<code>>>> python manage.py migrate</code>

Run the server and check the documentation for further actions:

<code>>>> python manage.py runserver</code>

Go to http://127.0.0.1:8000/swagger/ in order to check the docs


## Authentication

First step — user registration from site (not social auth).

- **POST** request to url - _`.../auth/users/`_.

  Body of a request:

  ```
  username: <str> (required) (*)
  email: <str> (required)
  password: <str> (required)
  type: <str> (required) (**)
  ```

  **(\*)** —

  **(\*\*)** —

  Successful response: 200 OK

  ```
  id: <int> (unique id number of user)
  username: <str>
  email: <str>
  type: <str>
  ```

  **Note:**

Second step — user activation.

- **POST** request to url — `.../auth/users/activate/`:

  Body of a request:

  ```
  uid: <str> (required)
  token: <str> (required)
  ```

  Successful response : 204 No content

Third step — user login.

- **POST** request to url — `.../auth/token/login/`:

  Body of a request:

  ```
  username: <str> (required)
  password: <str> (required)
  ```

  Successful response : 200 OK

  ```
  access_token: <str> (*)
  ```

  **(\*)** —

  `Authorization : Token <access_token>`

Fourth step — user check:

- **GET** request to url — `.../auth/users/me/`

  Headers:

  `Authorization : Token <access_token>`

  Successful response: 200 OK

  ```
  id: <int>
  username: <str>
  email: <str>
  type: <str>  (user type)
  ```

Fifth step — user logout:

- **POST** request to url — `.../auth/token/logout/`

  Headers:

  `Authorization : Token <access_token>`

  Successful response: 204 No content

**Password reset and other such stuff will be added soon.**

# Social Authentication (Oauth2)

## Google

First step — user registration.

- GET request to url — `https://accounts.google.com/o/oauth2/v2/auth`.

  Get request parameters:

  ```
  response_type: code
  client_id: your client id
  scope: openid email profile
  redirect_uri: redirect_uri
  login_hint: jsmith@example.com
  nonce: 0394852-3190485-2490358
  hd: your domain
  ```

  **(\*)** —

Second step — getting access token from google.

- **POST** request to — `https://oauth2.googleapis.com/token`

  Parameters:

  ```
  code: <str>
  client_id: client_id
  client_secret: client_secret
  redirect_uri: redirect_uri
  grant_type: authorization_code
  ```

  **Make sure you changed `code` parameter.**

  Successful response: 200 OK (example)

  ```
  {
  "access_token": "ya29.a0AfH6SMDiBvcgxUHUOVkhIJcBtTckRoSX4kbSVnc6NIwAaxRZJJ7nJBZReI_tLT2RmPRYG8V2s2Mhc2pas_At28LU1zd75QjjHp8yS9y1brMDOoPVboxPjBKhoAfCuXFbtBmwMlKRSp88oON2zCgNwR1lU1T4Sb0RgIA",
  "expires_in": 3599,
  "scope": "openid https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile",
  "token_type": "Bearer",
  "id_token": "eyJhbGciOiJSUzI1NiIsImtpZCI6Ijc0NGY2MGU5ZmI1MTVhMmEwMWMxMWViZWIyMjg3MTI4NjA1NDA3MTEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI5MDk5MzUzOTc1MTUtNjQ2cmtrM3RyZHM4dWtycGo3MzczMTVkZGlydGtvZDkuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI5MDk5MzUzOTc1MTUtNjQ2cmtrM3RyZHM4dWtycGo3MzczMTVkZGlydGtvZDkuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMDc0NDI4MTgyNjgxNTY2NjU3MjAiLCJlbWFpbCI6ImphbWlrNjMzMzMzM0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6IlQzSWpOUklPdENMSUJFTFVVOEJPUkEiLCJub25jZSI6IjAzOTQ4NTItMzE5MDQ4NS0yNDkwMzU4IiwibmFtZSI6ImlsbHUxb18wbiIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS0vQU9oMTRHamNrNzlxZkR1bWxCQ1pURjVRNEh5c0FMajVPemgzUUdXYWtlZ2I9czk2LWMiLCJnaXZlbl9uYW1lIjoiaWxsdTFvXzBuIiwibG9jYWxlIjoiZW4iLCJpYXQiOjE1OTY4Nzg3MzksImV4cCI6MTU5Njg4MjMzOX0.GbyiRHI9jBMCGUoNz8dWc0ecQ8KxHeRC-cfs9vTLfOhVXmz_tPVEI3VyTbRaEpEkb_kop8LrO5jsRm8DahvjSC3_Rodfr5EwVdGSeJdINKcuCMC87MqekO5xT1n69wqF3K_DYK5UvDybJPYat9sTuuMd9RJj8PkHlnfmw--NglZKTmHiTGvszQ35aEG2r9QNnG-c6yDoUqgaFlj6fxs2Ea-E-kJZEs_doevoQw8RnIGYjS_HmAFRrVv4tmrJ9f9g-9DveRjd-__FOUoLgrExkQe1vsLkDeMSjcKMKhnhgWS7MvDE_XiKyh9wN_jt2ZfapyocyMark8XJNMB5Cb1zVQ"
  }
  ```

  **Note:**

Third step — Getting user info

- **GET** request to — `https://openidconnect.googleapis.com/v1/userinfo`

  Headers:
  `Authorization : Bearer access_token`

  Successful response: 200 Ok (example)

  ```
  {
   "sub": "1074428182681566657",
   "name": "illu1o_0n",
   "given_name": "illu1o_0n",
   "picture": "https://lh3.googleusercontent.com/a-/AOh14Gjck79qfDumlBCZTF5Q4HysALj5Ozh3QGWakegb",
   "email": "jamik6333333@gmail.com",
   "email_verified": true,
   "locale": "en"
  }
  ```

  Fifth step — getting all endpoints (optional, if you need more info)

- _GET_ request to url — `https://accounts.google.com/.well-known/openid-configuration`

  Headers:
  `Authorization : Bearer access_token`

  Successful response: 200 Ok (example)

  ```
  {
  "issuer": "https://accounts.google.com",
  "authorization_endpoint": "https://accounts.google.com/o/oauth2/v2/auth",
  "device_authorization_endpoint": "https://oauth2.googleapis.com/device/code",
  "token_endpoint": "https://oauth2.googleapis.com/token",
  "userinfo_endpoint": "https://openidconnect.googleapis.com/v1/userinfo",
  "revocation_endpoint": "https://oauth2.googleapis.com/revoke",
  "jwks_uri": "https://www.googleapis.com/oauth2/v3/certs",
  "response_types_supported": [
      "code",
      "token",
      "id_token",
      "code token",
      "code id_token",
      "token id_token",
      "code token id_token",
      "none"
  ],
  "subject_types_supported": [
      "public"
  ],
  "id_token_signing_alg_values_supported": [
      "RS256"
  ],
  "scopes_supported": [
      "openid",
      "email",
      "profile"
  ],
  "token_endpoint_auth_methods_supported": [
      "client_secret_post",
      "client_secret_basic"
  ],
  "claims_supported": [
      "aud",
      "email",
      "email_verified",
      "exp",
      "family_name",
      "given_name",
      "iat",
      "iss",
      "locale",
      "name",
      "picture",
      "sub"
  ],
  "code_challenge_methods_supported": [
      "plain",
      "S256"
  ],
  "grant_types_supported": [
      "authorization_code",
      "refresh_token",
      "urn:ietf:params:oauth:grant-type:device_code",
      "urn:ietf:params:oauth:grant-type:jwt-bearer"
  ]
  }
  ```

Sixth step — convert google access_token and save token to db.

- **POST** request to url — `.../auth/convert-token`

  Body of the request:

  ```
  grant_type: convert_token
  client_id: client_id of the app (create in admin-panel)
  backend: google-oauth2
  token: <google `access_token`>
  type: <str>  (user_type) (*)
  ```

  **(\*)** —

  Successful response: 200 OK (example)

  ```
  {
  "access_token": "IrfWekJyLDBVlSojk4cpBoz6aJgUwE",
  "expires_in": 36000,
  "token_type": "Bearer",
  "scope": "read write",
  "refresh_token": "u2Mpj39uiZeAg14O3kNtPI9gPeesWm"
  }
  ```

  **Note:**

  `Authorization: Bearer 'access_token'`

Seventh step — checking user.

- **GET** request to url — `/auth/users/me/`.

  Headers:

  `Authorization: Bearer 'access_token'`

## Facebook

soon

## Mail.ru

Soon

# Usage of filters

Soon

# Contributions

Pull requests are welcome! (develop branch)

# Contributions

Pull requests are welcome!
