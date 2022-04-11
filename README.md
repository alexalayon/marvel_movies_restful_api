# marvel_movies_restful_api
<p align="center">
  <img src="https://cdn.shopify.com/s/files/1/1140/8354/articles/header_8bac5658-b4d6-49cb-9ccc-5be5042679b7_1600x.jpg?v=1616651617" />
</p>

## Table of Contents
- [About](#about)
- [System Architecture](#system-architecture)
- [Backend](#backend)
- [Serving the application over HTTPS](#Serving-the-application-over-HTTPS)
 - [Disclaimer](#disclaimer)

## About
This Project Marvel Movies Restful Api is a developed as a part of our CLOUD COMPUTING MODULE whose goal is to apply and extend the techniques of different aspects of Cloud applications. The aim of the project is to help users gain knowledge on Marvel movies and the superhero characters. The Marvel films are based on characters that appear in American comic books published by Marvel Comics. The shared universe, much like the original Marvel Universe in comic books, was established by crossing over common plot elements, settings, cast, and characters. So, to fecilitate the effective search we have created a database on Marvel Movies and Marvel Characters with important yet common features, which are a of much interest to the viewers.

## System Architecture
<p align="center">
  <img src="https://raw.githubusercontent.com/Codecademy/articles/0b631b51723fbb3cc652ef5f009082aa71916e63/images/rest_api.svg" />
</p>
The backend is a REST-based service interface for CRUD operations (for example GET, POST, PUT, DELETE) deployed via GITHUB to facilitate scalable performance with our dockerized image.  It is deployed in LINUX server on the Google Cloud Platform to facilitate scalable performance. Our system uses a MYSQL external Cloud database to store information. 
Using the Postman, we  interact with any available HTTP endpoint, including REST-enabled database endpoints. Instead of querying a database directly, we are using Postman to read and write to a database via a REST API

## Backend
It is advisable to use Postman for CRUD operations when accessing the backend.
### CRUD Operations
Basic CRUD operations are possible by accessing the API routes via adding ``api/movie`` and ``api/character`` at the end of the web address following the REST standard.
### REST API 
REST stands for Representation State Transfer. 
The server responds to Create, Read, Update and Delete in a standard way.
The idea behinf REST is to treat all server URL as access points for the various resourses on the server.
REST is a client- server architecture for distributed applications which is just a set of guidelines and not a specific protocol.
The server doesnot store any state about client session on the server side. Every HTTP request happens in complete isolation.
The communication is directly done through HTTP (so a
REST call is just a HTTP request). So all the interactions
with a restful application should be encoded using HTTP
methods:
- GET
- POST
-  PUT 
-  DELETE
#### GET
Requests the state of an identified
resource from the server
- Request body is empty
- Information can be encoded in the request path
- Server returns a representation of the state of the resource
- e.g.: GET /modules
GET /modules/<module-id>

#### POST
Creates a new resource according to
the attached representation as a “subordinate” of the
resource identified by the request URI (so should be a“collection” URI)
- Request body contains the representation of the resource tobe created
- e.g. POST /modules
#### PUT 
  It updates the representation of a resource identified by the request URI according to the attached representation
- Request body contains the representation of the resource to be stored instead.
- If the Request-URI refers to an already existing resource, then an update operation will happen, otherwise create operation should happen if Request-URI is a valid resourceURI.
- e.g. PUT /modules/<module-id>
  
  ### DELETE
  
 Delete the identified resource
- Request body is empty.
- e.g. DELETE /modules/<module-id>
  
  ## Serving the application over HTTPS
  We used the GET operation to extract data from Internet.
  
  <p align="center">
  <img src="https://phpenthusiast.com/theme/assets/images/blog/what_is_rest_api.png" />
</p>
  
  ## DISCLAIMER
This project is part of a cloud computing coursework taught by Dr. Sukhpal Gill at the Queen Mary University of London Electrical Engineering & Computer Science Department to create a prototype of a cloud application.


