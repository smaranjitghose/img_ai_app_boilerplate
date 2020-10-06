<h1 align = "center">Image Classification App Boilerplate</h1>

Have you been puzzled by tons of videos,blogs and other resources on the internet that want you to deploy your AI models?
<p align = "center"><img src = "https://media.giphy.com/media/8mndEBLsg9Whg2Sduv/giphy.gif" width = 30%></p>
Won't it be nice if you could have a template where you just put your trained model files, edit some promo text and Voila, it's done?
<p align = "center"><img src = "https://media.giphy.com/media/3NtY188QaxDdC/giphy.gif" width = 25%></p>
Well, look no further because this repository makes it as easy for you as it sounds!
<p align = "center"><img src = "https://media.giphy.com/media/ohMtDzrhrWgnK/giphy.gif" width = 25%></p>

## How to use this?
<p align = "center"><img src = "https://media.giphy.com/media/26AHPxxnSw1L9T1rW/giphy.gif" width = 50%></p>

__NOTE: For now we are exclusively focused on image classification models built using tensorflow/pytorch. Later we would expand to models dealing with text,speech data as well as training using MXNet or a julia environment__

- I assume you have Python(with Anaconda) installed in your operating system and set to path. If not, please visit [this](https://docs.anaconda.com/anaconda/install/)
- Now, that being done, please clone this repository for your local system and use this as the template repo on your GitHub
- After cloning the repo, move inside the repo

```cd ai_img_app_boilerplate ```

- Now, let's fetch our dependencies to run our app. [A python package called [StreamLit](https://docs.streamlit.io/en/stable/) is the heart this app]

```pip install -r requirements.txt```

- Now, let's put our model files in the app. Open the ```model``` sub-directory and paste your Keras h5 model files there
- Time for some changes!. First let's tackle how our machine learning model works.
    - Open VSCode or your favorite code editor/IDE

         ``` code .``` [Type this in the terminal to open VSCode if you already have it installed]

    - Now open the file ```img_classifier.py```
    - Search for ```labels``` in the code and set them as per your model training

       [say if you are are doing Cats Vs Dogs classification, then ```= {0: "Cats", 1: "Dogs"```]

       __NOTE: This is totally dependent on your model training__

    - Search for ```model``` and update the name of your model file.

      [say ```model = tensorflow.keras.models.load_model('model/catsvsdogs.h5')```]

    - Save the changes

- Continuing with changes to the User Interface or front of our app

    - Open the file ```img_classifier.py```

    - Search for ```st.title``` and update the Title of the app as per your application's needs

      [say ```st.title('Our Cats vs Dogs Classifier')```]

    - Now, let's do the same for our Page Title and tweak our SEO. Search for ```page_title``` and update it

      [say ```page_title="Cats Vs Dogs",```]

    - If you have some affiliation or maybe the app is made completely by you (perhaps with a group of your friends/colleageus) as a pet project, you can reflect that in the app by searching for ```st.subheader``` and updating it

      [say ```st.subheader("By John Doe and Jane Doe")```]

    - __SOME UPDATION OF OUR CONTACT PAGE__

    - You can add the name of you(and/or your teammates), profile picture,email and affiliation. Search for ```display_team``` and pass/update the following parameters: Name, path_to_image,Affiliation,email
    - For adding multiple contributors, you can call the same function multiple times.
    [Say
    ```python
    display_team("John Doe","./assets/john_doe.png","Stanford University","contact@johndoe.com"
    display_team("Jane Doe","./assets/jane_doe.png","Harvard University","contact@janedoe.com"
    ```
    ]

- [__Optional__] If you want to store your images in a cloud database like firebase, we have some more arrangements for you:
  - Open Your Web Browser
  - Visit Firebase [Console](https://console.firebase.google.com/)
  - Log in or Switch to your desired Google Account
  - Click on the ``+`` symbol to Add New Project
  - Give a project name say ``your-project-name`` [Make sure it is not a name of some other firebase project your already have] and click Continue
  - [__Unless you have lots of projects with Google Analytics__:] Keep it enabled and click on continue
    - [__If you opted for Google Analytics__] Select your Google Analytics account
  - Give it a few seconds to allocate the resources
  - Now click on the icon to create a web app
  - Give a name. [Preferrably the same name as your project name]
  - Unless required, do not select Hosting option and click Next
  - Copy the code in a ``config.txt`` file [This will be used later]
  - Click on Continue to Console
  - From the panel on the left, Click on __Storage__
  - Now click on __Get Started__
  - Click Next
  - Select a server closest to your location
  - Now click on the rules tab
  - Change the ``allow read, write: if request.auth != null;`` to `` allow read, write`` [Note this only for prototyping purposes. Refrain from doing this in a real-life scenario]
  - This basically allows us the upload and download the images without authenticating every time
  - Open the ```firebase_bro.py``` file
  - Update the config variable with the values previously stored inside the ``config.txt file`` [After this you can delete the ``config.txt`` file]
  - Save it
  - [__NOTE__:] If you are not using firebase please feel free to:
      - remove the ``firebase_bro.py`` file,
      - Delete the ``import firebase_bro`` line from the ``app.py`` file
      - ``firebase_bro.send_img(image)`` line inside the ``Home`` function of the ``app.py`` file
      - remove ``firebase`` and all the lines below the comment `` For Handling firebase and pyrebase dependency issues`` in the requirements.txt file

    __A FINAL NOTE: The current version of the app only supports jpg,png and jpeg images as input__

- Now, we are all set to test it. Open the terminal/command prompt and type ```streamlit run app.py```
- Give it a few seconds to start our local server, load Tensorflow and the other cool stuff and soon a window will pop up
- Upload Your Image, Click on Predict, Verify the working
- __NOTE: If you face any difficulties please raise an issue and let me know__
- Voila! You have your models deployed
- [__Optional:__] If you wish to share this as a prototype for others to try, please follow these steps:
    - Track,Commit and Push the changes to your GitHub repository that you initially made using this template repository
      ```
         git add .
         git commit -m "App v.0.0.1"
         git push origin master
      ```
      __NOTE: You must be inside the folder containing the app to send the update your copy on GitHub__

      - Now as per your choice of hosting, please refer the following guides:
        - [Heroku [Recommended for Beginners]](./Heroku_Guide.MD)
        - [Google Cloud Platform](.Guides/GKE_Guide.MD)
        - [Microsoft Azure](.Guides/Microsoft_Azure_Guide.MD)
        - Amazon Web Services [Bean Stalk or EC2]
        - Digital Ocean (__Comming Soon!__)
        - Linode (__Comming Soon!__)
        - Python Everywhere (__Comming Soon!__)



## Further Work 🏗

- [ ] Improve the UI of the app using custom HTML,CSS or REACT
- [ ] Make the App more descriptive
- [ ] Guide for Deployment to Digital Ocean
- [ ] Guide for Deployment to GCP
- [ ] Guide for Deployment to AWS
- [ ] Guide for Deployment to Azure
- [ ] Add Favicon option, Improve SEO
- [ ] Add Multiple Pages
     - [ ] Contact Page
     - [ ] About Page
     - [ ] Feedback Page
- [ ] Support for PyTorch models
- [ ] Support for MXNET models
- [ ] Support for saved_model TF format
- [ ] Add Animations
- [ ] Dark Mode
- [ ] Similar Efforts for a mobile app using TFLite + Flutter ( From building to serving)
- [ ] Experiment with TFJS
