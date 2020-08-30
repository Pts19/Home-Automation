# Predictive Automation Using Home Assistant
> A integration for Home Assitant that track users and their smart device usage while they go about their daily lives within their home. Our integration will then use Machine Learning to automate tasks the user typically preforms by scheduling them within Home Assitant. 

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Features](#features)
* [Status](#status)
* [Retrospective](#retrospective)
* [Contact](#contact)

## General info
Our integration will help non-technical users tackle home automation. Home assistant has a tedious and diffucult to understand configuration processes for home automation. Our integration simplifies the configuration process to be as minimal as possible. Our integration will configure the scheduling of all smart devices in the home by tracking how the user normally utilizes them. The integration then builds and maintains predictive schedules for the devices.   


![Example screenshot](./img/icon.png)

## Technologies
* [Home Assistant](https://www.home-assistant.io/) - version 0.98.5
* [Sci-kit Learn](https://scikit-learn.org/stable/) - version 0.21.2
* [Rasberry pi - Model 3](https://www.raspberrypi.org/products/raspberry-pi-3-model-b/) - Model B
* [Google Maps API](https://developers.google.com/maps/documentation/)

[//]: <> (## Setup)
[//]: <> (Describe how to install / setup your local environement / add link to demo version.)

[//]: <> (## Code Examples)
[//]: <> (Show examples of usage:)
[//]: <> (`put-your-code-here`)

## Features
List of features ready and TODOs for future development

* Improved Accuracy of Machine Learning Code and corrected output- Shaun
* Reworked Database and Management - Stavros
* Integrating Google API for presence detection and travel time - Sherwin
* Captured event triggers, and implemented machine learning output to Automation.yaml - Derek
* Created write_to_automations.py that will format and store machine learning generated automations - Patrick



To-do list:
 Study for final (no Sprint 4)

## Status
Project is: _Alpha_ As it is functioning but not published and contains limited features
* [Demonstration Video](https://youtu.be/bm1OZir9xpg) - Team
* [Integrated everything into the Integration to run as one single process](https://github.com/CS3398-Bolians-Booleans/CS3398-Bolians-S2019/blob/master/custom_components/box1/__init__.py) - Shaun
* [Created Database to pass data into machine learning code, upgraded server](https://github.com/CS3398-Bolians-Booleans/CS3398-Bolians-S2019/blob/master/Database/app.py) - Stavros
* [Created a Flask server to get real-time data. Next step is to create a pipeline for our integration to get real-time data](https://github.com/CS3398-Bolians-Booleans/CS3398-Bolians-S2019/tree/master/Architecture%20and%20API) - Sherwin
* [Created write_to_automations.py which formats the machine learning tuple, and writes it to automations.yaml](https://github.com/CS3398-Bolians-Booleans/CS3398-Bolians-S2019/blob/master/config/python_scripts/write_to_automations.py%20-%20SuperUser%20and%20TAG)- Patrick
* [Logging complete, Next build out multiple user action tracking](https://github.com/CS3398-Bolians-Booleans/CS3398-Bolians-S2019/tree/master/user%20location) - Derek 

## Retrospective
What Went Well or Maybe Not:
* Still Maintained Frequent Communication
* All Code Integrated Together, Compiles, and Runs in the Home Assistant Environment
* Still Attended Regulary Scheduled Meetings (including additional emergency meetings)
* Downsized tasks for better assumed hours (most, at least)
  * Shaun - Task hours were more than expected but I found the time
  * Patrick - Fully accomplished goals in a timely manner
  * Stavros - Rebuilt server multiple times after failures/crashes - got us running
  * Sherwin - Finished Google Traffic API integration
  * Derek - Automations actually execute!
     

What Might Be Impeding Us from Performing Better:
* Complexity increased tremendously as more components were implemented. 
* The Home Assistant environment we were working with seemed to be convoluted at times.

What Can We do to Improve:
* Integrate code together in smaller pieces. Catch issues sooner.
  * Shaun - Push smaller increments of code on github for team members to digest 
  * Patrick - Reach out to team members more often to assist with work load
  * Sherwin - Better unit testing
  * Stavros - Be more proactive with security measures
  * Derek - Schedule work and social life better to participate in more team meetings
  
  


[//]: <> (## Inspiration)
[//]: <> (Add here credits. Project inspired by..., based on...)

## Contact
Created by [@Bolians](https://github.com/CS3398-Bolians-Booleans) - feel free to contact us! 
* Email: spc51@txstate.edu
