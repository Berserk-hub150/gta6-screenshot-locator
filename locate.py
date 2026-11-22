import argparse, json
from PIL import Image
from matcher import locate
if __name__=='__main__':
    parser=argparse.ArgumentParser(description='Locate a same-scale north-up minimap crop in a reference atlas.')
    parser.add_argument('atlas')
    parser.add_argument('crop')
    args=parser.parse_args()
    with Image.open(args.atlas) as atlas, Image.open(args.crop) as crop:
        print(json.dumps(locate(atlas,crop),indent=2))
