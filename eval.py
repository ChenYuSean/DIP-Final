import os
import argparse
import cv2
import numpy as np
import h5py
import scipy.io as sio

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('predict', type=str, help='Path to the predicted image')
    parser.add_argument('target', type=str, help='Path to the ground truth image')
    parser.add_argument('--output_path',default="./OutputImages",type=str)
    return parser.parse_args()

def get_mat_data(mat_file):
    datas = []
    mat = sio.loadmat(mat_file)
    gt = mat['groundTruth']
    for i in range(6):
        _, binary = cv2.threshold(gt[0][i][0][0][1], 0.5, 255, cv2.THRESH_BINARY)
        datas.append(binary)
    return datas

def main():
    np.random.seed(0)
    args = parse_args()
    
    output_folder = args.output_path
    os.makedirs(output_folder, exist_ok=True)

    file = args.predict
    fname = os.path.basename(file)
    pred = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
    _, pred = cv2.threshold(pred, 127, 255, cv2.THRESH_BINARY)
    
    gts = get_mat_data(args.target)
    
    cv2.imshow("pred", pred)
    for i, gt in enumerate(gts):
        cv2.imshow(f"gt_{i}", gt)
    cv2.waitKey(0)
    


if __name__ == "__main__":
    main()