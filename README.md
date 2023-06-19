# PJ with NeRF（Graphics-project）
Computer Graphics Course (COMP130018.01) Project-3 of Fudan University.

## Part1--基于JNeRF的实拍物重建
#### 环境搭建

——使用百度飞桨AI平台搭建环境（GPU：16G V100）

```bash
pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/
```

#### 运行代码（训练、测试、生成视频一体化）

```bash
python run_net.py --config-file ./projects/ngp/configs/ngp_bear.py
```

#### 数据处理

新建文件夹存放.mp4视频文件(以/mydata/chick.mp4为例)  
将视频切分为图片
```bash
python .\scripts\colmap2nerf.py --video_in .\mydata\chick.mp4 --video_fps 2 --run_colmap --aabb_scale 16 --overwrite
```
挑选好图片后生成位姿信息
```bash
cd mydata
python ..\scripts\colmap2nerf.py --colmap_matcher exhaustive --run_colmap --aabb_scale 16 --overwrite
```
在transforms.json文件中将会有相机信息和所有图片位姿信息，可自行将数据划分为训练集，验证集和测试集用以3D重建和测评

#### 参考代码仓库

[Jittor/JNeRF(github.com)](https://github.com/Jittor/JNeRF)

