import json
import os

import cv2

test_data = json.load(open('./data10/annotations/fabric_testa_round2.json'))
anns = json.load(open('./result_data10.bbox.json'))

images_name = dict()
for image in test_data.get('images'):
    images_name[image.get('id')] = image.get('file_name')
data_home = '/tcdata/guangdong1_round2_testB_20191024/'
image_with_anns = dict()
for a in anns:
    score = a.get('score')
    name = images_name.get(a.get('image_id'))
    bbox = a.get('bbox')
    image_name = os.path.split(name)[-1]
    base_name = image_name.split('.')[0]
    image_path = f'{data_home}{base_name}/{image_name}'

    if image_with_anns.get(image_path):
        image_with_anns[image_path].append(a)
    else:
        image_with_anns[image_path] = [a]

for image_path, anns in image_with_anns.items():
    img = cv2.imread(image_path)
    for ann in anns:
        score = ann.get('score')
        name = images_name.get(ann.get('image_id'))
        bbox = ann.get('bbox')
        image_name = os.path.split(name)[-1]
        cv2.rectangle(img, pt1=(int(bbox[0]), int(bbox[1])), pt2=(int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3])),
                      color=(0, 255, 0),
                      thickness=4)
    cv2.imwrite(f'./result/{os.path.split(image_path)[-1]}', img)
