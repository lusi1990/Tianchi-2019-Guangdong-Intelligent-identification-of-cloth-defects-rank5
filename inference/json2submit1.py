# 转换 疵点标注格式 coco 格式 转为 ，左上 右下 点, 补全 图片信息
import json
import os

from tqdm import tqdm

# isfilter = True
PROJECT_HOME = os.path.dirname(os.path.dirname(__file__))
test_json_raw = json.load(open(os.path.join(PROJECT_HOME, "data/fabric/annotations/fabric_testa_round2.json"), "r"))
test_json = json.load(open(os.path.join(PROJECT_HOME, 'data/result_map.bbox.json'), "r"))

raw_image_filenames = []
images_ids = {}
for img in test_json_raw["images"]:
    images_ids[img["id"]] = img["file_name"]
    raw_image_filenames.append(img["file_name"])
raw_image_filenames = set(raw_image_filenames)

img_scores = dict()
for anno in tqdm(test_json):
    img_id = anno["image_id"]
    score = anno["score"]
    if img_id not in img_scores.keys():
        img_scores[img_id] = score
    else:
        if score > img_scores[img_id]:
            img_scores[img_id] = score

results = []
for anno in tqdm(test_json):
    img_id = anno["image_id"]
    if img_scores[img_id] > 0.1:
        label = anno["category_id"]
        bbox = anno["bbox"]
        # filename = images_ids[img_id]
        filename = images_ids[img_id].split('/')[-1]
        w, h = bbox[2], bbox[3]
        xmin = bbox[0]
        ymin = bbox[1]
        xmax = bbox[0] + w
        ymax = bbox[1] + h
        score = anno["score"]
        results.append(
            {'name': filename, 'category': int(label), 'bbox': [xmin, ymin, xmax, ymax], 'score': float(score)})

with open('./data/result_map.json', 'w') as fp:
    json.dump(results, fp, indent=4, separators=(',', ': '))
