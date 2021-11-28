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

$$
\begin{align*}
    \begin{array}{c c}
    & \begin{array} {@{} c c c @{}}
      u_1 & \cdots & u_q
    \end{array} \\
    \begin{array}{c}
      e_1 \\ \vdots \\ e_n
    \end{array}\hspace{-1em} &
    \left(
      \begin{array}{@{} c c c @{}}
        u_{11} & \cdots & u_{1q} \\
        \vdots &        & \vdots \\
        u_{n1} & \cdots & u_{nq}
      \end{array}
    \right) \\
    \mbox{} % Blank line to match column names so as to align the = vertically
  \end{array}
\end{align*}
$$

FOOTER3 CCML'21 面向半监督聚类的最优间隔分布学习机 tengzhang@hust.edu.cn
