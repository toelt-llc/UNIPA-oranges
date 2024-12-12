## Number of instances (865, of which 625 to be annotated)

### Unannotated (total : 617)
OneDrive - new images : 277 (48 evening_sunny, 5 evening_cloudy, 106 afternoon_sunny, 118 afternoon_cloudy)  
Roboflow - unannotated : 340 morning_sunny 

### Annotated (total : 248)
First large dataset : 64  
LabelStudio-retrain 1 : 11 (three afternoon types : 2 rainy, 4 sunny, 5 cloudy)  
LS-retrain 2 : 38 afternoon_cloudy  
LS-retrain 3 : 24 afternoon_sunny  
LS-retrain 4 : 111 morning_cloudy_sunny  

#### Remark  
90 images are in the first large dataset, but some were duplicates and were also found in the LS-retrain folders. This comes from our Roboflow management, there may be files copied to some other folders.  
In all cases, these duplicates shared the exact same number of instances, i.e. they were exact **annotated** duplicates.  
We therefore end up with 64 images instead of 90 in this first large dataset (the old orange_night dataset). 
