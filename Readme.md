# OpenCv Python Demo

[TOC]

- IDE: PyCharm
- Python: 3.7
- OpenCV: 4.2.0
- Video: https://www.bilibili.com/video/av24998616
- Dependency: 
    - numpy
    - opencv_python
    - opencv_python_headless

## ch3 Color Space

常见的颜色空间：
- RGB (Red Green Blue)
- HSV (Hue Saturation Value)
- HIS
- YCrCb (皮肤检测用的多)
- YUV (linux底层硬件使用，安卓也是)

![@HSV色彩空间](./note/HSV.png)
![@RGB色彩空间](./note/RGB.png)

RGB色彩空间不好表达，HSV的能很好的表述一个颜色。在OpenCV中有一个inRange函数可以很方便的使用HSV来进行颜色识别。

最常见的转换：
1. RGB - HSV
2. RGB - YUV

#### HSV的颜色范围
|  | 黑 | 灰 | 白 | 红 | 红 | 橙 | 黄 | 绿 | 青 | 蓝 | 紫 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| hmin | 0 | 0 | 0 | 0 | 156 | 11 | 26 | 35 | 78 | 100 | 125 |
| hmax | 180 | 180 | 180 | 10 | 180 | 25 | 34 | 77 | 99 | 124 | 155 |
| smin | 0 | 0 | 0 | 43 | 43 | 43 | 43 | 43 | 43 | 43 | 43 |
| smax | 255 | 43 | 30 | 255 | 255 | 255 | 255 | 255 | 255 | 255 | 255 |
| vmin | 0 | 46 | 221 | 46 | 46 | 46 | 46 | 46 | 46 | 46 | 46 |
| vmax | 46 | 220 | 255 | 255 | 255 | 255 | 255 | 255 | 255 | 255 | 255 |




