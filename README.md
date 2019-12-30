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
$ python manage.py runserver

## The following endpoints will be available:
- The base url is `http://13.87.166.192/` you can then add the below endpoints i.e
      - http://13.87.166.192/api/v1/authentication/login
