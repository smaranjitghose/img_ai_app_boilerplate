# Hosting your app using a cloud service provider

Now as per your choice of hosting service, please refer the following guides:

## Heroku

-  Visit [Heroku's website](http://heroku.com/).

- Log In. If you do not have an account please set it up. [Tip: *Using GitHub to setup account makes things easier + you can make use of GitHub Education Pack if you are a student*]

- Open Your [Dashboard](https://dashboard.heroku.com/apps)

- Click on Create New App.

- Give an appropriate name and click `next`.

- Change the `Deployment method` to `GitHub` and connect your account.

- Now, search for the repository you made and modified using this template.

- Connect it.

- Choose the branch. (Initially, this would be the master branch and later you can have multiple branches to choose from if you are experimenting with prototypes of different models trained for the same task.)

- Choose either automatic or manual deploy.

    __NOTE:__ Unless you have a CI like [CircleCI](https://circleci.com/) set up in your repository and are aware of how it works please go for `Manual Deploy` option.

- Click on `Deploy Branch`.

Sit back and relax! Your entire app is being setup and will be served in a while.

#### Some useful tips:

1. If you wish to check the size occupied by your files for the deploy in Heroku:
    - Open your app dashboard

    - Click on `More` Option on the right of the Menu bar

    - Select `Run Console`

    - Paste the command:
        ```
        $ du -sh * | sort -hr
        ```
    - Press Enter.


2. You can add a `.slugignore` file (Similar to a `.gitignore` file we use for git to untrack files while we add/commit) to your application to tell the slug compiler to ignore any unnecessary files in your application, such as *static assets*.

3. To View Logs using CLI:
    ```
    $ heroku logs --tail
    ```

__NOTE:__ For the free tier, it is suggested that you use models that are small in size to avoid issues to the limited slug size Heroku Provides.

#### References
1. [My slug size is too large. How can I make it smaller?](https://help.heroku.com/KUFMEES1/my-slug-size-is-too-large-how-can-i-make-it-smaller)


## Google Kubernetes Engine

- Log in to Your preferred Google Account and Open Your [Google Cloud Console](https://console.cloud.google.com/)

- Search for Manage Resources

- Click on create New Project

- Give a suitable Project Name (say your-project-name)

- Open Google Cloud Console from the top right

- Fetch our source code using git

```
git clone  https://github.com/yourusername/your-project-repo-name.git
```

- Checking what we got

```
ls -aH
```

- Navigating to the directory that contains our source code

```
cd your-project-repo-name
```

- Setting Project ID Environment Variable

```
export PROJECT_ID=export PROJECT_ID=your-project-name
```

- Now let's build our docker image and tag it for uploading

 ```
 docker build -t gcr.io/${PROJECT_ID}/insurance-streamlit:v1
 ```

- Checking what we got

```
docker images
```

- Ensure Google Cloud [Container Registry](https://cloud.google.com/container-registry) is enabled

- Authenticate Google Container Registry

```
gcloud auth configure-docker
```

- Let's upload our Docker Image to Google Cloud Container Registry

```
docker push gcr.io/${PROJECT_ID}/insurance-streamlit:v1
```

- Set up the project ID and Compute Engine Zone for gcloud tool


```
gcloud config set project $PROJECT_ID
gcloud config set compute/zone us-central1
```


- Create a Kubernetes Cluster

```
gcloud container clusters create streamlit-cluster --num-nodes=2
```

- Use Kubernetes Cluster Management System to deploy our app replicas and schedule them to run on nodes in the cluster

```
kubectl create deployment insurance-streamlit --image=gcr.io/${PROJECT_ID}/insurance-streamlit:v1
```

- Expose the app to Internet traffic by creating an external IP and a Load Balancer

```
kubectl expose deployment insurance-streamlit --type=LoadBalancer --port 80 --target-port 8501
```

- Checking our app

```
kubectl get service
```

- Set up a DNS***

- Scale up the application by adding additional pods, or delete the Service and container cluster to avoid incurring unwanted charge***

*** Will be covered later


## Amazon EC2

- Visit [AWS Portal](https://aws.amazon.com/free/).

- Log in.
If you dont have an account set it up. It will ask you for **Credit Card details**.  <br><br>
[:bulb: **Tip**: *Use College Email ID if possible, so you can access AWS Educate without any hassle of using a Credit Card or without any fear of charges.*] <br> <br>
[**Caution**: *When you create an AWS account, you're automatically signed up for the Free Tier for 12 months. Your Free Tier eligibility expires at the end of the 12-month period. When your Free Tier expires, AWS starts charging the regular rates for any AWS services and resources that you're using.
For more details refer [this]( https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-free-tier.html).*]

- The new user created will be root user and will have access to all the services and resources (unrestricted access)
 [*Not applicable for people using AWS Educate, though you will have have access to all the services and resources*]

- Search for **EC2 Service** on Management Console Search.

- On EC2 Dashboard, click on **“Launch Instance”.**

- Choose an AMI (Amazon Machine Instance). Here choose, **Amazon Linux AMI 2018.03.0** as it comes under Free Tier.

- Choose an Instance Type. Here, choose **t2.micro**. You can opt for a bigger machine to deal with a powerful model or are willing to pay.

- Configure Instance Details, Add Storage and Tags (_All default value, no change, click on Next_).

- Configure Security Group *

    1. SSH (port 22) is by default added to Inbound Rule.

    2. ** Click on Add Rule Type = Custom TCP Rule, Port Range = 8501 and Source: Anywhere.
    ** _We use the port 8501 here since it is the custom port used by Streamlit._

    3. Ignore Warning as of now


- Click on Review & Launch

    1. _Review the configuration you provided, ignore the warning about Security Group as of now._
    2. Click on **“Launch”**

- A pop-up will appear and ask you to Create a new key-pair (Public-Private)

    1. Select - Create a new key pair
    2. Provide key pair name = img_ai_app_streamlit
    3. Click on “Download Key Pair”

        :white_check_mark: Keep this key safe as it would be required every time you need to login to this particular machine.

    4. Click on **“Launch Instance”** after downloading the key pair

- Click on **View Instances.** You can now go to your instances to see if your instance has started.

### EC2 Setup form Local Machine

*There are several methods of getting access into our instance using SSH. If you are on a Unix based system such as Linux or macOs you will have SSH already. For Windows users you will need to use putty and puttygen to gain access.*

**For *Unix* users**

1. Your key must not be publicly viewable for SSH to work. Use this command:

```
chmod 400 img_ai_app_streamlit.pem
```
2. Then, connect to your instance using its Public DNS:

```
ssh i img_ai_app_streamlit.pem ec2-user@your_public_dns_address
```

Select your instance, and copy the Public DNS(IPv4) Address from the description. It should be something starting with ec2.

**For *Windows* users**

- Follow [this]( https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html?icmpid=docs_ec2_console).

Now we are in our AWS EC2 Instance.

#### Setting Up Environment

- The next step is to install python and all the necessary libraries for your app.

```
sudo apt-get install python3 git
```

- After these two installation we can use git to get our app within our instance.<br>
If you are on **Windows** you can also use **WinSCP** to copy your files to your instance. Refer [this]( https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html#Transfer_WinSCP).

- Now, clone your repository into instance.

```
 git clone link_to_your_repository.git
```

- The next step is to  `cd `  into repository and install required packages using

```
python3 -m pip install streamlit
```

- Now, just run the app and you can see your app live on the External URL.

```
streamlit run app.py
```

- However in order to keep the app running even after you close SSH shell, you need to use **tmux**. We will use this to create a session and run app in that session.

```
sudo apt-get install tmux
tmux new -s NewSession
```
-  You can see that the session name is “NewSession” at the bottom of the screen. You can now start running streamlit in the tmux session.

```
streamlit run app.py
```

-  The next step is to **detach tmux session** so that it continues running in the background when you leave the SSH shell.
To do this just press `Ctrl+B and then D`

- You can now close your SSH session and the app will continue running at the External URL.
