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


