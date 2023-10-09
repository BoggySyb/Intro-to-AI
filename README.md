# 学习记录

> 仅用作记录个人学习课程，课程介绍如下

![](https://p.ipic.vip/yrr3fk.png)

## UC Berkeley **CS 188** | Introduction to Artificial Intelligence

> 学习时间：2023/09 - 2023/10                                                                                                                   

#### 课程内容：

​	人工智能导论。主要介绍智能系统设计的基本思想和技术，统计和决策理论建模方法相关的内容。 [课程链接](https://inst.eecs.berkeley.edu/~cs188/fa18/)

#### 项目介绍：

- p1-search:   在本项目中，您将实现通用搜索算法并将其应用于 Pacman 场景，让 Pacman 在迷宫世界中找到到达特定位置的路径以收集食物。(q4, 6, 7 unfinished)

   + Depth First Search 深度优先搜索

     <img src="https://p.ipic.vip/be9s2a.png" style="max-width:50%;" />

   + Breadth First Search 宽度优先搜索

     <img src="https://p.ipic.vip/vbrlr9.png" style="max-width:50%;" />

   + Uniform Cost Search 统一成本搜索

     ​	UCS 的基本思想是从起始节点开始，不断扩展当前成本最低的节点，直到达到目标节点或搜索空间中没有更多节点可供扩展。

     <img src="https://p.ipic.vip/29xb2o.png" style="zoom:50%;" />

   + A* Search A*搜索

     <img src="https://p.ipic.vip/44p63b.png" style="max-width:50%;" />

   + Heuristic 启发式方法

     

- p2-multiagent:   在本项目中，您将实现极小极大和期望极大搜索算法，以及设计评估函数，来为游戏设计更聪明的幽灵与 Pacman。(debugging)

- p3-reinforcement:  在本项目中，您将实现价值迭代和 Q 学习。首先在 Gridworld 上测试您的特工，然后将它们应用于模拟机器人控制器（Crawler）和 Pacman。(q1, 2, 3, 4, 5, 8 unfinished)

- p4-ghostbusters:  在本项目中，您将设计使用传感器来定位和吃掉看不见的幽灵的 Pacman (HMM隐马尔可夫模型)

   - Exact Inference 精确推断

     ​	指在概率图模型（如贝叶斯网络或马尔可夫随机场）中进行精确概率计算的过程。这种推断方法旨在精确地计算给定一组观测数据条件下的概率分布或概率查询。

     <img src="https://p.ipic.vip/v9jpme.png" style="max-width:70%;" />

   - Approximate Inference 近似推断

     ​	项目采用粒子滤波(Particle Filtering)做近似推断，通过一组随机粒子来估计系统状态的后验分布。

     <img src="https://p.ipic.vip/jx33yn.png" style="max-width:70%;" />

   - DBNs 动态贝叶斯网络

     ​	是一种用于建模时间序列数据和动态系统的概率图模型，它是贝叶斯网络的扩展，用于表示和推断关于随时间变化的随机变量之间关系的概率模型。

     <img src="https://p.ipic.vip/kwnuo4.png" style="max-width:80%;" />

- p5-machinelearning:   在此项目中，您将构建一个神经网络来对数字图片进行分类。
