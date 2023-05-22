from ast import parse
import jittor as jt
from tqdm import tqdm
import argparse
import numpy as np
import os
from jnerf.runner import Runner,NeuSRunner
from jnerf.utils.config import init_cfg, get_cfg
from jnerf.utils.registry import build_from_cfg,NETWORKS,SCHEDULERS,DATASETS,OPTIMS,SAMPLERS,LOSSES
import time
# jt.flags.gopt_disable=1
jt.flags.use_cuda = 1


def main():
    assert jt.flags.cuda_archs[0] >= 61, "Failed: Sm arch version is too low! Sm arch version must not be lower than sm_61!"
    parser = argparse.ArgumentParser(description="Jittor Object Detection Training")
    parser.add_argument(
        "--config-file",
        default="",
        metavar="FILE",
        help="path to config file",
        type=str,
    )
    parser.add_argument(
        "--save_dir",
        default="",
        type=str,
    )

    args = parser.parse_args()

    if args.config_file:
        init_cfg(args.config_file)

    runner = Runner()

    start_time = time.time()
    runner.train()
    end_time = time.time()
    train_time = end_time - start_time
    print("train_time: ", train_time, "s")

    runner.test(True)
    # runner.render(True, args.save_dir)

if __name__ == "__main__":
    main()
