<h1 align = "center"> Microsoft Azure Deployment Guide</h1>

1. Visit [Azure Portal](https://portal.azure.com/).
2. Log in with your Microsoft Account [ Create one using LinkedIn or GitHub if you do not have it)
3. Click on terminal icon on the top right to open __Azure Cloud Shell__
4. Intialize your shell environment. [ I prefer going with ```Bash``` but I guess ```Powershell``` would work just fine too]
5. Select your subscription [ Google a bit to figure out how to get a free trial subscription for 12 months or a Azure Students Subscription]
6. Give it some seconds to mount to memory
7. If you are not logged in already, type ```az login``` and provide your credentials
8. Now lets create a __Resource Group__ for our __Container Registry__ and __Web App Service__ with the name say ```your-project``` and select the East US server
(This works fine usually but for more details please have a look at the documentation on how to select the location)
        
        az group create --name your-project-RG --location eastus

9. Cool! Now we need to build our Container Registry with the name say ``your-project-RG`` and standard ``basic`` with admin access enabled inside the resource group

        az acr create --name your-project-registry --resource-group your-project-RG --sku basic --admin-enabled true
        
10. Let's fetch our source code using git

        git clone https://github.com/yourusername/your-project-repo-name.git

11. Checking what we got

        ls -aH

12. Navigating inside our source folder
        
        cd your-project-name
        
13. Send the contents of this directory to Azure Container Registry which uses our Dockerfile to build the image and store it

        az acr build --registry your-project-registry --resource-group your-project-RG --image your-project-name .
        
14. Give this a couple of minutes

15. Create an App Service Plan for the web app 

        az appservice plan create --resource-group your-project-RG --name your-project-SP --location eastus --is-linux --sku B1
        
 16. Now,we shall finally create our web app from the Docker container in the Azure Container Registry
        
    az webapp create --name your-project-name --resource-group your-project-RG --plan your-project-SP --image your-project-registry.azurecr.io/your-project-name:latest
        
17. To redeploy the webapp

        az acr build --registry your-project-regitry --resource-group your-project-RG --image your-project-name
