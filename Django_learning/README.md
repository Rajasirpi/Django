# Django

This project Rest API have scripts for creation on APIs with validation using model serializers and also has view for CRUD Operations.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

 pip intsall django
 pip install djangorestframework

### Development Guidelines

Procedure:

1. After installation, created a rest_api project and a myapi app.
2. created a model named restaurant with required fields and resgistered it in admin.py.
3. Then created a serializer with proper validators using regular expressions.  
4. With that serializers, created class based views for list, create, edit, delete operations and then views are mapped  in urls.py.
