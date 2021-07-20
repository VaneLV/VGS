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


Video demonstration

A short video demonstration can be found by the following link

https://drive.google.com/file/d/1Zx2L0FiGdk1Bo_TEIxJ01s1Mi1McPNF9/view?usp=sharing 


