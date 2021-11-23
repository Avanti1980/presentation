---
presentation:
  transition: "none"
  enableSpeakerNotes: true
  margin: 0
---

@import "../common/css/font-awesome-4.7.0/css/font-awesome.css"
@import "../common/css/style-color.css"
@import "../common/css/margin.css"

<!-- slide data-notes="" -->
<div class="header"><img class="hust"><img class="bdts"></div>

<div class="bottom15"></div>

# 青年科学基金项目申请

<hr class="width60">

## 资源受限的最优间隔分布学习机的研究

### 张腾

### tengzhang@hust.edu.cn

### 2020 / 03 / 27

<!-- slide data-notes=""-->

HEADER 背景

@import "../dot/odm-review-fund.dot" {.center .top5}

FOOTER3 华科计算机学院 SCTS/CGCL/BDTS tengzhang@hust.edu.cn

<!-- slide data-notes="" vertical=true -->

HEADER 问题

@import "../dot/odm-inefficiency.dot" {.center .top10}

FOOTER3 华科计算机学院 SCTS/CGCL/BDTS tengzhang@hust.edu.cn

<!-- slide data-notes="" -->

HEADER 内容

@import "../dot/odm-speedup.dot" {.center}

<div></div>

- 训练：自适应选择核函数，并实现加速
- 更新：分布动态变化，多个候选模型对冲，控制其数量，理论保证？
- 选择：已知 (超参数 1、最优解 1)，是否可以 / 如何快速得到 (超参数 2、？)
- 复用：已有以准确率为优化目标的学习模型，是否可以 / 如何快速得到以 Precision、Recall、F-measure、AUC 等其它评价指标为优化目标的学习模型

FOOTER3 华科计算机学院 SCTS/CGCL/BDTS tengzhang@hust.edu.cn

<!-- slide data-notes="" vertical=true -->

HEADER 意义

创新

- 我们 AAAI'19 的文章曾对 ODM 的核函数加速做过初步探索，现同时做核函数<span class="blue">选择</span>和<span class="blue">加速</span>，毕其功于一役
- 我们 AAAI'20 的文章曾对 ODM 的<span class="blue">动态遗憾界</span>做过分析，但 ODM 的数学性质没充分用起来，这意味着还可探索更加苛刻的<span class="blue">自适应遗憾界</span>
- 曾有人探索过部分统计学习模型中单个超参数与最优解的 (分段线性) 关系，而 ODM 则是<span class="blue">多个</span>超参数与最优解的<span class="blue">非线性关系</span>
- 如何将性质相近的评价指标纳入到统一的形式化框架下？如何高效求解？

价值

- 让最优间隔分布学习机这一新型统计学习框架可以进入更多的实际应用
- 在全民跟风 all in 深度学习时，需有人不忘初心，坚守退潮的领域 (大雾)

<p class="center top5 bottom-5">敬请各位专家批评指正!!</span>

FOOTER3 华科计算机学院 SCTS/CGCL/BDTS tengzhang@hust.edu.cn
