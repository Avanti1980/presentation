---
presentation:
  transition: 'none'
  enableSpeakerNotes: true
  margin: 0
---

@import "../common/css/zhangt-style.css"
@import "../common/css/font-awesome-4.7.0/css/font-awesome.css"


<!-- slide data-notes="自我介绍<br><br>为何改题目<br><br>前沿需要太多的铺垫 一学期的课程<br><br>前沿不一定有价值 非前沿可以是经典" -->  
<div id="logo">
  <img src="../common/img/university.gif" height=120px>
  <img src="../common/img/logo.jpg" height="120px">
  <img src="img/QR-code.png" height="240px" style="margin-left:5%;margin-right: auto">
</div>

<div>
  <h1 class="front_page_title top_10">强化学习<strike>研究前沿</strike>简介</h1>

  <hr class="hr_medium_1">

  <h4 class="author top_3">张腾</h4>
  <h4 class="mail">zhangt_@hust.edu.cn</h4>
  <h4 class="date">2019 - 07 - 31</h4>
</div>


<!-- slide data-notes="强化学习最高光的时刻 16年 17年 简述下历史14年前还很小众" data-background-video="videos/alphago.mp4" data-background-video-loop data-background-video-muted vertical=true -->


<!-- slide vertical=true data-notes="强化学习是  分支  从人工智能讲起 不会讲太细" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">大纲</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  rankdir=LR
  node [shape="box" fontsize=15 fontname="fz-sxslk"]
  edge [arrowhead=vee arrowsize=0.8]
  
  人工智能 -> 逻辑推理 
  人工智能 -> 知识工程 

  人工智能 -> 机器学习

  机器学习 -> 监督学习
  机器学习 -> 无监督学习
  机器学习 -> 半监督学习
  机器学习 -> 主动学习
  机器学习 -> 强化学习

  强化学习 -> 值函数估计  
  强化学习 -> 策略搜索
  强化学习 -> 其它话题

  值函数估计 -> 策略迭代
  值函数估计 -> 值迭代
  值函数估计 -> 蒙特卡洛
  值函数估计 -> 时序差分

  策略搜索 -> 策略梯度
  ac [label="演员-评论家"]
  策略搜索 -> ac
}
```

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">大纲</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  rankdir=LR
  node [shape="box" fontsize=15 fontname="fz-sxslk"]
  edge [arrowhead=vee arrowsize=0.8]
  
  人工智能 -> 逻辑推理 
  人工智能 -> 知识工程 
  人工智能 -> 机器学习

  node[fontcolor=lightgray color=lightgray]
  edge [color=lightgray]
  机器学习 -> 监督学习
  机器学习 -> 无监督学习
  机器学习 -> 半监督学习
  机器学习 -> 主动学习
  机器学习 -> 强化学习

  强化学习 -> 值函数估计  
  强化学习 -> 策略搜索
  强化学习 -> 其它话题

  值函数估计 -> 策略迭代
  值函数估计 -> 值迭代
  值函数估计 -> 蒙特卡洛
  值函数估计 -> 时序差分

  策略搜索 -> 策略梯度
  ac [label="演员-评论家"]
  策略搜索 -> ac
}
```

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">人工智能 时代背景</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

N. Wiener 《控制论》:

> 第一次工业革命：用某种机器来减轻甚至代替<font color=blue>体力</font>劳动

> 上世纪中叶：用某种新型机器来减轻甚至代替某些<font color=blue>脑力</font>劳动

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>

<!-- slide vertical=true data-notes="下面介绍几位大佬 Minsky是位传奇人物 他建造了第一台可以学习的神经网络机器 他有一本非常有名的书叫感知机 感知机就是一层的神经网络 他在书里又全盘否定了人工智能 感知机连简单的异或函数都学习不了 因为大佬的盖棺定论 整个领域直接冷掉10年 直到八十年代中期 hinton提出了反向传播 多层神经网络终于可以学习非线性函数了 这个插个题外话 反向传播并不是hinton第一个发明的 60年代就被发现过很多次 而且反向传播就是个链式法则" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">人工智能 起源</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

- 时间：1956年
- 地点：达特茅斯学院
- 人物：Shannon、McCarthy、Minsky、Simon、Newell等
- 事件：讨论用机器模拟人的智能

<div class="multi_column top_2">
<img src="img/birth-school.jpg" width=425px height=277px style="margin-left:2.5%"/>
<img src="img/birth-people.jpg" width=425px height=277px style="margin-right:2.5%;margin-left:auto"/>
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>

<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">人工智能 发展</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

三次浪潮

- 推理期
  - 热潮：1956 - 60年代初
  - 凛冬：60年代中 - 60年代末
  <br>
- 知识期
  - 热潮：70年代初 - 80年代初
  - 凛冬：80年代中 - 90年代初
  <br>
- 学习期
  - 热潮：90年代中 - 2012
  - 井喷：2012 - ？

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide data-notes="我个人猜测原因是数学原理讲的是公理集合论 当然是罗素的 不是zfc 天生符号化 连续函数如何符号化" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">逻辑推理</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

机器：擅长固定套路的计算　vs.　人类：擅长妙手偶得的推理

符号主义：<font color=blue>智能 = 逻辑推理</font>

Simon和Newell设计了“逻辑理论家”程序

- 1952年，“逻辑理论家”证明了《数学原理》中的38条定理
- 1963年，证明了全部52条定理，其中定理2.85的证明比原书作者更巧妙
- Simon和Newell获得了75年的图灵奖
<br>
- 面对更难的定理就无能为力了，十万步无法证明“两个连续函数之和还是连续函数”

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">符号化 归结原理</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

$A$：“$B$和$C$都是说谎者”；$B$：“$A$和$C$都是说谎者”；$C$：“$A$和$B$中至少有一个说谎者”，谁说了实话？

<table class="dataset" style="width:88%;margin-left:6%">
  <thead>
    <tr>
      <th style="border-right: 1px solid">公式</th>
      <th>$p \rightarrow q$</th>
      <th>$\Longleftrightarrow$</th>
      <th>$\neg p \vee q$</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="border-right: 1px solid"><b>条件</b></td>
      <td>$A \rightarrow \neg B \wedge \neg C$</td>
      <td>$\Longleftrightarrow$</td>
      <td>$1.~\neg A \vee \neg B$</td>
    </tr>
    <tr>
      <td style="border-right: 1px solid"></td>
      <td>&nbsp;</td>
      <td>$\Longleftrightarrow$</td>
      <td>$2.~\neg A \vee \neg C$</td>
    </tr>
    <tr>
      <td style="border-right: 1px solid"></td>
      <td>$\neg A \rightarrow B \vee C$</td>
      <td>$\Longleftrightarrow$</td>
      <td>$3.~A \vee B \vee C$</td>
    </tr>
    <tr>
      <td style="border-right: 1px solid"></td>
      <td>$B \rightarrow \neg A \wedge \neg C$</td>
      <td>$\Longleftrightarrow$</td>
      <td>$4.~\neg B \vee \neg C$</td>
    </tr>
    <tr>
      <td style="border-right: 1px solid"></td>
      <td>$\neg B \rightarrow A \vee C$</td>
      <td>$\Longleftrightarrow$</td>
      <td>$3.~A \vee B \vee C$</td>
    </tr>
    <tr>
      <td style="border-right: 1px solid"></td>
      <td>$C \rightarrow \neg A \vee \neg B$</td>
      <td>$\Longleftrightarrow$</td>
      <td>$5.~\neg A \vee \neg B \vee \neg C$</td>
    </tr>
    <tr>
      <td style="border-right: 1px solid"></td>
      <td>$\neg C \rightarrow A \wedge B$</td>
      <td>$\Longleftrightarrow$</td>
      <td>$6.~A \vee C$</td>
    </tr>
    <tr>
      <td style="border-right: 1px solid"></td>
      <td>&nbsp;</td>
      <td>$\Longleftrightarrow$</td>
      <td>$7.~B \vee C$</td>
    </tr>
    <tr>
      <td style="border: 1px solid;border-left: none"><b>归结</b></td>
      <td style="border-top: 1px solid;border-bottom: 1px solid">$1 + 7 \rightarrow 8.~\neg A \vee C$</td>
      <td style="border-top: 1px solid;border-bottom: 1px solid">$6 + 8 \rightarrow C$</td>
      <td style="border-top: 1px solid;border-bottom: 1px solid">$C$说了实话</td>
    </tr>
  </tbody>
</table>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">知识工程</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

教训：光有逻辑推理远远不够，机器得拥有知识

基本想法：“知识就是力量”，<font color=blue>智能 = 知识 + 逻辑推理</font>

专家系统(知识工程) = 知识库 + 推理引擎
- 在特定领域内具有专家水平解决问题能力的程序系统
- 第一个成功的专家系统DENDRAL于1968年问世
- “知识工程”之父E. A. Feigenbaum获得了94年的图灵奖
<br>
- 人工构建知识库成本太高
- 知识获取困难

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>

<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">动物识别专家系统</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  graph [nodesep=0.45, ranksep=0.01]
  node [fontsize=14 height=0.4 fontname="fz-sxslk"]
  edge [arrowhead=vee arrowsize=0.6 fontsize=14 fontcolor=red fontname="fz-sxslk"]

  subgraph cluster_0 {
    label = <<font face='fz-sxslk'>知识库</font>>
    node [shape=box, fontcolor=blue]
    猫 鸡 null 蛇 蜥蜴

    node [shape=ellipse, fontcolor=black]
    是否冷血 -> 是否有羽毛 -> 猫 [label="否"]
    是否冷血 -> 是否有腿 -> 蜥蜴 [label="是"]
    是否有羽毛 -> 是否会飞 -> null [label="是"]
    是否会飞 -> 鸡 [label="否"]
    是否有腿 -> 蛇 [label="否"]
  }

  subgraph cluster_1 {
    label = <<font face='fz-sxslk'>推理</font>>
    ？？ [shape=box, fontcolor=blue]
    不冷血 -> ？？
    没羽毛 -> ？？
  }
}
```

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide data-notes="前两个领域并非就此销声匿迹 因果学习 知识图谱" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">大纲</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  rankdir=LR
  node [shape="box" fontsize=15 fontname="fz-sxslk" fontcolor=lightgray color=lightgray]
  edge [arrowhead=vee arrowsize=0.8 color=lightgray]
  
  node[fontcolor=lightgray]
  人工智能 -> 逻辑推理 
  人工智能 -> 知识工程 

  node[fontcolor=black color=black]
  人工智能 -> 机器学习
  
  edge [color=black]  
  机器学习 -> 监督学习
  机器学习 -> 无监督学习
  机器学习 -> 半监督学习
  机器学习 -> 主动学习
  机器学习 -> 强化学习

  node[fontcolor=lightgray color=lightgray]
  edge [color=lightgray]
  强化学习 -> 值函数估计  
  强化学习 -> 策略搜索
  强化学习 -> 其它话题

  值函数估计 -> 策略迭代
  值函数估计 -> 值迭代
  值函数估计 -> 蒙特卡洛
  值函数估计 -> 时序差分

  策略搜索 -> 策略梯度
  ac [label="演员-评论家"]
  策略搜索 -> ac
}
```

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="横轴为对动物的特征描述 类标记为是否为猫" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">机器学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

基本想法：<font color=blue>知识由机器从数据中自动学习得到</font>

$$
\begin{align*}
  数据 = 
  \begin{array}{c|ccc|c}
    样本 & & 特征 & & 类标记 \\ 
    \hline 
    \xv_1 & [~x_{11} & \cdots & x_{1n}~] & y_1 \\
    \xv_2 & [~x_{21} & \cdots & x_{2n}~] & y_2 \\
    \vdots & \vdots & \ddots & \vdots & \vdots \\
    \xv_m & [~x_{m1} & \cdots & x_{mn}~] & y_m \\
	\end{array}
\end{align*}
$$

- 被动接收数据：监督学习、无监督学习、半监督学习
- 主动获取数据：主动学习、强化学习

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="特征是二维平面坐标 类标记是颜色" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">监督学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

- 分类
- 输入：$\{ (\xv_1,y_1), \ldots, (\xv_m,y_m) \}$
- 输出：$y = f(\xv)$，$\Pr[y | \xv]$

<div class="top_5">
  <img src="plot/super1.svg" height="300px">
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">监督学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

- 分类
- 输入：$\{ (\xv_1,y_1), \ldots, (\xv_m,y_m) \}$
- 输出：$y = f(\xv)$，$\Pr[y | \xv]$

<div class="top_5">
  <img src="plot/super2.svg" height="300px">
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide data-notes="商店新注册用户 无法判断用户类型 只能靠相似度先归类" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">无监督学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

- 聚类：从样本层面，对数据进行分组
- 输入：$\{ \xv_1, \ldots, \xv_m \}$
- 输出：样本所属的组，$c_i = f(\xv_i)$

<div class="top_5">
  <img src="plot/cluster1.svg" height="300px">
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">无监督学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

- 聚类：从样本层面，对数据进行分组
- 输入：$\{ \xv_1, \ldots, \xv_m \}$
- 输出：样本所属的组，$c_i = f(\xv_i)$

<div class="top_5">
  <img src="plot/cluster2.svg" height="300px">
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="有些数据中存在高度冗余的特征 例如下面这张图 横轴是身高 纵轴是体重 降维" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">无监督学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

- 降维：从特征层面，对数据进行压缩
- 输入：$\{ \xv_1, \ldots, \xv_m \}$
- 输出：投影映射$y_i = f(\xv_i)$

<div class="top_5">
  <img src="plot/dr1.svg" height="300px">
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">无监督学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

- 降维：从特征层面，对数据进行压缩
- 输入：$\{ \xv_1, \ldots, \xv_m \}$
- 输出：投影映射$y_i = f(\xv_i)$

<div class="top_5">
  <img src="plot/dr2.svg" height="300px">
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide data-notes="顾名思义 介于两者之间 分界面穿过低密度区域 多条 少量有标记样本可以甄别" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">半监督学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

- 对未标记样本进行分类
- 输入：$\{ (\xv_1,y_1), \ldots, (\xv_l,y_l), \xv_{l+1}, \ldots, \xv_{l+u} \}, ~ l \ll u$
- 输出：$y_i = f(\xv_i),~i = l+1, \ldots, l+u$

<div class="top_5">
  <img src="plot/semi1.svg" height="300px">
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">半监督学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

- 对未标记样本进行分类
- 输入：$\{ (\xv_1,y_1), \ldots, (\xv_l,y_l), \xv_{l+1}, \ldots, \xv_{l+u} \}, ~ l \ll u$
- 输出：$y_i = f(\xv_i),~i = l+1, \ldots, l+u$

<div class="top_5">
  <img src="plot/semi2.svg" height="300px">
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6><h6 class="bottom_center">SCTS & CGCL</h6><h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="用于类标记获取代价很高的问题 例如医疗影像标注 这个时候假设有未标记样本 可以向oracle询问 但问的次数越少越好" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">主动学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

- 分类：选择尽可能少的样本查询其类标记，构建分类器
- 输入：$\{ \xv_1, \ldots, \xv_m \}$
- 输出：$y = f(\xv)$，$\Pr[y | \xv]$

<div class="top_5">
  <img src="plot/active1.svg" height="300px">
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">主动学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

- 分类：选择尽可能少的样本查询其类标记，构建分类器
- 输入：$\{ \xv_1, \ldots, \xv_m \}$
- 输出：$y = f(\xv)$，$\Pr[y | \xv]$

<div class="top_5">
  <img src="plot/active2.svg" height="300px">
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">主动学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

- 分类：选择尽可能少的样本查询其类标记，构建分类器
- 输入：$\{ \xv_1, \ldots, \xv_m \}$
- 输出：$y = f(\xv)$，$\Pr[y | \xv]$

<div class="top_5">
  <img src="plot/active3.svg" height="300px">
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>

<!-- slide data-notes="最后来看下 强化学习 如果知道/不知道房间结构 直接走出去 先探探路 熟悉环境" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">强化学习 引子</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

2$\longrightarrow$5

<div class="multi_column top_2">
<img src="img/rl.svg" width=530px height=431px style="margin:-50px auto"/>
</div>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="抽象化成有向无环图 但还不够 没有引导作用" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">强化学习 引子</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  graph [ranksep=0.7 nodesep=0.6]
  node [shape=circle fontsize=16 fontname="Source Sans Pro"]
  edge [arrowhead=vee arrowsize=0.8]
  rankdir=LR
  
  0 -> 4 -> 0

  {1, 4} -> 5
  5 -> {1, 4}
  5:e -> 5:e

  2 -> 3 -> 1 -> 3 -> 2

  3 -> 4 -> 3

  5 [fillcolor=gray, style=filled]
  2 [fillcolor=gold, style=filled]

  {rank = same; 0; 2;}
  {rank = same; 3; 4;}
  {rank = same; 1; 5;}
}
```

形式化：有限状态自动机

核心问题：快速熟悉环境，走向目标状态

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="引入边上的权重 可以看作移动一步获得的分数 二步的分数计算 引入折扣引子 二步到目标状态和一步到目标状态肯定不一样" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">强化学习 引子</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  graph [ranksep=0.7 nodesep=0.6]
  node [shape=circle fontsize=16 fontname="Source Sans Pro"]
  edge [arrowhead=vee arrowsize=0.8]
  rankdir=LR

  0 -> 4 -> 0 [xlabel=0]

  {1, 4} -> 5 [xlabel=100]
  5:e -> 5:e [xlabel=100]
  5 -> {1, 4} [xlabel=0]

  2 -> 3 -> 1 -> 3 -> 2 [xlabel=0]

  3 -> 4 -> 3 [xlabel=0]

  5 [fillcolor=gray, style=filled]
  2 [fillcolor=gold, style=filled]

  {rank = same; 0; 2;}
  {rank = same; 3; 4;}
  {rank = same; 1; 5;}
}
```

<div style="margin-top:-230px;margin-left:360px">
<p style="font-size:26px">
$$
\begin{align*}
  Q^1 = 
  \begin{array}{c|ccccc}
    & 0 & 1 & 2 & 3 & 4 & 5 \\ 
    \hline 
    0 & & & & & 0 \\
    1 & & & & 0 & & 100 \\
    2 & & & & 0 \\
    3 & & 0 & 0 & & 0 \\
    4 & 0 & & & 0 & & 100 \\
    5 & & 0 & & & 0 & 100 \\
	\end{array}
\end{align*}
$$
</p></div>

引入折扣引子$\gamma = 0.8$
$$
  \begin{align*}
    Q^2 (0,4) & = 0 + \gamma \cdot \max \{ Q^1 (4,0), Q^1 (4,3), \color{blue}{Q^1 (4,5)} \} = 80 \\
    Q^2 (3,1) & = 0 + \gamma \cdot \max \{ Q^1 (1,3), \color{blue}{Q^1 (1,5)} \} = 80
  \end{align*}
$$

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="所以更新一下 这个矩阵记为Q2" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">强化学习 引子</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  graph [ranksep=0.7 nodesep=0.6]
  node [shape=circle fontsize=16 fontname="Source Sans Pro"]
  edge [arrowhead=vee arrowsize=0.8]
  rankdir=LR

  0 -> 4 [xlabel=80]
  4 -> 0 [xlabel=0]

  {1, 4} -> 5 [xlabel=180]
  5:e -> 5:e [xlabel=180]

  {1, 2, 4} -> 3 [xlabel=0]
  {3,5} -> {1,4} [xlabel=80]
  3 -> 2 [xlabel=0]

  5 [fillcolor=gray, style=filled]
  2 [fillcolor=gold, style=filled]

  {rank = same; 0; 2;}
  {rank = same; 3; 4;}
  {rank = same; 1; 5;}
}
```

<div style="margin-top:-230px;margin-left:360px">
<p style="font-size:26px">
$$
\begin{align*}
  Q^2 = 
  \begin{array}{c|ccccc}
    & 0 & 1 & 2 & 3 & 4 & 5 \\ 
    \hline 
    0 & & & & & 80 \\
    1 & & & & 0 & & 180 \\
    2 & & & & 0 \\
    3 & & 80 & 0 & & 80 \\
    4 & 0 & & & 0 & & 180 \\
    5 & & 80 & & & 80 & 180 \\
	\end{array}
\end{align*}
$$
</p></div>

引入折扣引子$\gamma = 0.8$
$$
  \begin{align*}
    Q^2 (0,4) & = 0 + \gamma \cdot \max \{ Q^1 (4,0), Q^1 (4,3), \color{blue}{Q^1 (4,5)} \} = 80 \\
    Q^2 (3,1) & = 0 + \gamma \cdot \max \{ Q^1 (1,3), \color{blue}{Q^1 (1,5)} \} = 80
  \end{align*}
$$

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="同理可以算出三步的分数" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">强化学习 引子</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  graph [ranksep=0.7 nodesep=0.6]
  node [shape=circle fontsize=16 fontname="Source Sans Pro"]
  edge [arrowhead=vee arrowsize=0.8]
  rankdir=LR

  0 -> 4 [xlabel=144]
  4 -> 0 [xlabel=64]

  {1, 4} -> 5 [xlabel=244]
  5:e -> 5:e [xlabel=244]

  {1, 2, 4} -> 3 [xlabel=64]
  {3,5} -> {1,4} [xlabel=144]
  3 -> 2 [xlabel=0]

  5 [fillcolor=gray, style=filled]
  2 [fillcolor=gold, style=filled]

  {rank = same; 0; 2;}
  {rank = same; 3; 4;}
  {rank = same; 1; 5;}
}
```

<div style="margin-top:-230px;margin-left:360px">
<p style="font-size:26px">
$$
\begin{align*}
  Q^3 = 
  \begin{array}{c|ccccc}
    & 0 & 1 & 2 & 3 & 4 & 5 \\ 
    \hline 
    0 & & & & & 144 \\
    1 & & & & 64 & & 244 \\
    2 & & & & 64 \\
    3 & & 144 & 0 & & 144 \\
    4 & 64 & & & 64 & & 244 \\
    5 & & 144 & & & 144 & 244 \\
	\end{array}
\end{align*}
$$
</p></div>

$$
  \begin{align*}
    Q^3 (*,4) & = 0 + \gamma \cdot \max \{ Q^2 (4,0), Q^2 (4,3), \color{blue}{Q^2 (4,5)} \} = 144 \\
    Q^3 (*,1) & = 0 + \gamma \cdot \max \{ Q^2 (1,3), \color{blue}{Q^2 (1,5)} \} = 144 \\
    Q^3 (*,3) & = 0 + \gamma \cdot \max \{ \color{blue}{Q^2 (3,1)}, Q^2 (3,2), \color{blue}{Q^2 (3,4)} \} = 64
  \end{align*}
$$

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="由于折扣引子的存在 最终会收敛 这个值反应了一直不停地走可以获得的最大值" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">强化学习 引子</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  graph [ranksep=0.7 nodesep=0.6]
  node [shape=circle fontsize=16 fontname="Source Sans Pro"]
  edge [arrowhead=vee arrowsize=0.8]
  rankdir=LR

  0 -> 4 [xlabel=400]
  4 -> 0 [xlabel=320]

  {1, 4} -> 5 [xlabel=<<font color='blue'>500</font>> color=blue]
  5:e -> 5:e [xlabel=500]

  {1, 4} -> 3 [xlabel=320]
  2 -> 3 [xlabel=<<font color='blue'>320</font>> color=blue]
  3 -> {1,4} [xlabel=<<font color='blue'>400</font>> color=blue]
  5 -> {1,4} [xlabel=400]
  3 -> 2 [xlabel=256]

  5 [fillcolor=gray, style=filled]
  2 [fillcolor=gold, style=filled]

  {rank = same; 0; 2;}
  {rank = same; 3; 4;}
  {rank = same; 1; 5;}
}
```

<div style="margin-top:-230px;margin-left:360px">
<p style="font-size:26px">
$$
\begin{align*}
  \begin{array}{c|ccccc}
    & 0 & 1 & 2 & 3 & 4 & 5 \\ 
    \hline 
    0 & & & & & 400 \\
    1 & & & & 320 & & 500 \\
    2 & & & & 320 \\
    3 & & 400 & 256 & & 400 \\
    4 & 320 & & & 320 & & 500 \\
    5 & & 400 & & & 400 & 500 \\
	\end{array}
\end{align*}
$$
</p></div>

最优轨迹：
- $2 \longrightarrow 3 \longrightarrow 1 \longrightarrow 5$
- $2 \longrightarrow 3 \longrightarrow 4 \longrightarrow 5$

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">基本概念</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  graph [ranksep=0.7 nodesep=0.6]
  node [shape=circle fontsize=16 fontname="Source Sans Pro"]
  edge [arrowhead=vee arrowsize=0.8]
  rankdir=LR

  0 -> 4 -> 0 [xlabel=0]

  {1, 4} -> 5 [xlabel=100]
  5:e -> 5:e [xlabel=100]

  5 -> {1, 4} [xlabel=0]

  2 -> 3 -> 1 -> 3 -> 2 [xlabel=0]

  3 -> 4 -> 3 [xlabel=0]

  5 [fillcolor=gray, style=filled]
  2 [fillcolor=gold, style=filled]

  {rank = same; 0; 2;}
  {rank = same; 3; 4;}
  {rank = same; 1; 5;}
}
```

<div style="margin-top:-220px;margin-left:460px">
<p>
<ul style="width:100%">
  <li>
    状态集合$S = \{0, 1, 2, 3, 4, 5\}$
  </li>
  <li>
    动作集合$A = \{ 有向边 \}$
  </li>
  <li>
    转移概率$P_{s \rightarrow s'}^a: S \times A [\times S] \mapsto \Rbb$
  </li>
  <li>
    奖赏函数$R_{s \rightarrow s'}^a: S [\times A] \times S \mapsto \Rbb$
  </li>
  <li>
    确定策略$\pi(s): S \mapsto A$
  </li>
  <li>
    随机策略$\pi(a|s): S \times A \mapsto \Rbb$
  </li>
</ul>
</p></div>

<p style="margin-top:40px;margin-bottom:-30px">
“传统”机器学习　vs.　强化学习
</p>

```dot
digraph g {
  node[shape=box, fontsize=20, fontname="fz-sxslk"]
  edge [arrowhead=vee arrowsize=0.8, fontname="fz-sxslk"]
  graph [nodesep=0.8, ranksep=2.6]

  subgraph ml {
    label = 机器学习
    subgraph nrl {
      label = 非强化学习
      m1 [label="机器"]
      {rank = same; m1 数据 模型}
      m1 -> 数据 -> 模型
    }
    subgraph rl {
      label = 强化学习
      m2 [label="机器"]
      {rank = same; m2 环境}
      m2:ne -> 环境:nw [xlabel="动作"]
      环境:sw -> m2:se [xlabel="  状态"]
      环境:w -> m2:e [xlabel="  奖赏", style=dashed]
    }
  }
}
```

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="给定策略 就可以得到一个状态转移轨迹 目标就是寻找策略 最大化期望累积奖赏 考虑全部路径比较麻烦 可以先考虑初始状态为s的case 然后再对s求期望 类似于算年级平均分时先按班级算" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">基本概念</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

策略$\pi \rightarrow$轨迹$\tau: s_0 \stackrel{a_0 / r_1}{\longrightarrow} s_1 \stackrel{a_1 / r_2}{\longrightarrow} s_2 \stackrel{a_2 / r_3}{\longrightarrow} \cdots \stackrel{a_{t-1} / r_t}{\longrightarrow} s_t \stackrel{a_t / r_{t+1}}{\longrightarrow} \cdots$

轨迹$\tau$的累积奖赏：$G^\pi (\tau) = \sum_{t=0}^\infty \gamma^t r_{t+1}$

目标：$\pi^\star = \argmax_\pi \sum_\tau G^\pi (\tau) = \argmax_\pi \sum_s \sum_\tau G^\pi (\tau(s_0) = s)$

```dot
digraph g {
  graph [nodesep=0.2, ranksep=0.15]
  node [label="" shape=circle]
  edge [arrowhead=vee arrowsize=0.8]

  subgraph cluster_0 {
    style = invis
    s [label=<<i>s</i>>]
    s -> {a1, a2, a3}
    a1 -> {a11, a12} [style=dashed]
    a2 -> {a21, a22} [style=dashed]
    a3 -> {a31, a32} [style=dashed]
    a11 [style = dashed]
    a12 [style = dashed]
    a21 [style = dashed]
    a22 [style = dashed]
    a31 [style = dashed]
    a32 [style = dashed]
  }

  subgraph cluster_1 {
    style = invis
    s1 -> {b1, b2, b3}
    b1 -> {b11, b12} [style=dashed]
    b2 -> {b21, b22} [style=dashed]
    b3 -> {b31, b32} [style=dashed]
    b11 [style = dashed]
    b12 [style = dashed]
    b21 [style = dashed]
    b22 [style = dashed]
    b31 [style = dashed]
    b32 [style = dashed]
  }
}
```

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="从状态s出发期望得到的总分数就是状态值函数 想象成一个向量 最大特点 有递归形式 称为Bellman方程 最终解就是唯一的不动点" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">值函数</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  graph [nodesep=0.2, ranksep=0.25]
  node [shape=circle]
  edge [arrowhead=vee arrowsize=0.8 fontname="fz-sxslk"]

  s [label=<<i>s</i>> fillcolor=gold style=filled]

  node [shape=box]
  a [label=<<i>a</i>>]
  a2 [label="" style=dashed]
  a3 [label="" style=dashed]
  a4 [label="" style=dashed]
  s -> a [xlabel="动作"]
  s -> {a2, a3, a4} [style=dashed]
  
  node [shape=circle]
  ss [label=<<i>s'</i>>]
  a -> ss [xlabel="转移"]
  a -> {a12, a13} [style=dashed]
  a2 -> {a21, a22, a23} [style=dashed]
  a3 -> {a31, a32, a33} [style=dashed]
  a4 -> {a41, a42, a43} [style=dashed]
  
  a12 [label="" style=dashed]
  a13 [label="" style=dashed]
  a21 [label="" style=dashed]
  a22 [label="" style=dashed]
  a23 [label="" style=dashed]
  a31 [label="" style=dashed]
  a32 [label="" style=dashed]
  a33 [label="" style=dashed]
  a41 [label="" style=dashed]
  a42 [label="" style=dashed]
  a43 [label="" style=dashed]
}
```

状态值函数：$\color{blue}{V^\pi (s)} = \sum_a \pi(a|s) \sum_{s'} P_{s \rightarrow s'}^a [R_{s \rightarrow s'}^a + \gamma \color{blue}{V^\pi (s')]}$

Bellman方程：递归形式，压缩映射，不动点

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="如果关注从状态s出发 采用动作a得到的期望分数 就是状态动作值函数 从图上看 就是只看这个分支 如果确定策略 即只有一个分支 我们前面那个例子里 一直迭代计算的就是状态动作值函数" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">值函数</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  graph [nodesep=0.2, ranksep=0.25]
  node [shape=circle]
  edge [arrowhead=vee arrowsize=0.8 fontname="fz-sxslk"]

  s [label=<<i>s</i>> fillcolor=gold style=filled]

  node [shape=box]
  a [label=<<i>a</i>> fillcolor=gold style=filled]
  a2 [label="" style=dashed]
  a3 [label="" style=dashed]
  a4 [label="" style=dashed]
  s -> a [xlabel=<<font color='gold'>动作</font>> color=gold]
  s -> {a2, a3, a4} [style=dashed]
  
  node [shape=circle]
  ss [label=<<i>s'</i>>]
  a -> ss [xlabel="转移"]
  a -> {a12, a13} [style=dashed]
  a2 -> {a21, a22, a23} [style=dashed]
  a3 -> {a31, a32, a33} [style=dashed]
  a4 -> {a41, a42, a43} [style=dashed]
  
  a12 [label="" style=dashed]
  a13 [label="" style=dashed]
  a21 [label="" style=dashed]
  a22 [label="" style=dashed]
  a23 [label="" style=dashed]
  a31 [label="" style=dashed]
  a32 [label="" style=dashed]
  a33 [label="" style=dashed]
  a41 [label="" style=dashed]
  a42 [label="" style=dashed]
  a43 [label="" style=dashed]
}
```

状态值函数：$V^\pi (s) = \sum_a \pi(a|s) \color{blue}{\sum_{s'} P_{s \rightarrow s'}^a [R_{s \rightarrow s'}^a + \gamma V^\pi (s')]}$

状态-动作值函数：$Q^\pi(s,a) = \sum_{s'} P_{s \rightarrow s'}^a [R_{s \rightarrow s'}^a + \gamma V^\pi (s')]$

当$\pi$为确定策略且$\pi(s) = a$时，$V^\pi (s) = Q^\pi(s,a)$

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">大纲</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  rankdir=LR
  node [shape="box" fontsize=15 fontname="fz-sxslk" fontcolor=lightgray color=lightgray]
  edge [arrowhead=vee arrowsize=0.8 color=lightgray]

  人工智能 -> 逻辑推理 
  人工智能 -> 知识工程 
  人工智能 -> 机器学习

  机器学习 -> 监督学习
  机器学习 -> 无监督学习
  机器学习 -> 半监督学习
  机器学习 -> 主动学习

  node[fontcolor=black color=black]
  机器学习 -> 强化学习

  edge [color=black]
  强化学习 -> 值函数估计  
  强化学习 -> 策略搜索
  强化学习 -> 其它话题

  值函数估计 -> 策略迭代
  值函数估计 -> 值迭代
  值函数估计 -> 蒙特卡洛
  值函数估计 -> 时序差分

  策略搜索 -> 策略梯度
  ac [label="演员-评论家"]
  策略搜索 -> ac

}
```

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="总的来说有两种思路" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">两种思路</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

值函数估计：
- 先估计最优值函数，再据此求得最优策略$\pi^\star(s) = \argmax_a Q^\star (s,a)$
- 固定最优策略，最优值函数是Bellman方程的不动点
- 先有鸡？先有蛋？
- DeepMind

策略搜索：
- 绕过值函数，直接求最优策略
- OpenAI

孰优孰劣？信仰

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">大纲</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  rankdir=LR
  node [shape="box" fontsize=15 fontname="fz-sxslk" fontcolor=lightgray color=lightgray]
  edge [arrowhead=vee arrowsize=0.8 color=lightgray]

  人工智能 -> 逻辑推理 
  人工智能 -> 知识工程 
  人工智能 -> 机器学习

  机器学习 -> 监督学习
  机器学习 -> 无监督学习
  机器学习 -> 半监督学习
  机器学习 -> 主动学习

  node[fontcolor=black color=black]
  机器学习 -> 强化学习

  edge [color=black]
  强化学习 -> 值函数估计  
  
  值函数估计 -> 策略迭代
  值函数估计 -> 值迭代
  值函数估计 -> 蒙特卡洛
  值函数估计 -> 时序差分

  node [fontcolor=lightgray color=lightgray]
  edge [color=lightgray]
  强化学习 -> 策略搜索
  强化学习 -> 其它话题

  策略搜索 -> 策略梯度
  ac [label="演员-评论家"]
  策略搜索 -> ac
}
```

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide data-notes="刚才说了这里有个先有蛋还是先有鸡的问题 最简单的办法就是交替更新 值函数是连续的 策略函数是离散的" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">策略迭代</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

策略迭代：交替更新
1. 随机初始化策略$\pi$和$\pi'$
2. while $\pi \neq \pi'$ do
3. &emsp;&emsp;迭代$V^\pi(s) \leftarrow \sum_a \pi(a|s) \sum_{s'} P_{s \rightarrow s'}^a [R_{s \rightarrow s'}^a + \gamma V^\pi (s')]$至不动点
4. &emsp;&emsp;计算状态-动作值函数$Q^\pi(s,a) \leftarrow \sum_{s'} P_{s \rightarrow s'}^a [R_{s \rightarrow s'}^a + \gamma V^\pi (s')]$
5. &emsp;&emsp;更新策略$\pi'(s) \leftarrow \argmax_a Q^\pi(s,a)$
6. end while

缺点：当值函数$V^\pi (s)$未收敛到不动点时，策略函数$\pi$可能就已经收敛了，计算力的巨大浪费

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="由于最优策略必然是确定性策略 因为当值函数达到最优时 最大化期望分数必然是在每个状态取分数最大的动作 因此可以直接考虑值函数迭代 以上两种方法都依赖状态转移矩阵已知" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">值迭代</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

最优策略必然是确定策略：
$$
\begin{align*}
  V^\star (s) = \max_a \sum_{s'} P_{s \rightarrow s'}^a [R_{s \rightarrow s'}^a + \gamma V^\star (s')]
\end{align*}
$$

<p style="margin-top:-2%">
值迭代：
</p>

1. 随机初始化状态值函数$V(s)$
2. while $V(s)$没有收敛 do
3. &emsp;&emsp;$V (s) \leftarrow \max_a \sum_{s'} P_{s \rightarrow s'}^a [R_{s \rightarrow s'}^a + \gamma V (s')]$直至收敛到不动点
4. end while
5. 计算$Q^\star(s,a)$，$\pi^\star (s) = \argmax_a Q^\star(s, a)$

有模型方法：状态转移矩阵$P$已知，可以求解Bellman方程

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="当状态转移矩阵未知时 无法求解Bellman方程 因此可以考虑用蒙特卡洛法进行随机模拟 蒙特卡洛就是撒豆子" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">蒙特卡洛</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

基本想法：多次随机模拟求平均
$$
\begin{align*}
  V^\pi (s) \approx \frac{1}{N} \sum_{n=1}^N G(\tau_{s_0=s}^{(n)})
\end{align*}
$$

1. 随机初始化状态值函数$V(s)$
2. for $t = 1, 2, \ldots$ do
3. &emsp;&emsp;for $s \in S$ do
4. &emsp;&emsp;&emsp;&emsp;执行策略$\pi$产生$N$条轨迹，计算$V^\pi (s)$
5. &emsp;&emsp;end for
6. &emsp;&emsp;计算$Q (s,a)$，更新策略$\pi(s)$
7. end for

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="利用走一步值估计当前" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">时序差分</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

蒙特卡洛需要足够多的完整轨迹，效率太低，结合Bellman方程和蒙特卡洛随机模拟
$$
\begin{align*}
  V(s) \leftarrow (1 - \alpha) V(s) + \alpha (R_{s \rightarrow s'}^{\pi(s)} + \gamma V(s'))
\end{align*}
$$

1. 随机初始化状态值函数$V(s)$
2. for $t = 1, 2, \ldots$ do
3. &emsp;&emsp;for $s \in S$ do
4. &emsp;&emsp;&emsp;&emsp;$V(s) \leftarrow (1 - \alpha) V(s) + \alpha (R_{s \rightarrow s'}^{\pi(s)} + \gamma V(s'))$
5. &emsp;&emsp;end for
6. &emsp;&emsp;计算$Q (s,a)$，更新策略$\pi(s)$
7. end for

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="之前假设都是有限 所以值函数只是个数组 不可能遍历无穷个状态 只能依靠有限个采样进行插值 和统计机器学习类似 这时什么事样本" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">值函数近似</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

有限状态和动作：值函数是数组

无限状态和动作：值函数是真·函数

基本想法：借助统计机器学习，对值函数进行拟合：
$$
\begin{align*}
  \theta_\pi = \argmin_\theta (V^\pi(s) - \theta^\top \phi(s))^2
\end{align*}
$$

- $\phi(s)$：样本，$\phi$是对$s$的编码方式，类似于核函数
- $V^\pi(s)$：通过随机模拟获得
- $\theta$：通过梯度下降之类的方法进行更新

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">大纲</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  rankdir=LR
  node [shape="box" fontsize=15 fontname="fz-sxslk" fontcolor=lightgray color=lightgray]
  edge [arrowhead=vee arrowsize=0.8 color=lightgray]

  人工智能 -> 逻辑推理 
  人工智能 -> 知识工程 
  人工智能 -> 机器学习

  机器学习 -> 监督学习
  机器学习 -> 无监督学习
  机器学习 -> 半监督学习
  机器学习 -> 主动学习

  node[fontcolor=black color=black]
  机器学习 -> 强化学习

  node [fontcolor=lightgray color=lightgray]
  edge [color=lightgray]

  强化学习 -> 值函数估计  
  
  值函数估计 -> 策略迭代
  值函数估计 -> 值迭代
  值函数估计 -> 蒙特卡洛
  值函数估计 -> 时序差分

  node [fontcolor=black color=black]
  edge [color=black]
  强化学习 -> 策略搜索
  策略搜索 -> 策略梯度
  ac [label="演员-评论家"]
  策略搜索 -> ac

  node [fontcolor=lightgray color=lightgray]
  edge [color=lightgray]
  强化学习 -> 其它话题
}
```

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">策略梯度</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

基本想法：将策略$\pi(a|s)$写成以$\theta$为参数的连续可微函数
$$
\begin{align*}
  \theta \longrightarrow \pi_\theta (a|s) \longrightarrow \tau \longrightarrow \sum_\tau G^\pi (\tau)
\end{align*}
$$

<p style="margin-top:-2%" >
目标：$\pi^\star = \argmax_\pi \sum_\tau G^\pi (\tau) \longrightarrow \theta^\star = \argmax_\theta \sum_\tau G^\pi (\tau)$

代表性方法：

- REINFORCE算法：采样一条轨迹，随机梯度上升更新$\theta$
- 带基准线的REINFORCE算法：多引入一个控制变量减小方差

缺点：需要采集整条轨迹

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="名字很酷 但并没有太多创新 只是之前想法的结合 所以给算法起个抓眼的名字也很重要 具体来说演员是 评论家是 每轮根据时序差分估计出的值来更新值函数的参数 然后用策略梯度法更新策略函数的参数" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">演员-评论家</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

基本想法：不采样整条轨迹，利用时序差分

演员-评论家算法：
- 演员：策略函数$\pi_\theta (a|s)$
- 评论家：值函数$V_\varphi (s)$

每一轮：
- 时序差分更新$\varphi = \argmin_\varphi (V_\varphi (s) - R_{s \rightarrow s'} - \gamma V_\varphi (s'))^2$
- 策略梯度法更新$\theta$

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="以上都是强化学习领域最经典的算法 都是写进教科书的 可以看到它们都相同的套路 就是。。。 然后这些算法都各有很多改进的变种 这里简单列一些 比如对值函数近似 可以引进很多传统机器学习常用的技术" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">一些改进工作</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

固定套路：执行策略$\longrightarrow$估计回报$\longrightarrow$更新策略

值函数近似：$\theta_\pi = \argmin_\theta (V^\pi(s) - \theta^\top \phi(s))^2$
- 引进正则项控制过拟合，$\| \theta \|_2^2 \rightarrow$岭回归、$\| \theta \|_1 \rightarrow$LASSO
- 编码方式$\phi(\cdot)$的设计方式：高斯核、拉普拉斯核、扩散小波

策略迭代：
- 提高样本的使用效率：重要性采样
- 引入主动学习的思想加速收敛

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide data-notes="最后聊点这个领域比较前沿的话题" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">大纲</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

```dot
digraph g {
  rankdir=LR
  node [shape="box" fontsize=15 fontname="fz-sxslk" fontcolor=lightgray color=lightgray]
  edge [arrowhead=vee arrowsize=0.8 color=lightgray]

  人工智能 -> 逻辑推理 
  人工智能 -> 知识工程 
  人工智能 -> 机器学习

  机器学习 -> 监督学习
  机器学习 -> 无监督学习
  机器学习 -> 半监督学习
  机器学习 -> 主动学习

  node[fontcolor=black color=black]
  机器学习 -> 强化学习

  node [fontcolor=lightgray color=lightgray]
  edge [color=lightgray]

  强化学习 -> 值函数估计  
  
  值函数估计 -> 策略迭代
  值函数估计 -> 值迭代
  值函数估计 -> 蒙特卡洛
  值函数估计 -> 时序差分

  强化学习 -> 策略搜索
  策略搜索 -> 策略梯度
  ac [label="演员-评论家"]
  策略搜索 -> ac

  node [fontcolor=black color=black]
  edge [color=black]
  强化学习 -> 其它话题
}
```

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="首先就是深度强化学习" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">其它话题</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

深度强化学习：策略函数和值函数全部采用神经网络来近似

- 基于视觉感知的控制任务，打游戏：卷积神经网络
- 连续历史状态信息：循环神经网络
- 复杂状态：注意力机制

逆向强化学习：从人类专家提供的决策轨迹数据反推奖赏函数

分层强化学习：将最终目标分解为多个子任务来学习层次化的策略

迁移强化学习：星际争霸$\longrightarrow$DOTA

多智能体强化学习：八人局三国杀，无人机群

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="这些前沿话题中 最火爆的当属深度强化学习 alphago之父在16年ICML的tutorial上说  " --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">深度强化学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

研究现状：
- 门庭若市：三天的会议，一天半的深度强化学习

主要问题：
- 奖赏信号稀疏：很难甄别算法不work与代码有bug
- 性能不稳定：同一个算法同一套参数跑两次，结果可以大相近庭
- 幸存者偏差：大多数问题上其实都不work

适用任务：
- 数据获取非常容易
- 可以进行左右互搏
- 奖励函数容易定义

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>


<!-- slide vertical=true data-notes="至于未来的发展方向 堆硬件 这其实是全部用到深度学习的领域的通法 买显卡 加层数" --> 
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">深度强化学习</h5>
  </div>
  <img class="lab" src="../common/img/logo.jpg">
</div>

发展方向：
- 大力出奇迹：堆硬件，硬杠有限时间下随机模拟的不靠谱
- 利用有模型的学习任务：与迁移强化学习结合
- 自动学习奖励函数：与逆向强化学习结合

<h3 class="top_10">谢谢！</h3>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">zhangt_@hust.edu.cn</h6>
  </div>
</div>

