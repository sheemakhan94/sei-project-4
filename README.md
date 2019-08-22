# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project

# #4: REFLKT

## Overview

The fourth project is to  **build a full-stack React application** that comprises of a **back-end and front-end**.

### Technical Requirements

Before we started the project we were given this brief, we were told that our app must:

* **Have a back-end** – this had to be created using Python and Flask.
* **Have several components** - At least one classical and one functional.
* **Include a router** - with several "pages".
* **Be deployed online** and accessible to the public.
---
# Software Engineering Immersive: Project 4

This is my fourth project during the General Assembly Software Engineering Immersive course. The project was created solo and I had seven days to create it

---

# REFLKT

An online journal where users can create diary entries, task lists and view upcoming events.

## Built using

1. HTML5
2. CSS3
3. JavaScript
4. React.js
5. Python


## Deployment

This app is deployed on Heroku and it can be found here: https://reflkt.herokuapp.com/


### Building the back-end

I seeded a number of diary entries, tasks and events in my back end and used Axios to make requests. I implemented strict authentication in order to make each user's journal as private as possible and created a router in order to make multiple pages in my front-end.

### Functionality

Without being logged in, users can only choose to register or login to an existing account. Once logged in, users are taken to an overview of the current day and can see any current diary entries or events for that day and outstanding tasks. If there is no entry, the user has the option of creating one using the form. Once an entry has been created the form disappears and the entry is rendered instead. The user has the option of viewing all entries and events on a calendar from this page as well as seeing all outstanding tasks. The user has the option to edit and delete entries and events and to create new tasks with multiple steps.

## Future Scope

There is not yet the option to add a new event by clicking on a date on the calendar which is something I would like to implement in future. The styling of the app has also not been fully completed.


