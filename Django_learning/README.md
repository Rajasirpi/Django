# Django

This project Rest API have scripts for creation on APIs with validation using model serializers and also has view for CRUD Operations.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

 pip intsall django
 pip install djangorestframework

For DRF concepts reference use this Document link: https://teams.microsoft.com/l/file/AB1B1C49-218E-4540-93CB-9919F816B677?tenantId=171ad24c-3217-4669-8d94-b77826105594&fileType=docx&objectUrl=https%3A%2F%2Fkcubeconsultancy.sharepoint.com%2Fsites%2FkCubeFreshersTraining-RajasirpiTraining%2FShared%20Documents%2FRajasirpi%20Training%2FDjango%2FDRF%20concepts.docx&baseUrl=https%3A%2F%2Fkcubeconsultancy.sharepoint.com%2Fsites%2FkCubeFreshersTraining-RajasirpiTraining&serviceName=teams&threadId=19:4d485b9303484328a9a6e4dcb9f5a2da@thread.tacv2&groupId=ef8c7f18-a473-4a9f-ae28-28cb0ca70e38

### Development Guidelines

Procedure:

1. After installation, created a rest_api project and a myapi app.
2. created a model named restaurant with required fields and resgistered it in admin.py.
3. Then created a serializer with proper validators using regular expressions.  
4. With that serializers, created class based views for list, create, edit, delete operations and then views are mapped  in urls.py.