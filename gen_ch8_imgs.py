#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Generate images for ch8 and supplementary images. No Unicode sub/superscripts."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.font_manager as fm
import numpy as np
import os

# Chinese font setup
for fname in ['Microsoft YaHei', 'SimHei', 'Noto Sans SC', 'SimSun']:
    if any(f.name == fname for f in fm.fontManager.ttflist):
        matplotlib.rcParams['font.family'] = fname
        break
matplotlib.rcParams['axes.unicode_minus'] = False

IMG_DIR = os.path.join(os.path.dirname(__file__), 'img')
os.makedirs(IMG_DIR, exist_ok=True)

def save(fig, name):
    fig.savefig(os.path.join(IMG_DIR, name), dpi=180, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close(fig)
    print(f"  saved {name}")

# ============================================================
# 1. ch8: Alcohol oxidation comparison
# ============================================================
def ch8_alcohol_oxidation():
    fig, ax = plt.subplots(figsize=(9, 4.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5)
    ax.axis('off')
    ax.set_title('醇的氧化反应对比', fontsize=16, fontweight='bold', pad=12)

    data = [
        ('伯醇 (1\u00b0)', 'RCH2OH', 'RCHO (醛)', 'RCOOH (酸)',
         'PCC/PDC\n(停在醛)', 'KMnO4/K2Cr2O7\n(继续氧化)', '#2ecc71'),
        ('仲醇 (2\u00b0)', 'R2CHOH', 'R2C=O (酮)', '(不继续)',
         'KMnO4\nK2Cr2O7\nPCC', '', '#3498db'),
        ('叔醇 (3\u00b0)', 'R3COH', '不易氧化', '',
         '无\u03b2-H\n无法消除', '', '#e74c3c'),
    ]

    for i, (label, start, mid, end, cond1, cond2, color) in enumerate(data):
        y = 3.8 - i * 1.4
        ax.add_patch(mpatches.FancyBboxPatch((0.2, y-0.35), 1.6, 0.7,
            boxstyle='round,pad=0.1', facecolor=color, alpha=0.15, edgecolor=color, lw=2))
        ax.text(1.0, y, label, ha='center', va='center', fontsize=11, fontweight='bold', color=color)

        ax.text(2.3, y, start, ha='left', va='center', fontsize=10)
        ax.annotate('', xy=(4.2, y), xytext=(3.5, y),
                    arrowprops=dict(arrowstyle='->', color=color, lw=2))
        ax.text(3.85, y+0.25, cond1, ha='center', va='bottom', fontsize=7, color='#555')
        ax.text(4.5, y, mid, ha='left', va='center', fontsize=10, fontweight='bold')

        if end:
            ax.annotate('', xy=(7.5, y), xytext=(6.5, y),
                        arrowprops=dict(arrowstyle='->', color=color, lw=2))
            if cond2:
                ax.text(7.0, y+0.25, cond2, ha='center', va='bottom', fontsize=7, color='#555')
            ax.text(7.8, y, end, ha='left', va='center', fontsize=10)

    ax.text(5.0, 0.3, 'PCC = 氯铬酸吡啶鎓 (可将伯醇氧化停留在醛阶段)',
            fontsize=8, ha='center', style='italic', color='#777')
    save(fig, 'ch8_alcohol_oxidation.png')

# ============================================================
# 2. ch8: Lucas test
# ============================================================
def ch8_lucas_test():
    fig, ax = plt.subplots(figsize=(8, 3.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4)
    ax.axis('off')
    ax.set_title('Lucas试剂鉴别1\u00b0/2\u00b0/3\u00b0醇', fontsize=15, fontweight='bold', pad=10)

    cols = ['醇的类型', '反应速度', '现象', '原因']
    col_x = [1.0, 3.5, 5.8, 8.2]

    for j, (c, x) in enumerate(zip(cols, col_x)):
        ax.add_patch(mpatches.FancyBboxPatch((x-0.9, 3.1), 1.8, 0.5,
            boxstyle='round,pad=0.05', facecolor='#0d6b3d', edgecolor='#0d6b3d'))
        ax.text(x, 3.35, c, ha='center', va='center', fontsize=10, color='white', fontweight='bold')

    rows = [
        ('叔醇 (3\u00b0)', '立即浑浊', 'RCl沉淀析出', 'SN1快速\n(稳定碳正离子)', '#e74c3c'),
        ('仲醇 (2\u00b0)', '5~10分钟', '逐渐浑浊', 'SN1中速', '#f39c12'),
        ('伯醇 (1\u00b0)', '不反应', '保持透明', 'SN1太慢', '#27ae60'),
    ]
    for i, (typ, speed, obs, reason, color) in enumerate(rows):
        y = 2.5 - i * 0.8
        bg = '#fff5f5' if i == 0 else ('#fffbf0' if i == 1 else '#f0fff0')
        ax.add_patch(mpatches.Rectangle((0.1, y-0.3), 9.8, 0.6, facecolor=bg, edgecolor='#ddd'))
        ax.text(col_x[0], y, typ, ha='center', va='center', fontsize=10, color=color, fontweight='bold')
        ax.text(col_x[1], y, speed, ha='center', va='center', fontsize=10)
        ax.text(col_x[2], y, obs, ha='center', va='center', fontsize=10)
        ax.text(col_x[3], y, reason, ha='center', va='center', fontsize=8, color='#555')

    ax.text(5, 0.3, 'Lucas试剂 = 无水ZnCl2 + 浓HCl\n仅适用于6碳以下的醇（需溶于试剂）',
            ha='center', va='center', fontsize=8, color='#888')
    save(fig, 'ch8_lucas_test.png')

# ============================================================
# 3. ch8: Epoxide opening selectivity
# ============================================================
def ch8_epoxide_opening():
    fig, ax = plt.subplots(figsize=(9, 4))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5)
    ax.axis('off')
    ax.set_title('环氧化合物开环的区域选择性', fontsize=15, fontweight='bold', pad=10)

    # Acid catalyzed
    ax.add_patch(mpatches.FancyBboxPatch((0.3, 2.8), 4.2, 1.8,
        boxstyle='round,pad=0.15', facecolor='#fff3e0', edgecolor='#e67e22', lw=2))
    ax.text(2.4, 4.2, '酸催化开环', fontsize=12, fontweight='bold', ha='center', color='#e67e22')
    ax.text(2.4, 3.7, 'H2O / ROH / HX (H+催化)', fontsize=9, ha='center')
    ax.text(2.4, 3.2, 'Nu 进攻取代较多的碳\n(类Markovnikov / SN1性质)',
            fontsize=9, ha='center', color='#c0392b')

    # Base catalyzed
    ax.add_patch(mpatches.FancyBboxPatch((5.3, 2.8), 4.4, 1.8,
        boxstyle='round,pad=0.15', facecolor='#e8f5e9', edgecolor='#27ae60', lw=2))
    ax.text(7.5, 4.2, '碱催化/亲核开环', fontsize=12, fontweight='bold', ha='center', color='#27ae60')
    ax.text(7.5, 3.7, 'RO- / RMgX / LiAlH4', fontsize=9, ha='center')
    ax.text(7.5, 3.2, 'Nu 进攻位阻小的碳\n(反Markovnikov / SN2性质)',
            fontsize=9, ha='center', color='#0d6b3d')

    # Common features
    ax.add_patch(mpatches.FancyBboxPatch((1.5, 0.5), 7, 1.8,
        boxstyle='round,pad=0.15', facecolor='#f3e5f5', edgecolor='#8e24aa', lw=1.5))
    ax.text(5, 2.0, '共同点', fontsize=11, fontweight='bold', ha='center', color='#8e24aa')
    ax.text(5, 1.5, '1. 都是反式(anti)开环 - 亲核试剂从环氧的背面进攻', fontsize=9, ha='center')
    ax.text(5, 1.05, '2. 产物为邻二醇衍生物 (1,2-位置)', fontsize=9, ha='center')
    ax.text(5, 0.65, '3. Grignard试剂 + 环氧乙烷 -> RCH2CH2OH (增长2碳的伯醇)', fontsize=9, ha='center')

    save(fig, 'ch8_epoxide_opening.png')

# ============================================================
# 4. ch8: Phenol preparation methods
# ============================================================
def ch8_phenol_prep():
    fig, ax = plt.subplots(figsize=(8, 4.5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 5.5)
    ax.axis('off')
    ax.set_title('酚的制备方法汇总', fontsize=15, fontweight='bold', pad=10)

    methods = [
        ('1. 异丙苯法(工业)', 'C6H5CH(CH3)2 -> C6H5OH + (CH3)2CO',
         'O2/H2SO4', '#e74c3c'),
        ('2. 磺酸碱熔法', 'ArSO3Na -> ArONa -> ArOH',
         'NaOH熔融/300\u00b0C', '#3498db'),
        ('3. 重氮盐水解', 'ArNH2 -> ArN2(+) -> ArOH',
         'NaNO2/HCl -> H2O/\u0394', '#27ae60'),
        ('4. 卤代芳烃水解', 'ArCl + NaOH -> ArOH',
         '高温高压(Dow法)', '#8e24aa'),
    ]

    for i, (name, eq, cond, color) in enumerate(methods):
        y = 4.5 - i * 1.1
        ax.add_patch(mpatches.FancyBboxPatch((0.3, y-0.4), 9.4, 0.8,
            boxstyle='round,pad=0.1', facecolor=color, alpha=0.08, edgecolor=color, lw=1.5))
        ax.text(0.5, y, name, fontsize=10, fontweight='bold', va='center', color=color)
        ax.text(5.0, y+0.1, eq, fontsize=10, va='center', ha='center')
        ax.text(5.0, y-0.2, f'({cond})', fontsize=8, va='center', ha='center', color='#777')

    ax.text(5, 0.3, '工业首选异丙苯法（同时获得苯酚和丙酮）',
            fontsize=9, ha='center', color='#c0392b', fontweight='bold')
    save(fig, 'ch8_phenol_prep.png')

# ============================================================
# 5. ch1: Inductive vs conjugation effects
# ============================================================
def ch1_inductive_vs_conjugation():
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.axis('off')
    ax.set_title('感应效应 vs 共轭效应 对比', fontsize=15, fontweight='bold', pad=10)

    headers = ['比较项', '感应效应 (I)', '共轭效应 (C)']
    hx = [1.5, 4.5, 7.8]
    for j, (h, x) in enumerate(zip(headers, hx)):
        ax.add_patch(mpatches.FancyBboxPatch((x-1.3, 5.2), 2.6, 0.5,
            boxstyle='round,pad=0.05', facecolor='#0d6b3d', edgecolor='#0d6b3d'))
        ax.text(x, 5.45, h, ha='center', va='center', fontsize=10, color='white', fontweight='bold')

    rows = [
        ('传递路径', '\u03c3键传递', '\u03c0键/p轨道共轭'),
        ('传递距离', '短程(3键内显著)', '长程(整个共轭链)'),
        ('衰减', '随距离迅速衰减', '不随距离衰减'),
        ('方向', '固定(沿\u03c3键)', '交替传递'),
        ('本质', '静电诱导', '电子离域'),
        ('判断依据', '电负性/原子大小', '孤电子对/\u03c0键是否共轭'),
    ]

    for i, (item, ind, conj) in enumerate(rows):
        y = 4.8 - i * 0.7
        bg = '#f9f9f9' if i % 2 == 0 else '#ffffff'
        ax.add_patch(mpatches.Rectangle((0.2, y-0.28), 9.6, 0.56, facecolor=bg, edgecolor='#ddd'))
        ax.text(hx[0], y, item, ha='center', va='center', fontsize=9, fontweight='bold')
        ax.text(hx[1], y, ind, ha='center', va='center', fontsize=9, color='#e67e22')
        ax.text(hx[2], y, conj, ha='center', va='center', fontsize=9, color='#2980b9')

    ax.text(5, 0.7, '两者可同时存在，相互协同或对抗\n如：-Cl在苯环上: -I(吸电子) + +C(给电子p-\u03c0共轭)\n净效果：邻对位定位但使环钝化',
            ha='center', va='center', fontsize=8.5, color='#555',
            bbox=dict(boxstyle='round', facecolor='#fffbf0', edgecolor='#f39c12', alpha=0.5))
    save(fig, 'ch1_inductive_vs_conjugation.png')

# ============================================================
# 6. ch9: SN1/SN2/E1/E2 decision flowchart
# ============================================================
def ch9_reaction_flowchart():
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_xlim(0, 12); ax.set_ylim(0, 7)
    ax.axis('off')
    ax.set_title('SN1/SN2/E1/E2 快速判断流程', fontsize=15, fontweight='bold', pad=10)

    # Start
    ax.add_patch(mpatches.FancyBboxPatch((4, 6), 4, 0.7,
        boxstyle='round,pad=0.1', facecolor='#2c3e50', edgecolor='#2c3e50'))
    ax.text(6, 6.35, '卤代烃 R-X + Nu-/B-', ha='center', va='center', fontsize=11, color='white', fontweight='bold')

    # Step 1
    ax.annotate('', xy=(6, 5.5), xytext=(6, 6), arrowprops=dict(arrowstyle='->', lw=2, color='#333'))
    ax.add_patch(mpatches.FancyBboxPatch((3.5, 5), 5, 0.5,
        boxstyle='round,pad=0.1', facecolor='#3498db', alpha=0.2, edgecolor='#3498db', lw=2))
    ax.text(6, 5.25, '第一步：看底物碳级', ha='center', va='center', fontsize=11, fontweight='bold', color='#2980b9')

    # Left: 1°
    ax.annotate('', xy=(2, 4.2), xytext=(4.5, 5), arrowprops=dict(arrowstyle='->', lw=1.5, color='#27ae60'))
    ax.text(3.2, 4.7, '1\u00b0/CH3X', fontsize=9, color='#27ae60', fontweight='bold')
    ax.add_patch(mpatches.FancyBboxPatch((0.5, 3.5), 3, 0.7,
        boxstyle='round,pad=0.1', facecolor='#27ae60', alpha=0.12, edgecolor='#27ae60'))
    ax.text(2, 3.85, 'SN2为主', ha='center', va='center', fontsize=10, fontweight='bold', color='#27ae60')
    ax.text(2, 3.1, '强碱/高温 -> E2\n弱碱/低温 -> SN2', ha='center', fontsize=8, color='#555')

    # Middle: 2°
    ax.annotate('', xy=(6, 4.2), xytext=(6, 5), arrowprops=dict(arrowstyle='->', lw=1.5, color='#f39c12'))
    ax.text(6.3, 4.7, '2\u00b0', fontsize=9, color='#f39c12', fontweight='bold')
    ax.add_patch(mpatches.FancyBboxPatch((4.2, 3.5), 3.6, 0.7,
        boxstyle='round,pad=0.1', facecolor='#f39c12', alpha=0.12, edgecolor='#f39c12'))
    ax.text(6, 3.85, '最复杂 - 看试剂+溶剂', ha='center', va='center', fontsize=10, fontweight='bold', color='#e67e22')
    ax.text(6, 2.8, '强碱(t-BuO-) -> E2\n强亲核弱碱(I-) -> SN2\n弱碱+极性质子 -> SN1/E1',
            ha='center', fontsize=8, color='#555')

    # Right: 3°
    ax.annotate('', xy=(10, 4.2), xytext=(7.5, 5), arrowprops=dict(arrowstyle='->', lw=1.5, color='#e74c3c'))
    ax.text(9, 4.7, '3\u00b0', fontsize=9, color='#e74c3c', fontweight='bold')
    ax.add_patch(mpatches.FancyBboxPatch((8.5, 3.5), 3, 0.7,
        boxstyle='round,pad=0.1', facecolor='#e74c3c', alpha=0.12, edgecolor='#e74c3c'))
    ax.text(10, 3.85, '不发生SN2!', ha='center', va='center', fontsize=10, fontweight='bold', color='#e74c3c')
    ax.text(10, 3.0, '强碱 -> E2\n弱碱/无碱 -> SN1+E1\n高温偏E1', ha='center', fontsize=8, color='#555')

    # Bottom summary
    ax.add_patch(mpatches.FancyBboxPatch((1, 0.5), 10, 1.5,
        boxstyle='round,pad=0.15', facecolor='#f3e5f5', edgecolor='#8e24aa', lw=1.5))
    ax.text(6, 1.6, '关键口诀', fontsize=11, fontweight='bold', ha='center', color='#8e24aa')
    ax.text(6, 1.15, 'SN2: 伯碳+强亲核+非质子溶剂 | E2: 强碱+高温+\u03b2-H反式共平面', fontsize=8.5, ha='center')
    ax.text(6, 0.75, 'SN1: 叔碳+弱亲核+质子溶剂 | E1: 叔碳+弱碱+高温(伴随SN1)', fontsize=8.5, ha='center')

    save(fig, 'ch9_reaction_flowchart.png')

# ============================================================
# 7. ch4: Configuration representation conversion
# ============================================================
def ch4_config_conversion():
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set_xlim(0, 10); ax.set_ylim(0, 6)
    ax.axis('off')
    ax.set_title('四种构型表示法互转关系', fontsize=15, fontweight='bold', pad=10)

    nodes = [
        ('Fischer\n投影式', 2, 4.5, '#e74c3c'),
        ('楔线式\n(透视式)', 8, 4.5, '#3498db'),
        ('Newman\n投影式', 2, 1.5, '#27ae60'),
        ('锯架式', 8, 1.5, '#8e24aa'),
    ]

    for name, x, y, color in nodes:
        ax.add_patch(mpatches.Circle((x, y), 0.9, facecolor=color, alpha=0.15, edgecolor=color, lw=2.5))
        ax.text(x, y, name, ha='center', va='center', fontsize=10, fontweight='bold', color=color)

    drawn = set()
    pairs = [
        (2, 4.5, 8, 4.5), (2, 4.5, 2, 1.5),
        (8, 4.5, 8, 1.5), (2, 1.5, 8, 1.5),
    ]
    for x1, y1, x2, y2 in pairs:
        dx, dy = x2-x1, y2-y1
        length = (dx**2+dy**2)**0.5
        ux, uy = dx/length, dy/length
        ax.annotate('', xy=(x2-ux*0.95, y2-uy*0.95), xytext=(x1+ux*0.95, y1+uy*0.95),
                    arrowprops=dict(arrowstyle='<->', lw=1.5, color='#555'))

    ax.text(5, 4.8, '横前竖后 / 确定前后', ha='center', fontsize=8, color='#777')
    ax.text(5, 1.2, '展开/折叠', ha='center', fontsize=8, color='#777')
    ax.text(0.8, 3, '重叠式构象', ha='center', fontsize=8, color='#777', rotation=90)
    ax.text(9.2, 3, '旋转展平', ha='center', fontsize=8, color='#777', rotation=90)

    ax.text(5, 3, '验证：在两种表示法中\n分别标R/S，必须一致！',
            ha='center', va='center', fontsize=9, color='#c0392b', fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='#fff3e0', edgecolor='#e67e22', alpha=0.7))

    save(fig, 'ch4_config_conversion.png')

# ============================================================
if __name__ == '__main__':
    print("Generating ch8 and supplementary images...")
    ch8_alcohol_oxidation()
    ch8_lucas_test()
    ch8_epoxide_opening()
    ch8_phenol_prep()
    ch1_inductive_vs_conjugation()
    ch9_reaction_flowchart()
    ch4_config_conversion()
    print("Done! All images generated.")
