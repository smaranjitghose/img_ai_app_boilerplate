
<h1 align = "center">Google Kubernetes Engine Guide</h1>

1. Log in to Your preferred Google Account and Open Your [Google Cloud Console](https://console.cloud.google.com/)

2. Search for Manage Resources

3. Click on create New Project

4. Give a suitable Project Name (say your-project-name)

5. Open Google Cloud Console from the top right 

6. Fetch our source code using git

  ```git clone  https://github.com/yourusername/your-project-repo-name.git ```

7. Checking what we got

  ```ls -aH ```

8. Navigating to the directory that contains our source code

```cd your-project-repo-name```

9. Setting Project ID Environment Variable

  ```export PROJECT_ID=export PROJECT_ID=your-project-name```

10. Now let's build our docker image and tag it for uploading

  ```docker build -t gcr.io/${PROJECT_ID}/insurance-streamlit:v1```

11. Let's check what we got

  ```docker images```

12. Ensure Google Cloud [Container Registry](https://cloud.google.com/container-registry) is enabled

13. Authenticate Google Container Registry

  ```gcloud auth configure-docker```

14. Let's upload our Docker Image to Google Cloud Container Registry

  ```docker push gcr.io/${PROJECT_ID}/insurance-streamlit:v1```

15. Set up the project ID anf Compute Engine Zone for gloud tool


```terminal 
gcloud config set project $PROJECT_ID 
gcloud config set compute/zone us-central1
```


16. Create a Kubernetes Cluster

  ```gcloud container clusters create streamlit-cluster --num-nodes=2```

17. Use Kubernetes Cluster Management System to deploy our app replicas and schdeule them to run on nodes in the cluster

  ```kubectl create deployment insurance-streamlit --image=gcr.io/${PROJECT_ID}/insurance-streamlit:v1```

18. Expose the app to Internet traffic by creating an external IP and a Load Balancer

  ```kubectl expose deployment insurance-streamlit --type=LoadBalancer --port 80 --target-port 8501```

19. Checking our app

  ```kubectl get service```

20. Set up a DNS***

21. Scale up the application by adding additional pods, or delete the Service and container cluster to avoid incurring unwanted charge***

*** To be explained later


