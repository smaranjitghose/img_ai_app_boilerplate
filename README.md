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
- Now, that being done, please clone this repository for your local system and use this as template repo on your GitHub
- After cloning the repo, move inside the repo

```cd ai_img_app_boilerplate ```

- Now, let's fetch our dependencies to run our app. [A python package called [StreamLit](https://docs.streamlit.io/en/stable/) is the heart this app]

```pip install -r requirements.txt```

- Now, let's put our model files in the app. Open the ```model``` sub-directory and paste your keras h5 model files there
- Time for some final changes:
    - Open VSCode or your favourite editor and edit the file ```app.py```

         ``` code .```
    - Search for ```labels``` in your code and set them as per your model training

       [say if you are are doing Cats Vs Dogs classification, then ```= {0: "Cats", 1: "Dogs"```]

       __NOTE: This is totally dependent on your model training__

    - Search for ```model``` and update the name of your model file.

      [say ```model = tensorflow.keras.models.load_model('model/catsvsdogs.h5')```]

    - Search for ```st.title``` and update the Title of the app as per your application's needs

      [say ```st.title('Our Cats vs Dogs Classifier')```]

    - Now, let's do the same for our Page Title and tweak our SEO. Search for ```page_title``` and update it

      [say ```page_title="Cats Vs Dogs",```]

    - If you have some affliation or maybe the app is made completely by you (perhaps with a group of your friends/collegeus) as a pet project, you can reflect that in the app by seaching for ```st.subheader``` and updating it

      [say ```st.subheader("By John Doe and Jane Doe")```]

    - __SOME UPDATION OF OUR CONTACT PAGE__

    - You can add the name of you(and/or your teammates), profile picture,email and affliation. Search for ```display_team``` and pass/update the following parameters: Name, path_to_image,Affliation,email
    - For adding multiple contributors, you can call the same function multiple times.
    [Say
    ```python
    display_team("John Doe","./assets/john_doe.png","Stanford University","contact@johndoe.com"
    display_team("Jane Doe","./assets/jane_doe.png","Harvard University","contact@janedoe.com"
    ```
    ]


    __A FINAL NOTE: The current version of the app only supports jpg,png and jpeg images as input__
- Now, we are all set to test it. Open the terminal/command prompt and type ```streamlit run app.py```
- Give it a few seconds to start our local server, load tensorflow and the other cool stuff and soon a window will pop up
- Upload Your Image, Click on Predict, Verify the working
- __NOTE: If you face any difficulties please raise an issue and let me know__
- Voila! You have your models deployed
- [__Optional:__] If you wish to share this as a prototype for others to try, please follow these steps:
    - Track,Commit and Push the changes to your GitHub repository that you intially made using this template repository
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
