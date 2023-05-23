# NeRF（Graphics-project）
Computer Graphics Course (COMP130018.01) Project-3 of Fudan University.

## Part1--基于JNeRF的实拍物重建
#### 环境搭建

——使用百度飞桨AI平台搭建环境（GPU：16G V100）

```bash
pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/
```

#### 运行代码（训练、测试、生成视频一体化）

```bash
python run_net.py --config-file ./projects/ngp/configs/ngp_ikun.py
```

#### 参考代码仓库

[Jittor/JNeRF(github.com)](https://github.com/Jittor/JNeRF)

