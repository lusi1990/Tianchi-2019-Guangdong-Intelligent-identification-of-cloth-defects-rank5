"""
将训练集中的图片按照推断代码中的格式存放
"""
import os
import shutil


def main(src_dir, dst_dir):
    """

    """
    pics_list = os.listdir(src_dir)
    for pic_name in pics_list:

        pic_path = os.path.join(src_dir, pic_name)
        base_name = os.path.basename(pic_name).split('.')[0]
        if not base_name.startswith('201903'):
            continue

        new_dir = os.path.join(dst_dir, base_name)
        print(pic_path, new_dir)

        shutil.copytree(pic_path, new_dir)
        template_path = os.path.join(new_dir, base_name)
        if not os.path.isdir(template_path):
            os.makedirs(template_path)
        temp_name = 'template_{}.jpg'.format(base_name.split('_')[0])
        shutil.move(os.path.join(new_dir, temp_name), os.path.join(template_path, temp_name))


if __name__ == '__main__':
    src_dir = './data/fabric/template_Images'
    dst_dir = '/tcdata/guangdong1_round2_testB_20191024'

    main(src_dir, dst_dir)
