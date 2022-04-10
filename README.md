# marvel_movies_restful_api
<p align="center">
  <img src="https://cdn.shopify.com/s/files/1/1140/8354/articles/header_8bac5658-b4d6-49cb-9ccc-5be5042679b7_1600x.jpg?v=1616651617" />
</p>

## Table of Contents
- [About](#about)
- [System Architecture](#system-architecture)
- [Backend](#backend)
 - [Disclaimer](#disclaimer)

## About
This Project Marvel Movies Restful Api is a developed as a part of our CLOUD COMPUTING MODULE whose goal is to apply and extend the techniques of different aspects of Cloud applications. The aim of the project is to help users gain knowledge on Marvel movies and the superhero characters. The Marvel films are based on characters that appear in American comic books published by Marvel Comics. The shared universe, much like the original Marvel Universe in comic books, was established by crossing over common plot elements, settings, cast, and characters. So, to fecilitate the effective search we have created a database on Marvel Movies and Marvel Characters with important yet common features, which are a of much interest to the viewrs.

## System Architecture
<p align="center">
  <img src="https://raw.githubusercontent.com/Codecademy/articles/0b631b51723fbb3cc652ef5f009082aa71916e63/images/rest_api.svg" />
</p>
The backend is a REST-based service interface for CRUD operations (for example GET, POST, PUT, DELETE) deployed via Google Cloud to facilitate scalable performance with our dockerized image. SSL deployments are facilitated through {{{Microsoft Azure and Heroku}}}. The node server interacts with Google API. Furthermore, our system uses a MYSQL external Cloud database (MongoDB) to securely store our community user information. 
Using the Postman, we  interact with any available HTTP endpoint, including REST-enabled database endpoints. Instead of querying a database directly, we are using Postman to read and write to a database via a REST API

## Backend
It is advisable to use [Postman] for CRUD operations when accessing the backend.
### CRUD Operations
Basic CRUD operations are possible by accessing the API routes via adding ``api/movie`` and ``api/character`` at the end of the web address following the REST standard.
### REST API 
REST stands for Representation State Transfer. 
The server responds to Create, Read, Update and Delete in a standard way.
The idea behinf REST is to treat all server URL as access points for the various resourses on the server.
REST is a client- server architecture for distributed applications

