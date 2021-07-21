Registration

Register following the link below to get your personal VaultID, Username and Password

https://dashboard.verygoodsecurity.com/


Environment Setup

Put your personal VaultID, Username and Password into the routes.py as below:
response = requests.post('https://[VaultID].SANDBOX.verygoodproxy.com/post'


os.environ['HTTPS_PROXY'] = 'http://[Username]:[Password].SANDBOX.verygoodproxy.com:8080'


Start your local Web server

$ python simple_app.py

Once the above is done, you can access it at http://127.0.0.1:5000/

You will aslo need to setup yor NGRok tunnel and change it's config under your VGS route.

On how to setup your NGRok please refer to the article below:
https://dashboard.ngrok.com/get-started/setup

Once NGRok script will provide you with a tunnel link kindly do the following:
1. Go to your routes
2. Create a new inbound route with the following settings:
    a. Upstream Host: [your NGRok link]
    b. Add filter with "Fields in JSON path" $.CVV with "Targets" Body
    b. Add filter with "Fields in JSON path" $.Card with "Targets" Body
    c. Add filter with "Fields in JSON path" $.Expiration with "Targets" Body
3. Create a new uotbound route with the following settings:
     a. Upstream Host: echo.apps.verygood.systems
    b. Add filter with "Fields in JSON path" $.CVV with "Targets" Body
    b. Add filter with "Fields in JSON path" $.Card with "Targets" Body
    c. Add filter with "Fields in JSON path" $.Expiration with "Targets" Body
    
Kindly note that filter's operations should be set to "Redact" for inbound and "Revel" for outbound 


Video demonstration

A short video demonstration can be found by the following link

https://drive.google.com/file/d/1Zx2L0FiGdk1Bo_TEIxJ01s1Mi1McPNF9/view?usp=sharing 


