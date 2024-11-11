# How to install label-studio?

First, install Docker.  
Then, open a terminal window and do the following :  

pip install label-studio  
label-studio start  
(I used a conda environment but it is not necessary)  

A window opens with label-studio interface. Go to the account settings and find the API key. Keep it. 

Then clone the label-studio rep : git clone https://github.com/HumanSignal/label-studio-ml-backend.git  

Once it has been cloned, open the file located at label_studio_ml>examples>yolo>docker-compose.yaml  
Set the LABEL_STUDIO_API_KEY with the API key from your account settings (without the " around the key)  
Set the LABEL_STUDIO_URL as http://host.docker.internal:8080 (do **not** put the " around the address)  

# How to use a custom YOLO model?

Your YOLO model should be a .pt file (your_model.pt e.g.)  
In the same yolo directory as before, you should find a models folder. Put the your_model.pt file there.  
In the previous docker-compose.yaml file, ensure that ALLOW_CUSTOM_MODEL_PATH=true and MODEL_ROOT=/app/models  

Now, in the terminal window, go the the same yolo folder and run : docker compose up --build  

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

Go in the settings of the model.  
Go to the Labeling Interface and then click on Code.  
In the RectangleLabels section, tune the model_score_threshold feature, between 0.0 and 1.0.  

## Keyboard shortcuts  
When (auto)-labelling images, you can go faster by using <a href="https://labelstud.io/guide/labeling.html"> keyboard shortcuts </a>.

# References  

https://labelstud.io/tutorials/yolo  
