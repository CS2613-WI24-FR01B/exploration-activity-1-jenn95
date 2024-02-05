# **Flask**

## **Flask Overview**
Flask is a web framework, even sometimes referred to as a micro-framework due to it's light build. Web frameworks provide developers
with resources and tools for building, managing, and testing web applications. A web framework is a collection of libraries and modules. Flask is more flexible 
with less structure than some more powerful and popular python frameworks such as Django. Even though flask is considered to be a micro-framework,
it can provide both beginners and experiences developers alike with the right tools for their web application [[ref]](https://pythonbasics.org/what-is-flask-python/). Developers do not need to use Python frameworks to develop applications, but they can provide tools that make this task easier and more efficient. Because of this, frameworks are widely used throughout the industry. As each framework has it's stengths and weaknesses, the choice of framework varies based on business requirements, as well as ease of use of the framework. Flask is a popular framework in part due to it's ease of use and flexibility [[ref]](https://radixweb.com/blog/best-python-frameworks#Significance).

## **Purpose of Flask**
The purpose of Flask is to provide a lightweight framework to developers, with tools for web development. A single python file can be used for a web application. Flask handles more of the complexity, and the functionality is very readable and user friendly. Code can be run and tested on a local server while developing, and can also be deployed to production. Flask is a backend framework that runs on the server, and can communicate with the front end to create interactive web applications for users [[ref]](https://www.analyticsvidhya.com/blog/2021/10/flask-python/).

## **Using Flask**
The use of virtual environments is common when building a flask application. This is simple to do from the command line:
``` 
$ pip3 install virtualenv
$ source env/bin/activate
```
Now, you should be in your virtual environment and can install flask. After installing Flask, calling create is useful as it will set up some basic code in the sample app.py file that it creates to get the user started [[ref]](https://realpython.com/introduction-to-flask-part-1-setting-up-a-static-site/):
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
>There is a lot of documentation online. I found the Flask documentation at https://flask.palletsprojects.com/en/2.3.x/quickstart/# to be a well organized resource. If a step-by-step learning resource is of interest, https://python-adv-web-apps.readthedocs.io/en/latest/flask.html# is a very well laid out resource, with "What You Should Know Now" sections at the end of each page to recap and solidify new information for readers. 

A simple project with has three main components to its structure: the **static folder** contains CSS files and images, the **template folder** contains HTML files, and then you have your **Python files**. In a small application, the logic can be in a single app.py file, but as the application grows in size and complexity, it is good practice to move the functionality into separate smaller files [[ref]](https://flask.palletsprojects.com/en/2.3.x/tutorial/layout/). 

More details on using specific functionalities will be provided in the next section, "Functionalities of Flask".

## **Functionalities of Flask**
I have selected some key functionalities of Flask below, some of which I have implemented in my demo project.

### **1. Debug Mode**
     I found debug mode to be very useful during the development of the small demo project. Debug can simply be set to true in your main method within the parameter of the run call, as seen below in my app.py file [[ref]](https://www.youtube.com/watch?v=WfpFUmV1d0w&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=1).
 https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/a11d32ccf5ffa9729d75e71b1f76983b36428ef8/app.py#L92-L94

In debug mode, your application will be monitored for changes and the server will reload if changes occur.
<img width="815" alt="Screenshot 2024-02-04 at 4 40 18 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/assets/112823585/f40ac0b1-5d13-4bfc-894f-5126e0808815">

If a problem is detected, the debugger will provide some insights to the problem, and suggest some possible solutions [[ref]](https://www.analyticsvidhya.com/blog/2021/10/flask-python/),[[ref]](https://flask.palletsprojects.com/en/3.0.x/quickstart/). As you can see below, the debugger told me what it was looking for, and posed that I had made a nesting mistake (it was the case that I had incorrecty terminated my block section of a template, but more on template inheritance later). With the information from the debugger I was able to easily track down my problem.
<img width="1108" alt="Screenshot 2024-02-04 at 3 38 18 PM" src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/assets/112823585/09204c7b-cb3a-488f-bbff-726148554af4">



### **2. Routes**
With Flask, the route() method is used for setting a route path, and using the @app.route() annotation links it to the function below it. 
https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/a11d32ccf5ffa9729d75e71b1f76983b36428ef8/app.py#L27-L29

A call to the route method can also contain parameters to further specify actions within the function below. If the page associated with that route is making a POST request, then we would want to handle this data in the backend [[ref]](https://www.turing.com/kb/build-flask-routes-in-python#creating-a-route-in-flask). 
https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/a11d32ccf5ffa9729d75e71b1f76983b36428ef8/app.py#L33-L36


### **3. Templates and Inheritance**
The templates folder contains our HTML files. In Flask, these HTML files can be rendered and displayed to the user in the browser when returning `render_template('SomeExample.html')`. As you might have noticed under the first code snippet in Routes, the route for home will return the rendered template "welcome.html".

Since a lot of HTML files may contain the same information, rather than copying an HTML file, pasting to a new file, just to change a few things on a new page, Flask provides us with the option to use template inheritance. A base.html template may be set up, and by using some key words, we can give temlplates the ability to inject their own HTML content into these bodies, while keeping the inherited html [[ref]](https://www.geeksforgeeks.org/template-inheritance-in-flask/).

https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/a11d32ccf5ffa9729d75e71b1f76983b36428ef8/templates/base.html#L1-L18

By simply extending the base.html, we are able to use the template, but insert new html in the blocks:

https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/a11d32ccf5ffa9729d75e71b1f76983b36428ef8/templates/welcome.html#L1-L13

One additional and important functionality that we get with the render_template() method, is that we can pass parameters to the method that can be used on the HTML page for a dynamic application [[ref]](https://www.youtube.com/watch?v=bLA6eBGN-_0&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM&index=2).

For example,
https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/a11d32ccf5ffa9729d75e71b1f76983b36428ef8/app.py#L90

And this list is used in the HTML file, with double brace brackets we iterate through a list and can display the information to the user:
https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/a11d32ccf5ffa9729d75e71b1f76983b36428ef8/templates/restrictedAdmin.html#L8-L11

   
### **4. Message Flashing**

A way to provide users with feedback. `flash("message")` can be called in a function. If a message is flashed at the end of a request, the message is accessible at the next request [[ref]](https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/).
https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/a11d32ccf5ffa9729d75e71b1f76983b36428ef8/app.py#L41-L42
Again, there can be specific handling of messages within the HTML to display to the user. These do NOT need to be passed in the render_template() method, get_flashed_messages() can access messages that are passed to flash()
https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/a11d32ccf5ffa9729d75e71b1f76983b36428ef8/templates/subscribe.html#L17-L19

  
### **5. Sessions**
Sessions were not an area that I was able to explore with great depth in the creation of my demo project, but they were part of a tutorial I followed and I implemented them in a somewhat trvial way to just explore a bit of functionality with them in my small application. Since HTTP requests do not store any information about the requests that have been made, we often want to store information about these requests as the client continues to interact with the application. This is possible with sessions. Sessions can store data for a period of time, as compared to a database where data can be stored indefinitely. A session in Flask can be created using `Session['someValue']`. If a user were to access the application in a new browser, a new session could be started [[ref]](https://testdriven.io/blog/flask-sessions/).

https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/a11d32ccf5ffa9729d75e71b1f76983b36428ef8/app.py#L72

Above, True was saved in the session. Information from requests can continue to be added to the session. 

To close a session, we can simply call `session.pop('someValue', None)`. 
https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/a11d32ccf5ffa9729d75e71b1f76983b36428ef8/app.py#L79



## **Flask Creation**
Funny enough, Flask was actually releasted as an April Fool's Day joke in 2010 by developer Armin Ronacher. Flask is more "pythonic" in nature than other web frameworks that rely on boiler plate code or dependencies [[ref]](https://www.educative.io/courses/flask-develop-web-applications-in-python/what-is-flask#Origins-of-Flask). This can feel more intuitive and lightweight for developers, and this framework met this desire as Flask became very popular and maintains popularity today [[ref]](https://www.fullstackpython.com/flask.html).

## **Motivation for Choosing Flask**
I really wanted to take advantage of this exploration activity and use it as an opportunity to learn about different packages/libraries/frameworks, but also to be able to build on an area that I consider to be a weakness of mine. Web development is something that I am still uncomfortable with, particularly interacting with HTML pages and servers, even after being in a year-long co-op position as a full stack developer. Since Python is considered to be an easier language, and that it is likely that I will be applying to full-stack jobs following graduation, I thought it was a great opportunity to work with a web development framework. After much research, through reading documentation, tutorials, and watching videos, I decided on Flask for my first exploration activity to get a sense of the underpinnings of web development frameworks, since it is a micro-framework, there is less under the hood and can be easier to develop a deeper understanding as a learner. 

## **Learning Experience**
I found a fantastic tutorial on YouTube, by Michael Herman of RealPython. This resource had an accompanying blog post for each tutorial video, which was important in really digesting what was being presented in the videos, which can be found on the [blog](https://realpython.com/introduction-to-flask-part-1-setting-up-a-static-site/) and [video channel](https://www.youtube.com/playlist?list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM). This is the third small demo project I started for this task and I have discovered more about how I like to approach a new task and what works for me. Throughout my co-op I was encouraged to use ChatGPT for questions about the framework we were using because the documentation wasn't the best for some situations, and recognized during this process, without the access to ChatGPT or senior developers, how frustrating it can be when you want to do something very simple and cannot seem to find the answer to your problem. Compared to the other frameworks I explored, I found that Flask has much better resources for beginners. That being said, I think it would take me a long time to become proficient in a framework, unless I really dig in and make detailed notes and examples on different use cases. 

## **Reflection on Working with Flask**
As I previously mentioned, I have worked with frameworks in the past, and throughout the process of working with Flask there were multiple instances where I thought something was a really nifty feature. I also imported a simple library, Twilio, to show how Flask can help integrate users with the libraries that the developer has used to implement certain features. In this case, Flask allowed me to collect a cell phone number that a user provides, and return the information to my python function to use the functions of the twilio library and handle this user request.  

### **Recommendation** 
I would definitely recommend this framework to a beginner in Python that was still learning the language and wanted to move into some web development projects and utilize a framework. It feels very intuitive and neat using Flask, which I feel really complements working in Python since the lanaguage itself is very explicit.

### **Personal Use**
With the intuitive nature, I found it enjoyable to use. There were many times that I thought a functionality described was very neat, and I just scratched the surface of possibilities with this framework. I could see myself continuing to build small personal projects with this framework to get better at reading and applying what I have learned from documentation and online resources. Since Flask is popular there are a lot of great resources which makes a big difference when learning something new. 

