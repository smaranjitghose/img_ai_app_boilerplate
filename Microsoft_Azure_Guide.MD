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
        
        az group create --name your-project --location eastus

9. Cool! Now we need to build our Container Registry inside the resource group

        az acr create --name your-project-registry --resource-group your-project --sku basic --admin-enabled true
        
