## Installation
To run, ensure you have python 3.8, and clone the repo.
In the root of the repo, install all required packages with `python3 -m pip install -r requirements.txt`

Next you have to fill out the secrets.json. Enter the mailgun and sendgrid api keys into their associated parts of the secrets file. For mailgun, you need to specify a domain; this is either one that you provide when setting up a mailgun account, or use the one provided. Put this value in `mailgun_endpoint`.

Once the required packages are installed, run the code with `flask run`
This should start the flask server, and you should be able to send requests to `http://127.0.0.1:5000/email` unless the port is taken. 

This was build using python3 and flask, due to simplicity and ease of development. They are the tools I am most comfortable with, and work very well for building APIs.

if I had more time, I would probably have more unit tests and have a more extensive input validations, but I believe checking that all values are not empty, and that the emails are valid are enough to cover most issues that would happen. I would also make a more proper interface to hold all the client data, to make it more scalable, which would be good if we were to add more email clients, but I felt that since this is only a prototype, simply having the same class structure was sufficient. Any more feature development on the clients would probably require a base class to derive from.

In total I tried to keep the time worked on this to be around 4 hours, but with lots of time breaking up due to other responsibilities I had to take care of.