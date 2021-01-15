# Frontend and Content Changes

<p align = "center"><img src = "https://media.giphy.com/media/3o72F2vvc71VgmlvgI/giphy.gif" width = 50%></p>

Continuing with changes to the User Interface or the frontend of our app please follow the steps mentioned below:

### Home Page 🏡

1. Open `app.py`

2. Search for `st.title` and update the Title of the app as per your application's needs.

    [say `st.title('Our Cats vs Dogs Classifier')`]

3. Now search for variable `page_title` and update it with the same. This will tweak the *SEO*. 

    [say `page_title="Cats Vs Dogs",`]

4. If you have some affiliation or maybe the app is made completely by you (perhaps with a group of your friends/colleagues) as a pet project, you can reflect that in the app by searching for `st.subheader` and updating it

      [say ```st.subheader("By John Doe and Jane Doe")```]


__^^ Delete any or all code that you won't use from the above__

### Contact Page 🤳

1. Search for the function call `display_team("Your Awesome Name", "./assets/profile_pic.png","Your Awesome Affliation","hello@youareawesome.com"` and update the following parameters as per your own discretion:

    - **Name**
    - **path_to_image** (I would suggest storing the images inside `assets/images/`
    - **Affiliation**
    - **email**

2. For adding multiple members, you can call the same function multiple times. For example:

```
    display_team("John Doe","./assets/john_doe.png","Stanford University","contact@johndoe.com")
    display_team("Jane Doe","./assets/jane_doe.png","Harvard University","contact@janedoe.com")
```