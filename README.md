# 学习记录

> 仅用作记录个人学习课程，课程介绍如下

## UC Berkeley **CS 188** | Introduction to Artificial Intelligence

> 学习时间：2023/09 - 2023/10                                                                                                              

#### 课程内容：

​	人工智能导论。主要介绍智能系统设计的基本思想和技术，统计和决策理论建模方法相关的内容。 [课程链接](https://inst.eecs.berkeley.edu/~cs188/fa18/)

#### 项目介绍：

##### p1-search:   在本项目中，您将实现通用搜索算法并将其应用于 Pacman 场景，让 Pacman 在迷宫世界中找到到达特定位置的路径以收集食物。（q7  2/4）

+ Depth First Search 深度优先搜索

<p align="center">
  <img src="./imgs/dfs.jpg" style="zoom:50%;" />
</p>


+ Breadth First Search 宽度优先搜索

  <p align="center">
    <img src="./imgs/bfs.png" style="max-width:50%;" />
  </p>

+ Uniform Cost Search 统一成本搜索

​		UCS 的基本思想是从起始节点开始，不断扩展当前成本最低的节点，直到达到目标节点或搜索空间中没有更多节点可供扩展。

<p align="center">
  <img src="./imgs/ucs.png" style="zoom:50%;" />
</p>


+ A* Search & Heuristic 启发式方法

​		A*搜索算法是一种常用于寻找最短路径或最优解的启发式搜索算法，路径的实际成本（已经花费的代价）和预估的剩余成本（从当前节点到目标节点的估计代价)。

<p align="center">
  <img src="./imgs/a*.png" style="zoom:75%;" />
</p>


------

##### p2-multiagent:   在本项目中，您将实现极小极大和期望极大搜索算法，以及设计评估函数，来为游戏设计更聪明的幽灵与 Pacman。(q5  0/6)

+ Reflex Agent  3/4

  <p align="center">
    <img src="./imgs/reflex.png" style="zoom:67%;" />
  </p>

+ Minimax 最小最大算法

  ​	Minimax 算法的主要目标是帮助一个玩家找到在对手采取最优策略的情况下，自己能够获得的最大利益，或者说最小化可能的最大损失。

  <p align="center">
    <img src="./imgs/minimax.png" style="zoom:75%;" />
  </p>

+ Alpha-Beta Pruning 

  ​	Alpha-Beta剪枝是一种优化Minimax算法的技术，用于在博弈树搜索中减少计算开销。Alpha和Beta分别是两个参数，它们用于跟踪在搜索过程中找到的最佳值。Alpha表示Max层（当前玩家）已经找到的最佳值，而Beta表示Min层（对手）已经找到的最佳值。

  <p align="center">
    <img src="./imgs/alpha_beta.png" style="zoom:75%;" />
  </p>

+ Expectimax

  ​	Expectimax（期望极大算法）是一种用于解决概率性决策问题的算法，通常用于博弈、规划和其他与不确定性相关的问题。该算法的名称来自于"expectation"（期望）和"maximization"（极大化）两个词的组合，这反映了它的工作原理。

  <p align="center">
    <img src="./imgs/expectimax.png" style="zoom:75%;" />
  </p>

------

##### p3-reinforcement:  在本项目中，您将实现价值迭代和 Q 学习。首先在 Gridworld 上测试您的特工，然后将它们应用于模拟机器人控制器（Crawler）和 Pacman。

+ Value Iteration & Asynchronous Value Iteration  价值迭代

  ​	Value Iteration 算法的主要目标是计算每个状态的价值函数，即从每个状态开始执行最佳策略所能获得的期望累积奖励。这个过程通常通过反复迭代来实现，直到价值函数收敛为止。

  <p align="center">
    <img src="./imgs/value_iter.png" style="zoom:50%;" />
  </p>

+ Q-Learning

  <p align="center">
   	<img src="./imgs/q_learn.png" style="zoom:30%;" />
  </p>

+ Approximate Q-Learning

  <p align="center">
   	<img src="./imgs/appro_q_learn.png" style="zoom:50%;" />
  </p>

------

##### p4-ghostbusters:  在本项目中，您将设计使用传感器来定位和吃掉看不见的幽灵的 Pacman (HMM隐马尔可夫模型)

- Exact Inference 精确推断

  ​	指在概率图模型（如贝叶斯网络或马尔可夫随机场）中进行精确概率计算的过程。这种推断方法旨在精确地计算给定一组观测数据条件下的概率分布或概率查询。

  <p align="center">
   	<img src="./imgs/exact_infer.png" style="max-width:70%;" />
  </p>

- Approximate Inference 近似推断

  ​	项目采用粒子滤波(Particle Filtering)做近似推断，通过一组随机粒子来估计系统状态的后验分布。

  <p align="center">
   	<img src="./imgs/appro_infer.png" style="max-width:70%;" />
  </p>

- DBNs 动态贝叶斯网络

  ​	是一种用于建模时间序列数据和动态系统的概率图模型，它是贝叶斯网络的扩展，用于表示和推断关于随时间变化的随机变量之间关系的概率模型。

  <p align="center">
   	<img src="./imgs/dbns.png" style="max-width:80%;" />
  </p>

------

##### p5-machinelearning:   在此项目中，您将构建神经网络来对数字图片和外语词汇进行分类。

+ Perceptron 感知机

<p align="center">
 	<img src="./imgs/percept.png" style="max-width:80%;" />
</p>


+ Non-linear Regression 非线性回归 $sin(x)$ 函数

<p align="center">
 	<img src="./imgs/nlr.png" style="max-width:80%;" />
</p>


+ MLP 多层感知机 数字图像 0-9 识别

<p align="center">
 	<img src="./imgs/mlp.png" style="max-width:50%;" />
</p>


+ RNN 循环神经网络 语言识别

<p align="center">
 	<img src="./imgs/rnn.png" style="max-width:50%;" />
</p>
