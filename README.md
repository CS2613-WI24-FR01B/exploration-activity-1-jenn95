# **Flask**

## **Flask Overview**
Flask is a web framework, even sometimes referred to as a micro-framework due to it's light build. Web frameworks provide developers
with resources and tools for building, managing, and testing web applications. A web framework is a collection of libraries and modules. Flask is more flexible 
with less structure than some more powerful and popular python frameworks such as Django. Even though flask is considered to be a micro-framework,
it can provide both beginners and experiences developers alike with the right tools for their web application. [ref: https://pythonbasics.org/what-is-flask-python/]. Developers do not need to use Python frameworks to develop applications, but they can provide tools that make this task easier and more efficient. Because of this, frameworks are widely used throughout the industry. As each framework has it's stengths and weaknesses, the choice of framework varies based on business requirements, as well as ease of use of the framework. Flask is a popular framework in part due to it's ease of use and flexibility. [https://radixweb.com/blog/best-python-frameworks#Significance]. Flask can be used for 

### **Purpose of Flask**
The purpose of Flask is to provide a lightweight framework to developers, with tools for web development. A single python file can be used for a web application. Flask handles more of the complexity, and the functionality is very readable and user friendly. Code can be run and tested on a local server while developing, and can also be deployed to production. Flask is a backend framework that runs on the server, and can communicate with the front end to create interactive web applications for users. [https://www.analyticsvidhya.com/blog/2021/10/flask-python/]

### **Using Flask**
The use of virtual environments is common when building a flask application. This is simple to do from the command line:
``` 
$ pip3 install virtualenv
$ source env/bin/activate
```
Now, you should be in your virtual environment and can install flask. After installing Flask, calling create is useful as it will set up some basic code in the sample app.py file that it creates to get the user started:
```
$ pip3 install flask
$flask create my_first_app
```
This app can be started using Visual Studio Code's Live Server extension, or alternatively, from the command line:
```
$flask serve
```
And you will see the app from app.py displayed in your browser. 

Given the structure that is provided in the code base through the setup detailed above, Flask makes it very intuitive to continue to build on this to develop your web application. 

>[!TIP]
>There is a lot of documentaiton online. I found the Flask documentation at https://flask.palletsprojects.com/en/2.3.x/quickstart/#debug-mode to be a well organized >resource. If a step-by-step learning resource is of interest, https://python-adv-web-apps.readthedocs.io/en/latest/flask.html#what-you-know-now-about-flask is a >very well laid out resource, with "What You Should Know Now" sections at the end of each page to recap and solidify new information for readers. 

More details on using specific functionalities will be provided in the next section, "Functionalities of Flask".

### **Functionalities of Flask**
With Flask, we are able to handle HTTP GET and POST requests. 

### **Flask Creation**
Funny enough, Flask was actually releasted as an April Fool's Day joke in 2010 by developer Armin Ronacher. Flask is more "pythonic" in nature than other web frameworks that rely on boiler plate code or dependencies. This can feel more intuitive and lightweight for developers, and this framework met this desire as Flask became very popular and maintains popularity today. 

### **Motivation for Choosing Flask**
I really wanted to take advantage of this exploration activity and use it as an opportunity to learn about different packages/libraries/frameworks, but also to be able to build on an area that I consider to be a weakness of mine. Web development is something that I am still uncomfortable with, particularly interacting with HTML pages and servers, even after being in a year-long co-op position as a full stack developer. Since Python is considered to be an easier language, and since it is likely that I will be applying to full-stack jobs following graduation, I thought it was a great opportunity to work with a web development framework. After much research, through reading documentation, tutorials, and watching videos, I decided on Flask for my first exploration activity to get a sense of the underpinnings of web development frameworks, since it is a micro-framework, there is less under the hood and can be easier to develop a deeper understanding as a learner. 

### **Learning Experience**
I found a fantastic tutorial on YouTube, by Michael Herman of RealPython. This resource had an accompanying blog post for each tutorial video, which was important in really digesting what was being presented in the videos. This is the third small demo project I started for this task and I have discovered more about how I like to approach a new task and what works for me. Throughout my co-op I was encouraged to use ChatGPT for questions about the framework we were using because the documentation wasn't the best for some situations, and recognized during this process, without the access to ChatGPT or senior developers, how frustrating it can be when you want to do something very simple and cannot seem to find the answer to your problem. I think it would take me a long time to become proficient in a framework, unless I really dig in and make detailed notes and examples on different use cases. 

### **Reflection on Working with Flask**
As I previously mentioned, I have worked with frameworks in the past, and throughout the process of working with Flask there were multiple instances where I thought something was a really nifty feature. I also imported a simple library, Twilio, to show how Flask can help integrate users with the libraries that the developer has used to implement certain features. In this case, Flask allowed me to collect a cell phone number that a user provides, and return the information to my python function to use the functions of the twilio library and handle this user request.  