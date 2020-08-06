# INFS3605

Currently our website is being hosted on AWS as an ec2 instance.
You will be able to access the live production site via:

http://ec2-18-223-168-56.us-east-2.compute.amazonaws.com:8000/

This site will be hosted 24/7 for 12 months. If the website goes down and you require its contents,
please do not hesitate to contact nicholasliang325@gmail.com.

To run the website locally please follow these instructions:

1. Install python3 on your device.
2. Install pip3 on your device.
3. Using pip3 install Django.
4. Try to run the site via command prompt/terminal by navigating to INFS3605/website/manage.py and using the command "python3 manage.py runserver".
5. You should see that the additional things are required in order to run the site.
6. Using pip3 install all other remaining requirements as specified by the message you receive in step 5.
7. After you install all other dependencies, navigate back to INFS3605/website/manage.py.
8. Type the command "python3 manage.py runserver".
9. You should see the server boot up and the site available at the address: 127.0.0.1:8000. 
10. Type 127.0.0.1:8000 to visit site locally.

# Additional Information [IMPORTANT]
The website currently uses the HaveIbeenPwned API to pull data for breached emails. 
As this is a paid API, the API key will be valid until: 4TH SEPTEMBER 2020. 

If you require the the email feature past this date, please contact nicholasliang325@gmail.com for further details. 

The design of our website is originally created using the GrapeJS tool. For further information please see:
https://grapesjs.com/

