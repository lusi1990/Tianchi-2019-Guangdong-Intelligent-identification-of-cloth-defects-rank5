"""
将需要推断的图片按照代码中的格式存放
"""
import os
import shutil

dst_dir = '/tcdata/guangdong1_round2_testB_20191024'


def main(pic_dir, dst_dir):
    """

    """
    pics_list = os.listdir(pic_dir)
    for pic_name in pics_list:
        pic_path = os.path.join(pic_dir, pic_name)
        base_name = os.path.basename(pic_name).split('.')[0]
        print(pic_path, base_name)
        new_dir = os.path.join(dst_dir, base_name)
        os.makedirs(new_dir)
        shutil.copy(pic_path, new_dir)


if __name__ == '__main__':
    main('/home/lu/share/海康面料采集图片/淡蓝色物料/NG物料', dst_dir)
