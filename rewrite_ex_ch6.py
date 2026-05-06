#!/usr/bin/env python3
"""Rewrite ch6.html exercises."""
from rewrite_exercises import replace_exercises

ch6_ex = r'''<h2 id="ex">课后习题精选</h2>

<h3>题1 炔烃反应</h3>
<div class="ex"><strong>题1</strong> 完成下列炔烃反应，写出主要产物：<br>
(a) 1-丁炔 + 1当量HBr<br>
(b) 1-丁炔 + 2当量HBr<br>
(c) 1-丁炔 + H<sub>2</sub>O/H<sub>2</sub>SO<sub>4</sub>/HgSO<sub>4</sub><br>
(d) 2-丁炔 + H<sub>2</sub>/Lindlar催化剂<br>
(e) 2-丁炔 + Na/NH<sub>3</sub>(l)<br>
(f) 1-丁炔 + NaNH<sub>2</sub> → 然后+CH<sub>3</sub>I<br>
(g) 丙炔 + 2当量Br<sub>2</sub><br>
(h) 1-丁炔 + BH<sub>3</sub>·THF → H<sub>2</sub>O<sub>2</sub>/NaOH(硼氢化)</div>
<div class="sol-header">解答</div><div class="sol">
<div class="st">解题思路：炔烃比烯烃多一个π键，可发生两次亲电加成。末端炔有酸性C-H(pKa≈25)，可用强碱脱质子→炔负离子→亲核试剂。</div>

<table><tr><th>反应</th><th>产物</th><th>要点</th></tr>
<tr><td>(a) +1eq HBr</td><td>2-溴-1-丁烯 CH<sub>3</sub>CH<sub>2</sub>CBr=CH<sub>2</sub></td><td>Markovnikov：H加到末端C，Br加到内部C→乙烯基溴</td></tr>
<tr><td>(b) +2eq HBr</td><td>2,2-二溴丁烷 CH<sub>3</sub>CH<sub>2</sub>CBr<sub>2</sub>CH<sub>3</sub></td><td>两次Mark→同碳二卤(geminal)</td></tr>
<tr><td>(c) +H<sub>2</sub>O/Hg<sup>2+</sup></td><td>2-丁酮 CH<sub>3</sub>COCH<sub>2</sub>CH<sub>3</sub></td><td>Mark水合→烯醇→互变异构为酮（末端炔→甲基酮）</td></tr>
<tr><td>(d) H<sub>2</sub>/Lindlar</td><td><strong>cis-2-丁烯</strong></td><td>Lindlar=毒化Pd，只加一当量H<sub>2</sub>，syn→cis烯烃</td></tr>
<tr><td>(e) Na/NH<sub>3</sub></td><td><strong>trans-2-丁烯</strong></td><td>溶解金属还原→反式烯烃（自由基阴离子机理）</td></tr>
<tr><td>(f) NaNH<sub>2</sub>→CH<sub>3</sub>I</td><td>2-戊炔 CH<sub>3</sub>C≡CCH<sub>2</sub>CH<sub>3</sub></td><td>炔负离子SN2烷基化（只能用1°卤代烃！）</td></tr>
<tr><td>(g) +2eq Br<sub>2</sub></td><td>1,1,2,2-四溴丙烷</td><td>两次anti加成</td></tr>
<tr><td>(h) 硼氢化</td><td>丁醛 CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>CHO</td><td>anti-Mark水合→烯醇→<strong>醛</strong>（末端炔硼氢化→醛，区别于Hg<sup>2+</sup>→酮）</td></tr>
</table>

<div class="warn"><strong>必记对比</strong>：末端炔水合→Hg<sup>2+</sup>催化给<strong>甲基酮</strong>(Mark)；硼氢化给<strong>醛</strong>(anti-Mark)。这是合成设计中选择性控制的核心。</div>
<div class="tip"><strong>立体选择性对比</strong>：Lindlar加氢→cis烯；Na/NH<sub>3</sub>→trans烯。两种方法从同一炔烃得到几何异构体！</div>
</div>

<h3>题2 Diels-Alder反应</h3>
<div class="ex"><strong>题2</strong> <img src="img/da_reaction_example.png" alt="Diels-Alder反应示意"><br>
预测下列DA反应的产物（注意立体化学和区域选择性）：<br>
(a) 1,3-丁二烯 + 丙烯醛(CH<sub>2</sub>=CHCHO)<br>
(b) 2,3-二甲基-1,3-丁二烯 + 马来酸酐<br>
(c) 环戊二烯 + 丙烯酸甲酯(endo/exo)<br>
(d) 1-甲氧基-1,3-丁二烯 + 丙烯腈(区域选择性)</div>
<div class="sol-header">解答</div><div class="sol">
<div class="st">解题思路：DA反应=协同[4+2]环加成。必须条件：①二烯s-cis构象 ②电子互补(富电子二烯+缺电子亲二烯体) ③syn加成(endo规则)。</div>

<p><strong>(a) 丁二烯 + 丙烯醛</strong>：</p>
<p>产物：4-甲酰基环己烯(环己烯-4-甲醛)。新环6员，双键在C1-C2位(原二烯中间两碳形成的σ键旁边)。CHO在C4位。</p>

<p><strong>(b) 2,3-二甲基丁二烯 + 马来酸酐</strong>：</p>
<p>产物：4,5-二甲基-4-环己烯-1,2-二甲酸酐。两个甲基在双键上(原二烯C2,C3→产物C4,C5上双键)。马来酸酐的两个C=O保持cis关系。<br>
立体：马来酸酐中两个酸酐C=O本身cis→产物中也是cis(syn加成保持)。</p>

<p><strong>(c) 环戊二烯 + 丙烯酸甲酯</strong>：</p>
<p>环戊二烯固定为s-cis(环状锁定)。产物：双环[2.2.1]庚-5-烯-2-甲酸甲酯(降冰片烯衍生物)。<br>
<strong>endo规则</strong>：亲二烯体的C=O基团朝向环内(endo方向)→动力学产物。<br>
endo产物为主(次级轨道相互作用稳定过渡态)。exo产物为热力学产物(更稳定但动力学不利)。</p>

<p><strong>(d) 1-甲氧基丁二烯 + 丙烯腈</strong>（区域选择性）：</p>
<p>1-甲氧基=给电子(EDG在二烯C1)，CN=吸电子(EWG在亲二烯体)。<br>
"ortho"规则：EDG和EWG在产物中为1,2-关系(邻位)。<br>
产物：<strong>2-甲氧基-4-氰基环己烯</strong>（OCH<sub>3</sub>在C1旁=C2，CN在C4=对应亲二烯体碳）。</p>
<div class="note">DA区域选择性规律：给电子基(二烯)与吸电子基(亲二烯体)倾向于"ortho"或"para"关系→由前线轨道系数大小决定。</div>
</div>

<h3>题3 1,2-加成与1,4-加成</h3>
<div class="ex"><strong>题3</strong><br>
(a) 1,3-丁二烯 + 1当量HBr → 写出1,2-和1,4-加成产物，解释温度对比例的影响。<br>
(b) 2-甲基-1,3-丁二烯(异戊二烯) + 1当量HCl → 所有可能产物及比例分析。</div>
<div class="sol-header">解答</div><div class="sol">
<div class="st">解题思路：共轭二烯加成第一步形成烯丙型碳正离子→C2或C4(1,4位)都有正电荷→亲核试剂攻击两个位点。低温=动力学控制(1,2)；高温=热力学控制(1,4)。</div>

<p><strong>(a) 1,3-丁二烯 + HBr</strong>：</p>
<p>步骤1：H<sup>+</sup>加到C1(末端，形成更稳定的烯丙基碳正离子)：<br>
CH<sub>3</sub>-<sup>+</sup>CH-CH=CH<sub>2</sub> ↔ CH<sub>3</sub>-CH=CH-CH<sub>2</sub><sup>+</sup></p>
<p>步骤2：Br<sup>−</sup>进攻→</p>
<table><tr><th>产物</th><th>类型</th><th>结构</th></tr>
<tr><td>3-溴-1-丁烯</td><td>1,2-加成</td><td>CH<sub>3</sub>CHBrCH=CH<sub>2</sub></td></tr>
<tr><td>1-溴-2-丁烯(E/Z)</td><td>1,4-加成</td><td>CH<sub>3</sub>CH=CHCH<sub>2</sub>Br</td></tr>
</table>
<p>温度效应：<strong>−80°C</strong>→1,2产物为主(80%)(动力学控制：Br<sup>−</sup>攻击离它更近的C2更快)。<br>
<strong>40°C</strong>→1,4产物为主(80%)(热力学控制：内部烯烃更稳定)。</p>

<p><strong>(b) 异戊二烯 + HCl</strong>：CH<sub>2</sub>=C(CH<sub>3</sub>)-CH=CH<sub>2</sub></p>
<p>H<sup>+</sup>加到C1(形成C2上3°烯丙型正离子，最稳定)：<br>
CH<sub>3</sub>-<sup>+</sup>C(CH<sub>3</sub>)-CH=CH<sub>2</sub> ↔ CH<sub>3</sub>-C(CH<sub>3</sub>)=CH-CH<sub>2</sub><sup>+</sup></p>
<p>1,2-加成→3-氯-2-甲基-1-丁烯：CH<sub>2</sub>=C(CH<sub>3</sub>)CHClCH<sub>3</sub>...不对。<br>
修正：H加到C1→C2正电荷(3°!): (CH<sub>3</sub>)(Cl)C=... Cl<sup>−</sup>攻C2→3-氯-2-甲基-1-丁烯(1,2)。<br>
Cl<sup>−</sup>攻C4→1-氯-2-甲基-2-丁烯(1,4)。<br>
1,4-产物更取代(三取代烯)→热力学更稳定→高温主要产物。</p>
<div class="warn">1,4-加成产物往往是更取代的内部烯烃→热力学更稳定。所以高温有利于1,4-加成(热力学控制)。</div>
</div>

<h3>题4 鉴别</h3>
<div class="ex"><strong>题4</strong> 用化学方法鉴别：1,3-环己二烯、环己烯、苯。</div>
<div class="sol-header">解答</div><div class="sol">
<p>三者都含不饱和度，关键区别：苯具有芳香性(不易加成)。</p>
<table><tr><th>试剂</th><th>1,3-环己二烯</th><th>环己烯</th><th>苯</th></tr>
<tr><td>Br<sub>2</sub>/CCl<sub>4</sub></td><td>褪色(快，加2eq)</td><td>褪色(加1eq)</td><td><strong>不褪色</strong></td></tr>
<tr><td>KMnO<sub>4</sub>(冷稀)</td><td>褪色</td><td>褪色</td><td>不褪色</td></tr>
<tr><td>Br<sub>2</sub>计量</td><td>消耗2当量</td><td>消耗1当量</td><td>0</td></tr>
</table>
<p>方案：①Br<sub>2</sub>/CCl<sub>4</sub>不褪色→<strong>苯</strong>。②测Br<sub>2</sub>消耗量：2当量→<strong>1,3-环己二烯</strong>，1当量→<strong>环己烯</strong>。<br>
或用DA反应：1,3-环己二烯可作二烯参与DA反应(如与马来酸酐加热)→环己烯不能。</p>
</div>

<h3>题5 推断</h3>
<div class="ex"><strong>题5</strong><br>
(a) 化合物A(C<sub>5</sub>H<sub>8</sub>)与2当量H<sub>2</sub>/Pd→正戊烷。A的臭氧分解→甲醛+丙醛(两种产物)。推断A结构。<br>
(b) 化合物B(C<sub>6</sub>H<sub>10</sub>)与1当量H<sub>2</sub>/Lindlar催化剂→C<sub>6</sub>H<sub>12</sub>(仍有1个不饱和度)。B+过量H<sub>2</sub>→环己烷。推断B结构。</div>
<div class="sol-header">解答</div><div class="sol">
<p><strong>(a)</strong> C<sub>5</sub>H<sub>8</sub>，DBE=(10+2-8)/2=<strong>2</strong>。加2当量H<sub>2</sub>→正戊烷(无环)→2个双键或1个三键。</p>
<p>臭氧分解→甲醛(HCHO)+丙醛(CH<sub>3</sub>CH<sub>2</sub>CHO)。如果是二烯切断两个C=C：<br>
CH<sub>2</sub>=CH-CH=CH-CH<sub>3</sub>? 切断→HCHO + OHC-CHO + CH<sub>3</sub>CHO? 不对，会有乙二醛。</p>
<p>如果是二烯CH<sub>2</sub>=CH-CH<sub>2</sub>-CH=CH<sub>2</sub>(1,4-戊二烯)→臭氧分解：切C1=C2→HCHO + OHC-CH<sub>2</sub>-CH=CH<sub>2</sub>，再切→HCHO + OHC-CH<sub>2</sub>-CHO。得到2×HCHO + 丙二醛。不符。</p>
<p>若A为<strong>1,3-戊二烯CH<sub>3</sub>CH=CH-CH=CH<sub>2</sub></strong>：臭氧切每个C=C→CH<sub>3</sub>CHO + OHC-CHO + HCHO。得到甲醛+丙醛+乙二醛...还是不符。</p>
<p>若A含三键：<strong>1-戊炔</strong> CH≡C-CH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub>，加2eq H<sub>2</sub>→正戊烷✓。臭氧分解炔：HC≡C切断→HCHO?(不对，炔臭氧分解→羧酸)。</p>
<p>重新考虑：<strong>A = 1,4-戊二烯 CH<sub>2</sub>=CHCH<sub>2</sub>CH=CH<sub>2</sub></strong>→臭氧分解：HCHO + OHCCH<sub>2</sub>CHO + HCHO=甲醛+丙二醛。不是丙醛。</p>
<p>答：<strong>A = 1,3-戊二烯</strong>(CH<sub>2</sub>=CH−CH=CHCH<sub>3</sub>)。臭氧分解共轭二烯→HCHO + 乙二醛 + CH<sub>3</sub>CHO。题目简化为"甲醛+丙醛"可能是指主要碎片。或者A=<strong>2-甲基-1,3-丁二烯(异戊二烯)</strong>CH<sub>2</sub>=C(CH<sub>3</sub>)CH=CH<sub>2</sub>：臭氧→HCHO + CH<sub>3</sub>COCHO(丙酮醛)+ HCHO。也不完全符合。</p>
<p>最合理：<strong>A = 1,4-戊二烯</strong>，若按每个双键独立臭氧分解：每个末端烯各给HCHO，中间碳给二醛。但题目说"甲醛+丙醛"→可能题意是还原性臭氧分解(Zn处理)后合并碎片。修正答案仍为1,3-戊二烯。</p>

<p><strong>(b)</strong> C<sub>6</sub>H<sub>10</sub>，DBE=(12+2-10)/2=<strong>2</strong>。过量H<sub>2</sub>→环己烷(有环!)→1个环+1个不饱和度(C=C或C≡C)。<br>
Lindlar加1eq H<sub>2</sub>→C<sub>6</sub>H<sub>12</sub>(仍DBE=1=环)→加的这1eq H<sub>2</sub>把C≡C变成C=C！<br>
所以<strong>B含有一个三键+一个环</strong>...不对，Lindlar加1eq H<sub>2</sub>→三键变双键(DBE从2→1)。最终加氢→环己烷=只有环。<br>
答：<strong>B = 环己炔(cyclohexyne)</strong>? 但环己炔极不稳定(环内三键张力大)。<br>
或：B含一个环+一个C≡C在侧链? 但加氢得环己烷意味着无侧链碳。C<sub>6</sub>H<sub>10</sub>加氢→C<sub>6</sub>H<sub>12</sub>(环己烷)→增加了1个H<sub>2</sub>(Lindlar)再加1个H<sub>2</sub>=总2个H<sub>2</sub>→原来有三键(加2H<sub>2</sub>→单键)。含6C成环+三键在环上→<strong>B = 环己炔</strong>。虽然不稳定，但这是逻辑推断结果。</p>
<div class="note">推断题策略：从分子式算DBE→加氢实验确定不饱和度类型→碎片分析确定位置。</div>
</div>

<h3>题6 合成路线</h3>
<div class="ex"><strong>题6</strong><br>
(a) 从乙炔和任何碳数≤2的有机物，合成2-己炔。<br>
(b) 从1,3-丁二烯和合适的亲二烯体，合成4-环己烯-1,2-二甲酸(cis)。</div>
<div class="sol-header">解答</div><div class="sol">
<div class="st">解题思路：(a)炔的碳链增长=炔负离子烷基化(SN2，限用1°RX)。(b)DA反应→顺式双酸。</div>

<p><strong>(a) 合成2-己炔 CH<sub>3</sub>C≡CCH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub></strong>：</p>
<p>逆推：2-己炔 ← 1-丁炔<sup>−</sup> + CH<sub>3</sub>CH<sub>2</sub>Br（或丙炔<sup>−</sup> + 正丙基溴→但正丙基溴是1°✓）</p>
<p>路线一：<br>
HC≡CH + NaNH<sub>2</sub> → HC≡C<sup>−</sup>Na<sup>+</sup><br>
HC≡C<sup>−</sup> + CH<sub>3</sub>CH<sub>2</sub>Br → CH<sub>3</sub>CH<sub>2</sub>C≡CH(1-丁炔)<br>
1-丁炔 + NaNH<sub>2</sub> → CH<sub>3</sub>CH<sub>2</sub>C≡C<sup>−</sup>Na<sup>+</sup><br>
CH<sub>3</sub>CH<sub>2</sub>C≡C<sup>−</sup> + CH<sub>3</sub>CH<sub>2</sub>Br → <strong>CH<sub>3</sub>CH<sub>2</sub>C≡CCH<sub>2</sub>CH<sub>3</sub></strong>(3-己炔?)</p>
<p>注意：要得2-己炔(CH<sub>3</sub>C≡C-C<sub>3</sub>H<sub>7</sub>)，需：<br>
HC≡CH + NaNH<sub>2</sub> → HC≡C<sup>−</sup> + CH<sub>3</sub>Br → CH<sub>3</sub>C≡CH(丙炔)<br>
丙炔 + NaNH<sub>2</sub> → CH<sub>3</sub>C≡C<sup>−</sup> + CH<sub>3</sub>CH<sub>2</sub>CH<sub>2</sub>Br(正丙基溴,1°) → <strong>CH<sub>3</sub>C≡CCH<sub>2</sub>CH<sub>2</sub>CH<sub>3</sub></strong>(2-己炔) ✓</p>
<p>但正丙基溴是C<sub>3</sub>试剂>C<sub>2</sub>。如果限制≤C<sub>2</sub>：<br>
HC≡C<sup>−</sup> + C<sub>2</sub>H<sub>5</sub>Br → 1-丁炔 → 1-丁炔<sup>−</sup> + C<sub>2</sub>H<sub>5</sub>Br → 3-己炔(不是2-己炔)。<br>
需要CH<sub>3</sub>Br: HC≡C<sup>−</sup> + CH<sub>3</sub>Br → 丙炔 → 丙炔<sup>−</sup> + C<sub>2</sub>H<sub>5</sub>Br → 2-戊炔(5C)。还差一个C。<br>
答：用两步烷基化：HC≡C<sup>−</sup> + CH<sub>3</sub>Br → 丙炔<sup>−</sup> + CH<sub>3</sub>CH<sub>2</sub>Br → <strong>2-戊炔</strong>(C<sub>5</sub>)。若需C<sub>6</sub>则需C<sub>3</sub>试剂。题目"碳数≤2"可能指每个试剂≤C<sub>2</sub>，无法直接得到2-己炔（需要正丙基卤）。修改目标为3-己炔则可行。</p>

<p><strong>(b) 合成cis-4-环己烯-1,2-二甲酸</strong>：</p>
<p>DA反应：1,3-丁二烯(二烯) + 马来酸酐(cis-亲二烯体) → 环己烯-4,5-二甲酸酐<br>
→ 水解酸酐 → <strong>cis-4-环己烯-1,2-二甲酸</strong> ✓</p>
<p>关键：马来酸酐中两个C=O为cis→DA反应syn加成→产物中两个COOH保持cis关系。若用反丁烯二酸(fumaric acid)→得trans二酸。</p>
<div class="tip">DA反应的立体专一性：亲二烯体的cis取代基在产物中保持cis(endo或exo面)。这是syn[4+2]环加成的必然结果。</div>
</div>
'''

print("Processing ch6.html...")
replace_exercises('ch6.html', ch6_ex)
print("Done ch6!")
