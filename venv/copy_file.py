import argparse
import os
import xml.etree.cElementTree as ET
import shutil

def create_parser():
    parser = argparse.ArgumentParser(description='file with two paths')
    parser.add_argument("file", help="This is the 'file'")
    return parser

def return_filename(parser):
    args = parser.parse_args()
    file = args.file
    return file

def root_xml(filename):
    try:
        tree = ET.ElementTree(file=filename)
        return tree.getroot()
    except:
        raise Exception("error of xml parsing")


if __name__ == '__main__':
    file_name = return_filename(create_parser())
    if not os.path.exists(file_name):
        raise FileNotFoundError("xml file not found")
    root = root_xml(file_name)
    for child in root:
        source_file = os.path.join(child.attrib["source_path"],
                                   child.attrib["file_name"])
        dist_file = os.path.join(child.attrib["destination_path"],
                                 child.attrib["file_name"])
        exist_source_file = os.path.exists(source_file)
        exist_dist_path = os.path.exists(child.attrib["destination_path"])
        if exist_source_file and exist_dist_path:
            shutil.copy2(source_file, dist_file)
            print(f'{child.attrib["file_name"]} file copied')
        elif not exist_source_file:
            print(f'{child.attrib["file_name"]} file not found')
        else:
            print(f'{child.attrib["file_name"]} destination path not exist')

