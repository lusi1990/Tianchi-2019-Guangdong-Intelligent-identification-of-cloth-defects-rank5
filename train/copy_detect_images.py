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
    for root_dir, dirs, files in os.walk(args.data_home):
        for file_name in files:
            if not file_name.endswith('jpg'):
                continue
            if file_name.startswith('template_'):
                continue
            if 'normal' in root_dir:
                continue
            image_path = os.path.join(root_dir, file_name)
            images.append(image_path)
            # print(root_dir, dirs, files)
    print(len(images))
    for image_path in images:
        print(f'copy {image_path}')
        shutil.copy(image_path, '../data/fabric/defect_Images')


if __name__ == '__main__':
    main()
