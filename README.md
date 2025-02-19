# Getting Started  
1. Place the given dataset in the `FINAL_SUBIMAGES` folder.  
2. Create the conda environment:  
   ```bash
   conda env create -f environment.yml  
   ```  
3. Activate the environment:  
   ```bash
   conda activate conda_dataset  
   ```  
4. Use `benchmark.csv` and `wc_benchmark.csv` in `figures.ipynb` to reproduce the results.  

---

## `environment.yml`  
This file allows you to reproduce the conda environment.  

## `detection.ipynb`  
Contains code to train a YOLO or RT-DETR model on YOLO data or `FINAL_SUBIMAGES`.  

## `data_pipeline.ipynb`  
Use this notebook with new data to generate sub-images in YOLO format using `CUT-IMG`.  
Once processed, you can run `detection.ipynb` as usual.  
At the bottom of the notebook, you’ll find instructions on converting YOLO format to COCO format.  

## `clip_check.ipynb`  
Use this notebook to process new sub-images before passing them to `CUT-IMG` in `data_pipeline.ipynb`.  
If using the provided sub-images from `FINAL_SUBIMAGES`, they are already sorted.  

## `figures.ipynb`  
This notebook reproduces the figures from the paper.  
Before running `figures.ipynb`, generate `clip_stats.csv` by running `clip_check.ipynb` (see the bottom of the notebook).
