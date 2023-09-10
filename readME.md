# Description

A simple user CRUD flask App which connects to your mongoDB.

# Pre-requisites  

- Install Docker Desktop.

# Instructions

1) Run `docker compose up`
2) API can be tested at `http://localhost:5001/`
    3) Endpoints are `\users` and `\users\<id>`

# Notes

- SQLAlchemy doesn't support NoSQL databases. Used pyMongo instead.
- His series is amazing! 
https://dev.to/paurakhsharma/flask-rest-api-part-2-better-structure-with-blueprint-and-flask-restful-2n93