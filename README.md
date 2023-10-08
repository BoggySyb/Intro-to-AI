# 学习记录

> 仅用作记录个人学习课程，课程介绍如下

![](https://p.ipic.vip/yrr3fk.png)

## UC Berkeley **CS 188** | Introduction to Artificial Intelligence

> 学习时间：2023/09 - 2023/10                                                                                                                   

#### 课程内容：

​	人工智能导论。主要介绍智能系统设计的基本思想和技术，统计和决策理论建模方法相关的内容。 [课程链接](https://inst.eecs.berkeley.edu/~cs188/fa18/)

#### 项目介绍：

- p1-search: 实现DFS、BFS、UCS、A*等搜索算法；启发式函数(Heuristic)优化，实现基础吃豆人自动化

- p2-multiagent: 

- p3-reinforcement:

- p4-ghostbusters:  在本项目中，设计使用传感器来定位和吃掉看不见的幽灵的吃豆人(HMM隐马尔可夫模型)

   - *Exact Inference 精确推断*

     ​	指在概率图模型（如贝叶斯网络或马尔可夫随机场）中进行精确概率计算的过程。这种推断方法旨在精确地计算给定一组观测数据条件下的概率分布或概率查询。

     <img src="https://p.ipic.vip/v9jpme.png" style="zoom:50%;" />

   - ==Approximate Inference 近似推断==

     ​	项目采用**粒子滤波(Particle Filtering)**做近似推断，通过一组随机粒子来估计系统状态的后验分布。

     <img src="https://p.ipic.vip/jx33yn.png" style="zoom:50%;" />

   - <u>DBNs 动态贝叶斯网络</u>

     ​	是一种用于建模时间序列数据和动态系统的概率图模型，它是贝叶斯网络的扩展，用于表示和推断关于随时间变化的随机变量之间关系的概率模型。

     <img src="https://p.ipic.vip/kwnuo4.png" style="zoom:50%;" />

- p5-machinelearning: 
