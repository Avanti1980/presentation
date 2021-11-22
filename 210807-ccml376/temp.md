---
presentation:
  transition: "none"
  enableSpeakerNotes: true
  margin: 0
---

@import "../common/css/font-awesome-4.7.0/css/font-awesome.css"
@import "../common/css/style-color.css"
@import "../common/css/margin.css"
@import "css/210807-ccml376.css"

<!-- slide vertical=true data-notes="我们在每个数据集上均进行了10次随机实验，并总结了均值和标准差。每个数据集上的最好结果以粗体显示，实心圆/空心圆分别代表对应数据集上ODMSSC在以95%显著性水平的成对t检验意义下显著优/劣于对比方法，可以看出在大多时候都显著优于其它对比方法，FM指数和归一化互信息也有类似的结果，我就不一一贴出来了" -->

HEADER Rand 指数结果

<div class="rand center threelines top2 head-highlight-1 tr-hover row12-border-bottom-solid column1-border-right-solid">

| 数据集         |     COPKMEANS      |       LCVQE        |      PCKMEANS      |      MKMEANS       |     MPCKMEANS      |        ODMSSC        |
| :------------- | :----------------: | :----------------: | :----------------: | :----------------: | :----------------: | :------------------: |
| dbworld        | $.494±.002\bullet$ | $.844±.035\bullet$ | $.494±.000\bullet$ | $.803±.035\bullet$ | $.501±.007\bullet$ | $\textbf{.939±.068}$ |
| leukemia       | $.528±.039\bullet$ | $.815±.143\bullet$ | $.576±.006\bullet$ | $.592±.021\bullet$ | $.542±.035\bullet$ | $\textbf{.931±.057}$ |
| fruitfly       | $.502±.005\bullet$ | $.499±.002\bullet$ | $.500±.002\bullet$ | $.503±.000\bullet$ | $.501±.004\bullet$ | $\textbf{.594±.043}$ |
| semeion        | $.840±.011\bullet$ | $.977±.003\bullet$ | $.975±.000\bullet$ |    $.981±.000$     | $.828±.019\bullet$ | $\textbf{.983±.004}$ |
| pizzaCutter    | $.528±.001\bullet$ | $.544±.049\bullet$ | $.530±.000\bullet$ | $.528±.000\bullet$ | $.588±.118\bullet$ | $\textbf{.827±.000}$ |
| pieChart       | $.531±.001\bullet$ | $.534±.056\bullet$ | $.531±.001\bullet$ | $.529±.000\bullet$ | $.531±.002\bullet$ | $\textbf{.816±.000}$ |
| pc4            | $.506±.000\bullet$ | $.502±.000\bullet$ | $.506±.000\bullet$ | $.505±.000\bullet$ | $.545±.079\bullet$ | $\textbf{.785±.000}$ |
| hivaAgnostic   | $.508±.001\bullet$ | $.509±.003\bullet$ | $.514±.000\bullet$ | $.509±.001\bullet$ | $.510±.003\bullet$ | $\textbf{.931±.001}$ |
| wilt           | $.500±.000\bullet$ | $.500±.000\bullet$ | $.500±.000\bullet$ | $.500±.000\bullet$ | $.500±.000\bullet$ | $\textbf{.900±.000}$ |
| wilpageBlo.  | $.632±.000\bullet$ | $.632±.000\bullet$ | $.632±.000\bullet$ | $.632±.000\bullet$ | $.632±.000\bullet$ | $\textbf{.817±.000}$ |
| JapaneseVo. | $.501±.000\bullet$ | $.500±.000\bullet$ | $.501±.000\bullet$ | $.501±.000\bullet$ | $.501±.000\bullet$ | $\textbf{.728±.000}$ |
| letter         | $.507±.000\bullet$ | $.507±.000\bullet$ | $.507±.000\bullet$ | $.507±.000\bullet$ | $.507±.000\bullet$ | $\textbf{.922±.000}$ |
| w/t/l          |      $12/0/0$      |      $12/0/0$      |      $12/0/0$      |      $11/1/0$      |      $12/0/0$      |        &nbsp;        |

</div>

FOOTER3 CCML'21 面向半监督聚类的最优间隔分布学习机 tengzhang@hust.edu.cn
