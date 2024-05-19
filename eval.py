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
    nsample = gt.shape[1]
    for i in range(nsample):
        _, binary = cv2.threshold(gt[0][i][0][0][1], 0.5, 255, cv2.THRESH_BINARY)
        datas.append(binary)
    return datas

def show_images(pred, gts):
    cv2.imshow("pred", pred)
    for i, gt in enumerate(gts):
        cv2.imshow(f"gt_{i}", gt)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def precsion_recall(pred, gt):
    tp = np.sum(np.logical_and(pred == 255, gt == 255))
    fp = np.sum(np.logical_and(pred == 255, gt == 0))
    fn = np.sum(np.logical_and(pred == 0, gt == 255))
    tn = np.sum(np.logical_and(pred == 0, gt == 0))
    
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    return precision, recall

def f1_score(precision, recall):
    return 2 * (precision * recall) / (precision + recall)

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
    # cv2.imwrite(os.path.join(output_folder,f"gt_{fname}"), gts[0])
    
    avg_precision = 0
    avg_recall = 0
    avg_f1 = 0
    for i, gt in enumerate(gts):
        precision, recall = precsion_recall(pred, gt)
        f1 = f1_score(precision, recall)
        avg_precision += precision
        avg_recall += recall
        avg_f1 += f1
    avg_precision = round(avg_precision/len(gts),5)
    avg_recall = round(avg_recall/len(gts),5)
    avg_f1 = round(avg_f1/len(gts),5)
    print(f"{fname}: Precision: {avg_precision}, Recall: {avg_recall}, F1 Score: {avg_f1}")


if __name__ == "__main__":
    main()