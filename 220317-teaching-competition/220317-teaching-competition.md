---
presentation:
  transition: "none"
  enableSpeakerNotes: true
  margin: 0
---

@import "../common/css/font-awesome-4.7.0/css/font-awesome.css"
@import "../common/css/style-color.css"
@import "../common/css/margin.css"
@import "../plugins/chalkboard/plugin.js"
@import "../plugins/customcontrols/plugin.js"

<!-- slide data-notes="各位专家老师下午好，我是张腾，我的教学竞赛题目是机器学习，首先是说课环节" -->
<div class="header"><img class="hust"></div>

<div class="bottom15"></div>

# 机器学习

<hr class="width50">

## 教学竞赛院系初赛 说课环节

<div class="bottom5"></div>

### 计算机科学与技术学院 &nbsp; &nbsp; 张腾

<br>

### 2022 - 03 - 17

<!-- slide vertical=true data-notes="首先提到机器学习，大家会想到什么？" -->

HEADER 引子

@import "../puml/ml.puml" {.center .top10}

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide data-notes="可能有人会想到alphago，这个围棋程序16年一经面世就横扫围棋界，将李世乭、柯杰等多位世界冠军杀得毫无还手之力" data-background-video="../videos/alphago.mp4" data-background-video-loop data-background-video-muted -->

<!-- slide data-notes="可能也有人会想到自动驾驶，现在百度、谷歌、特斯拉、比亚迪许多公司都在布局研究，我们国家也在出政策大力扶持" data-background-video="../videos/self-driving.mp4" data-background-video-loop data-background-video-muted vertical=true -->

<!-- slide data-notes="可能还有人会想到这个要destroy全人类的机器人sophia" data-background-video="../videos/sophia.mp4" data-background-video-loop data-background-video-muted vertical=true -->

<!-- slide data-notes="没有问题，这些都是机器学习的经典应用，除此之外还有很多，例如文字、图像、语音识别，自然语言处理等等……但是我们这是一门课，不可能以纪传体的形式，给大家挨个介绍应用，这样走马观花，大家也学不到什么硬核的干货" -->

HEADER 引子

@import "../dot/ml-app.dot"

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide data-notes="所以本课程会以编年体的形式来组织内容，首先我们会先讲讲机器学习产生的时代背景<br><br>然后以时间顺序回顾整个领域的发展历程，机器学习是一个由计算机、统计、应用数学、最优控制等多个学科交叉出来的新兴学科<br><br>在这门课大家会看到在机器学习这个大舞台上，这些来自不同学科背景的研究者逐渐形成的各大学派，是如何你方唱罢我登场的<br><br>最重要的，我们会带大家深入学习这些学派各自压箱底的独门绝技" vertical=true -->

HEADER 课程安排

@import "../dot/ml-app-dev.dot"

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="这张图就算这门课程的大纲，也是机器学习界的常见黑话大集合，这里给大家捋一下它们之间的关系<br><br>我们从更广义的概念人工智能说起，其方法从一开始的逻辑推理，到后来的知识工程，以及现在占绝对主导地位的机器学习<br><br>之后我们就会深入机器学习，依次给大家介绍三类经典模型的代表性方法<br><br>线性模型从简单的感知机，到引入间隔概念的支持向量机和可以进行概率输出的对数几率回归，多学习器组合模型则介绍基于bagging思想的随机森林、基于boosting思想的梯度提升树XGBoost，以及以贝叶斯公式为核心的生成式模型，包括隐马尔可夫模型、隐狄利克雷模型" -->

HEADER 课程大纲

@import "../dot/outline.dot"

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide data-notes="本课程会以周志华老师的西瓜书作为教材，李航老师的统计学习方法为参考补充，对于喜欢读外文著作的同学，推荐纽约大学Mohri教授的FOML" -->

HEADER 教科书 参考书 英文书

<div class="multi_column top6">
    <img src="../common/img/xigua.jpg" title="机器学习" width=280px height=400px class="left5">
    <img src="../common/img/lihang.jpeg" title="2006年会议50周年时还健在的5位参会者" width=280px height=400px class="left2">
    <img src="../common/img/foml.jpg" title="2006年会议50周年时还健在的5位参会者" width=280px height=400px class="left2">
</div>

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide data-notes="下面就是完整讲课部分" -->
<div class="header"><img class="hust"></div>

<div class="bottom15"></div>

# 机器学习

<hr class="width50">

## 教学竞赛院系初赛 完整讲课

<div class="bottom5"></div>

### 计算机科学与技术学院 &nbsp; &nbsp; 张腾

<br>

### 2022 - 03 - 17

<!-- slide vertical=true data-notes="这节课我们介绍机器学习的本源，关于人工智能的研究为何从一开始的逻辑推理，演化成了现在的机器学习" -->

HEADER 课程大纲

@import "../dot/outline-ai.dot"

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="首先，我们为什么要研究人工智能？控制论之父维纳，就是维纳滤波的那个维纳，在他的大作《控制论》中提到<br><br>第一次工业革命，人们期望...，于是瓦特发明了蒸汽机，第二次工业革命其实是第一次的延续，在法拉第发现电磁感应后，可以用更高效的电动机代替蒸汽机了<br><br>但是到了上世纪中叶，两次工业革命的红利已经消耗殆尽，于是人们又开始想...于是人工智能应运而生，要让机器像人一样拥有智能，关键问题是什么是智能？<br><br>讲完后提一下，现在我们国家也高度重视人工智能的发展，因为1760年第一次工业革命，1870年第二次工业革命我国都完全没赶上，互联网和移动互联网引发的第三次工业革命我们国家也只赶上个末班车，而西方国家确立对非西方的绝对优势就是这三次工业革命，所以对于人工智能技术推动的第四次工业革命非常重视，大家现在上车还来得及，但前提是好好学习这门课" -->

HEADER 背景

<br>

维纳 《控制论》：

<br>

> 第一次工业革命：用某种机器来减轻甚至代替<span class="blue">体力</span>劳动

> 上世纪中叶：用某种新型机器来减轻甚至代替某些<span class="blue">脑力</span>劳动

</br>

关键：让机器具有人类的智能

</br>

问题：什么是智能？

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="智能这一说法最早是图灵在他1950年的论文里提出的，后来被人们称为图灵测试...<br><br>要想通过图灵测试...学习指学习新东西、探索未知的能力，感知处理看和听，认知是思考和推理" -->

HEADER 起源

《Computing Machinery and Intelligence》

<div class="width62 left0 right0 top2 bottom2">

图灵在他 1950 年的这篇论文中提出了<span class="blue">图灵测试</span>：一个人在不接触对方的情况下，通过一种特殊的方式，和对方进行一系列的问答，如果在相当长时间内，他无法根据这些问题判断对方是人还是计算机，那么就可以认为这个计算机是智能的

</div>

要想通过图灵测试，机器得具备多种能力

- 学习：机器学习
- 感知：计算机视觉，语音识别
- 认知：知识表示，逻辑推理

<img src="../common/img/turing.jpg" title="图灵" style="margin-right:4rem;margin-left:auto;margin-top:-28rem;width:30%">

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="人工智能的元年一般认为是1956年，标志性事件就是达特茅斯会议<br><br>当时参会者一共有10个人，其中大佬有5位，麦卡锡(右图左二)是第一个函数式程序语言Lisp的发明人，1971年图灵奖得主<br><br>明斯基(右图中间)建造了世界上第一个神经网络模拟器，1969年图灵奖得主，但他后来写了本非常有名的书叫《感知机》，在书里明确表达了对领域的悲观，说神经网络连简单的异或问题都解决不了，直接带来了人工智能的10年寒冬<br><br>西蒙和纽厄尔编写了一个程序叫“逻辑理论家”，证明了罗素《数学原理》中的全部定理，1975年图灵奖得主，西蒙是中科院外籍院士，9个博士学位，中文名司马贺<br><br>纽厄尔一直是西蒙的合作者，曾在美国智库兰德公司供职<br><br>香农就是那个信息论之父，他是被麦卡锡拉过去站台的，他其实比这些人要大一些，成名也更早，虽然没得过图灵奖，不过他应该也不care，就像C罗搞个C罗奖颁给梅西，梅西也不一定会要<br><br>右图的5位是06年会议50周年时还建在的5位，另外5位已经仙逝，左一是东道主摩尔local chair，右二模式识别的奠基人赛弗里奇，MIT的人工智能实验室也是他创立的，右一是发明了算法概率论的所罗门诺夫" -->

HEADER 元年

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

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="前面已经说了，人工智能的发展按时间先后可大致可以分成三个阶段，<br><br>注意虽然现在是学习期，但不代表前两方面的研究已经销声匿迹，他们其实早就和机器学习结合，纷纷秽土转生了，例如..." -->

HEADER 发展

@import "../mermaid/ai.mermaid"

秽土转生

- 推理：反绎学习
- 知识：知识图谱

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide data-notes="首先是推理期，当时人工智能的先驱普遍都是数学家，所以他们的学科背景决定了当时对人工智能的理解就是能帮人证明数学定理，数学定理都是高度符号化的，所以这些人也被称为符号主义" -->

HEADER 推理期

机器擅长固定套路的计算 vs. 人类擅长妙手偶得的推理

<div class="bottom4"></div>

符号主义：<span class="blue">智能 = 逻辑推理</span>

<div class="bottom4"></div>

西蒙和纽厄尔设计了<span class="blue">逻辑理论家</span>程序

- 1952 年，逻辑理论家证明了 《数学原理》 中的 38 条定理
- 1963 年，证明了全部 52 条定理，其中定理 2.85 的证明比原书作者更巧妙
- 西蒙和纽厄尔获得了 1975 年的图灵奖

<div class="bottom4"></div>

衰退：

- 并非所有定理都可以方便地符号化，也并非所有问题都可以转换成推理问题
- 十万步内无法证明<span class="blue">两个连续函数之和还是连续函数</span>

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="下面我们看个简单的例子，机器怎么做推理" -->

HEADER 符号主义

根据以下事实判别谁说了实话

- $A$：$B$和$C$都是说谎者
- $B$：$A$和$C$都是说谎者
- $C$：$A$和$B$中至少有一个说谎者

<div class="threelines row7-border-top-solid column1-border-right-solid">

|   公式   |          $p \rightarrow q$           |  $\Longleftrightarrow$   |                   $\neg p \vee q$                    |
| :------: | :----------------------------------: | :----------------------: | :--------------------------------------------------: |
| **条件** | $A \rightarrow \neg B \wedge \neg C$ |  $\Longleftrightarrow$   | $1.~\neg A \vee \neg B, \quad 2.~\neg A \vee \neg C$ |
|          |    $\neg A \rightarrow B \vee C$     |  $\Longleftrightarrow$   |                 $3.~A \vee B \vee C$                 |
|          | $B \rightarrow \neg A \wedge \neg C$ |  $\Longleftrightarrow$   |               $4.~\neg B \vee \neg C$                |
|          |    $\neg B \rightarrow A \vee C$     |  $\Longleftrightarrow$   |                 $3.~A \vee B \vee C$                 |
|          |  $C \rightarrow \neg A \vee \neg B$  |  $\Longleftrightarrow$   |         $5.~\neg A \vee \neg B \vee \neg C$          |
|          |   $\neg C \rightarrow A \wedge B$    |  $\Longleftrightarrow$   |           $6.~A \vee C, \quad 7.~B \vee C$           |
| **归结** | $1 + 7 \rightarrow 8.~\neg A \vee C$ | $6 + 8 \rightarrow C$ |                     $C$说了实话                      |

</div>

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="从推理期得到的教训是光有逻辑推理远远不够，机器还得拥有知识，智能是将两者结合起来，于是出现了一些在特定领域内具有专家水平解决问题能力的程序系统，称为专家系统" -->

HEADER 知识期

教训：光有逻辑推理远远不够，机器还得拥有知识

<div class="bottom4"></div>

信仰：知识就是力量，<span class="blue">智能 = 知识 + 逻辑推理</span>

<div class="bottom4"></div>

专家系统 = 知识库 + 推理机

- 在特定领域内具有专家水平解决问题能力的程序系统
- 第一个成功的专家系统 DENDRAL 于 1968 年问世
- 知识工程之父费根鲍姆获得了 1994 年的图灵奖

<div class="bottom4"></div>

衰退：

- 人工构建知识库成本太高
- 很多知识获取困难，甚至无法被清晰地表示出来

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide vertical=true data-notes="" -->

HEADER 动物识别专家系统

@import "../dot/reasoning.dot"

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn

<!-- slide data-notes="对于人类的很多智能行为(比如语言理解、图像识别等) 我们很难知道其中的原理 也无法描述出这些智能行为背后的“知识” <br><br> 因此 我们也很难通过知识和推理的方式来实现这些行为的智能系统，为了解决这类问题，人们开始将研究重点转向让计算机从数据中自己学习，这就是机器学习<br><br>机器学习的基本流程是..." -->

HEADER 学习期

基本想法：让<span class="blue">机器</span>从数据中自动<span class="blue">学习</span>得到某种知识 (规律)

基本流程：

@import "../dot/ml-old.dot"

<div class="bottom0"></div>

原始数据：图片、视频、文本、语音、……

特征工程：

- 提取：选取对目标任务有用的潜在特征，如对西瓜提取色泽、根蒂、敲声等
- 处理：无序的离散类别特征 → 数值特征，特征缺失处理，特征标准化
- 变换：对特征进行挑选或映射得到对目标任务更有效的特征

模型学习：机器学习最核心的部分，学习一个特征到类别标记的映射

FOOTER3 教学竞赛院系初赛 机器学习 tengzhang@hust.edu.cn
