import os
import json

# switch the current structure to an int id
def to_id(strr):
    # current structure: MS280_2025-01-20_03 (WCID_YYYY-MM-DD_SUBID)
    # where ID is the ID of the initial images
    # and SUBID is one of the subimages associated to this initial image
    char1 = str(ord(strr[0])-64) 
    char2 = str(ord(strr[1])-64) # for A-Z it will assign 1,...,26
    pieces = strr[2:].split("-")

    piece1 = pieces[0].split('_')[0]+pieces[0].split('_')[1]
    piece2 = pieces[2].split('_')[0]+pieces[2].split('_')[1]
    return int(char1+char2+piece1+pieces[1]+piece2)

# main converter
def all_yolo_to_coco(images_dir, labels_dir, output_file):
    coco_format = {
        "images": [],
        "annotations": [],
        "categories": [{"id": 0, "name": "orange"}]
    }

    # bbox converter
    def yolo_to_coco(x_center, y_center, width, height, img_width, img_height):
        x_min = (x_center - width / 2) * img_width
        y_min = (y_center - height / 2) * img_height
        w = width * img_width
        h = height * img_height
        return x_min, y_min, w, h

    annotation_id = 0
    image_files = sorted(os.listdir(images_dir))
    total_files = len(image_files)
    for idx, image_file in enumerate(image_files):
        if not image_file.endswith(".jpg"):
            continue

        print(f"Processing {idx + 1}/{total_files}: {image_file}")

        image_path = os.path.join(images_dir, image_file)
        label_path = os.path.join(labels_dir, image_file.replace(".jpg", ".txt"))

        if not os.path.exists(label_path):
            print(f"Label file missing for {image_file}. Skipping.")
            continue
        img_id = to_id(image_file.split('.')[0]) # we do not want the extension

        # image details
        coco_format["images"].append({
            "id": img_id, # this is also used for image_id below
            "file_name": image_file,
            "height": 640,
            "width": 640
        })

        # label processing
        with open(label_path, "r") as file:
            for line in file:
                parts = line.strip().split()
                class_id = int(parts[0])
                x_center, y_center, width, height = map(float, parts[1:])
                x_min, y_min, w, h = yolo_to_coco(x_center, y_center, width, height, 640, 640)

                coco_format["annotations"].append({
                    "id": annotation_id,
                    "image_id": img_id, # needs to be the same id as the associated image
                    "category_id": class_id,
                    "bbox": [x_min, y_min, w, h],
                    "area": w * h,
                    "iscrowd": 0
                })
                annotation_id += 1

    with open(output_file, "w") as f:
        json.dump(coco_format, f, indent=4)

    print(f"COCO annotations saved to {output_file}")