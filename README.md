## Medical
- Medical is a web application that enables you to get quality treament by easily getting acccess to medication and being able to verify a drug, medical officer, get pharmacies near you.

## Basic Information.
- This application has three levels of users, a Patient, a Pharmacist and Government official.Each having a separate set of permissions.All users sign up expect the Patient, then its only a Government official who can verify a Pharmacist.

- As a user of the application, you will be able to do the following:
   - Verify a drug.
   - Rate a pharmacy.
   - verify a pharmacist.
   
- As a Goverment Official you can be able to do the following:
   - Add drugs to available drugs.
   - Approve an application of one to be a pharmacist.
   - Verify a pharmacy after background checks and submissions of basic information.
   
- As a Pharmacist you will be able to do the following:
   - Add drugs to your store, this is only possible by buying from the list of available drugs which will be provided after a      Governement official approves drugs to be in the list of available drugs.
 
  
### Core Features
- A user can verify a drug.
- A user can verify a medical personell.
- A user can verify a chemist.
- A government official can add a drug to a list of available drugs.It is this drugs that a Pharmacist can then add to his store.
- A pharmacist can apply to be recognized in the application.


## Prerequisite

- [Python3.6](https://www.python.org/downloads/release/python-365/)
- [Virtual Environment](https://virtualenv.pypa.io/en/stable/installation/)
- [Django](https://www.djangoproject.com/)
- [Django Rest Framework](https://www.django-rest-framework.org/)

## Technologies & Languages

**Project management (Agile)** [https://www.pivotaltracker.com](url)

**Version control (Git)** [https://git-scm.com/](url)
**Microsoft Azure (Hosting)** [https://www.portal.azure.com](url)

# Installation and Setup

Clone the repository below

```
git clone https://github.com/kelvinndmo/Medical.git
```

### Create and activate a virtual environment

    virtualenv venv --python=python3.6

    source venv/bin/activate

### Install required Dependencies

    pip install -r requirements.txt
    - Ensure that the virtual  environment is active before going forward with the next steps.

## Running the application

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```
### Open Terminal and type
To run the app, then finally run 
```
$ python manage.py runserver
```

## The following endpoints will be available:
- The base url is `http://13.87.166.192/` you can then add the below endpoints i.e
      - http://13.87.166.192/api/v1/authentication/login
      
## Endpoints Available
```
- Below are a list of available endpoints in the application.This are the endpoints that our web and mobile applications are     going to consume.
- The images below show how you can access the specific endpoints listed  below.
```
      
| Method | Endpoint                        | Description                           | Roles               |
| ------ | ------------------------------- | ------------------------------------- | ------------------- |
| POST   | /api/v1/authentication/register | sign up                               | Every User          |
| POST   | /api/v1/authentication/login    | login                                 | Every body          |
| GET    | /api/v1/drugs/                  | Get Drugs                             | Every User          |
| POST   | /api/v1/drugs/pharmacy/<int:id> | Create a pharmacy                     | Government Official |
| GET    | /api/v1/drugs/pharmacies/       | return a list of pharmacies           | All Users           |
| POST   | /api/v1/drugs/add_drug/<int:id> | Add drug to list of avalaible drugs   | Goverment Official  |
| GET    | /api/v1/drugs/pharmacy/<int:id> | verify a pharmacy                     | Users               |
| POST   | api/v1/drugs/                   | Create a drug                         | Government Official |
| GET    | /api/v1/drugs/<int:id>          | Verify a drug                         | Any User            |

## Accessing the endpoints
```
- Before you do anything you have to first and foremost register then login to get an access token.
- You will use this token to access most of the endpoints, we use the permissions after decoding the token
  to enable user to access endpoints they are allowed to
```

## 1. Register.
```
### You need the following:
    - first_name
    - last_name
    - password
    - email
    - confirmed_password
    - role
       - Roles include.
          - GO - Goverment Official
          - PH - Pharmacist
          - PT - Patient.
```
- The screenshot below shows a visual representation.
![Register](https://github.com/kelvinndmo/ImagineCupDemoImages/blob/master/register.png)

## 2. Login.
```
You need the following to login:
 - email
 - password

- After login in access token which should be sent with each request will be return.
```
![Login](https://github.com/kelvinndmo/ImagineCupDemoImages/blob/master/login.png)

- After login, you will get back a response such as this one with the following data,
```
access_token, email, message
```
- Copy the token, we will add it our headers on any request that requires authentication.

![access token](https://github.com/kelvinndmo/ImagineCupDemoImages/blob/master/access_token.png)

### Passing the token;
- To send any request that requires authentication.
- In postman add the Authorization option and pass the token as shown below.

![access_token](https://github.com/kelvinndmo/ImagineCupDemoImages/blob/master/pass_token.png)

## Create/Register a new drug.

- This requires you to be logged in as a Goverment Official.
- The pass the token in postman to the headers sections as shown below.

![access_token](https://github.com/kelvinndmo/ImagineCupDemoImages/blob/master/creeate%20drug.png)

## Verify a pharmacy.
- This endpoint enables a user to verify if a specific is authentic, it does not require a user to be logged in

![access_token](https://github.com/kelvinndmo/ImagineCupDemoImages/blob/master/verfy%20pharmacy.png)

## Get Pharmacies
- This endpoint enables you to get a list of available pharmacies.This does not also require once to be logged in.

![access_token](https://github.com/kelvinndmo/ImagineCupDemoImages/blob/master/get%pharmacies.png)


## Create Pharmacy
- This endpoint enables you to create a pharmacy.This endpoint can only be accessed by a verified approved Pharmacist.

![access_token](https://github.com/kelvinndmo/ImagineCupDemoImages/blob/master/create%20pharmcy.png)

## Add drug to store.
- This endpoint enables a user to add a drug to a store. This endpoint requires a user to be logged in as a Pharmacist.
You pass the drug id which will then be used to add the drug to the pharamcy store as shown below.

![access_token](https://github.com/kelvinndmo/ImagineCupDemoImages/blob/master/add%20drug%20to%20store.png)

## Get drugs.
- This endpoints enables you to get a list of available drugs.This does not also require you to be logged in.
![access_token](https://github.com/kelvinndmo/ImagineCupDemoImages/blob/master/get%20drugs.png)
