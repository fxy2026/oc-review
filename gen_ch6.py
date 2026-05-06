#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from gen_all import write_page

BODY = r'''
<h1>第6章 炔烃和二烯烃</h1>

<h2 id="kp">核心知识点</h2>

<h3 id="kp1">6.1 炔烃结构</h3>
<div class="card">
<div class="fb"><div class="t">炔烃的杂化与几何</div>
<p>C≡C 中碳为 <strong>sp 杂化</strong>，键角 <strong>180°</strong>（直线形）</p>
<p>三键 = 1σ + 2π，π 电子云呈圆筒形对称分布</p></div>
</div>

<h3 id="kp2">6.2 端炔的酸性</h3>
<div class="card">
<div class="fb"><div class="t">端炔 C-H 的酸性</div>
<p>$\text{RC≡CH}$ 的 $pK_a \approx 25$（远强于烯烃 ~44 和烷烃 ~50）</p>
<p>原因：sp 碳 s 成分 50%，电子更靠近碳核，稳定负电荷</p></div>

<div class="warn"><strong>酸性排序</strong>：$\text{C-H}$ 酸性 sp > sp$^2$ > sp$^3$<br>
$\text{HC≡CH}$ ($pK_a$ 25) > $\text{H}_2\text{C=CH}_2$ ($pK_a$ 44) > $\text{CH}_3\text{CH}_3$ ($pK_a$ 50)</div>

<div class="fb"><div class="t">炔钠的制备与应用</div>
<p>$\text{RC≡CH} + \text{NaNH}_2 \xrightarrow{\text{液NH}_3} \text{RC≡CNa} + \text{NH}_3$</p>
<p>炔钠是强亲核试剂，可与伯卤代烃发生 $\text{S}_\text{N}\text{2}$ 反应 → <strong>增长碳链</strong></p>
<p>$\text{RC≡CNa} + \text{R'CH}_2\text{X} \to \text{RC≡CCH}_2\text{R'}$</p></div>

<div class="warn"><strong>只能用伯卤代烃！</strong>仲/叔卤代烃会发生 E2 消除而非取代。</div>
</div>

<h3 id="kp3">6.3 炔烃的加氢</h3>
<div class="card">
<div class="fb"><div class="t">选择性加氢——控制产物立体化学</div>
<table>
<tr><th>条件</th><th>产物</th><th>立体化学</th></tr>
<tr><td>$\text{H}_2$/Lindlar 催化剂（Pd/CaCO$_3$/喹啉毒化）</td><td>顺式烯烃</td><td><strong>Z（cis）</strong></td></tr>
<tr><td>$\text{Na}/\text{NH}_3$(l)（溶解金属还原）</td><td>反式烯烃</td><td><strong>E（trans）</strong></td></tr>
<tr><td>$\text{H}_2$/Pd（过量）</td><td>烷烃</td><td>完全加氢</td></tr>
</table></div>

<div class="tip"><strong>记忆口诀</strong>：Lindlar → cis（L = 两个都在左/同侧）；Na/NH$_3$ → trans</div>
</div>

<h3 id="kp4">6.4 炔烃的亲电加成</h3>
<div class="card">
<div class="fb"><div class="t">加 HX（马氏规则）</div>
<p>1 mol HX → 乙烯基卤代物（可控停在一次加成）</p>
<p>2 mol HX → 偕二卤代物（两个 X 在同一碳上，马氏）</p></div>

<div class="fb"><div class="t">水合反应</div>
<p>内炔/端炔 + $\text{H}_2\text{O}$（$\text{HgSO}_4/\text{H}_2\text{SO}_4$ 催化）→ 烯醇 → 互变异构为<strong>酮</strong>（马氏）</p>
<p><strong>特例</strong>：乙炔水合 → 乙烯醇 → <strong>乙醛</strong>（唯一生成醛的情况）</p></div>

<div class="fb"><div class="t">硼氢化反应（端炔→醛）</div>
<p>端炔 + $(\text{Sia})_2\text{BH}$（二环己基硼烷），然后 $\text{H}_2\text{O}_2/\text{NaOH}$</p>
<p>→ 烯醇 → 互变异构为<strong>醛</strong>（反马氏，B 加到端碳）</p></div>

<div class="note"><strong>对比记忆</strong><br>
&bull; 汞盐水合（马氏）→ 酮（乙炔例外→醛）<br>
&bull; 硼氢化（反马氏）→ 醛</div>
</div>

<h3 id="kp5">6.5 端炔的鉴别</h3>
<div class="card">
<div class="fb"><div class="t">银氨/铜氨溶液鉴别端炔</div>
<p>$\text{RC≡CH} + \text{AgNO}_3/\text{NH}_3$ → $\text{RC≡CAg}↓$（白色沉淀）</p>
<p>$\text{RC≡CH} + \text{CuCl}/\text{NH}_3$ → $\text{RC≡CCu}↓$（红棕色沉淀）</p>
<p>内炔 $\text{RC≡CR'}$ <strong>无反应</strong>（无端基 H）</p></div>

<div class="warn"><strong>炔化银/炔化铜干燥后易爆炸！</strong>实验中需用稀硝酸分解回收。</div>
</div>

<h3 id="kp6">6.6 共轭二烯的加成</h3>
<div class="card">
<div class="fb"><div class="t">1,2-加成 vs 1,4-加成</div>
<p>1,3-丁二烯 + HBr：</p>
<table>
<tr><th>条件</th><th>主要产物</th><th>控制类型</th></tr>
<tr><td>低温（−80°C）快速</td><td>3-溴-1-丁烯（1,2-加成）</td><td><strong>动力学控制</strong></td></tr>
<tr><td>高温（40°C）/ 长时间</td><td>1-溴-2-丁烯（1,4-加成）</td><td><strong>热力学控制</strong></td></tr>
</table></div>

<div class="tip"><strong>解释</strong>：<br>
&bull; 1,2-产物：活化能低，生成速度快（动力学有利）<br>
&bull; 1,4-产物：内部双键更稳定，产物能量更低（热力学有利）<br>
&bull; 高温提供足够能量越过两个活化能垒，平衡倾向更稳定产物</div>
</div>

<h3 id="kp7">6.7 Diels-Alder 反应</h3>
<div class="card">
<div class="fb"><div class="t">Diels-Alder 反应（[4+2]环加成）</div>
<p><strong>二烯体</strong>（4π，需 s-cis 构象）+ <strong>亲二烯体</strong>（2π，含吸电子基更活泼）→ 六元环</p>
<p>特点：协同反应，一步完成，无中间体</p></div>

<div class="fb"><div class="t">立体化学规则</div>
<p><strong>cis 规则（顺式原则）</strong>：二烯体和亲二烯体上取代基的顺反关系在产物中<strong>保持不变</strong>（suprafacial）</p>
<p><strong>endo 规则</strong>：亲二烯体的吸电子基团倾向于朝向二烯体（endo 产物为动力学主要产物）</p></div>

<div class="warn"><strong>二烯体必须能采取 s-cis 构象！</strong><br>
&bull; s-cis 可以反应 ✓<br>
&bull; s-trans 不能反应（两端 p 轨道距离太远）✗<br>
&bull; 锁定 s-cis 的环状二烯（如环戊二烯）反应性极强</div>
</div>

<!-- ========== 习题 ========== -->
<h2 id="exercises">课后习题详解</h2>

<div class="ex"><strong>第1题</strong>：端炔与内炔的鉴别。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>用 $\text{AgNO}_3/\text{NH}_3$ 溶液：端炔生成白色 $\text{RC≡CAg}$ 沉淀；内炔无反应。<br>
或用 $\text{CuCl}/\text{NH}_3$ 溶液：端炔生成红棕色沉淀。</p>
</div></details></div>

<div class="ex"><strong>第2题</strong>：写出下列反应的产物。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>(1) 1-丁炔 + $\text{H}_2$/Lindlar → <strong>(Z)-1-丁烯</strong>（顺式）<br>
(2) 2-丁炔 + Na/NH$_3$(l) → <strong>(E)-2-丁烯</strong>（反式）<br>
(3) 1-丁炔 + 2 HBr → <strong>2,2-二溴丁烷</strong>（马氏，偕二卤）<br>
(4) 1-丁炔 + 1 HBr → <strong>2-溴-1-丁烯</strong>（马氏，一次加成）</p>
</div></details></div>

<div class="ex"><strong>第3题</strong>：炔烃水合产物。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>(1) 1-丁炔 + $\text{H}_2\text{O}$（$\text{HgSO}_4/\text{H}_2\text{SO}_4$）→ <strong>2-丁酮</strong>（马氏，酮）<br>
(2) 乙炔 + $\text{H}_2\text{O}$（$\text{HgSO}_4/\text{H}_2\text{SO}_4$）→ <strong>乙醛</strong>（唯一生成醛的情况）<br>
(3) 1-丁炔 + $(\text{Sia})_2\text{BH}$，然后 $\text{H}_2\text{O}_2/\text{NaOH}$ → <strong>丁醛</strong>（反马氏，醛）</p>
</div></details></div>

<div class="ex"><strong>第4题</strong>：用炔钠增长碳链完成合成。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>从乙炔合成 1-丁炔：<br>
$\text{HC≡CH} \xrightarrow{\text{NaNH}_2} \text{HC≡CNa} \xrightarrow{\text{CH}_3\text{CH}_2\text{Br}} \text{HC≡CCH}_2\text{CH}_3$（1-丁炔）</p>
<p>从 1-丁炔合成 5-癸炔：<br>
$\text{CH}_3\text{CH}_2\text{C≡CH} \xrightarrow{\text{NaNH}_2} \text{CH}_3\text{CH}_2\text{C≡CNa} \xrightarrow{n\text{-C}_4\text{H}_9\text{Br}} \text{CH}_3\text{CH}_2\text{C≡C(CH}_2\text{)}_3\text{CH}_3$</p>
</div></details></div>

<div class="ex"><strong>第5题</strong>：比较酸性大小。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>$\text{HC≡CH}$ ($pK_a$ 25) > $\text{H}_2\text{C=CH}_2$ ($pK_a$ 44) > $\text{CH}_3\text{CH}_3$ ($pK_a$ 50)<br>
酸性：sp C-H > sp$^2$ C-H > sp$^3$ C-H（s 成分越大，电子越靠近核，共轭碱越稳定）</p>
</div></details></div>

<div class="ex"><strong>第6题</strong>：1,3-丁二烯 + HBr 在不同温度下的产物。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>−80°C（动力学控制）：主要 <strong>3-溴-1-丁烯</strong>（1,2-加成产物）<br>
40°C（热力学控制）：主要 <strong>1-溴-2-丁烯</strong>（1,4-加成产物，内部双键更稳定）</p>
</div></details></div>

<div class="ex"><strong>第7题</strong>：Diels-Alder 反应产物。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>(1) 1,3-丁二烯 + 丙烯醛 → 环己烯-4-甲醛（endo 主产物，CHO 朝向二烯）<br>
(2) 环戊二烯 + 马来酸酐 → 降冰片烯二酸酐（endo 产物）<br>
(3) 1,3-丁二烯 + 乙烯 → 环己烯</p>
</div></details></div>

<div class="ex"><strong>第8题</strong>：判断哪些二烯可以发生 Diels-Alder 反应。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>(1) 1,3-丁二烯 → <strong>可以</strong>（能旋转成 s-cis）<br>
(2) (E,E)-2,4-己二烯 → <strong>可以</strong>（能旋转成 s-cis）<br>
(3) (2E,4E)-二甲基丁二烯 → <strong>可以</strong><br>
(4) 1,3-环己二烯 → <strong>不能</strong>（锁定在 s-trans 构象）<br>
(5) 1,3-环戊二烯 → <strong>可以且反应性极强</strong>（锁定在 s-cis 构象）</p>
</div></details></div>

<div class="ex"><strong>第9题</strong>：用化学方法区分 1-丁炔、2-丁炔和 1-丁烯。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>Step 1: $\text{AgNO}_3/\text{NH}_3$ → 1-丁炔产生白色沉淀（端炔），其余无反应<br>
Step 2: $\text{Br}_2/\text{CCl}_4$ → 2-丁炔和 1-丁烯都褪色，但可用 $\text{KMnO}_4$ 氧化后产物区分<br>
或：2-丁炔 + 2 $\text{Br}_2$（需两倍量）；1-丁烯 + 1 $\text{Br}_2$（消耗量不同）</p>
</div></details></div>

<div class="ex"><strong>第10题</strong>：从乙炔出发合成顺式-2-丁烯和反式-2-丁烯。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p><strong>顺式</strong>：$\text{HC≡CH} \xrightarrow{\text{NaNH}_2} \text{HC≡CNa} \xrightarrow{\text{CH}_3\text{Br}} \text{CH}_3\text{C≡CH} \xrightarrow{\text{NaNH}_2} \text{CH}_3\text{C≡CNa} \xrightarrow{\text{CH}_3\text{Br}} \text{CH}_3\text{C≡CCH}_3 \xrightarrow{\text{H}_2/\text{Lindlar}}$ <strong>(Z)-2-丁烯</strong></p>
<p><strong>反式</strong>：同上得 2-丁炔 $\xrightarrow{\text{Na/NH}_3\text{(l)}}$ <strong>(E)-2-丁烯</strong></p>
</div></details></div>

<div class="ex"><strong>第11题</strong>：Diels-Alder 反应的 cis 规则应用。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>顺式亲二烯体（如顺丁烯二酸酐）→ 产物中两个 $\text{COOH}$ 保持 cis 关系<br>
反式亲二烯体（如反丁烯二酸）→ 产物中两个 $\text{COOH}$ 保持 trans 关系<br>
立体化学完全保留（suprafacial 协同过程）</p>
</div></details></div>

<div class="ex"><strong>第12题</strong>：写出以下反应完整机理。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>1-丙炔 + HBr（1 mol，马氏加成）：<br>
$\text{H}^+$ 加到端碳 C1 → C2 形成乙烯型碳正离子（更稳定，与 $\text{CH}_3$ 超共轭）→ $\text{Br}^-$ 加到 C2 → <strong>2-溴丙烯</strong></p>
</div></details></div>

<div class="ex"><strong>第13题</strong>：解释动力学控制与热力学控制的区别。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p><strong>动力学控制</strong>：低温/短时间，产物由活化能决定，生成速度快的产物为主（1,2-加成，活化能低）<br>
<strong>热力学控制</strong>：高温/长时间，达到平衡，能量更低的产物为主（1,4-加成，内部双键稳定）<br>
二者关系：动力学产物不一定是热力学产物</p>
</div></details></div>

<div class="ex"><strong>第14题</strong>：从乙炔合成乙醛和丙酮。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p><strong>乙醛</strong>：$\text{HC≡CH} \xrightarrow{\text{HgSO}_4/\text{H}_2\text{SO}_4/\text{H}_2\text{O}}$ <strong>$\text{CH}_3\text{CHO}$</strong><br>
<strong>丙酮</strong>：$\text{HC≡CH} \xrightarrow{\text{NaNH}_2} \text{HC≡CNa} \xrightarrow{\text{CH}_3\text{Br}} \text{CH}_3\text{C≡CH} \xrightarrow{\text{HgSO}_4/\text{H}_2\text{SO}_4/\text{H}_2\text{O}}$ <strong>$\text{CH}_3\text{COCH}_3$</strong></p>
</div></details></div>

<div class="ex"><strong>第15题</strong>：Diels-Alder 逆合成分析。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>给定环己烯衍生物，找到 σ 键断裂位置（新形成的两个 C-C 单键），拆分为二烯体和亲二烯体。<br>
规则：含吸电子基的双键部分为亲二烯体，含两个双键的部分为二烯体。</p>
</div></details></div>

<div class="ex"><strong>第16题</strong>：炔烃的选择性还原用于合成。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>合成 (Z)-3-己烯：<br>
$\text{HC≡CH} \xrightarrow{\text{NaNH}_2} \text{NaC≡CH} \xrightarrow{n\text{-PrBr}} \text{CH}_3\text{CH}_2\text{CH}_2\text{C≡CH} \xrightarrow{\text{NaNH}_2} \text{C}_3\text{H}_7\text{C≡CNa} \xrightarrow{\text{?}}$<br>
更简洁：3-己炔 $\xrightarrow{\text{H}_2/\text{Lindlar}}$ <strong>(Z)-3-己烯</strong></p>
</div></details></div>

<div class="ex"><strong>挑战题1</strong>：为什么 Lindlar 催化剂给顺式而 Na/NH$_3$ 给反式？
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p><strong>Lindlar</strong>：异相催化，炔烃平躺在 Pd 表面，两个 H 从同一面加入 → syn addition → cis<br>
<strong>Na/NH$_3$</strong>：自由基阴离子机理，反式乙烯基阴离子更稳定（取代基远离减少排斥）→ 质子化后得 trans</p>
</div></details></div>

<div class="ex"><strong>挑战题2</strong>：设计从乙炔到 2-己酮的合成路线。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>$\text{HC≡CH} \xrightarrow{\text{NaNH}_2} \text{HC≡CNa} \xrightarrow{n\text{-BuBr}} \text{CH}_3\text{(CH}_2\text{)}_3\text{C≡CH} \xrightarrow{\text{HgSO}_4/\text{H}_2\text{SO}_4/\text{H}_2\text{O}}$ <strong>2-己酮</strong>（马氏水合→酮）</p>
</div></details></div>

<div class="ex"><strong>挑战题3</strong>：endo 规则的例外讨论。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>endo 规则是<strong>动力学</strong>控制的结果（二级轨道相互作用）。在高温或可逆条件下，可能得到 exo（热力学）产物。<br>
例：环戊二烯 + 马来酸酐在室温 → endo 主产物；在高温长时间 → exo 增多。</p>
</div></details></div>

<div class="ex"><strong>挑战题4</strong>：综合合成——从乙炔和溴甲烷出发合成 (E)-2-戊烯。
<details><summary>查看解答</summary><div class="sol"><div class="st">解</div>
<p>$\text{HC≡CH} \xrightarrow{\text{NaNH}_2} \text{HC≡CNa} \xrightarrow{\text{CH}_3\text{Br}} \text{CH}_3\text{C≡CH}$<br>
$\xrightarrow{\text{NaNH}_2} \text{CH}_3\text{C≡CNa} \xrightarrow{\text{C}_2\text{H}_5\text{Br}} \text{CH}_3\text{C≡CCH}_2\text{CH}_3$（2-戊炔）<br>
$\xrightarrow{\text{Na/NH}_3\text{(l)}}$ <strong>(E)-2-戊烯</strong></p>
</div></details></div>

<h2 id="sum">考点总结</h2>
<div class="card">
<table>
<tr><th>考点</th><th>题型</th><th>重要度</th></tr>
<tr><td>Lindlar vs Na/NH$_3$ 选择性加氢</td><td>完成反应/合成</td><td>⭐⭐⭐</td></tr>
<tr><td>炔烃水合（汞盐→酮 vs 硼氢化→醛）</td><td>完成反应/对比</td><td>⭐⭐⭐</td></tr>
<tr><td>炔钠的烷基化（增长碳链）</td><td>合成设计</td><td>⭐⭐⭐</td></tr>
<tr><td>Diels-Alder 反应（cis 规则/endo 规则）</td><td>产物/立体化学</td><td>⭐⭐⭐</td></tr>
<tr><td>1,2- vs 1,4-加成（动力学 vs 热力学）</td><td>选择/解释</td><td>⭐⭐⭐</td></tr>
<tr><td>端炔酸性与鉴别（银/铜盐）</td><td>鉴别/酸性比较</td><td>⭐⭐</td></tr>
<tr><td>端炔 $pK_a$≈25（sp 杂化）</td><td>酸性排序</td><td>⭐⭐</td></tr>
<tr><td>s-cis 构象与 DA 反应活性</td><td>判断/解释</td><td>⭐⭐</td></tr>
</table>
</div>
'''

write_page('ch6.html', '第6章 炔烃和二烯烃', '<a href="ch5.html">&larr; 第5章</a> <a href="ch7.html">第7章 &rarr;</a>', BODY)
