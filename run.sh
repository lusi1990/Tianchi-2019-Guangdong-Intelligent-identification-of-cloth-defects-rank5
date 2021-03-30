## 初始化测试集图片
#python inference/generate_test_json_round2.py
#./inference/dist_test.sh config/fabric_defect/cascade_rcnn_r50_fpn_70e.py weights/cascade_rcnn_r50_fpn_70e/latest.pth 1 --json_out data/result_map.json
#wait
#./inference/dist_test.sh config/fabric_defect/cascade_rcnn_r50_fpn_400.py weights/cascade_rcnn_r50_fpn_400/latest.pth 1 --json_out data/result_zj.json

./inference/dist_test.sh config/fabric_defect/cascade_rcnn_r50_fpn_data10.py weights/cascade_rcnn_r50_fpn_70e/latest-submit-f9f4a654.pth 1 --json_out data/result_data10.json

#wait
