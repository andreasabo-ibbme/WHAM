import os
import argparse
import os.path as osp
import glob
from collections import defaultdict
import sys

import numpy as np

import cv2
import torch
import joblib
from loguru import logger
from progress.bar import Bar

from configs.config import get_cfg_defaults

# from lib.data.datasets import CustomDataset
# from lib.utils.imutils import avg_preds
# from lib.utils.transforms import matrix_to_axis_angle
# from lib.models import build_network, build_body_model
from lib.models import build_body_model

# from lib.models.preproc.detector import DetectionModel
# from lib.models.preproc.extractor import FeatureExtractor
# from lib.models.smplify import TemporalSMPLify
from icecream import ic
from lib.vis.run_vis import run_vis_on_demo_prompthmr


INPUT_FOLDER_ROOT = r"/home/saboa/mnt/ndrive_andrea/AMBIENT/AMBIENT_Belmont"
OUTPUT_FOLDER_ROOT = (
    r"/home/saboa/mnt/ndrive_andrea/AMBIENT/AMBIENT_Belmont_posetracked/WHAM_30FPS"
)

INPUT_FOLDER = r"/home/saboa/mnt/ndrive_andrea/AMBIENT/Andrea_S/EDS/PROMPTHMR_DEC2025/pipeline_dev/BODY_JOINTS"


sys.setrecursionlimit(5000)


SAVE_PKL = True
VISUALIZE = True
RUN_SMPLFY = True
FORCE_RERENDER_ALL = False

try:
    from lib.models.preproc.slam import SLAMModel

    _run_global = True
except:
    logger.info("DPVO is not properly installed. Only estimate in local coordinates !")
    _run_global = False


def render_vid(cfg, input_pkl, run_global=True):

    try:
        results = joblib.load(input_pkl)
        output_pth = os.path.split(input_pkl)[0]
        if "input_vid" not in results:
            print(f"No input video found in {input_pkl}, skipping...")
            return
        input_video = results["input_vid"]

        if not FORCE_RERENDER_ALL:
            output_video_pth = osp.join(output_pth, "prompt_hmr_v2.mp4")
            if os.path.exists(output_video_pth):
                print(f"Video already rendered at {output_video_pth}, skipping...")
                return

        smpl = build_body_model(cfg.DEVICE, cfg.TRAIN.BATCH_SIZE * cfg.DATASET.SEQLEN)
        with torch.no_grad():
            run_vis_on_demo_prompthmr(
                cfg, input_video, results, output_pth, smpl, vis_global=run_global
            )

    except Exception as e:
        print(input_pkl)
        ic(e)


def render_vid_main(cfg, video, input_pkl, output_pth, run_global=True):
    smpl = build_body_model(cfg.DEVICE, cfg.TRAIN.BATCH_SIZE * cfg.DATASET.SEQLEN)
    results = joblib.load(input_pkl)
    run_global = True
    from lib.vis.run_vis import run_vis_on_demo_prompthmr

    with torch.no_grad():
        run_vis_on_demo_prompthmr(
            cfg, video, results, output_pth, smpl, vis_global=run_global
        )


def filter_by_date(all_vids):
    vids = [
        vid
        for vid in all_vids
        if (
            os.path.split(vid)[-1][5:13] >= START_DATE
            and os.path.split(vid)[-1][5:13] <= STOP_DATE
        )
    ]
    return vids


def print_keys(struct, prefix=""):
    for key in struct.keys():
        print(f"{prefix}[{key}]")
        if isinstance(struct[key], dict):
            print_keys(struct[key], prefix + "   ")


def render_all_vids(cfg):

    vid_extensions = ["*prompt_hmr_output.pkl"]

    videos_list = sorted(
        [
            vid
            for ext in vid_extensions
            for vid in glob.glob(os.path.join(INPUT_FOLDER, "**", ext), recursive=True)
        ]
    )

    i = 0
    for vid in videos_list:
        if i % 10 == 0:
            print(f"Processing video {i+1} / {len(videos_list)}")

        render_vid(cfg, vid)
        i += 1


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    args = parser.parse_args()

    cfg = get_cfg_defaults()
    cfg.merge_from_file("configs/yamls/demo.yaml")
    render_all_vids(cfg)

    quit()

    ## DEVLEOPMENT
    video = r"/home/saboa/mnt/ndrive_andrea/AMBIENT/Andrea_S/EDS/sorted_vids/formatted_input_downsampled_540x960/BODY_JOINTS/elbow_l/EDS012__elbow_l.mp4"
    input_pkl_prompthmr = r"/home/saboa/code/PromptHMR/prompt_hmr_output.pkl"
    input_pkl_prompthmr = r"/home/saboa/mnt/ndrive_andrea/AMBIENT/Andrea_S/EDS/PROMPTHMR_DEC2025/pipeline_dev/BODY_JOINTS/elbow_l/EDS012__elbow_l/prompt_hmr_output.pkl"
    # /home/saboa/mnt/ndrive_andrea/AMBIENT/Andrea_S/EDS/sorted_vids/formatted_input_downsampled_540x960/BODY_JOINTS/elbow_l/EDS012__elbow_l.mp4
    output_pth = r"prompthmr_v4"
    os.makedirs(output_pth, exist_ok=True)
    render_vid_main(cfg, video, input_pkl_prompthmr, output_pth)
    quit()
