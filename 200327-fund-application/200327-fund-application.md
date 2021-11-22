---
presentation:
  transition: "none"
  enableSpeakerNotes: true
  margin: 0
---

@import "zhangt-style.css"
@import "../common/css/font-awesome-4.7.0/css/font-awesome.css"

<!-- slide data-notes="" -->
<div id="logo">
  <img src="../common/img/xiaohui.png" style="margin-left:1%" height=120px>
  <img src="../common/img/logo.png" height="120px">
</div>

<div>
  <h1 class="front_page_title top_10">青年科学基金项目申请</h1>
  <hr width=60%> 
  <h4 class="front_page_subtitle top_2">资源受限的最优间隔分布学习机的研究</h4>

  <h4 class="author top_10">张 腾</h4>
  <h4 class="mail">tengzhang@hust.edu.cn</h4>
  <h4 class="date">2020 / 03 / 27</h4>
</div>

<!-- slide data-notes="啊啊啊啊啊啊啊啊啊啊啊"-->
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">背景</h5>
  </div>
  <img class="lab" src="../common/img/logo.png">
</div>

```dot
digraph g {
  graph [nodesep=0.2 ranksep=0.5]
  style=filled
	bgcolor="#fdf6e3"

  node [shape=ellipse color="#073642" fontcolor="#b58900" fontsize=16 fontname="EB Garamond,fz-sxslk"]
  edge [arrowhead=vee color="#073642" fontcolor="#268bd2" fontsize=16 fontname="EB Garamond,fz-sxslk" arrowsize=0.6]

  间隔：样本点到分界面的距离 -> 最小间隔 [headlabel="VC维理论" labeldistance=3.5 labelangle=55]
  间隔：样本点到分界面的距离 -> "间隔均值 间隔方差" [label="间隔理论"]

  最小间隔 -> 支持向量机 [label="  启发"]

  node [fontcolor="#d33682"]

  "间隔均值 间隔方差" -> 最优间隔分布学习机 [label="  启发"]

  edge [fontcolor="#dc322f"]

  "间隔均值 间隔方差" -> 最小间隔 [label="更本质" constraint=false]

  最优间隔分布学习机 -> 支持向量机 [label="更优异" constraint=false]

  node [shape=box]

  最优间隔分布学习机 -> {二分类 多分类 聚类 半监督 多示例}

  subgraph cluster_R {
    label="一点微小的工作"
    fontname="EB Garamond,fz-sxslk"
    fontcolor="#268bd2"
    style="dashed"
    labelloc="b"
    二分类 多分类 聚类 半监督 多示例
  }

  最优间隔分布学习机 -> {多标记 回归 特征选择}
}
```

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学计算机学院</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">tengzhang@hust.edu.cn</h6>
  </div>
</div>

<!-- slide data-notes="啊啊啊啊啊啊啊啊啊啊啊" vertical=true -->
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">问题</h5>
  </div>
  <img class="lab" src="../common/img/logo.png">
</div>

```dot
digraph g {
  graph [nodesep=0.8 ranksep=0.5]
  style=filled
	bgcolor="#fdf6e3"

  node [shape=ellipse color="#073642" fontcolor="#b58900" fontsize=16 fontname="EB Garamond,fz-sxslk"]
  edge [arrowhead=vee color="#073642" fontcolor="#268bd2" fontsize=16 fontname="EB Garamond,fz-sxslk" arrowsize=0.6]

  ODM效率不高

  node [fontcolor="#d33682"]
  ODM效率不高 -> 资源受限的应用场景 [label=" 制约" fontcolor="#dc322f"]

  资源受限的应用场景 -> {计算资源,存储资源,时间资源}

  node [shape=box]
  时间资源 -> {实时交易,人机交互}
}
```

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学计算机学院</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">tengzhang@hust.edu.cn</h6>
  </div>
</div>

<!-- slide data-notes="啊啊啊啊啊啊啊啊啊啊啊" -->
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">内容</h5>
  </div>
  <img class="lab" src="../common/img/logo.png">
</div>

```dot
digraph g {
  graph [nodesep=0.5, ranksep=0.5]
  style=filled
	bgcolor="#fdf6e3"

  node [shape=ellipse color="#073642" fontcolor="#b58900" fontsize=16 fontname="EB Garamond,fz-sxslk"]
  edge [arrowhead=vee color="#073642" fontcolor="#268bd2" fontsize=16 fontname="EB Garamond,fz-sxslk" arrowsize=0.6]

  提高ODM的效率 -> {模型训练,模型测试,模型选择,模型复用}

  subgraph cluster_R {
    label="一个学习模型的完整生命周期"
    fontname="EB Garamond,fz-sxslk"
    fontcolor="#268bd2"
    style="dashed"
    模型训练 -> 模型测试 -> 模型选择 -> 模型复用 [constraint=false]
  }

  node [shape=box fontcolor="#d33682"]

  模型训练 -> 非线性核函数

  模型测试 -> 分布动态变化

  模型选择 -> 超参数过多

  模型复用 -> 多评价指标
}
```

- 非线性核函数：自适应选择核函数，并实现加速
- 分布动态变化：多个候选模型对冲，控制其数量，理论保证？
- 超参数过多：已知(超参数1、最优解1)，是否可以/如何快速得到(超参数2、？)
- 多评价指标：已有以准确率维优化目标的学习模型，是否可以/如何快速得到以Precision、Recall、F-measure、AUC等其它评价指标为优化目标的学习模型

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学计算机学院</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">tengzhang@hust.edu.cn</h6>
  </div>
</div>


<!-- slide data-notes="啊啊啊啊啊啊啊啊啊啊啊" vertical=true -->
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">意义</h5>
  </div>
  <img class="lab" src="../common/img/logo.png">
</div>

创新

- 我们AAAI'19的文章曾对ODM的核函数加速做过初步探索，现同时做核函数<span class="blue">选择</span>和<span class="blue">加速</span>，毕其功于一役
- 我们AAAI'20的文章曾对ODM的<span class="blue">动态遗憾界</span>做过分析，但ODM的数学性质没充分用起来，这意味着还可探索更加苛刻的<span class="blue">自适应遗憾界</span>
- 曾有人探索过部分统计学习模型中单个超参数与最优解的(分段线性)关系，而ODM则是<span class="blue">多个</span>超参数与最优解的<span class="blue">非线性关系</span>
- 如何将性质相近的评价指标纳入到统一的形式化框架下？如何高效求解？

价值

- 让最优间隔分布学习机这一新型统计学习框架可以进入更多的实际应用
- 在全民跟风 all in 深度学习时，需有人不忘初心，坚守退潮的领域(大雾)

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学计算机学院</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">tengzhang@hust.edu.cn</h6>
  </div>
</div>


<!-- slide data-notes="" -->
<div class="multi_column">
  <div class="title_hr">
    <hr class="hr_top">
    <h5 class="title">完结</h5>
  </div>
  <img class="lab" src="../common/img/logo.png">
</div>

<h3 class="top_15">敬请各位专家批评指正</h3>
<h3 class="top_3">谢谢！</h3>

<div class="footer">
  <hr class="hr_bottom">
  <div class="multi_column">
    <h6 class="bottom_left">华中科技大学计算机学院</h6>
    <h6 class="bottom_center">SCTS & CGCL</h6>
    <h6 class="bottom_right">tengzhang@hust.edu.cn</h6>
  </div>
</div>
