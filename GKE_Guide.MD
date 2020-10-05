<h1 align = "center">Google Kubernetes Engine Guide</h1>

1. Log in to Your preferred Google Account and Open Your [Google Cloud Console](https://console.cloud.google.com/).

2. Search for Manage Resources.

3. Click on Create New Project.

4. Give a suitable Project Name (say your-project-name). Just like I've given KubernetesPR here.

![created-a-project](images\gke-guide\1-console-after-loggin-in.jpg)

5. Open Google Cloud Console from the top right.

![click-on-cloud-shell](images\gke-guide\8-click-on-cloud-shell.PNG)

6. Fetch our source code using git.

```git clone  https://github.com/yourusername/your-project-repo-name.git .```

![clone-repo](images\gke-guide\9-clone-your-repository.jpg)

7. Checking what we got.

```ls -aH ```

8. Navigating to the directory that contains our source code.

```cd your-project-repo-name```

![change-directory](images\gke-guide\10-change-directory.jpg)

9. Setting Project ID Environment Variable.

```export PROJECT_ID=export PROJECT_ID=your-project-name```

![export-project-id](images\gke-guide\11-export-project-id.PNG)

10. Now let's build our docker image and tag it for uploading.

```docker build -t gcr.io/${PROJECT_ID}/insurance-streamlit:v1```

![docker-build](images\gke-guide\12-run-this-command-to-build-docker-image.PNG)

**gcloud** asks for credentials to make a GCP API call.

![click-on-authorize](images\gke-guide\13-click-on-authorize.PNG)

11. It's always good to cross-check first.

```docker images```

![cross-check](images\gke-guide\14-confirm.jpg)

12. Ensure Google Cloud [Container Registry](https://cloud.google.com/container-registry) is enabled.

13. Authenticate Google Container Registry.

```gcloud auth configure-docker```

![configure-docker](images\gke-guide\15-configure-docker.jpg)

14. Let's upload our Docker Image to Google Cloud Container Registry.

```docker push gcr.io/${PROJECT_ID}/insurance-streamlit:v1```

To use the image, we have to push it to the Google Cloud Container registry always.

![upload-image](images\gke-guide\16-push-the-image.PNG)

Now let's cross-check:

![go-to-container-registry](images\gke-guide\7-go-to-container-registry.PNG)

![cross-check-push](images\gke-guide\17-to-confirm.PNG)

15. Set up the project ID and Compute Engine Zone for gloud tool.


```terminal 
gcloud config set project $PROJECT_ID 
gcloud config set compute/zone us-central1
```


16. Create a Kubernetes Cluster.

**GUI:**

To use the Kubernetes engine provided by Google, we have to go here first.

![kubernetes-engine](images\gke-guide\2-go-to-kubernetes-engine.PNG)

Click on create cluster.

![create-cluster](images\gke-guide\3-click-on-create-cluster.PNG)

Here we give our requirements. If we select **Zonal**, then it means that our cluster will launch on zonal bases and if select **Regional**, then it means that our cluster will launch on Regional bases.

![configure-1](images\gke-guide\4-configuration(1).PNG)

We can go for more nodes but then it exceeds the requirements.

![configure-2](images\gke-guide\5-configuration(2).PNG)

![cluster-launched](images\gke-guide\6-wait-for-cluster-to-get-launched.PNG)

**CLI:**

```gcloud container clusters create streamlit-cluster --num-nodes=1```

17. **GUI:**

Click on Workloads. Then, click on Deploy.

![workload](images\gke-guide\18-go-back-to-kubernetes-deploy.PNG)

Click on select to select the image that we created.

![select-the-image](images\gke-guide\19-click-on-select.PNG)

Change the name if you want to!

![change-app-name](images\gke-guide\20-change-the-name.PNG)

Don't forget to select the cluster that we just created!

![select-the-cluster](images\gke-guide\21-select-the-cluster.PNG)

![deploying-process](images\gke-guide\22-while-deploying.PNG)

**CLI:**

Use the Kubernetes Cluster Management System to deploy our app replicas and schedule them to run on nodes in the cluster.

```kubectl create deployment insurance-streamlit --image=gcr.io/${PROJECT_ID}/insurance-streamlit:v1```

18. **GUI:**

Click on expose and expose the app using the Load Balancer service of Kubernetes or Google Cloud. 

![click-on-expose](images\gke-guide\23-click-on-expose.PNG)

We've to select the target port to 8501 because we are exposing our app to 8501 port number while creating the image.

![exposing](images\gke-guide\24-exposing.PNG)

**CLI:**

Expose the app to Internet traffic by creating an external IP and a Load Balancer

```kubectl expose deployment insurance-streamlit --type=LoadBalancer --port 80 --target-port 8501```

19. Checking our app. And we are good to go!

![good-to-go](images\gke-guide\25-click-here.PNG)

```kubectl get service```

20. Set up a DNS***

21. Scale up the application by adding additional pods, or delete the Service and container cluster to avoid incurring the unwanted charge. ***

To delete the cluster. 

![delete-cluster](images\gke-guide\27-after-using-click-on-delete.PNG)

*** To be explained later