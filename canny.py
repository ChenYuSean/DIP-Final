import os
import argparse
import cv2
import numpy as np

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', default="./SampleImages/lena.png", type=str)
    parser.add_argument('--output_path',default="./OutputImages/canny",type=str)
    parser.add_argument('-tl', '--threshold_low', default=50, type=float)
    parser.add_argument('-th', '--threshold_high', default=200, type=float)
    return parser.parse_args()

def main():
    np.random.seed(0)
    args = parse_args()
    
    output_folder = args.output_path
    os.makedirs(output_folder, exist_ok=True)

    input_files = []
    if os.path.isdir(args.input_path):
        input_files = [os.path.join(args.input_path, f) for f in os.listdir(args.input_path) if f.endswith('.png') or f.endswith('.jpg')]
    else:
        input_files.append(args.input_path)
        
    for file in input_files:
        fname = os.path.basename(file)
        sample = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
        print(f"Processing {fname}...")
        
        # Canny edge detection
        sample = cv2.GaussianBlur(sample, (5, 5), 0)
        edges = cv2.Canny(sample, args.threshold_low, args.threshold_high)
        cv2.imwrite(os.path.join(output_folder, f"{fname}_canny.png"), edges)


if __name__ == "__main__":
    main()