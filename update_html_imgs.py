#!/usr/bin/env python3
"""Insert new images into all chapter HTML files at appropriate locations."""
import re

def img_card(src, alt, max_width=660):
    return f'\n<div class="card" style="text-align:center;padding:8px;">\n<img src="img/{src}" alt="{alt}" style="max-width:{max_width}px;width:100%;">\n</div>\n'

def insert_after(html, anchor, insertion):
    """Insert insertion string right after anchor."""
    idx = html.find(anchor)
    if idx == -1:
        print(f'  [WARN] anchor not found: {anchor[:60]}')
        return html
    pos = idx + len(anchor)
    return html[:pos] + insertion + html[pos:]

# ──────────────────────────────────────────────
# ch2.html
# ──────────────────────────────────────────────
print('Updating ch2.html...')
with open('ch2.html', encoding='utf-8') as f:
    html = f.read()

# After DBE section (2.3)
html = insert_after(html,
    'DBE值的规律：每个环或双键DBE=1，每个三键DBE=2，苯DBE=4。已知DBE还需结合分子式推结构。</p></div>\n</div>',
    img_card('ch2_dbe_guide.png', '不饱和度计算与应用', 640))

# After resonance rules (2.2)
html = insert_after(html,
    '判断共振结构贡献大小：完整Lewis结构 > 电荷少 > 负电荷在电负性大原子。',
    img_card('ch2_resonance_rules.png', '共振结构书写七条规则', 700))

# After Z/E section (2.6)
html = insert_after(html,
    'Z/E与顺/反的关系：顺式≡Z不一定成立！CIP优先级决定Z/E，不是简单看"相同基团"。',
    img_card('ch2_ze_vs_cistrans.png', 'Z/E命名 vs 顺/反命名对比', 680))

with open('ch2.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('  ch2.html done')

# ──────────────────────────────────────────────
# ch3.html
# ──────────────────────────────────────────────
print('Updating ch3.html...')
with open('ch3.html', encoding='utf-8') as f:
    html = f.read()

# After Newman ethane image
html = insert_after(html,
    '<img src="img/struct_newman_ethane.png"',
    '\n')  # just ensure spacing; main insert below

# After butane conformations section
html = insert_after(html,
    '稳定性顺序（正丁烷）：<strong>anti(对位交叉) > gauche(邻位交叉) > 部分重叠式 > 全重叠式(完全重叠)</strong>',
    img_card('ch3_butane_energy.png', '正丁烷构象能量变化图', 620))

# After cyclohexane chair section
html = insert_after(html,
    'A值越大，基团倾向于占e键的趋势越强：叔丁基A≈23 kJ/mol，完全偏好e键（锁定椅式）。',
    img_card('ch3_methylcyclohexane_conf.png', '甲基环己烷 e键vs a键构象', 680))

# After ring strain section (3.5)
html = insert_after(html,
    '环丙烷的特殊性：弯曲键（香蕉键），C-C-C角约60°，有开环倾向（类似烯烃）。',
    img_card('ch3_ring_strain.png', '各环烷烃环张力比较', 640))

# After radical halogenation section
html = insert_after(html,
    'Br₂选择性远高于Cl₂（Hammond假说：Br·吸热→晚过渡态→底物差异显著）。',
    img_card('ch3_halogenation.png', '卤代反应选择性与自由基机理', 680))

with open('ch3.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('  ch3.html done')

# ──────────────────────────────────────────────
# ch4.html
# ──────────────────────────────────────────────
print('Updating ch4.html...')
with open('ch4.html', encoding='utf-8') as f:
    html = f.read()

# After R/S section
html = insert_after(html,
    '<img src="img/struct_rs_config.png"',
    img_card('ch4_stereo_relations.png', '对映体vs非对映体vs相同化合物', 700))

# After optical activity section
html = insert_after(html,
    '外消旋体(racemic mixture)：等量对映体混合，[α]=0，物理性质与各对映体相同（除比旋光度外）。',
    img_card('ch4_optical_activity.png', '旋光性、比旋光度与ee%', 660))

with open('ch4.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('  ch4.html done')

# ──────────────────────────────────────────────
# ch5.html
# ──────────────────────────────────────────────
print('Updating ch5.html...')
with open('ch5.html', encoding='utf-8') as f:
    html = f.read()

# After Markovnikov section
html = insert_after(html,
    '<img src="img/struct_carbocation_stability.png"',
    img_card('ch5_markovnikov.png', 'Markovnikov规则与碳正离子稳定性', 700))

# After hydroboration section
html = insert_after(html,
    '硼氢化-氧化是制备反Markovnikov醇的标准方法，实验室常用。',
    img_card('ch5_hydroboration.png', '硼氢化-氧化反应机理', 660))

# After carbocation rearrangement
html = insert_after(html,
    '<img src="img/struct_bromonium.png"',
    img_card('ch5_carbocation_rearrange.png', '碳正离子重排——1,2-迁移', 680))

# After oxidation section
html = insert_after(html,
    '臭氧化/还原：C=C断裂为醛(Zn/H₂O)或羧酸(H₂O₂)，是推断烯烃结构的重要手段。',
    img_card('ch5_oxidation_compare.png', '烯烃氧化反应全比较', 720))

with open('ch5.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('  ch5.html done')

# ──────────────────────────────────────────────
# ch6.html
# ──────────────────────────────────────────────
print('Updating ch6.html...')
with open('ch6.html', encoding='utf-8') as f:
    html = f.read()

# After alkyne reduction section
html = insert_after(html,
    'Na/液NH₃：自由基负离子机理，anti加成，得反式(E)烯烃。',
    img_card('ch6_alkyne_reduction.png', '炔烃还原——Lindlar vs Na/NH₃', 680))

# After Kucherov section
html = insert_after(html,
    '乙炔水合→乙醛（特殊！端炔水合→甲基酮）。',
    img_card('ch6_kucherov.png', '炔烃水合——库切洛夫反应', 660))

# After 1,2 vs 1,4 section
html = insert_after(html,
    '低温动力学控制→1,2-加成；高温热力学控制→1,4-加成。',
    img_card('ch6_kinetic_thermodynamic.png', '1,2-加成 vs 1,4-加成（动力学/热力学）', 680))

# After DA reaction
html = insert_after(html,
    '<img src="img/struct_da_reaction.png"',
    img_card('da_reaction_example.png', 'Diels-Alder反应——endo规则与立体化学', 640))

with open('ch6.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('  ch6.html done')

# ──────────────────────────────────────────────
# ch7.html
# ──────────────────────────────────────────────
print('Updating ch7.html...')
with open('ch7.html', encoding='utf-8') as f:
    html = f.read()

# After Hückel section
html = insert_after(html,
    '反芳香性：平面环形共轭，4n个π电子（如环丁二烯4π），极不稳定。',
    img_card('ch7_huckel_rule.png', 'Hückel规则与芳香性判断', 720))

# After EAS mechanism section
html = insert_after(html,
    '<img src="img/struct_eas_mechanism.png"',
    img_card('ch7_five_eas.png', '苯的五大亲电取代反应', 720))

# After directing effects section
html = insert_after(html,
    '卤素（F,Cl,Br,I）：钝化苯环，但定邻/对位（+C效应 > -I效应，对位置而言）。',
    img_card('ch7_directing_effects.png', '苯环定位效应总结', 740))

# After naphthalene section
html = insert_after(html,
    '萘的磺化：低温→α磺化（动力学）；高温→β磺化（热力学）。',
    img_card('ch7_naphthalene.png', '萘的化学反应——α/β位选择性', 660))

# After side chain section
html = insert_after(html,
    'KMnO₄氧化带α-H的苯环侧链→苯甲酸（无论侧链多长）；无α-H的叔烷基苯不被氧化。',
    img_card('ch7_side_chain.png', '芳烃侧链反应总结', 660))

with open('ch7.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('  ch7.html done')

# ──────────────────────────────────────────────
# ch9.html
# ──────────────────────────────────────────────
print('Updating ch9.html...')
with open('ch9.html', encoding='utf-8') as f:
    html = f.read()

# After SN2 section
html = insert_after(html,
    '<img src="img/struct_sn2_mechanism.png"',
    img_card('ch9_sn1_sn2_compare.png', 'SN1 vs SN2 全面对比', 760))

# After E2 section
html = insert_after(html,
    '<img src="img/struct_e2_mechanism.png"',
    img_card('ch9_four_competition.png', 'SN1/SN2/E1/E2 四大竞争判断', 720))

# After Grignard section
html = insert_after(html,
    'Grignard试剂与环氧乙烷反应：增加两个碳，得伯醇。',
    img_card('ch9_grignard_reactions.png', 'Grignard试剂制备与反应', 700))

with open('ch9.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('  ch9.html done')

print('\nAll HTML files updated!')
