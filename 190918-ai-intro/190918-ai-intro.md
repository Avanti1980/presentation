---
presentation:
  transition: "none"
  enableSpeakerNotes: true
  margin: 0
---

@import "../common/css/font-awesome-4.7.0/css/font-awesome.css"
@import "../common/css/style-color.css"
@import "../common/css/margin.css"

<!-- slide data-notes="大家下午好，我是来自计算机学院的张腾，我的演讲题目是人工智能简介" -->
<div class="header"><img class="hust"><img class="bdts"></div>

<div class="bottom15"></div>

# 人工智能 简介

<hr class="width50">

## 微格教学法培训

<br>

### 张腾

### 2019 / 09 / 18

<!-- slide vertical=true data-notes="首先提到人工智能，大家会想到什么？" -->

HEADER 引子

@import "../puml/ai.puml" {.center .top10}

FOOTER3 SCTS/CGCL/BDTS 人工智能简介 tengzhang@hust.edu.cn

<!-- slide data-notes="可能有人会想到围棋程序alphago，16年一经面世就横扫围棋界，将李世乭、柯杰等多位世界冠军杀得毫无还手之力" data-background-video="../videos/alphago.mp4" data-background-video-loop data-background-video-muted -->

<!-- slide data-notes="可能也有人会想到自动驾驶，现在谷歌、百度、特斯拉许多公司都在布局研究" data-background-video="../videos/self-driving.mp4" data-background-video-loop data-background-video-muted vertical=true -->

<!-- slide data-notes="可能还有人会想到这个要destroy全人类的sophia" data-background-video="../videos/sophia.mp4" data-background-video-loop data-background-video-muted vertical=true -->

<!-- slide data-notes="没有问题，这些都是人工智能的经典应用，除此之外还有很多，例如……但是如果这个讲座只以纪传体的形式来展开，我觉得大家可能不会有太多收获，走马观花一样，看完就忘了" -->

HEADER 引子

@import "../dot/ai-app.dot"

FOOTER3 SCTS/CGCL/BDTS 人工智能简介 tengzhang@hust.edu.cn

<!-- slide data-notes="所以我打算以编年体的形式来组织内容，首先我会讲一讲人工智能产生的时代背景，然后以时间顺序简单回顾整个领域的发展历程，各个流派是如何你方唱罢我登场的，还有他们各自的想法和代表性技术分别是啥" vertical=true -->

HEADER 引子

@import "../dot/ai-app-dev.dot"

FOOTER3 SCTS/CGCL/BDTS 人工智能简介 tengzhang@hust.edu.cn

<!-- slide data-notes="人工智能的时代背景在维纳的《控制论》一书中有提到过，前两次工业革命出现了蒸汽机和发电机，人类开始用机器代替手工劳动，将人类从辛苦的体力劳动中解放出来，到上世纪中叶，前两次工业革命的红利基本吃完了，这些得益于前两次工业革命的资本主义强国又开始思考，是否还可以设计一些机器，将人类从复杂的脑力劳动中解放出来" -->

HEADER 人工智能 时代背景

维纳 《控制论》：

<br>

> 第一次工业革命：用某种机器来减轻甚至代替<span class="blue">体力</span>劳动

> 上世纪中叶：用某种新型机器来减轻甚至代替某些<span class="blue">脑力</span>劳动

FOOTER3 SCTS/CGCL/BDTS 人工智能简介 tengzhang@hust.edu.cn

<!-- slide data-notes="在这个大背景下，1956年，香浓、麦卡锡、明斯基、西蒙、纽维尔等人工智能的先驱在美国达特茅斯学院举行了一个研讨会，主题就是如何用机器模拟人的智能，这标志着人工智能的诞生，这一年也被称为人工智能元年" vertical=true -->

HEADER 人工智能 起源

达特茅斯会议

- 时间：1956 年
- 地点：达特茅斯学院
- 人物：香农、麦卡锡、明斯基、西蒙、纽厄尔等十人
- 事件：讨论用机器模拟人的智能

<br>

<div class="multi_column top_2">
    <img src="../common/img/birth-school.jpg" title="达特茅斯学院" width=425px height=277px class="left6">
    <img src="../common/img/birth-people.jpg" title="2006年会议50周年时还健在的5位参会者" width=425px height=277px class="right6 lefta">
</div>

FOOTER3 SCTS/CGCL/BDTS 人工智能简介 tengzhang@hust.edu.cn

<!-- slide data-notes="之后人工智能的发展经历了三次浪潮，首先是推理期" vertical=true -->

HEADER 人工智能 三次浪潮

推理期 热潮：1956 - 60 年代初，凛冬：60 年代中 - 60 年代末

- 机器擅长计算，人类擅长推理，<span class="blue">智能 = 逻辑推理</span>，数学机械化
- 西蒙和纽厄尔，“逻辑理论家”证明 《数学原理》 全部 52 条定理，1975 年图灵奖
- 面对更难的定理无能为力，十万步无法证明两个连续函数之和还是连续函数

<br>

知识期 热潮：70 年代初 - 80 年代初，凛冬：80 年代中 - 90 年代初

- 光会逻辑推理远远不够，机器得拥有知识，<span class="blue">智能 = 知识 + 逻辑推理</span>
- 费根鲍姆，专家系统 DENDRAL 于 1968 年问世，1994 年图灵奖
- 人工构建知识库成本太高，知识获取困难

<br>

学习期 热潮：90 年代中 - 2012，井喷：2012 - ？，凛冬将至？

- <span class="blue">知识由机器从数据中自动学习得到</span>
- PAC 可学习理论 (2010 年图灵奖)、贝叶斯网 (2011 年图灵奖)、深度学习 (2018 年图灵奖)

FOOTER3 SCTS/CGCL/BDTS 人工智能简介 tengzhang@hust.edu.cn

<!-- slide data-notes="人工智能的每一次兴起都伴随着对前一次热潮的反思，前两个流派也在借鉴最新的机器学习的思想，融合出了新的研究方向，符号主义现在摇身一变成了因果学习，专家系统也鸟枪换炮成了知识图谱，那么为了避免人工智能的第三次寒冬，我们应该思考机器学习的瓶颈是什么？又该引进哪些新技术新方法？" vertical=true -->

HEADER 小结

每一次兴起都伴随着对前一次热潮的反思

现状：流派间的相互融合

- 推理期：逻辑推理 → 因果学习
- 知识期：专家系统 → 知识图谱
- 学习期：机器学习

机器学习的瓶颈是啥？何去何从？

<hr class="width40 top10 bottom5">

### 谢谢！

FOOTER3 SCTS/CGCL/BDTS 人工智能简介 tengzhang@hust.edu.cn
