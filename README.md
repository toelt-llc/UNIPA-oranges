# UNIPA Oranges Dataset

A comprehensive dataset for orange detection in agricultural fields, featuring diverse environmental conditions and lighting scenarios.

## Dataset Overview

Reliable, on-tree detection and maturity assessment of oranges in real orchards is still limited by the lack of diverse, well-annotated datasets. This project describes a new *orange on-field dataset*, a large-scale, image collection under high environmental variability designed for fruit detection, classification, and maturity assessment in real-world orchard environments. This dataset was created from scratch to train and evaluate object detection models for oranges in field conditions. It contains **5,025 annotated images** captured across various times of day and weather conditions, providing robust training data for agricultural computer vision applications. Images were collected using different smartphone cameras and preprocessed through a custom cropping algorithm to optimize annotation efficiency. The dataset was labeled using a semi-automated approach, combining YOLO-based pre-annotations refined manually in Roboflow. To improve annotation quality, a CLIP-based verification step filtered images with incorrect labels. The dataset is provided with YOLO and COCO annotations, making it suitable for multiple object detection frameworks. Additionally, a benchmark evaluation was conducted using state-of-the-art models, including YOLO (v5, v8, v10, v11) and RT-DETR, assessed via standard precision, recall, and F1-score metrics. Results indicate that recent YOLO models outperform RT-DETR in both accuracy and inference speed. The structured format and environmental diversity of the dataset make it valuable for AI applications in precision agriculture, such as  fruit maturity assessment, yield estimation and automated harvesting. 



### Dataset Statistics

```
╒═════════════════╤══════════╤═══════════════╤═════════════╤══════════════╕
│ Environment     │ Images   │ Label Files   │ Avg Width   │ Avg Height   │
╞═════════════════╪══════════╪═══════════════╪═════════════╪══════════════╡
│ AC_CLIP_AFT_CLO │ 1082     │ 1082          │ 640         │ 640          │
├─────────────────┼──────────┼───────────────┼─────────────┼──────────────┤
│ AR_CLIP_AFT_RAI │ 13       │ 13            │ 629         │ 628          │
├─────────────────┼──────────┼───────────────┼─────────────┼──────────────┤
│ AS_CLIP_AFT_SUN │ 625      │ 625           │ 640         │ 640          │
├─────────────────┼──────────┼───────────────┼─────────────┼──────────────┤
│ EC_CLIP_EVE_CLO │ 34       │ 34            │ 640         │ 640          │
├─────────────────┼──────────┼───────────────┼─────────────┼──────────────┤
│ ES_CLIP_EVE_SUN │ 224      │ 224           │ 640         │ 640          │
├─────────────────┼──────────┼───────────────┼─────────────┼──────────────┤
│ IN_CLIP_INDOOR  │ 57       │ 57            │ 640         │ 640          │
├─────────────────┼──────────┼───────────────┼─────────────┼──────────────┤
│ MC_CLIP_MOR_CLO │ 126      │ 126           │ 640         │ 640          │
├─────────────────┼──────────┼───────────────┼─────────────┼──────────────┤
│ MS_CLIP_MOR_SUN │ 2768     │ 2768          │ 640         │ 640          │
├─────────────────┼──────────┼───────────────┼─────────────┼──────────────┤
│ NI_CLIP_NIGHT   │ 96       │ 96            │ 640         │ 640          │
╘═════════════════╧══════════╧═══════════════╧═════════════╧══════════════╛

```

### Dataset Structure

```
yoloorangedataset/
 ├── AC_CLIP_AFT_CLO       → Afternoon, Cloudy
 ├── AR_CLIP_AFT_RAI       → Afternoon, Rainy
 ├── AS_CLIP_AFT_SUN       → Afternoon, Sunny
 ├── EC_CLIP_EVE_CLO       → Evening, Cloudy
 ├── ES_CLIP_EVE_SUN       → Evening, Sunny
 ├── IN_CLIP_INDOOR        → Indoor
 ├── MC_CLIP_MOR_CLO       → Morning, Cloudy
 ├── MS_CLIP_MOR_SUN       → Morning, Sunny
 ├── NI_CLIP_NIGHT         → Night
 └── yolo10x_orange.pt     → Best trained model
```

## Getting Started

### Prerequisites

- Conda or Miniconda installed
- Python 3.x

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/toelt-llc/UNIPA-oranges.git
   cd UNIPA-oranges
   ```

2. Create a `FINAL_SUBIMAGES` folder to store the provided dataset:
   ```bash
   mkdir FINAL_SUBIMAGES
   ```

3. Create the conda environment:
   ```bash
   conda env create -f environment.yml
   ```

4. Activate the environment:
   ```bash
   conda activate conda_dataset
   ```

### Reproducing Results

To reproduce the results from the paper, use the provided benchmark files:
```bash
jupyter notebook figures.ipynb
```

The notebook uses `benchmark.csv` and `wc_benchmark.csv` to generate all figures and statistics.

## Repository Contents

### Core Notebooks

#### `detection.ipynb`
Train YOLO or RT-DETR models on the dataset. Supports both YOLO format data and custom `FINAL_SUBIMAGES` structure.

#### `data_pipeline.ipynb`
Process new data and generate sub-images in YOLO format using `CUT-IMG`. Once processed, images can be used directly with `detection.ipynb`. Also includes instructions for converting YOLO format to COCO format.

#### `clip_check.ipynb`
Pre-process and sort new sub-images before passing them to `CUT-IMG` in `data_pipeline.ipynb`. The provided `FINAL_SUBIMAGES` are already sorted and don't require this step. Run this notebook to generate `clip_stats.csv` for use in `figures.ipynb`.

#### `figures.ipynb`
Reproduce all figures from the paper. **ADD ARXIV LINK**

**Note:** Before running this notebook, generate `clip_stats.csv` by running the last cells of `clip_check.ipynb`.

#### `roboflow_api.ipynb`
Download unannotated images from Roboflow. Useful for recovering files that were uploaded but not annotated, or files from deleted folders.

### Python Scripts

- **`img_bbox.py`** - Bounding box utilities for image processing
- **`yolo_to_coco.py`** - Convert annotations from YOLO format to COCO format

### Documentation

- **`labelstudio.md`** - Complete guide for using Label Studio to annotate new datasets
- **`environment.yml`** - Conda environment specification for reproducibility

### Data Files

- **`benchmark.csv`** - Benchmark results for model evaluation
- **`wc_benchmark.csv`** - Additional benchmark metrics

## Citation

If you use this dataset in your research, please cite:

```
ADD ARXIV SOON
```
