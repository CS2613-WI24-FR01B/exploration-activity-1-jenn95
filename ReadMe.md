# **Flask Demo Application**

## **Package/Library Demonstrated**
The sample program, app.py, that I have developed uses the Flask framework. This framework has tools and resources to support development of Python web applications. Some specific Flask features that I utilized in this project were template rendering and inheritance, sessions, routes, and flash messaging to name a few. Each of these Flask functionalities are discussed in further detail, along with specific code examples from my application, in the FlaskOverview.md file in this repository. This ReadMe will focus on specific details of my application use.

## **Running the Application**

Once the required installations are complete, as per "Using Flask" in FlaskOverview.md, the virtual environment should be activated, then call python3 and the main application name, in the case of this demo application, app.py, to start the application. In addition to Python3, Flask, virtualenv, and Twilio should be installed (`pip3 install {necessary-package-here}`) before proceeding. 

MacOS:
```
$ source env/bin/activate
(venv) jenniferbell@Jenns-MacBook-Pro-2 flask-intro % python3 app.py
```
If using Windows, to activate the virtual environment use the following instead of the first line:
```venv\Scripts\activate```

> [!NOTE]
>https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/b132cd3405055fef3a01aae61f4449ad282b8fe2/app.py#L101-L102
> The port must not be in use. If you are running into issues you can change the port in the code,
> or alternatively, in the terminal use `lsof -i :{Your-Port-Here}`, then `kill -9 {The-PID-Result-Here}` to free up the port that you wish to use.

## **Purpose of Application**
The _usefulness_ of the program is limited due to the learning and exploratory nature of the exercise; it is not a fully realized tracking and subscription system, but the concepts and existing functionalities are described below. 

The application offers users with the option to track their completion of programming questions for CS2613. The number of questions completed, and the number of questions remaining for the semester are displayed to the user and continue to update as input is submitted. The user is able to navigte to different web pages, provide information to the program, and receive feedback from the program based on their inputs. For the Course Manager, you can select the language and number you plan on submitting on the next due date, and the course tracker will alert you if you have already submitted this question, and will not update the number of questions completed or change the due date until the user selects and submits a question that they have not previously submitted. 

A secondary functionality that I added to demonstrate the value of being able to retrieve, assess, and utilize user information using the Flask framework was to implement a couple of very basic features of Twilio. Twilio is a library that I have previous, but limited, experience using. Unfortunately, when my application was pushed to this GitHub repository, since my Twilio credentials are now visible (since it was simply set up as a light version to exemplify some uses and how Flask can help developers better involve other libraries in their projects, it was not protected information in my files), Twilio deactivated the specified authentication codes used in the application, so the functionality is no longer available. I have still included this as part of the project, and I can provide the codes for Twilio separately for local use. Please let me know if this is required. 

The administration page was created so that the administrator (username: 'admin' , password: 'admin') could access the list of phone numbers that have subscribed to notifications about the course. 


## **Sample Input and Output**

### **CS2613 Course Manager**
The HTML could be cleaner on this, particularly with a better use of CSS, but since Flask was the intended exploration of the exercise, I focused more on the functionality of Flask and less on the look of the HTML. A quick demo of the functionality explained above is displayed in the following video:


https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/assets/112823585/7adf123c-f8c1-49a8-8c7b-a9c9f6413048



### **Subscription**
After subscribing with a valid (and registered with Twilio number, due to only having the free trial version), a text message was sent to my phone:

https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/352e38f49320bcbb731d8395d5361efb247bfb83/templates/subscribe.html#L6-L12

And this POST request was handled here, and sent a message using Twilio:

https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/blob/352e38f49320bcbb731d8395d5361efb247bfb83/app.py#L40-L42

<img src="https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/assets/112823585/53b33fd7-339c-4ff2-aa41-3e8768a23008" width="250">

Unfortunately, due to reasons discussed above, Twilio is not working when published, but locally and with a proper setup of a paid version, a list of the messages that have been sent, and the contact information is stored. This list was originally displayed in the admin section. The page will work, but the live version will always be empty. 

This was not a key feature of Flask, so I am not too concerned about it as it was more to emphasize the value and ways we can integrate other libraries while using Flask.

### **Login Page**
The login page can be used to access a list of numbers that have subscribed to the course subscription service. This creates a session, as discussed in FlaskOverview.md. An option to logout is offered, with feedback message provided to the user after logging out. 



https://github.com/CS2613-WI24-FR01B/exploration-activity-1-jenn95/assets/112823585/9667f749-85a0-4704-ba3e-ba134d980405






