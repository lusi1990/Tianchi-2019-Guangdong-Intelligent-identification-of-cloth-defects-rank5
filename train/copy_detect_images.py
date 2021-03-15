#! /usr/bin/env python3
import argparse
import os
import shutil


def parse_args():
    parser = argparse.ArgumentParser(description='image file copy')
    parser.add_argument('-d', "--data_home", help='images data file path', )
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    if not args.data_home:
        print('查看帮助: python3 copy_detect_images.py -h')
        return
    images = list()
    template_dict = dict()
    for root_dir, dirs, files in os.walk(args.data_home):
        for file_name in files:
            if not file_name.endswith('jpg'):
                continue
            if file_name.startswith('template_'):
                temp_path = os.path.join(root_dir, file_name)
                template_dict[os.path.split(root_dir)[-1]] = temp_path
                continue
            if 'normal' in root_dir:
                continue
            image_path = os.path.join(root_dir, file_name)
            images.append(image_path)
            # print(root_dir, dirs, files)
    print(len(images))
    # 复制检测图片
    for image_path in images:
        print(f'copy {image_path}')
        shutil.copy(image_path, '../data/fabric/defect_Images')
    # 复制模板图片
    for name, template_path in template_dict.items():
        template_home = f'../data/fabric/template_Images/{name}'
        if not os.path.isdir(template_home):
            os.makedirs(template_home)
        shutil.copy(template_path, f'../data/fabric/template_Images/{name}')


if __name__ == '__main__':
    main()
