# Integrating our Trained Model:

<p align = "center"><img src = "https://media.giphy.com/media/9VfMSBNUmELTi/giphy.gif" width = 40%></p>



- Open the `model` sub-directory 

```
cd model
start .
```

- Paste your `Keras.h5` model files there

- Shoot up your favorite code editor/IDE (I prefer VSCode).

    `code .` [Type this in the terminal to open VSCode if you already have it installed]

- Now open the file `img_classifier.py`

- Search for the variable `labels` in the code and set its' value as per the labels of the dataset used for training your model. For example: if you are doing Cats Vs Dogs classification then,

```
labels = {0: "Cats", 1: "Dogs"}
```

**NOTE: This is totally dependent on your model training**

- Update the value of the variable `model` with the path of your model file. For Example:

```
     model = tensorflow.keras.models.load_model('model/catsvsdogs.h5')
```
    
- Save the changes.
