# these functions are used to read images, parse annotations, and visualize bounding boxes (mainly within the CLIP check and figures)
import cv2
import os
import shutil
import random
import matplotlib.pyplot as plt

def train_test_val_folders(folder_path, train_ratio, val_ratio):
    # Define paths to the original image and label folders (i.e. a WC folder)
    images_dir = folder_path+"/images" 
    labels_dir = folder_path+"/labels" 
    if not os.path.exists(images_dir) or not os.path.exists(labels_dir):
        raise ValueError(f"Could not find the image or label folder\n{images_dir}\n{labels_dir}")

    # Define paths to the new train, val, and test folders for images and labels
    output_dirs = {
        "train": {
            "images": folder_path+"train/images",
            "labels": folder_path+"train/labels"
        },
        "val": {
            "images": folder_path+"val/images",
            "labels": folder_path+"val/labels"
        },
        "test": {
            "images": folder_path+"test/images",
            "labels": folder_path+"test/labels"
        }
    }

    # Create output directories if they don't exist
    for split in output_dirs.values():
        os.makedirs(split["images"], exist_ok=True)
        os.makedirs(split["labels"], exist_ok=True)

    # List all image files and shuffle for randomness
    all_images= [img for img in os.listdir(images_dir) if img.endswith(".jpg")]
    random.shuffle(all_images)

    # Determine split indices
    train_count = int(len(all_images) * train_ratio)
    val_count = int(len(all_images) * val_ratio)
    train_files = all_images[:train_count]
    val_files = all_images[train_count:train_count + val_count]
    test_files = all_images[train_count + val_count:]

    # Function to move image-label pairs
    def move_pairs(files, target):
        for image_file in files:
            # Move the image
            shutil.move(os.path.join(images_dir, image_file), os.path.join(output_dirs[target]["images"], image_file))
            
            # Move the corresponding label : ensure that they have the same name but a different extension
            label_file = os.path.splitext(image_file)[0] + ".txt"
            if os.path.exists(os.path.join(labels_dir, label_file)):
                shutil.move(os.path.join(labels_dir, label_file), os.path.join(output_dirs[target]["labels"], label_file))

    # Move files for each split
    move_pairs(train_files, "train")
    move_pairs(val_files, "val")
    move_pairs(test_files, "test")

    print(f"Dataset split into training, validation, and test sets with corresponding images and labels.")



def read_image(image_path):
    """Read and convert an image to RGB."""
    img = cv2.imread(image_path)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    return img_rgb

def parse_annotations(label_path, img_shape):
    """Parse bounding box annotations and convert to pixel coordinates."""
    height, width, _ = img_shape
    with open(label_path, 'r') as label_file:
        lines = label_file.readlines()
        annotations = []
        for line in lines:
            class_id, x, y, w, h = map(float, line.strip().split())
            x = int(x * width)
            y = int(y * height)
            w = int(w * width)
            h = int(h * height)
            annotations.append((x, y, w, h))
    return annotations

def draw_bounding_boxes(img, annotations):
    """Draw all bounding boxes on the original image."""
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.axis('off')
    for x, y, w, h in annotations:
        rect = plt.Rectangle((x - w // 2, y - h // 2), w, h, linewidth=2, edgecolor='r', facecolor='none')
        ax.add_patch(rect)
    plt.show()

def display_cropped_boxes(img, annotations):
    """Display images cropped to each bounding box."""
    height, width, _ = img.shape
    for i, (x, y, w, h) in enumerate(annotations):
        x_min = max(x - w // 2, 0)
        y_min = max(y - h // 2, 0)
        x_max = min(x + w // 2, width)
        y_max = min(y + h // 2, height)
        cropped_img = img[y_min:y_max, x_min:x_max]
        plt.imshow(cropped_img)
        plt.axis('off')
        plt.title(f"Bounding Box {i+1}")
        plt.show()

def get_cropped_boxes(img, annotations):
    """Return a list of images cropped to each bounding box."""
    height, width, _ = img.shape
    cropped_images = []
    for x, y, w, h in annotations:
        x_min = max(x - w // 2, 0)
        y_min = max(y - h // 2, 0)
        x_max = min(x + w // 2, width)
        y_max = min(y + h // 2, height)
        cropped_img = img[y_min:y_max, x_min:x_max]
        cropped_images.append(cropped_img)
    return cropped_images

def pad_images_to_fixed_size(images, target_width, target_height):
    """Pad images with blue color to a fixed resolution."""
    padded_images = []
    for img in images:
        height, width, _ = img.shape
        pad_top = (target_height - height) // 2
        pad_bottom = target_height - height - pad_top
        pad_left = (target_width - width) // 2
        pad_right = target_width - width - pad_left
        padded_img = cv2.copyMakeBorder(img, pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_CONSTANT, value=[255, 0, 0])
        padded_images.append(padded_img)
    return padded_images

def quickview(image_path, label_path):
    """Main function to read image, parse labels, and visualize bounding boxes."""
    img_rgb = read_image(image_path)
    annotations = parse_annotations(label_path, img_rgb.shape)
    print(f"Number of bounding boxes: {len(annotations)}\n")
    draw_bounding_boxes(img_rgb, annotations)
    display_cropped_boxes(img_rgb, annotations)    