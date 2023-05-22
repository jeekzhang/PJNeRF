import numpy as np
import jittor as jt
from jittor import nn
from jnerf.utils.registry import LOSSES
from skimage.metrics import structural_similarity as compare_ssim

def img2mse(x, y): return jt.mean((x - y) ** 2)
def mse2psnr(x): return -10. * jt.log(x) / jt.log(jt.array(np.array([10.])))

def calculate_ssim(img1, img2):
    img1_gray = np.mean(img1, axis=-1)
    img2_gray = np.mean(img2, axis=-1)
    ssim = compare_ssim(img1_gray, img2_gray, data_range=img1_gray.max() - img1_gray.min(), multichannel=False)
    return ssim

@LOSSES.register_module()
class MSELoss(nn.Module):
    def __init__(self):
        pass

    def execute(self, x, target):
        return img2mse(x, target)