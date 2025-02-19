# How to install label-studio?

First, install <a href="https://docs.docker.com/compose/install/"> Docker</a>.  
Then, open a terminal window and do the following :  
```plaintext
pip install label-studio  
label-studio start
```
(I used a conda environment but it is not necessary)  

A Log-in interface opens. Create an account if necessary.  

#### Did you forget your password?

In this case, stop the running interface by pressing ctrl+C. Before re-starting a new window, type the following :  
 ```plaintext
label-studio reset_password
```
Then you can log in as usual.

A window opens with label-studio interface. Go to the account settings and find the API key. Keep it. 

Then clone the label-studio rep :
```plaintext
git clone https://github.com/HumanSignal/label-studio-ml-backend.git  
```

Once it has been cloned, open the file located at label_studio_ml>examples>yolo>docker-compose.yaml  
Set the LABEL_STUDIO_API_KEY with the API key from your account settings (without the " around the key)  
Set the LABEL_STUDIO_URL as http://host.docker.internal:8080 (do **not** put the " around the address)  

# How to use a custom YOLO model?

Your YOLO model should be a .pt file (your_model.pt e.g.)  
In the same yolo directory as before, you should find a models folder. Put the your_model.pt file there.  
In the previous docker-compose.yaml file, ensure that ALLOW_CUSTOM_MODEL_PATH=true and MODEL_ROOT=/app/models  

Now, in the terminal window, go to the same yolo folder and run :    
```plaintext
docker compose up --build
```

Go back to the label-studio page and create a new project with the name you want.  
Then go to the Model section and set "Yolo" as name with URL=http://localhost:9090   
If the latter does not work, try : http://localhost:8080  

Finally, still in the project settings, go to the Labeling Interface and find the Code tab.  
There, copy-paste the following :  
```plaintext
<View>  
  <Image name="image" value="$image"/>  
  <RectangleLabels name="label" toName="image" model_path="your_model.pt" model_score_threshold="0.25" >  
    	  
    <Label value="orange" predicted_values="orange"/>  
  </RectangleLabels>  
</View>
```  

There you can change the classes depending on what your model predicts.  
predicted_values should designate the exact name being used in the training of your model.  
Label value allows to rename it for label-studio.  
To keep control of automated labeling, you can limit the confidence level by using model_score_threshold.  

## How to refresh the back-end configuration?  

This is in case you bring any modification to the back-end after having ran : docker-compose up --build   
By modification is meant changing something in docker-compose.yml or uploading a new model (.pt file).  
You need to run
```plaintext
docker-compose down
docker-compose up --build
```  


## How to tune the confidence threshold?  

Go to the settings of the model.  
Go to the Labeling Interface and then click on Code.  
In the RectangleLabels section, tune the model_score_threshold feature, between 0.0 and 1.0.  

If you already have labels on some images, to activate the new detection threshold you need to delete existing annotations.  

### How to delete existing annotations?  
Go to the main menu where all images are listed.  
Select the image where you want to delete annotations.  
Click the button on the top-left (when no image is selected, "Actions" is written on this button).  
Click "Delete predictions" or "Delete anotations".  

## Keyboard shortcuts  

When (auto)-labelling images, you can proceed faster by using <a href="https://labelstud.io/guide/labeling.html"> keyboard shortcuts</a>.  

#### Some principal commands :  
H : pan the image  
R : selects the tool to create frames  
CTRL+Z : cancel the last action  
CTRL+R : duplicate the selected frame  
DELETE : delete the selected frame  
Sometimes a red frame appears (usually when a frame is selected and then H is pressed), click on R to remove it.  

### Regularly save the annotations  
For each image, the first time you press "Submit".  
Then it will switch to an "Update" button.  
**Shortcut** : CTRL+ENTER  

### Warning (remove doubled annotations)
During the labelling, if you are in Auto-detect mode (purple frame, shortcut M) this can happen :  
if you draw a new rectangle with this tool, it will re-detect all instances thus creating two bounding boxes per orange.  
If it happens, press CTRL+Z until you see back this small rectangle. Then press it again to make it disappear.  
#### If you see a doubled frame, delete it immediatly.
#### This happens really often, be careful! It is not easy to see these doubled frames!

# References  

https://labelstud.io/tutorials/yolo  
