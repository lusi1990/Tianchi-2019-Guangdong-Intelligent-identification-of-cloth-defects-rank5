#!/bin/bash

DATA_HOME="/home/lu/WorkData/data/天池广东2019布匹瑕疵检测"

rm -rf ../data/fabric/
rm -rf ../data/pretrained/
mkdir -p ../data/fabric/defect_Images
mkdir -p ../data/fabric/template_Images
mkdir -p ../data/fabric/annotations
mkdir -p ../data/fabric/Annotations
mkdir -p ../data/pretrained

python3 copy_detect_images.py -d $DATA_HOME

cp -r $DATA_HOME/guangdong1_round2_train_part1_20190924/defect/* ../data/fabric/template_Images/ &&
  cp -r $DATA_HOME/guangdong1_round2_train_part2_20190924/defect/* ../data/fabric/template_Images/ &&
  cp -r $DATA_HOME/guangdong1_round2_train_part3_20190924/defect/* ../data/fabric/template_Images/ &&
  cp -r $DATA_HOME/guangdong1_round2_train2_20191004_images/defect/* ../data/fabric/template_Images/

cp $DATA_HOME/guangdong1_round2_train_part1_20190924/Annotations/anno_train.json ../data/fabric/Annotations/anno_train_20190925.json
cp $DATA_HOME/guangdong1_round2_train2_20191004_Annotations/Annotations/anno_train.json ../data/fabric/Annotations/anno_train_20191008.json
python merage_data_json.py
python guangdong_round2.py
echo "guangdong_round2.py over"
python guangdong_round2_100.py
echo "guangdong_round2_100.py over"
wget https://open-mmlab.oss-cn-beijing.aliyuncs.com/mmdetection/models/cascade_rcnn_r50_fpn_20e_20181123-db483a09.pth -O ../data/pretrained/cascade_rcnn_r50_fpn_20e_20181123-db483a09.pth
python transorfarm_concatenate_model.py
CUDA_VISIBLE_DEVICES=0 ./dist_train.sh ../config/fabric_defect/cascade_rcnn_r50_fpn_70e.py 1
CUDA_VISIBLE_DEVICES=0 ./dist_train.sh ../config/fabric_defect/cascade_rcnn_r50_fpn_400.py 1
python publish_model.py ../data/work_dirs/cascade_rcnn_r50_fpn_70e/latest.pth ../data/work_dirs/cascade_rcnn_r50_fpn_70e/latest-submit.pth
python publish_model.py ../data/work_dirs/cascade_rcnn_r50_fpn_400/latest.pth ../data/work_dirs/cascade_rcnn_r50_fpn_400/latest-submit.pth
