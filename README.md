# Be Challenge MdeAssis

Hi there, I'm Matheus. I'm made this test to prove my skills in the field of software development. I tried to apply all the knowledge I've learned in the past few years and with short time I've been able to make this project. I hope that we can talk more about it.
# Choices

**Framework**: I chose fastapi because of the size and complexity of the project. This framework is very fast and easy to use has some nice features as background tasks that can helpful in the future

**Database**: I used postgresql as a relation database because of the relationships between the data structure.

# Train of thought

1. Planing the project and read all the necessary information about football api.
2. Setup all the project, like databases, migrations, docker, the API itself and tests to work with TDD.
3. The basic steps for import_league route, just insert the data inside the db without any business logic.
4. Add the business logic for the league import.
5. The other routes to provide the data for the client with tests cases and error handling.
6. Rate limit to handle the requests.
7. Caching for the routes, some performance improvements.
8. Database indexes.

# General Architecture
<p align="">
  <img src="https://user-images.githubusercontent.com/65235458/184613414-83e37a34-a475-441e-8903-a424da86b69e.png" alt="Architecture" float="rigth" width="400"> 
</p>


## Requirements

> Before start you'll need to install this systems

* Docker
* Docker Compose

## Setup

>In the root folder make a copy of **env-sample** and rename it to **.env**

```
cp env-sample .env
```
## Running
> You just have to run the containers with **docker compose**

```
docker compose up
```
> Open the browser and go to http://localhost:8080

> You can see the swagger here http://localhost:8080/docs

> If you want to test it on **postman** just download the [collection](https://www.getpostman.com/downloads/mac) and import there.  

[⬆ Voltar ao topo](README.md)<br>
