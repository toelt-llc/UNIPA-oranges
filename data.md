## Number of instances (862, of which 625 to be annotated)

### Unannotated (total : 617)
OneDrive - new images : 277 (48 evening_sunny, 5 evening_cloudy, 106 afternoon_sunny, 118 afternoon_cloudy)  
Roboflow - unannotated : 340 morning_sunny 

### Annotated (total : 245)
First large dataset : 63  
LabelStudio-retrain 1 : 11 (three afternoon types : 2 rainy, 4 sunny, 5 cloudy)  
LS-retrain 2 : 38 afternoon_cloudy  
LS-retrain 3 : 24 afternoon_sunny  
LS-retrain 4 : 110 morning_cloudy_sunny (21 cloudy, 89 sunny)    

#### Remark  
90 images are in the first large dataset, but some were duplicates and were also found in the LS-retrain folders. This comes from our Roboflow management, there may be files copied to some other folders.  
In all cases, these duplicates shared the exact same number of instances, i.e. they were exact **annotated** duplicates.  
We therefore end up with 64 images instead of 90 in this first large dataset (the old orange_night dataset).  
Actually we end up with 63 images since one contained the face of Alessandro.  
All images have been checked. In case of the presence of a person, the concerned image has been cropped out of this sensitive region.

Also removed one annotated image from orange_morning_sunny, Alessandro had his face visible on it (and it contained only two instance in all cases). Thus it is reduced to 110 images instead of 110.    
Removed another one from the first large dataset, hence this one is reduced to 63 images.
