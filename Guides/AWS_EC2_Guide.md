<h1 align = "center">Amazon Web Services EC2 Deployment Guide</h1>

1. Visit [AWS Portal](https://aws.amazon.com/free/).  

2. Log in.  
  If you do not have an account please set it up. It will ask you for **Credit Card details**.  
  :pushpin: The payment of 1 or 2 Rs. will be deducted to verify the card, it will be reverted for free users. If you exceed the free limits provided then the bill will be charged   to the card accordingly.  
  
:bulb: Tip: Use College Email ID if possible, so you can access AWS Educate without any hassle of using a Credit Card or without any fear of charges.
 
:heavy_exclamation_mark:  Caution: When you create an AWS account, you're automatically signed up for the Free Tier for 12 months. Your Free Tier eligibility expires at the end of the 12-month period. When your Free Tier expires, AWS starts charging the regular rates for any AWS services and resources that you're using.  
For more details refer: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-free-tier.html

3. The new user created will be root user and will have access to all the services and resources (unrestricted access) [Not applicable for people using AWS Educate, though you will have have access to all the services and resources]

4. Search for **EC2 Service** on Management Console Search. 

5. On EC2 Dashboard, click on **“Launch Instance”.**

6. Choose an AMI (Amazon Machine Instance). Here choose, **Amazon Linux AMI 2018.03.0** as it comes under Free Tier. 

7. Choose an Instance Type. Here, choose **t2.micro**.You can opt for a bigger machine to deal with a powerful model or are willing to pay.

8. Configure Instance Details (_All default value, no change, click on Next_)

9. Add Storage (_All default value, no change, click on Next_)

10. Add Tags (_All default value, no change, click on Next_)

11. Configure Security Group*
- SSH (port 22) is by default added to Inbound Rule
- **Click on Add Rule Type = Custom TCP Rule, Port Range = 8501 and Source: Anywhere.** _We use the port 8501 here since it is the custom port used by Streamlit._
- Ignore Warning as of now 
	
		*Security Groups Tips:
		- All Inbound Traffic blocked by default
		- All Outbound Traffic allowed by default
		- Only Allow rules, no deny rules
		- Multiple SG can be applied to one EC2
		- One SG can be applied to many EC2s
    
12. Click on Review & Launch  
		- _Review the configuration you provided, ignore the warning about Security Group as of now._
	 - Click on **“Launch”**

13. A pop-up will appear and ask you to Create a new key-pair (Public-Private)
  - Select - Create a new key pair
  - Provide key pair name = img_ai_app_streamlit
  - Click on “Download Key Pair”
	
:white_check_mark: Keep this key safe as it would be required every time you need to login to this particular machine. 

  Click on **“Launch Instance”** after downloading the key pair

14. Click on **View Instances.** You can now go to your instances to see if your instance has started.   
    Hint: See the Instance state, it should be showing **“Running”**
    
## Now let’s Connect to EC2 from Local Machine 

There are several methods of getting access into our instance using SSH. If you are on a Unix based system such as Linux or macOs you will have SSH already. For Windows users you will need to use putty and puttygen to gain access. 

For **Unix** users,

1. Your key must not be publicly viewable for SSH to work. Use this command:
```console 
chmod 400 img_ai_app_streamlit.pem                
```            
2. Then, connect to your instance using its Public DNS:  
```console 
ssh i img_ai_app_streamlit.pem ec2-user@your_public_dns_address 
 ```  
Select your instance, and copy the Public DNS(IPv4) Address from the description. It should be something starting with ec2.

For **Windows** users, follow this https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html?icmpid=docs_ec2_console

Now we are in our AWS EC2 Instance.

## Setting Up Environment 

1. The next step is to install python and all the necessary libraries for your app.
```console 
sudo yum install python36
 ```  
 2. Then we can further install git 
 ```console 
sudo yum install git
 ``` 
 3. After these two installation we can use git to get our app within our instance. If you are on **Windows** you can also use **WinSCP** to copy your files to your instance. 
  Refer this https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html#Transfer_WinSCP
  
 4. Now, clone your repository into instance. 
 ```console 
 git clone link_to_your_repository.git
 ``` 
 
 5. The next step is to  `cd `  into repository and install required packages either using the requirements.txt file or simply using
```console 
python36 -m pip install streamlit
 ``` 
 
 6. Now, just run the app and you can see your app live on the External URL.
```console 
streamlit run app.py
 ``` 
7. However in order to keep the app running even after you close SSH shell, you need to install **tmux**.
```console 
sudo yum install tmux
 ``` 
 8. We will then use tmux to create a session and run app in that session.
 ```console 
tmux new -s NewSession
 ``` 
9. You can see that the session name is “NewSession” at the bottom of the screen. You can now start running streamlit in the tmux session.
 ```console 
streamlit run app.py
 ``` 
10. The next step is to **detach tmux session** so that it continues running in the background when you leave the SSH shell.   
To do this just press `Ctrl+B and then D`

11. You can now close your SSH session and the app will continue running at the External URL.
