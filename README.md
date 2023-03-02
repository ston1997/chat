Django DRF Messaging App

This is a messaging app built using Django and Django REST Framework (DRF).

SETUP:

1. Clone the repository
2. Create a virtual environment and activate it
3. pip install -r requirements.txt # Install the dependencies using
4. python manage.py migrate # Create a database by running
5. python manage.py createsuperuser # Create a superuser by running
6. python manage.py runserver # Run the development server using

API Endpoints:

- /api/token/ - POST request to obtain a JWT token
- /api/token/refresh/ - POST request to refresh an existing JWT token
- /api/threads/ - GET request to retrieve a list of all threads or POST request to create a new thread
- /api/threads/<int:thread_id>/ - GET request to retrieve a specific thread or PUT request to update a specific thread
- /api/threads/<int:thread_id>/messages/ - GET request to retrieve all messages in a specific thread or POST request to create a new message in a specific thread
- /api/threads/<int:thread_id>/messages/<int:message_id>/ - GET request to retrieve a specific message in a specific thread, PUT request to update a specific message in a specific thread, or DELETE request to delete a specific message in a specific thread
- /api/messages/ - GET request to retrieve a list of all messages or POST request to create a new message
- /api/messages/<int:message_id>/ - GET request to retrieve a specific message, PUT request to update a specific message, or DELETE request to delete a specific message
- /api/unread-count/ - GET request to retrieve the number of unread messages for the current user
- /api/mark-as-read/ - POST request to mark one or more messages as read

AUTHENTICATION:

JWT authentication is used to authenticate users. To obtain a JWT token, send a POST request to /api/token/ with a username and password in the request body. The response will include an access token and a refresh token. The access token must be included in the Authorization header of subsequent requests to protected endpoints in the format Bearer <access_token>. To refresh an existing token, send a POST request to /api/token/refresh/ with a refresh token in the request body.

LIMITATIONS:

The app currently only supports two users per thread.
The app does not include real-time messaging capabilities. Users must manually refresh the page to see new messages.
The app does not include any file attachment capabilities.