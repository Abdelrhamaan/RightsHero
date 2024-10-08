# Online Book Store

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)

## Description

A simple project to create Unlimited Subcategories.

## Features

1. you can create unlimited subcategories.

## Technologies

1. **BackEnd**:

   - Django

2. **FrontEnd**:

   - bootstrap
   - jquery

3. **Database**:

   - PostgreSQL

4. **Containerization**:
   - Docker
   - Docker Compose

## Installation

1. Clone repository

   ```bash
        git clone https://github.com/Abdelrhamaan/RightsHero
   ```

2. Open your AWS account, go to ec2 instances then create keypair from the left side pair

3. Change the (KeyName: CloudFormationKeyPair) in the cloud formation template to your key name

4. In your Aws Account go to cloud formation

5. Create new stack

6. Choose upload template file and upload CloudFormation.yml

7. Connect To Your Ec2 instance, go to instances choose your instance and click on connect then browse to SSH and take the below command
   it will be some thing like that

   ```bash
       ssh -i "CloudFormationKeyPair.pem" ec2-user@ec2-3-92-3-105.compute-1.amazonaws.com
   ```

8. Make migrate
   ```bash
        docker exec -it rightshero-backend-1 python manage.py migrate
   ```
9. Add Allowed Hosts change ec2-3-92-3-105.compute-1.amazonaws.com to your ec2 dns name or ec2 ip

   ```bash
    docker exec -it rightshero-backend-1 echo "ALLOWED_HOSTS = ['ec2-3-92-3-105.compute-1.amazonaws.com', 'localhost', '127.0.0.1']">> settings.py
   ```

## Usage

1. Go To http://your ec2 dns or ip:8000
