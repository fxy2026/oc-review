#!/usr/bin/env python3
"""Generate ch1 orbital hybridization diagrams as PNG (replacing SVGs)."""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

import matplotlib.font_manager as fm
# Use Chinese font
for fname in ['Microsoft YaHei', 'SimHei', 'Noto Sans SC', 'SimSun']:
    if any(f.name == fname for f in fm.fontManager.ttflist):
        matplotlib.rcParams['font.family'] = fname
        break
matplotlib.rcParams['axes.unicode_minus'] = False

IMG = 'img'

def save(fig, name, dpi=180):
    fig.savefig(f'{IMG}/{name}', dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'  {name} OK')

# === CH4: sp3 tetrahedral ===
fig, ax = plt.subplots(figsize=(4, 4))
ax.axis('off')
ax.set_xlim(-2, 2); ax.set_ylim(-2, 2)
ax.set_aspect('equal')
# Central C
ax.plot(0, 0, 'ko', ms=18, zorder=5)
ax.text(0, 0, 'C', ha='center', va='center', fontsize=13, color='white', fontweight='bold', zorder=6)
# 4 H positions (tetrahedral projection)
pos = [(0, 1.5), (1.4, -0.5), (-1.4, -0.5), (0, -0.9)]
labels = ['H', 'H', 'H', 'H']
styles = ['-', '-', '--', '-']
for (x, y), lbl, sty in zip(pos, labels, styles):
    ax.plot([0, x*0.85], [0, y*0.85], 'b'+sty, lw=2.5)
    ax.plot(x, y, 'co', ms=14, zorder=5)
    ax.text(x, y, lbl, ha='center', va='center', fontsize=11, fontweight='bold', zorder=6)
ax.set_title('甲烷 CH₄\nsp³ 杂化, 四面体, 109.5°', fontsize=12, fontweight='bold', pad=4)
ax.text(0, -1.75, '4个等价σ键', ha='center', fontsize=10, color='gray', style='italic')
save(fig, 'ch1_methane.png')

# === CH2=CH2: sp2 planar ===
fig, ax = plt.subplots(figsize=(5, 3.5))
ax.axis('off')
ax.set_xlim(-2.5, 2.5); ax.set_ylim(-1.8, 1.8)
ax.set_aspect('equal')
# Two C atoms
for cx, lbl in [(-0.7, 'C'), (0.7, 'C')]:
    ax.plot(cx, 0, 'ko', ms=18, zorder=5)
    ax.text(cx, 0, lbl, ha='center', va='center', fontsize=12, color='white', fontweight='bold', zorder=6)
# C=C double bond (sigma + pi)
ax.plot([-0.7, 0.7], [0.08, 0.08], 'b-', lw=3, label='σ键')
ax.plot([-0.7, 0.7], [-0.08, -0.08], 'r-', lw=2.5, label='π键')
# H atoms (planar, 120°)
h_pos = [(-1.9, 0.9), (-1.9, -0.9), (1.9, 0.9), (1.9, -0.9)]
for hx, hy in h_pos:
    cx = -0.7 if hx < 0 else 0.7
    ax.plot([cx, hx*0.85], [0, hy*0.85], 'b-', lw=2)
    ax.plot(hx, hy, 'co', ms=13, zorder=5)
    ax.text(hx, hy, 'H', ha='center', va='center', fontsize=10, fontweight='bold', zorder=6)
ax.set_title('乙烯 CH₂=CH₂\nsp² 杂化, 平面形, 120°', fontsize=12, fontweight='bold', pad=4)
ax.text(0, -1.5, '蓝=σ键(sp²)  红=π键(p轨道侧面重叠)', ha='center', fontsize=9, color='gray', style='italic')
legend = ax.legend(handles=[
    mpatches.Patch(color='blue', label='σ键 (sp²-sp²)'),
    mpatches.Patch(color='red',  label='π键 (p-p侧面)')], loc='lower right', fontsize=8)
save(fig, 'ch1_ethylene.png')

# === HC≡CH: sp linear ===
fig, ax = plt.subplots(figsize=(5, 3))
ax.axis('off')
ax.set_xlim(-2.5, 2.5); ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
# H-C≡C-H linear
atoms = [(-1.8, 'H', 'c'), (-0.8, 'C', 'k'), (0.8, 'C', 'k'), (1.8, 'H', 'c')]
for x, lbl, col in atoms:
    ms = 13 if lbl=='H' else 18
    ax.plot(x, 0, color=col, marker='o', ms=ms, zorder=5)
    fc = 'white' if col=='k' else 'black'
    ax.text(x, 0, lbl, ha='center', va='center', fontsize=11, color=fc, fontweight='bold', zorder=6)
# Bonds: H-C single, C≡C triple
ax.plot([-1.8, -0.8], [0, 0], 'b-', lw=2.5)  # H-C
ax.plot([0.8, 1.8],   [0, 0], 'b-', lw=2.5)  # C-H
# Triple bond: 1 sigma + 2 pi
ax.plot([-0.8, 0.8], [0.10, 0.10], 'b-', lw=3)
ax.plot([-0.8, 0.8], [0,    0   ], 'r-', lw=2.5)
ax.plot([-0.8, 0.8], [-0.10,-0.10], 'r-', lw=2.5)
ax.set_title('乙炔 HC≡CH\nsp 杂化, 线形, 180°', fontsize=12, fontweight='bold', pad=4)
ax.text(0, -1.2, '蓝=σ键  红=2个π键(两对p轨道垂直侧面重叠)', ha='center', fontsize=9, color='gray', style='italic')
save(fig, 'ch1_acetylene.png')

# === Hybridization comparison summary ===
fig, axes = plt.subplots(1, 3, figsize=(13, 5))
data = [
    ('sp³\n甲烷 CH₄', '109.5°', '四面体', '4σ 0π', '#4CAF50'),
    ('sp²\n乙烯 CH₂=CH₂', '120°', '平面三角', '3σ 1π', '#2196F3'),
    ('sp\n乙炔 HC≡CH', '180°', '线形', '2σ 2π', '#FF5722'),
]
for ax, (title, angle, shape, bonds, col) in zip(axes, data):
    ax.axis('off')
    ax.set_facecolor('#f8f8f8')
    ax.set_xlim(0,1); ax.set_ylim(0,1)
    rect = mpatches.FancyBboxPatch((0.05,0.05),0.9,0.9, boxstyle='round,pad=0.02',
                                    facecolor=col, alpha=0.12, edgecolor=col, linewidth=2)
    ax.add_patch(rect)
    ax.text(0.5, 0.82, title, ha='center', va='center', fontsize=13, fontweight='bold', color=col, transform=ax.transAxes)
    ax.text(0.5, 0.62, f'键角: {angle}', ha='center', fontsize=12, transform=ax.transAxes)
    ax.text(0.5, 0.47, f'形状: {shape}', ha='center', fontsize=12, transform=ax.transAxes)
    ax.text(0.5, 0.32, f'键型: {bonds}', ha='center', fontsize=11, color='gray', transform=ax.transAxes)
    ax.text(0.5, 0.15, f'未杂化p轨道: {["0","1","2"][axes.tolist().index(ax)]}个', ha='center', fontsize=10, style='italic', transform=ax.transAxes, color='purple')
fig.suptitle('碳原子杂化方式对比', fontsize=15, fontweight='bold')
plt.tight_layout()
save(fig, 'ch1_hybridization_compare.png')

# === Bond polarity / dipole moment ===
fig, axes = plt.subplots(1, 3, figsize=(11, 3.5))
examples = [
    ('CO₂\n(非极性分子)', '两个C=O偶极矩相消\n线形→合力=0', False),
    ('H₂O\n(极性分子)',   '两个O-H偶极矩\n不相消→有净偶极', True),
    ('CCl₄\n(非极性分子)', '四个C-Cl偶极矩\n对称相消=0', False),
]
for ax, (mol, reason, polar) in zip(axes, examples):
    ax.axis('off')
    col = '#E53935' if polar else '#1E88E5'
    ax.set_facecolor('#f5f5f5')
    rect = mpatches.FancyBboxPatch((0.02,0.02),0.96,0.96,boxstyle='round,pad=0.02',
                                    facecolor=col,alpha=0.1,edgecolor=col,lw=2)
    ax.add_patch(rect)
    ax.text(0.5,0.82,mol,ha='center',fontsize=12,fontweight='bold',color=col,transform=ax.transAxes)
    ax.text(0.5,0.52,reason,ha='center',fontsize=10,transform=ax.transAxes,color='black',style='italic')
    label = '极性 μ≠0' if polar else '非极性 μ=0'
    ax.text(0.5,0.18,label,ha='center',fontsize=12,fontweight='bold',
            color='red' if polar else 'blue',transform=ax.transAxes)
fig.suptitle('分子极性判断：有极性键≠极性分子（要看对称性）', fontsize=13, fontweight='bold')
plt.tight_layout()
save(fig, 'ch1_dipole_examples.png')

# === Acid strength factors ===
fig, ax = plt.subplots(figsize=(11, 5))
ax.axis('off')
ax.set_xlim(0,11); ax.set_ylim(0,5)
ax.set_title('影响酸性强弱的四大因素（pKa越小酸性越强）', fontsize=14, fontweight='bold')

factors = [
    (1.5, 4.0, '①元素效应', 'HF < HCl < HBr < HI\n(同族：半径↑，键能↓，酸性↑)\nHF > H₂O > NH₃ > CH₄\n(同周期：电负性↑，酸性↑)', '#1565C0'),
    (4.0, 4.0, '②诱导效应', 'ClCH₂COOH > FCH₂COOH?\nNo: F > Cl (电负性)\n多氟 > 单氟\n距离越近效应越强', '#6A1B9A'),
    (7.5, 4.0, '③共振效应', 'RCOOH >> ROH\n羧酸负离子共振稳定\n酚 > 醇 (苯环共振)\n苦味酸极强酸', '#C62828'),
    (2.8, 1.5, '④杂化效应', 'sp > sp² > sp³\n（电负性: sp最强）\nHC≡C⁻ 最稳定\npKa: 25 < 44 < 50', '#2E7D32'),
]
for x, y, title, body, col in factors:
    rect = mpatches.FancyBboxPatch((x-1.3,y-1.1),2.6,1.9,boxstyle='round,pad=0.1',
                                    facecolor=col,alpha=0.12,edgecolor=col,lw=1.5)
    ax.add_patch(rect)
    ax.text(x, y+0.6, title, ha='center', fontsize=11, fontweight='bold', color=col)
    ax.text(x, y-0.1, body, ha='center', fontsize=8.5, color='black', va='top',
            family='monospace')

ax.text(5.5, 0.3, 'pKa参考: H₂O=15.7  ROH≈16  PhOH=10  RCOOH=4~5  HC≡CH=25  RNH₂=38  RH=50',
        ha='center', fontsize=9, color='gray', style='italic')
save(fig, 'ch1_acid_strength_factors.png')

# === Lewis acid/base ===
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')
ax.set_xlim(0,10); ax.set_ylim(0,4)
ax.set_title('Lewis酸碱 vs Brønsted酸碱（重要区别！）', fontsize=13, fontweight='bold')

# Lewis
rect1 = mpatches.FancyBboxPatch((0.2,0.5),4.2,3.0,boxstyle='round,pad=0.1',
                                  facecolor='#E3F2FD',edgecolor='#1565C0',lw=2)
ax.add_patch(rect1)
ax.text(2.3,3.2,'Lewis酸碱',ha='center',fontsize=12,fontweight='bold',color='#1565C0')
ax.text(2.3,2.5,'Lewis酸 = 电子对接受体\n(缺电子: BF₃, AlCl₃, Fe³⁺, H⁺)',ha='center',fontsize=9.5,color='black')
ax.text(2.3,1.4,'Lewis碱 = 电子对给予体\n(富电子: NH₃, H₂O, ROH, X⁻)',ha='center',fontsize=9.5,color='black')
ax.text(2.3,0.7,'范围更广！包含无质子酸碱',ha='center',fontsize=9,color='blue',style='italic')

# Bronsted
rect2 = mpatches.FancyBboxPatch((5.3,0.5),4.2,3.0,boxstyle='round,pad=0.1',
                                  facecolor='#FFF3E0',edgecolor='#E65100',lw=2)
ax.add_patch(rect2)
ax.text(7.4,3.2,'Brønsted酸碱',ha='center',fontsize=12,fontweight='bold',color='#E65100')
ax.text(7.4,2.5,'酸 = 质子给予体 (H⁺ donor)\n碱 = 质子接受体 (H⁺ acceptor)',ha='center',fontsize=9.5,color='black')
ax.text(7.4,1.4,'pKa: 越小酸性越强\n共轭酸碱对: 酸强→共轭碱弱',ha='center',fontsize=9.5,color='black')
ax.text(7.4,0.7,'必须有质子转移',ha='center',fontsize=9,color='orange',style='italic')

ax.annotate('', xy=(5.1,2), xytext=(4.5,2), arrowprops=dict(arrowstyle='<->',lw=2,color='purple'))
ax.text(4.8, 2.4, 'Brønsted\n⊂ Lewis', ha='center', fontsize=8.5, color='purple')
save(fig, 'ch1_lewis_bronsted.png')

# === Homolytic vs Heterolytic cleavage ===
fig, ax = plt.subplots(figsize=(10, 4))
ax.axis('off')
ax.set_xlim(0,10); ax.set_ylim(0,4)
ax.set_title('键的断裂方式（均裂 vs 异裂）', fontsize=13, fontweight='bold')

# Homolytic
ax.text(2.5,3.5,'均裂（Homolytic）→ 自由基', ha='center',fontsize=11,fontweight='bold',color='#C62828')
ax.text(2.5,2.7,'A—B  →  A•  +  B•', ha='center',fontsize=13,family='monospace',color='#C62828')
ax.text(2.5,2.0,'每个碎片各得1个电子\n→产生自由基（游离基）\n链式反应、光照/高温引发',ha='center',fontsize=9.5,color='black')
ax.text(2.5,0.7,'鱼钩箭头 ⇀ 表示单电子转移',ha='center',fontsize=9,color='gray',style='italic')
ax.axvline(5,color='gray',lw=1.5,ls='--')

# Heterolytic
ax.text(7.5,3.5,'异裂（Heterolytic）→ 离子', ha='center',fontsize=11,fontweight='bold',color='#1565C0')
ax.text(7.5,2.7,'A—B  →  A⁺  +  B:⁻', ha='center',fontsize=13,family='monospace',color='#1565C0')
ax.text(7.5,2.0,'两个电子全给一方\n→产生碳正离子/碳负离子\n极性溶剂、亲核/亲电反应',ha='center',fontsize=9.5,color='black')
ax.text(7.5,0.7,'弯箭头 → 表示电子对转移',ha='center',fontsize=9,color='gray',style='italic')
save(fig, 'ch1_bond_cleavage.png')

# === Functional groups overview ===
fig, ax = plt.subplots(figsize=(14, 7))
ax.axis('off')
ax.set_title('主要官能团总览（考试必背）', fontsize=15, fontweight='bold')
fg_data = [
    # (x, y, name, formula, class)
    (1.0, 6.2, '烯烃', 'C=C', 'alkene'),
    (3.2, 6.2, '炔烃', 'C≡C', 'alkyne'),
    (5.4, 6.2, '芳香', 'Ph (Ar)', 'aromatic'),
    (7.6, 6.2, '卤代烃', 'C–X', 'halide'),
    (9.8, 6.2, '醇', '–OH', 'alcohol'),
    (12.0,6.2, '酚', 'Ar–OH', 'phenol'),
    (1.0, 4.2, '醚', 'R–O–R', 'ether'),
    (3.2, 4.2, '醛', '–CHO', 'aldehyde'),
    (5.4, 4.2, '酮', 'C=O', 'ketone'),
    (7.6, 4.2, '羧酸', '–COOH', 'carboxylic'),
    (9.8, 4.2, '酯', '–COO–', 'ester'),
    (12.0,4.2, '酰卤', '–COX', 'acyl halide'),
    (1.0, 2.2, '酸酐', '(CO)₂O', 'anhydride'),
    (3.2, 2.2, '酰胺', '–CONH₂', 'amide'),
    (5.4, 2.2, '胺', '–NH₂', 'amine'),
    (7.6, 2.2, '腈', '–CN', 'nitrile'),
    (9.8, 2.2, '硝基', '–NO₂', 'nitro'),
    (12.0,2.2, '磺酸', '–SO₃H', 'sulfonic'),
]
colors_map = {'alkene':'#4CAF50','alkyne':'#66BB6A','aromatic':'#FFA726',
              'halide':'#EF5350','alcohol':'#42A5F5','phenol':'#29B6F6',
              'ether':'#AB47BC','aldehyde':'#FF7043','ketone':'#FF8A65',
              'carboxylic':'#EC407A','ester':'#F06292','acyl halide':'#E91E63',
              'anhydride':'#7E57C2','amide':'#9575CD','amine':'#26A69A',
              'nitrile':'#26C6DA','nitro':'#FFCA28','sulfonic':'#BDBDBD'}
for (x, y, name, formula, cls) in fg_data:
    col = colors_map.get(cls, '#888')
    rect = mpatches.FancyBboxPatch((x-0.9,y-0.7),1.8,1.3,boxstyle='round,pad=0.05',
                                    facecolor=col,alpha=0.2,edgecolor=col,lw=1.5)
    ax.add_patch(rect)
    ax.text(x, y+0.25, name, ha='center', fontsize=10, fontweight='bold', color=col)
    ax.text(x, y-0.25, formula, ha='center', fontsize=10, family='monospace', color='black')
ax.set_xlim(0,13.5); ax.set_ylim(0.8,7.2)
plt.tight_layout()
save(fig, 'ch1_functional_groups.png')

print("\nAll ch1 orbital/concept diagrams generated!")
