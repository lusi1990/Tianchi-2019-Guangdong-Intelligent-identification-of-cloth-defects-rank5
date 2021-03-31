"""
for cascade rcnn
cascadeRCNN是由一系列的检测模型组成，每个检测模型都基于不同IOU阈值的正负样本训练得到，前一个检测模型的输出作为后一个检测模型的输入，
因此是stagebystage的训练方式，而且越往后的检测模型，其界定正负样本的IOU阈值是不断上升的。
"""
import torch
import os
from torch.nn import init
import numpy as np

model_name = "../data/pretrained/cascade_rcnn_r50_fpn_20e_20181123-db483a09.pth"

model_coco = torch.load(model_name)

# weight
model_coco["state_dict"]["backbone.conv1.weight"] = torch.cat([model_coco["state_dict"]["backbone.conv1.weight"]] * 2,
                                                              dim=1)

num_class = 10
model_coco['state_dict']['bbox_head.0.fc_cls.weight'].resize_(num_class, 1024)
model_coco['state_dict']['bbox_head.1.fc_cls.weight'].resize_(num_class, 1024)
model_coco['state_dict']['bbox_head.2.fc_cls.weight'].resize_(num_class, 1024)
model_coco['state_dict']['bbox_head.0.fc_cls.bias'].resize_(num_class)
model_coco['state_dict']['bbox_head.1.fc_cls.bias'].resize_(num_class)
model_coco['state_dict']['bbox_head.2.fc_cls.bias'].resize_(num_class)
model_coco['state_dict']['bbox_head.0.fc_reg.weight'].resize_(4, 1024)

print(model_coco["state_dict"]["backbone.conv1.weight"].shape)

# save new model
torch.save(model_coco,
           "../data/pretrained/concatenate_coco_pretrained_cascade_rcnn_r50_fpn_20e_data10.pth")
