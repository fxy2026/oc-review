#!/usr/bin/env python3
"""
Comprehensive image generator for all chapters.
All PNGs, no SVG. Chinese fonts enabled.
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np
import os

# ── Chinese font setup ──────────────────────────────────────────────────
import matplotlib.font_manager as fm
for fname in ['Microsoft YaHei', 'SimHei', 'Noto Sans SC', 'SimSun']:
    if any(f.name == fname for f in fm.fontManager.ttflist):
        matplotlib.rcParams['font.family'] = fname
        break
matplotlib.rcParams['axes.unicode_minus'] = False

IMG = 'img'
os.makedirs(IMG, exist_ok=True)

def save(fig, name, dpi=180):
    fig.savefig(f'{IMG}/{name}', dpi=dpi, bbox_inches='tight', facecolor='white')
    plt.close(fig)
    print(f'  {name}')

# ════════════════════════════════════════════════════════════
# CH2 — Naming & Structure
# ════════════════════════════════════════════════════════════
print('\n=== CH2 ===')

# DBE calculation guide
fig, ax = plt.subplots(figsize=(11, 5))
ax.axis('off'); ax.set_xlim(0,11); ax.set_ylim(0,5)
ax.set_title('不饱和度（DBE）计算与应用', fontsize=15, fontweight='bold')
# Formula box
rect = mpatches.FancyBboxPatch((0.3,3.2),5.0,1.5,boxstyle='round,pad=0.1',
    facecolor='#E3F2FD',edgecolor='#1565C0',lw=2)
ax.add_patch(rect)
ax.text(2.8,4.1,'DBE = (2C + 2 + N - H - X) / 2',
    ha='center',fontsize=13,fontweight='bold',color='#1565C0',family='monospace')
ax.text(2.8,3.5,'C=碳数  N=氮数  H=氢数  X=卤素数  O/S不计',
    ha='center',fontsize=10,color='gray')
# Examples
examples = [
    (0.8,2.4,'苯 C₆H₆','DBE=(12+2-6)/2=4\n(1环+3双键)','#FF5722'),
    (3.3,2.4,'环己烷 C₆H₁₂','DBE=(12+2-12)/2=1\n(1个环)','#4CAF50'),
    (5.8,2.4,'乙炔 C₂H₂','DBE=(4+2-2)/2=2\n(1个三键=2)','#9C27B0'),
    (8.3,2.4,'丙酮 C₃H₆O','DBE=(6+2-6)/2=1\n(1个C=O)','#FF9800'),
]
for x,y,mol,dbe,col in examples:
    r=mpatches.FancyBboxPatch((x-0.7,y-0.8),2.2,1.4,boxstyle='round,pad=0.08',
        facecolor=col,alpha=0.13,edgecolor=col,lw=1.5)
    ax.add_patch(r)
    ax.text(x+0.4,y+0.3,mol,ha='center',fontsize=10,fontweight='bold',color=col)
    ax.text(x+0.4,y-0.35,dbe,ha='center',fontsize=9,color='black')
ax.text(5.5,0.5,'规律：DBE=1→1个环或1个双键；DBE=2→1个三键或2个不饱和度；苯DBE=4',
    ha='center',fontsize=10,style='italic',color='gray')
ax.text(5.5,0.1,'⚠ O、S不影响DBE！',ha='center',fontsize=10,color='red',fontweight='bold')
save(fig,'ch2_dbe_guide.png')

# Z/E vs cis/trans distinction
fig, axes = plt.subplots(1,2,figsize=(11,4.5))
ax1,ax2 = axes
for ax in axes: ax.axis('off'); ax.set_xlim(0,5); ax.set_ylim(0,4.5)
ax1.set_title('Z/E命名（CIP优先规则）',fontsize=12,fontweight='bold',color='#1565C0')
ax2.set_title('顺/反命名（仅适用简单情形）',fontsize=12,fontweight='bold',color='#C62828')

# Z/E example: 2-bromo-2-butene
# C=C backbone
ax1.plot([1.5,3.5],[2,2],'k-',lw=3)
ax1.plot([1.5,3.5],[2.1,2.1],'k-',lw=1.5)
ax1.text(1.5,2,'||',fontsize=8,ha='center',va='center',color='white')
# Left carbon substituents
ax1.plot([1.5,0.5],[2,3],'b-',lw=2); ax1.text(0.3,3.2,'CH₃',fontsize=11,color='blue',fontweight='bold')
ax1.plot([1.5,0.5],[2,1],'r-',lw=2); ax1.text(0.3,0.7,'Br',fontsize=11,color='red',fontweight='bold')
# Right carbon substituents
ax1.plot([3.5,4.5],[2,3],'g-',lw=2); ax1.text(4.5,3.2,'CH₃',fontsize=11,color='green',fontweight='bold')
ax1.plot([3.5,4.5],[2,1],'orange',lw=2); ax1.text(4.5,0.7,'H',fontsize=11,color='orange',fontweight='bold')
ax1.text(1.5,2.6,'①Br>CH₃',fontsize=9,ha='center',color='purple')
ax1.text(3.5,2.6,'①CH₃>H',fontsize=9,ha='center',color='purple')
ax1.text(2.5,0.3,'高优先基在同侧→Z（zusammen）\n高优先基异侧→E（entgegen）',
    ha='center',fontsize=10,style='italic')

# cis/trans: 2-butene
ax2.plot([1.5,3.5],[2,2],'k-',lw=3)
ax2.plot([1.5,3.5],[2.1,2.1],'k-',lw=1.5)
ax2.plot([1.5,0.5],[2,3],'b-',lw=2); ax2.text(0.3,3.2,'CH₃',fontsize=11,color='blue',fontweight='bold')
ax2.plot([1.5,0.5],[2,1],'gray',lw=2); ax2.text(0.3,0.7,'H',fontsize=11,color='gray')
ax2.plot([3.5,4.5],[2,3],'b-',lw=2); ax2.text(4.5,3.2,'CH₃',fontsize=11,color='blue',fontweight='bold')
ax2.plot([3.5,4.5],[2,1],'gray',lw=2); ax2.text(4.5,0.7,'H',fontsize=11,color='gray')
ax2.text(2.5,3.7,'顺-2-丁烯 (Z)',fontsize=11,ha='center',color='#C62828',fontweight='bold')
ax2.text(2.5,0.3,'相同基团在同侧=顺(cis)\n相同基团在异侧=反(trans)',ha='center',fontsize=10,style='italic')
ax2.text(2.5,-0.1,'⚠ 每端必须有相同基团才能用顺反！',ha='center',fontsize=9,color='red')
plt.tight_layout()
save(fig,'ch2_ze_vs_cistrans.png')

# Resonance rules summary
fig, ax = plt.subplots(figsize=(12,6))
ax.axis('off'); ax.set_xlim(0,12); ax.set_ylim(0,6)
ax.set_title('共振结构书写规则（7条必记）', fontsize=15, fontweight='bold')
rules = [
    ('①','原子骨架不变','只移动电子，不移动原子','#1565C0'),
    ('②','价电子总数不变','总电子数守恒','#1565C0'),
    ('③','只移动π电子和孤对电子','σ键电子不参与共振','#C62828'),
    ('④','每个原子不超过8电子','第二周期元素！(H除外最多2)','#C62828'),
    ('⑤','电荷分布尽量少','贡献大的结构更重要','#2E7D32'),
    ('⑥','负电荷在电负性大的原子上','O,N上的负电荷比C稳定','#2E7D32'),
    ('⑦','等价共振结构贡献相同','如苯的两个Kekulé结构','#6A1B9A'),
]
for i,(num,title,body,col) in enumerate(rules):
    row,col_idx = divmod(i,2) if i<6 else (3,0)
    x = 0.4 + col_idx*6.0
    y = 5.2 - row*1.5
    if i==6: x=3.0
    r=mpatches.FancyBboxPatch((x-0.2,y-0.55),5.5 if i<6 else 6,1.1,
        boxstyle='round,pad=0.08',facecolor=col,alpha=0.1,edgecolor=col,lw=1.5)
    ax.add_patch(r)
    ax.text(x+0.15,y+0.28,f'{num} {title}',fontsize=10.5,fontweight='bold',color=col)
    ax.text(x+0.15,y-0.18,body,fontsize=9.5,color='black',style='italic')
ax.text(6,0.25,'贡献越大的共振结构：价键越完整、电荷越少、电荷在合适原子上',
    ha='center',fontsize=10,color='purple',style='italic')
save(fig,'ch2_resonance_rules.png')

# ════════════════════════════════════════════════════════════
# CH3 — Alkanes & Conformations
# ════════════════════════════════════════════════════════════
print('\n=== CH3 ===')

# Butane conformation energy diagram
fig, ax = plt.subplots(figsize=(10,5))
angles = np.linspace(0,360,361)
# Approximate energy profile for butane
energy = (2.5*np.cos(np.radians(angles)) +
          1.5*np.cos(np.radians(3*angles)) +
          0.5*np.cos(np.radians(2*angles)))
energy = energy - energy.min()
ax.plot(angles, energy, 'b-', lw=2.5)
ax.fill_between(angles, 0, energy, alpha=0.08, color='blue')
# Label key conformations
key_pts = [(0,'anti\n(最稳定\n0 kJ)',(0,0.2)),
           (60,'gauche\n(+3.8 kJ)',(60,0.2)),
           (120,'eclipsed\n(部分重叠\n+16 kJ)',(120,0.2)),
           (180,'eclipsed\n(完全重叠\n+19 kJ)',(180,0.2)),
           (240,'eclipsed\n(部分重叠\n+16 kJ)',(240,0.2)),
           (300,'gauche\n(+3.8 kJ)',(300,0.2))]
e_vals = {0:0, 60:3.8, 120:16, 180:19, 240:16, 300:3.8}
colors_p = {0:'green',60:'orange',120:'red',180:'darkred',240:'red',300:'orange'}
for angle,label,_ in key_pts:
    e = e_vals[angle]
    # Find closest point
    idx = angle
    e_plot = energy[idx]
    ax.plot(angle, e_plot, 'o', ms=8, color=colors_p[angle])
    ax.annotate(label, xy=(angle,e_plot), xytext=(angle, e_plot+0.5+1.5*abs(np.cos(np.radians(angle*3)))),
        ha='center', fontsize=8, color=colors_p[angle], fontweight='bold',
        arrowprops=dict(arrowstyle='-',color=colors_p[angle],lw=0.8))
ax.set_xlabel('C2-C3二面角 (°)', fontsize=12)
ax.set_ylabel('相对能量', fontsize=12)
ax.set_title('正丁烷(C4H10)沿C2-C3旋转的构象能量变化', fontsize=13, fontweight='bold')
ax.set_xticks([0,60,120,180,240,300,360])
ax.set_xticklabels(['0°\nanti','60°\ngauche','120°','180°\neclipsed','240°','300°\ngauche','360°'])
ax.grid(True, alpha=0.3)
ax.text(5, energy.max()*0.15, '稳定性: anti > gauche > 部分重叠式 > 全重叠式',
    fontsize=10, color='gray', style='italic')
save(fig,'ch3_butane_energy.png')

# Halogenation selectivity
fig, ax = plt.subplots(figsize=(11,5))
ax.axis('off'); ax.set_xlim(0,11); ax.set_ylim(0,5)
ax.set_title('烷烃卤代反应：选择性与活性（自由基机理）', fontsize=14, fontweight='bold')

# Cl2 vs Br2 comparison table
headers = ['卤素','反应条件','选择性','1°H活性','2°H活性','3°H活性','用途']
cl_data = ['Cl₂','光照/高温','低','1','4','5','工业卤化']
br_data = ['Br₂','光照(较慢)','高','1','80','1600','合成选择性']
# Draw table
col_x = [0.3,1.6,2.9,4.2,5.3,6.4,7.7]
for i,(h,cx) in enumerate(zip(headers,col_x)):
    ax.text(cx,4.3,h,fontsize=9,fontweight='bold',color='white',
        bbox=dict(boxstyle='round',facecolor='#1565C0',pad=0.3))
for i,(v,cx) in enumerate(zip(cl_data,col_x)):
    c='#E3F2FD' if i%2==0 else '#BBDEFB'
    ax.text(cx,3.4,v,fontsize=9,ha='left',
        bbox=dict(boxstyle='round',facecolor='#FFCCBC',pad=0.3))
for i,(v,cx) in enumerate(zip(br_data,col_x)):
    ax.text(cx,2.7,v,fontsize=9,ha='left',
        bbox=dict(boxstyle='round',facecolor='#C8E6C9',pad=0.3))

# Mechanism steps
ax.text(0.5,2.0,'自由基链式机理:',fontsize=10,fontweight='bold',color='#C62828')
ax.text(0.5,1.55,'①引发: Cl₂ →(hν) 2Cl·  (均裂)',fontsize=9,family='monospace')
ax.text(0.5,1.15,'②增长: Cl· + R-H → R· + HCl    R· + Cl₂ → R-Cl + Cl·',fontsize=9,family='monospace')
ax.text(0.5,0.75,'③终止: 2R· → R-R   R·+Cl·→ R-Cl   2Cl·→Cl₂',fontsize=9,family='monospace')
ax.text(5.5,1.55,'Hammond假说:',fontsize=10,fontweight='bold',color='#1565C0')
ax.text(5.5,1.15,'放热反应(Cl·)→早过渡态→底物活性差异小→选择性低',fontsize=9)
ax.text(5.5,0.75,'吸热反应(Br·)→晚过渡态→底物活性差异大→选择性高',fontsize=9)
ax.text(5.5,0.3,'⇒ Br₂选择性更好，多用于合成',fontsize=9,color='green',fontweight='bold')
save(fig,'ch3_halogenation.png')

# Cyclohexane chair conformations - methylcyclohexane
fig, axes = plt.subplots(1,2,figsize=(12,5))
for ax in axes: ax.axis('off'); ax.set_xlim(-1,5); ax.set_ylim(-1,4)

def draw_chair(ax, title, sub_pos, sub_label, sub_color, energy_label):
    # Chair outline (simplified)
    verts = np.array([[0,1],[1,0],[2,0.5],[3,1.5],[2,2],[1,2]])
    for i in range(len(verts)):
        p1,p2 = verts[i], verts[(i+1)%len(verts)]
        ax.plot([p1[0],p2[0]],[p1[1],p2[1]],'k-',lw=2.5)
    # Axial bonds at each vertex
    dirs = [1,-1,1,-1,1,-1]
    for i,(v,d) in enumerate(zip(verts,dirs)):
        ax.plot([v[0],v[0]],[v[1],v[1]+d*0.6],'gray',lw=1.2,ls='--')
    # Substituent
    sp = sub_pos
    ax.plot([verts[sp][0],verts[sp][0]],[verts[sp][1],verts[sp][1]+dirs[sp]*0.7],
        sub_color,lw=2.5)
    ax.text(verts[sp][0],verts[sp][1]+dirs[sp]*0.9,sub_label,
        ha='center',fontsize=12,color=sub_color,fontweight='bold')
    ax.set_title(f'{title}\n{energy_label}',fontsize=11,fontweight='bold')

draw_chair(axes[0],'甲基环己烷：e键构象\n（平伏键）',
    2,'CH₃','#2196F3','更稳定 ΔG=-7.3 kJ/mol')
axes[0].text(2,-0.6,'平伏键(e)：基团指向外侧\n无1,3-二竖键作用',
    ha='center',fontsize=10,style='italic',color='#2196F3')

draw_chair(axes[1],'甲基环己烷：a键构象\n（直立键）',
    0,'CH₃','#F44336','不稳定\n1,3-二竖键排斥')
axes[1].text(2,-0.6,'直立键(a)：基团指向上/下\n与1,3位a键氢排斥（A值）',
    ha='center',fontsize=10,style='italic',color='#F44336')

plt.suptitle('取代基倾向占平伏键（e键）——减小1,3-二竖键张力', fontsize=13, fontweight='bold')
plt.tight_layout()
save(fig,'ch3_methylcyclohexane_conf.png')

# Ring strain comparison
fig, ax = plt.subplots(figsize=(10,4))
ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,4)
ax.set_title('环烷烃的环张力与稳定性', fontsize=14, fontweight='bold')
rings = [
    ('环丙烷\nC₃H₆','115°\n(应60°)','27.5','很高\n↓开环','#F44336'),
    ('环丁烷\nC₄H₈','90°\n(应109.5°)','26.4','高\n蝶形','#FF9800'),
    ('环戊烷\nC₅H₁₀','108°','6.5','较低\n信封式','#FFC107'),
    ('环己烷\nC₆H₁₂','111°\n椅式','0','最稳定\n椅式构象','#4CAF50'),
    ('环庚烷+','大于\n109.5°','增加','扭转\n张力','#2196F3'),
]
xs = [1,3,5,7,9]
for (name,angle,strain,stab,col),x in zip(rings,xs):
    r=mpatches.FancyBboxPatch((x-0.8,0.4),1.6,3.0,boxstyle='round,pad=0.08',
        facecolor=col,alpha=0.15,edgecolor=col,lw=2)
    ax.add_patch(r)
    ax.text(x,3.1,name,ha='center',fontsize=9.5,fontweight='bold',color=col)
    ax.text(x,2.3,f'键角\n{angle}',ha='center',fontsize=8.5)
    ax.text(x,1.55,f'张力\n{strain} kJ/mol',ha='center',fontsize=8.5,color=col)
    ax.text(x,0.7,stab,ha='center',fontsize=8,style='italic',color='gray')
save(fig,'ch3_ring_strain.png')

# ════════════════════════════════════════════════════════════
# CH4 — Stereochemistry
# ════════════════════════════════════════════════════════════
print('\n=== CH4 ===')

# R/S assignment step by step
fig, axes = plt.subplots(1,3,figsize=(13,5))
ax1,ax2,ax3 = axes
for ax in axes: ax.axis('off'); ax.set_xlim(0,4); ax.set_ylim(0,4.5)

ax1.set_title('①确定优先级\n(CIP规则)', fontsize=11, fontweight='bold', color='#1565C0')
ax1.text(2,3.8,'原子序数大→优先级高',ha='center',fontsize=10,color='#1565C0')
priority_ex = [('O(8)','1st','red'),('Cl(17)','↑','green'),('Br(35)','最高','darkred'),
               ('C>N>O','顺序','blue')]
ax1.text(2,3.2,'Br>Cl>OH>NH₂>CH₃>H',ha='center',fontsize=9.5,family='monospace',
    bbox=dict(facecolor='lightyellow',edgecolor='orange',boxstyle='round'))
ax1.text(2,2.5,'同层再比下一层\n(扩展原子法)',ha='center',fontsize=9.5,style='italic')
ax1.text(2,1.8,'不饱和键：\nC=O → C(O)(O)\nC=C → C(C)(C)',ha='center',fontsize=9,family='monospace',
    bbox=dict(facecolor='#e8f5e9',boxstyle='round'))
ax1.text(2,0.7,'H永远最低！',ha='center',fontsize=11,color='red',fontweight='bold')

ax2.set_title('②最低优先基朝后\n(H置于纸面里)', fontsize=11, fontweight='bold', color='#2E7D32')
# Draw tetrahedral carbon
cx,cy = 2,2.2
ax2.plot(cx,cy,'ko',ms=18,zorder=5)
ax2.text(cx,cy,'C*',ha='center',va='center',fontsize=11,color='white',fontweight='bold',zorder=6)
ax2.plot([cx,cx],[cy,cy+1.2],'b-',lw=2.5); ax2.text(cx,cy+1.4,'①',ha='center',fontsize=12,color='blue',fontweight='bold')
ax2.plot([cx,cx-1.1],[cy,cy-0.7],'b-',lw=2.5); ax2.text(cx-1.3,cy-0.9,'②',ha='center',fontsize=12,color='blue',fontweight='bold')
ax2.plot([cx,cx+1.1],[cy,cy-0.7],'b-',lw=2.5); ax2.text(cx+1.3,cy-0.9,'③',ha='center',fontsize=12,color='blue',fontweight='bold')
ax2.plot([cx,cx],[cy,cy-1.4],'r--',lw=2.5); ax2.text(cx,cy-1.7,'④(H)\n← 指向里',ha='center',fontsize=10,color='red')
ax2.text(2,0.3,'最低优先基(④)必须\n朝向观察者背面',ha='center',fontsize=9.5,style='italic',color='green')

ax3.set_title('③观察①→②→③转向\n判断R/S', fontsize=11, fontweight='bold', color='#C62828')
# R arrangement (clockwise)
theta = np.linspace(np.pi/2, np.pi/2-2*np.pi, 100)
x_circ = 2 + 0.9*np.cos(theta[:50])
y_circ = 2.5 + 0.9*np.sin(theta[:50])
ax3.plot(x_circ, y_circ, 'r-', lw=2.5)
ax3.annotate('', xy=(x_circ[-1],y_circ[-1]), xytext=(x_circ[-2],y_circ[-2]),
    arrowprops=dict(arrowstyle='->', color='red', lw=2))
ax3.text(2,2.5,'顺时针→R',ha='center',fontsize=12,color='red',fontweight='bold',
    bbox=dict(facecolor='#FFCDD2',boxstyle='round'))
# S arrangement
theta2 = np.linspace(np.pi/2, np.pi/2+2*np.pi, 100)
x_c2 = 2 + 0.9*np.cos(theta2[:50])
y_c2 = 1.0 + 0.9*np.sin(theta2[:50])
ax3.plot(x_c2, y_c2, 'b-', lw=2.5)
ax3.annotate('', xy=(x_c2[-1],y_c2[-1]), xytext=(x_c2[-2],y_c2[-2]),
    arrowprops=dict(arrowstyle='->', color='blue', lw=2))
ax3.text(2,1.0,'逆时针→S',ha='center',fontsize=12,color='blue',fontweight='bold',
    bbox=dict(facecolor='#BBDEFB',boxstyle='round'))
ax3.text(2,0.3,'④在前时：R↔S互换！',ha='center',fontsize=9.5,color='purple',style='italic')

plt.suptitle('R/S构型标记三步法（2-溴丁烷为例）', fontsize=14, fontweight='bold')
plt.tight_layout()
save(fig,'struct_rs_config.png')

# Enantiomers vs Diastereomers
fig, ax = plt.subplots(figsize=(12,5))
ax.axis('off'); ax.set_xlim(0,12); ax.set_ylim(0,5)
ax.set_title('对映体 vs 非对映体 vs 相同化合物（关系判断）', fontsize=14, fontweight='bold')

rel_data = [
    (2.0,3.2,'对映体','镜像关系，不可叠合\n所有手性中心构型全部相反\n物理性质相同\n旋光度绝对值相等方向相反','#1565C0'),
    (6.0,3.2,'非对映体','非镜像关系\n至少一个手性中心构型不同\n物理性质不同\n化学性质也有差异','#C62828'),
    (10.0,3.2,'相同化合物','所有手性中心\n构型完全相同\n可以叠合','#2E7D32'),
]
for x,y,name,desc,col in rel_data:
    r=mpatches.FancyBboxPatch((x-1.5,y-0.9),3.0,2.8,boxstyle='round,pad=0.1',
        facecolor=col,alpha=0.1,edgecolor=col,lw=2)
    ax.add_patch(r)
    ax.text(x,y+1.55,name,ha='center',fontsize=12,fontweight='bold',color=col)
    ax.text(x,y+0.5,desc,ha='center',fontsize=9,color='black')

ax.text(6,0.9,'判断方法：写出所有手性中心的R/S → 逐一比较',
    ha='center',fontsize=11,style='italic',color='purple')
ax.text(6,0.35,'含n个不同手性中心→最多2ⁿ种立体异构体；有meso化合物时减少',
    ha='center',fontsize=10,color='gray')
# Arrows
ax.annotate('',xy=(4.3,3.5),xytext=(3.7,3.5),arrowprops=dict(arrowstyle='<->',lw=1.5,color='gray'))
ax.annotate('',xy=(8.3,3.5),xytext=(7.7,3.5),arrowprops=dict(arrowstyle='<->',lw=1.5,color='gray'))
save(fig,'ch4_stereo_relations.png')

# Optical activity and ee%
fig, ax = plt.subplots(figsize=(11,4.5))
ax.axis('off'); ax.set_xlim(0,11); ax.set_ylim(0,4.5)
ax.set_title('旋光性、比旋光度与对映体过量（ee%）', fontsize=14, fontweight='bold')

boxes = [
    (1.5,3.2,'旋光性',
     '旋光仪测量\n平面偏振光旋转角α\n(+)=右旋  (-)=左旋\n与R/S无直接关联！','#1565C0'),
    (4.8,3.2,'比旋光度[α]',
     '[α] = α / (l × c)\nl=样品管长度(dm)\nc=浓度(g/mL)\n溶剂、温度、波长有影响','#2E7D32'),
    (8.2,3.2,'对映体过量ee%',
     'ee% = |R%-S%| × 100\n= (|α|obs / |α|pure) × 100\n0%=外消旋  100%=纯对映体\n光学纯度=ee%','#C62828'),
]
for x,y,name,desc,col in boxes:
    r=mpatches.FancyBboxPatch((x-1.2,y-0.7),2.4,2.5,boxstyle='round,pad=0.1',
        facecolor=col,alpha=0.1,edgecolor=col,lw=2)
    ax.add_patch(r)
    ax.text(x,y+1.5,name,ha='center',fontsize=11,fontweight='bold',color=col)
    ax.text(x,y+0.4,desc,ha='center',fontsize=9,color='black')

ax.text(5.5,0.7,'外消旋体(racemic mixture)：等量对映体混合，[α]=0，不能拆分',
    ha='center',fontsize=10,style='italic',color='purple')
ax.text(5.5,0.25,'拆分方法：结晶、色谱（手性固定相）、酶法、化学法（生成非对映体盐）',
    ha='center',fontsize=9.5,color='gray')
save(fig,'ch4_optical_activity.png')

# ════════════════════════════════════════════════════════════
# CH5 — Alkenes
# ════════════════════════════════════════════════════════════
print('\n=== CH5 ===')

# Markovnikov rule & carbocation mechanism
fig, ax = plt.subplots(figsize=(12,5))
ax.axis('off'); ax.set_xlim(0,12); ax.set_ylim(0,5)
ax.set_title('Markovnikov规则——本质是碳正离子稳定性', fontsize=14, fontweight='bold')

ax.text(1,4.5,'HX与不对称烯烃加成：H⁺加到含H多的碳', fontsize=11, fontweight='bold', color='#1565C0')
# Example: propene + HBr
ax.text(0.5,3.8,'CH₃-CH=CH₂  +  HBr', fontsize=12, family='monospace')
ax.text(5.5,3.8,'→', fontsize=16)
# Two pathways
ax.text(3.5,3.0,'途径A（Markovnikov）:', fontsize=10, color='green', fontweight='bold')
ax.text(3.5,2.5,'H⁺→CH₂=  形成 CH₃-CH⁺-CH₃', fontsize=9.5, family='monospace', color='green')
ax.text(3.5,2.0,'2°碳正离子 → 稳定 → 主产物', fontsize=9.5, color='green')
ax.text(3.5,1.5,'→ CH₃-CHBr-CH₃  (2-溴丙烷)', fontsize=9.5, family='monospace', color='green', fontweight='bold')

ax.text(7.5,3.0,'途径B（非Markovnikov）:', fontsize=10, color='red', fontweight='bold')
ax.text(7.5,2.5,'H⁺→CH=  形成 CH₃-CH=CH₂→CH₃CH₂CH₂⁺', fontsize=9, family='monospace', color='red')
ax.text(7.5,2.0,'1°碳正离子 → 不稳定 → 次产物', fontsize=9.5, color='red')
ax.text(7.5,1.5,'→ CH₃-CH₂-CH₂Br  (1-溴丙烷)', fontsize=9.5, family='monospace', color='red')

ax.text(6,0.6,'⚠ 过氧化物效应（ROOR）：HBr反马氏规则，自由基机理，Br先加',
    ha='center', fontsize=10, color='purple', style='italic',
    bbox=dict(facecolor='lightyellow',edgecolor='orange',boxstyle='round'))
ax.text(6,0.1,'⚠ 过氧化物只对HBr有效！HCl、HI无此效应',
    ha='center', fontsize=10, color='red')
save(fig,'ch5_markovnikov.png')

# Alkene oxidation comparison
fig, ax = plt.subplots(figsize=(12,6))
ax.axis('off'); ax.set_xlim(0,12); ax.set_ylim(0,6)
ax.set_title('烯烃氧化反应比较（高频考点）', fontsize=14, fontweight='bold')

ox_data = [
    (1.5,5.0,'冷稀KMnO₄\n(碱性)',
     'R-CH=CH-R → 顺-二醇\n(syn加成，两OH同面)',
     '顺-1,2-二醇\n(赤型/内消旋)',
     '#2196F3','#E3F2FD'),
    (5.5,5.0,'OsO₄\n(催化量+NMO)',
     'R-CH=CH-R → 顺-二醇\n(syn加成)',
     '顺-1,2-二醇\n(选择性更好)',
     '#4CAF50','#E8F5E9'),
    (9.5,5.0,'热浓KMnO₄\n(酸性)',
     'C=C断裂氧化\n末端=CH₂→CO₂+H₂O\nRCH=→RCOOH\nR₂C=→R₂C=O(酮)',
     '可用于\n结构鉴定',
     '#F44336','#FFEBEE'),
    (1.5,2.2,'臭氧化/Zn还原\nO₃→Zn/H₂O',
     'C=C断裂\n生成醛或酮\n(还原性条件)',
     'RCHO+R\'CHO\n(醛不进一步氧化)',
     '#FF5722','#FBE9E7'),
    (5.5,2.2,'臭氧化/H₂O₂\nO₃→H₂O₂',
     'C=C断裂\n醛→羧酸\n(氧化性条件)',
     'RCOOH+R\'COOH',
     '#9C27B0','#F3E5F5'),
    (9.5,2.2,'间氯过氧苯甲酸\nmCPBA',
     '环氧化\n(syn加成)\n构型保留',
     '环氧化物\n(保留双键立体化学)',
     '#FF9800','#FFF3E0'),
]
for x,y,reagent,mechanism,product,col,bg in ox_data:
    r=mpatches.FancyBboxPatch((x-1.3,y-1.0),2.6,2.2,boxstyle='round,pad=0.08',
        facecolor=bg,edgecolor=col,lw=2)
    ax.add_patch(r)
    ax.text(x,y+0.95,reagent,ha='center',fontsize=9.5,fontweight='bold',color=col)
    ax.text(x,y+0.25,mechanism,ha='center',fontsize=8.5,color='black')
    ax.text(x,y-0.65,product,ha='center',fontsize=8.5,fontweight='bold',color=col)

ax.text(6,0.35,'记忆口诀：冷稀/OsO₄→顺二醇  热浓→断键  O₃→切断  mCPBA→环氧',
    ha='center',fontsize=10,color='gray',style='italic',
    bbox=dict(facecolor='lightyellow',boxstyle='round'))
save(fig,'ch5_oxidation_compare.png')

# Hydroboration-oxidation
fig, ax = plt.subplots(figsize=(11,4.5))
ax.axis('off'); ax.set_xlim(0,11); ax.set_ylim(0,4.5)
ax.set_title('硼氢化-氧化反应（BH₃-THF → H₂O₂/NaOH）', fontsize=13, fontweight='bold')

# Boxes
b1=mpatches.FancyBboxPatch((0.3,0.8),2.5,2.8,boxstyle='round,pad=0.1',
    facecolor='#E3F2FD',edgecolor='#1565C0',lw=2)
ax.add_patch(b1)
ax.text(1.55,3.3,'步骤①：硼氢化',fontsize=10,fontweight='bold',color='#1565C0',ha='center')
ax.text(1.55,2.7,'BH₃与C=C协同加成\n(四中心过渡态)',fontsize=9,ha='center')
ax.text(1.55,2.0,'B加到含H多的碳\n(反Markovnikov)',fontsize=9,ha='center',color='#C62828',fontweight='bold')
ax.text(1.55,1.3,'syn加成！\n（B和H同面）',fontsize=9,ha='center',color='green')

ax.annotate('',xy=(3.5,2.2),xytext=(2.9,2.2),arrowprops=dict(arrowstyle='->',lw=2))
ax.text(3.2,2.6,'H₂O₂\nNaOH',fontsize=9,ha='center',color='gray')

b2=mpatches.FancyBboxPatch((3.7,0.8),2.5,2.8,boxstyle='round,pad=0.1',
    facecolor='#E8F5E9',edgecolor='#2E7D32',lw=2)
ax.add_patch(b2)
ax.text(4.95,3.3,'步骤②：氧化',fontsize=10,fontweight='bold',color='#2E7D32',ha='center')
ax.text(4.95,2.5,'H₂O₂氧化C-B键\n碱性条件水解',fontsize=9,ha='center')
ax.text(4.95,1.8,'B→OH\n(构型保留)',fontsize=9,ha='center',color='green',fontweight='bold')

ax.annotate('',xy=(7.2,2.2),xytext=(6.3,2.2),arrowprops=dict(arrowstyle='->',lw=2.5))

b3=mpatches.FancyBboxPatch((7.4,0.8),3.2,2.8,boxstyle='round,pad=0.1',
    facecolor='#FFF3E0',edgecolor='#E65100',lw=2)
ax.add_patch(b3)
ax.text(9.0,3.3,'总结果',fontsize=10,fontweight='bold',color='#E65100',ha='center')
ax.text(9.0,2.6,'反Markovnikov\n(OH在含H多碳)',fontsize=9,ha='center',color='#C62828',fontweight='bold')
ax.text(9.0,1.9,'syn总体加成\n无碳正离子中间体',fontsize=9,ha='center',color='green')
ax.text(9.0,1.2,'无重排！\n端烯→伯醇',fontsize=9,ha='center',color='blue',fontweight='bold')

ax.text(5.5,0.3,'BH₃加成 vs 酸催化水合：结果互补！酸催化→Markovnikov醇；BH₃→反Markovnikov醇',
    ha='center',fontsize=9,style='italic',color='gray')
save(fig,'ch5_hydroboration.png')

# Carbocation rearrangement
fig, ax = plt.subplots(figsize=(11,5))
ax.axis('off'); ax.set_xlim(0,11); ax.set_ylim(0,5)
ax.set_title('碳正离子重排（1,2-迁移）——考点！', fontsize=14, fontweight='bold')

ax.text(0.5,4.5,'重排条件：生成的碳正离子可通过1,2-迁移变为更稳定的碳正离子',
    fontsize=10,style='italic',color='#1565C0')

# Example 1: hydride shift
ax.text(0.5,3.8,'例1：氢迁移（1,2-hydride shift）',fontsize=10,fontweight='bold',color='#C62828')
ax.text(0.5,3.3,'  (CH₃)₂C⁺-CH₂CH₃  →  (CH₃)₂C=CH-CH₃ ?',fontsize=9,family='monospace')
ax.text(0.5,2.9,'  2°→H迁移→3°碳正离子（更稳定）',fontsize=9,color='green')

# Example 2: methyl shift
ax.text(0.5,2.3,'例2：甲基迁移（1,2-methyl shift）',fontsize=10,fontweight='bold',color='#9C27B0')
ax.text(0.5,1.9,'  新戊基正离子(1°)→甲基迁移→叔丁基正离子(3°)',fontsize=9,family='monospace')
ax.text(0.5,1.5,'  (CH₃)₃C-CH₂⁺ → (CH₃)₂C⁺-CH₂CH₃（经过重排）',fontsize=9,color='green',family='monospace')

# Example 3: ring expansion
ax.text(0.5,1.0,'例3：环扩张',fontsize=10,fontweight='bold',color='#1565C0')
ax.text(0.5,0.6,'  环丁基正离子→环戊基正离子（5元环更稳定）',fontsize=9,family='monospace')
ax.text(0.5,0.2,'  环戊基→环己基（亦可）',fontsize=9,family='monospace')

# Rule box
r=mpatches.FancyBboxPatch((6.5,1.0),4.2,3.5,boxstyle='round,pad=0.1',
    facecolor='#FFF9C4',edgecolor='#F57F17',lw=2)
ax.add_patch(r)
ax.text(8.6,4.2,'迁移优先规则',fontsize=11,fontweight='bold',ha='center',color='#F57F17')
ax.text(8.6,3.6,'氢>烷基（迁移能力）',fontsize=10,ha='center')
ax.text(8.6,3.0,'3°>2°>1°碳正离子\n（迁移方向→更稳定）',fontsize=10,ha='center')
ax.text(8.6,2.2,'重排信号：\n产物碳骨架与\n预期不同！',fontsize=9.5,ha='center',style='italic',color='#C62828')
ax.text(8.6,1.2,'E1反应也可发生重排\nSN1反应也可发生重排',fontsize=9,ha='center',color='gray')
save(fig,'ch5_carbocation_rearrange.png')

# ════════════════════════════════════════════════════════════
# CH6 — Alkynes & Dienes
# ════════════════════════════════════════════════════════════
print('\n=== CH6 ===')

# Alkyne reduction comparison
fig, ax = plt.subplots(figsize=(11,5))
ax.axis('off'); ax.set_xlim(0,11); ax.set_ylim(0,5)
ax.set_title('炔烃还原——产物立体化学对比（重要！）', fontsize=14, fontweight='bold')

# Lindlar
b1=mpatches.FancyBboxPatch((0.3,0.8),4.8,3.5,boxstyle='round,pad=0.1',
    facecolor='#E3F2FD',edgecolor='#1565C0',lw=2)
ax.add_patch(b1)
ax.text(2.7,4.0,'Lindlar催化剂 + H₂',fontsize=11,fontweight='bold',ha='center',color='#1565C0')
ax.text(2.7,3.4,'Pd/BaSO₄ + 喹啉\n（毒化催化剂）',fontsize=9.5,ha='center')
ax.text(2.7,2.8,'syn加成（顺式）',fontsize=10,ha='center',color='green',fontweight='bold')
ax.text(2.7,2.2,'RC≡CR  →  (Z)-RCH=CHR\n          顺式烯烃',fontsize=9.5,ha='center',family='monospace')
ax.text(2.7,1.4,'只加一个H₂\n不过度还原为烷烃',fontsize=9,ha='center',color='gray',style='italic')
ax.text(2.7,0.9,'→ 顺式（Z型）',fontsize=10,ha='center',color='#1565C0',fontweight='bold')

# Na/liq NH3
b2=mpatches.FancyBboxPatch((5.9,0.8),4.8,3.5,boxstyle='round,pad=0.1',
    facecolor='#FBE9E7',edgecolor='#C62828',lw=2)
ax.add_patch(b2)
ax.text(8.3,4.0,'Na（或Li）/ 液氨',fontsize=11,fontweight='bold',ha='center',color='#C62828')
ax.text(8.3,3.4,'Birch还原条件\n(-33°C)',fontsize=9.5,ha='center')
ax.text(8.3,2.8,'anti加成（反式）',fontsize=10,ha='center',color='orange',fontweight='bold')
ax.text(8.3,2.2,'RC≡CR  →  (E)-RCH=CHR\n          反式烯烃',fontsize=9.5,ha='center',family='monospace')
ax.text(8.3,1.4,'自由基负离子机理\n两步单电子还原',fontsize=9,ha='center',color='gray',style='italic')
ax.text(8.3,0.9,'→ 反式（E型）',fontsize=10,ha='center',color='#C62828',fontweight='bold')
save(fig,'ch6_alkyne_reduction.png')

# 1,2 vs 1,4 addition + kinetic/thermodynamic
fig, ax = plt.subplots(figsize=(11,5.5))
ax.axis('off'); ax.set_xlim(0,11); ax.set_ylim(0,5.5)
ax.set_title('1,3-丁二烯 + HBr：1,2-加成 vs 1,4-加成', fontsize=14, fontweight='bold')

ax.text(5.5,5.0,'CH₂=CH-CH=CH₂ + HBr →',ha='center',fontsize=12,family='monospace')
# Products
ax.text(2.5,4.2,'1,2-加成产物',ha='center',fontsize=10,fontweight='bold',color='#1565C0')
ax.text(2.5,3.7,'CH₂Br-CH=CH-CH₃\n(3-溴-1-丁烯)',ha='center',fontsize=9.5,family='monospace',color='#1565C0')
ax.text(8.0,4.2,'1,4-加成产物',ha='center',fontsize=10,fontweight='bold',color='#C62828')
ax.text(8.0,3.7,'CH₃-CH=CH-CH₂Br\n(1-溴-2-丁烯)',ha='center',fontsize=9.5,family='monospace',color='#C62828')

# Kinetic vs thermodynamic
b1=mpatches.FancyBboxPatch((0.3,0.5),4.8,2.8,boxstyle='round,pad=0.1',
    facecolor='#E3F2FD',edgecolor='#1565C0',lw=2)
ax.add_patch(b1)
ax.text(2.7,3.0,'动力学控制（低温,-80°C）',fontsize=10,fontweight='bold',ha='center',color='#1565C0')
ax.text(2.7,2.4,'活化能低→更快生成\n1,2-加成产物占优\n（BrCH₂更好亲核）',fontsize=9.5,ha='center')
ax.text(2.7,1.3,'低温：\nΔG‡小的→动力学产物\n=1,2-加成为主',ha='center',fontsize=9,color='#1565C0',fontweight='bold')

b2=mpatches.FancyBboxPatch((5.9,0.5),4.8,2.8,boxstyle='round,pad=0.1',
    facecolor='#FFF3E0',edgecolor='#C62828',lw=2)
ax.add_patch(b2)
ax.text(8.3,3.0,'热力学控制（高温,40°C+）',fontsize=10,fontweight='bold',ha='center',color='#C62828')
ax.text(8.3,2.4,'更稳定产物占优\n内烯烃比外烯烃稳定\n1,4-加成产物占优',fontsize=9.5,ha='center')
ax.text(8.3,1.3,'高温：\nΔG小的→热力学产物\n=1,4-加成为主',ha='center',fontsize=9,color='#C62828',fontweight='bold')
save(fig,'ch6_kinetic_thermodynamic.png')

# Kucherov reaction (alkyne hydration)
fig, ax = plt.subplots(figsize=(11,4.5))
ax.axis('off'); ax.set_xlim(0,11); ax.set_ylim(0,4.5)
ax.set_title('炔烃水合反应（库切洛夫反应）——互变异构是关键', fontsize=13, fontweight='bold')

# Terminal alkyne
ax.text(0.5,4.0,'①端炔水合（HgSO₄/H₂SO₄/H₂O）：',fontsize=10,fontweight='bold',color='#1565C0')
ax.text(0.5,3.4,'RC≡CH  →[H₂O/Hg²⁺]→ RC(OH)=CH₂ → RC(=O)-CH₃',fontsize=10,family='monospace',color='#1565C0')
ax.text(5.0,2.9,'烯醇  →互变异构→  甲基酮',fontsize=9,ha='center',style='italic',color='gray')
ax.text(5.0,2.4,'（Markovnikov：OH加到含H少的碳）',fontsize=9.5,ha='center',color='green')

ax.axhline(2.0,color='gray',lw=1,ls='--',xmin=0.03,xmax=0.97)

# Acetylene special case
ax.text(0.5,1.6,'②乙炔水合（特殊）：',fontsize=10,fontweight='bold',color='#C62828')
ax.text(0.5,1.1,'HC≡CH  →[H₂O/Hg²⁺]→ CH₂=CHOH → CH₃CHO',fontsize=10,family='monospace',color='#C62828')
ax.text(5.0,0.65,'乙烯醇(vinyl alcohol) → 乙醛',fontsize=9,ha='center',style='italic',color='gray')
ax.text(5.0,0.2,'乙炔→乙醛（不是酮！因为Markovnikov这里两端对称）',fontsize=9.5,ha='center',color='red',fontweight='bold')
save(fig,'ch6_kucherov.png')

# ════════════════════════════════════════════════════════════
# CH7 — Aromatics
# ════════════════════════════════════════════════════════════
print('\n=== CH7 ===')

# Hückel rule
fig, ax = plt.subplots(figsize=(12,5))
ax.axis('off'); ax.set_xlim(0,12); ax.set_ylim(0,5)
ax.set_title('Hückel规则与芳香性判断（4n+2 π电子）', fontsize=14, fontweight='bold')

huckel_data = [
    (1.2, 4.0, '苯 C₆H₆', 'n=1, 6π', '芳香\n(平面,环形共轭)', '#4CAF50', '✓'),
    (3.5, 4.0, '萘 C₁₀H₈', 'n=2, 10π', '芳香\n(稠环)', '#4CAF50', '✓'),
    (5.8, 4.0, '环戊二烯阴离子\nC₅H₅⁻', 'n=1, 6π', '芳香！\n(加H⁺pKa~15)', '#4CAF50', '✓'),
    (8.1, 4.0, '环庚三烯阳离子\nC₇H₇⁺(卓鎓)', 'n=1, 6π', '芳香！\n(特别稳定)', '#4CAF50', '✓'),
    (10.4,4.0, '吡啶 C₅H₅N', 'n=1, 6π\n(N提供1对孤电子)', '芳香\n(弱碱)', '#4CAF50', '✓'),
    (1.2, 1.8, '环丁二烯\nC₄H₄', 'n=1, 4π', '反芳香！\n(不稳定)', '#F44336', '✗'),
    (3.5, 1.8, '环辛四烯\nC₈H₈', '8π e⁻\n(4n,n=2)', '非芳香\n(盆形,非平面)', '#FF9800', '△'),
    (5.8, 1.8, '吡咯 C₄H₄NH', 'n=1, 6π\n(N孤对加入)', '芳香！\n(pKa~17,弱酸)', '#4CAF50', '✓'),
    (8.1, 1.8, '呋喃 C₄H₄O', 'n=1, 6π\n(O孤对1对加入)', '芳香\n(弱)', '#4CAF50', '✓'),
    (10.4,1.8, '噻吩 C₄H₄S', 'n=1, 6π\n(S孤对)', '芳香\n(较好)', '#4CAF50', '✓'),
]
for x,y,name,pi,result,col,mark in huckel_data:
    r=mpatches.FancyBboxPatch((x-0.9,y-0.7),1.8,2.1,boxstyle='round,pad=0.08',
        facecolor=col,alpha=0.12,edgecolor=col,lw=1.5)
    ax.add_patch(r)
    ax.text(x,y+1.15,mark,ha='center',fontsize=14,color=col,fontweight='bold')
    ax.text(x,y+0.6,name,ha='center',fontsize=8.5,fontweight='bold')
    ax.text(x,y+0.0,pi,ha='center',fontsize=8)
    ax.text(x,y-0.5,result,ha='center',fontsize=8,color=col,fontweight='bold')

ax.text(6,0.4,'芳香性必要条件：①平面 ②环状 ③全共轭 ④4n+2个π电子',
    ha='center',fontsize=11,style='italic',color='purple',
    bbox=dict(facecolor='lightyellow',boxstyle='round'))
save(fig,'ch7_huckel_rule.png')

# EAS directing groups
fig, ax = plt.subplots(figsize=(13,6))
ax.axis('off'); ax.set_xlim(0,13); ax.set_ylim(0,6)
ax.set_title('苯环亲电取代：定位效应总结（最重要考点！）', fontsize=14, fontweight='bold')

# ortho/para directors
b1=mpatches.FancyBboxPatch((0.2,1.0),5.8,4.5,boxstyle='round,pad=0.1',
    facecolor='#E8F5E9',edgecolor='#2E7D32',lw=2)
ax.add_patch(b1)
ax.text(3.1,5.2,'邻/对位定向基（活化/钝化）',fontsize=11,fontweight='bold',ha='center',color='#2E7D32')
ax.text(3.1,4.7,'—OH, —OR（强活化）',fontsize=9.5,ha='center')
ax.text(3.1,4.3,'—NH₂, —NHR, —NR₂（强活化）',fontsize=9.5,ha='center')
ax.text(3.1,3.9,'—CH₃, —R（弱活化）',fontsize=9.5,ha='center')
ax.text(3.1,3.5,'—Ph（弱活化）',fontsize=9.5,ha='center')
ax.text(3.1,2.9,'—F, —Cl, —Br, —I（钝化！但定邻/对位）',fontsize=9.5,ha='center',color='#C62828',fontweight='bold')
ax.text(3.1,2.4,'← 卤素：+C(共振给电)但-I(诱导吸电)，净效果钝化',fontsize=8.5,ha='center',style='italic')
ax.text(3.1,1.7,'机理：孤对电子共振\n推电子→σ络合物在邻/对位更稳定',fontsize=9,ha='center',color='green')

# meta directors
b2=mpatches.FancyBboxPatch((7.0,1.0),5.8,4.5,boxstyle='round,pad=0.1',
    facecolor='#FFEBEE',edgecolor='#C62828',lw=2)
ax.add_patch(b2)
ax.text(9.9,5.2,'间位定向基（钝化）',fontsize=11,fontweight='bold',ha='center',color='#C62828')
ax.text(9.9,4.7,'—NO₂（强钝化）',fontsize=9.5,ha='center')
ax.text(9.9,4.3,'—CN（强钝化）',fontsize=9.5,ha='center')
ax.text(9.9,3.9,'—COOH, —COOR（钝化）',fontsize=9.5,ha='center')
ax.text(9.9,3.5,'—CHO, —COR（钝化）',fontsize=9.5,ha='center')
ax.text(9.9,3.1,'—SO₃H（钝化）',fontsize=9.5,ha='center')
ax.text(9.9,2.7,'—CF₃, —CCl₃（钝化）',fontsize=9.5,ha='center')
ax.text(9.9,2.1,'机理：吸电子基→苯环缺电子\n邻/对位尤其缺电子→E⁺只能攻间位',fontsize=9,ha='center',color='#C62828')

ax.text(6.5,0.4,'⚠ 卤素：钝化但定邻/对位！(例外，务必记住)',
    ha='center',fontsize=11,color='red',fontweight='bold',
    bbox=dict(facecolor='#FFCDD2',boxstyle='round'))
save(fig,'ch7_directing_effects.png')

# Five EAS reactions
fig, ax = plt.subplots(figsize=(13,6))
ax.axis('off'); ax.set_xlim(0,13); ax.set_ylim(0,6)
ax.set_title('苯的五大亲电取代反应（EAS）', fontsize=14, fontweight='bold')

eas_reactions = [
    (1.3,4.8,'卤化','ArH + Cl₂/Br₂\n→(FeCl₃/FeBr₃)\nArX + HX',
     '亲电试剂: Cl⁺(ClFeCl₃⁻)\n路易斯酸活化卤素\n不需要光（区别于自由基）','#1565C0'),
    (4.0,4.8,'硝化','ArH + HNO₃\n→(浓H₂SO₄)\nArNO₂ + H₂O',
     '亲电试剂: NO₂⁺(硝酰离子)\nH₂SO₄质子化HNO₃\n温度控制多取代','#C62828'),
    (6.7,4.8,'磺化','ArH + H₂SO₄(发烟)\n→ ArSO₃H',
     '亲电试剂: SO₃\n可逆反应！\n稀H₂SO₄高温→去磺化','#2E7D32'),
    (9.4,4.8,'Friedel-Crafts烷基化',
     'ArH + RX → (AlCl₃)\nAr-R + HX',
     '亲电试剂: R⁺(碳正离子)\n可发生重排！\n多烷基化问题','#9C27B0'),
    (11.8,4.8,'Friedel-Crafts酰基化',
     'ArH + RCOCl → (AlCl₃)\nAr-COR + HCl',
     '亲电试剂: RC=O⁺(酰基离子)\n不发生重排\n产物钝化不多酰化','#FF5722'),
]
for x,y,name,equation,detail,col in eas_reactions:
    r=mpatches.FancyBboxPatch((x-1.1,y-2.0),2.2,3.2,boxstyle='round,pad=0.08',
        facecolor=col,alpha=0.1,edgecolor=col,lw=2)
    ax.add_patch(r)
    ax.text(x,y+0.95,name,ha='center',fontsize=9.5,fontweight='bold',color=col)
    ax.text(x,y+0.1,equation,ha='center',fontsize=8,family='monospace')
    ax.text(x,y-1.3,detail,ha='center',fontsize=7.5,color='gray',style='italic')

ax.text(6.5,0.4,'通用机理：ArH + E⁺ → σ络合物(arenium ion) → -H⁺ → ArE',
    ha='center',fontsize=10,style='italic',color='purple',
    bbox=dict(facecolor='lightyellow',boxstyle='round'))
save(fig,'ch7_five_eas.png')

# Naphthalene chemistry
fig, ax = plt.subplots(figsize=(11,5))
ax.axis('off'); ax.set_xlim(0,11); ax.set_ylim(0,5)
ax.set_title('萘的化学性质——α/β位选择性', fontsize=14, fontweight='bold')

ax.text(5.5,4.6,'萘的两种位置：α位(1,4,5,8)  β位(2,3,6,7)',ha='center',fontsize=11,fontweight='bold')
ax.text(5.5,4.1,'EAS反应优先α位（σ络合物更稳定，保留一个完整苯环）',ha='center',fontsize=10,color='#1565C0')

# Reactions table
reactions = [
    ('卤化','低温，α取代\nα-氯萘/溴萘','#1565C0'),
    ('硝化','HNO₃/H₂SO₄\n主要α-硝基萘','#C62828'),
    ('磺化','低温→α-磺酸\n高温→β-磺酸\n(热力学控制)','#2E7D32'),
    ('加氢','Ni催化，选择性加一环\n→四氢萘（1,2,3,4）','#9C27B0'),
    ('氧化','KMnO₄→邻苯二甲酸\nCrO₃→α-萘醌','#FF5722'),
]
for i,(name,detail,col) in enumerate(reactions):
    x=i*2.1+0.8; y=2.5
    r=mpatches.FancyBboxPatch((x-0.7,y-1.0),1.8,2.2,boxstyle='round,pad=0.08',
        facecolor=col,alpha=0.12,edgecolor=col,lw=1.5)
    ax.add_patch(r)
    ax.text(x+0.2,y+0.95,name,ha='center',fontsize=9.5,fontweight='bold',color=col)
    ax.text(x+0.2,y+0.0,detail,ha='center',fontsize=8.5,color='black')

ax.text(5.5,0.3,'记忆：磺化温度控制不同位置是经典考点！\n低温=动力学α位；高温=热力学β位',
    ha='center',fontsize=10,style='italic',color='gray',
    bbox=dict(facecolor='lightyellow',boxstyle='round'))
save(fig,'ch7_naphthalene.png')

# Side chain reactions of aromatics
fig, ax = plt.subplots(figsize=(11,5))
ax.axis('off'); ax.set_xlim(0,11); ax.set_ylim(0,5)
ax.set_title('芳烃侧链反应（与环上反应的区别）', fontsize=13, fontweight='bold')

reactions_sc = [
    (1.8,3.8,'苄位卤代\n(自由基条件)',
     '甲苯 + Br₂ → (hν)\n苄基溴 + HBr\nNBS也可做苄位溴代',
     '苄基自由基共振稳定\n→高选择性','#1565C0'),
    (5.5,3.8,'侧链氧化\n(KMnO₄)',
     '有α-H的侧链\n→被氧化为苯甲酸\n无论链多长都→COOH',
     '无α-H的叔丁苯\n→不被氧化！\n用于结构鉴定','#C62828'),
    (9.2,3.8,'芳烃燃烧\n与工业用途',
     '苯→苯甲酸\n甲苯→TDI（聚氨酯原料）\n苯乙烯→聚苯乙烯',
     '侧链越长\n氧化越难\n酮基不被氧化','#2E7D32'),
]
for x,y,name,detail,note,col in reactions_sc:
    r=mpatches.FancyBboxPatch((x-1.4,y-1.5),2.8,2.8,boxstyle='round,pad=0.08',
        facecolor=col,alpha=0.12,edgecolor=col,lw=2)
    ax.add_patch(r)
    ax.text(x,y+1.05,name,ha='center',fontsize=10,fontweight='bold',color=col)
    ax.text(x,y+0.1,detail,ha='center',fontsize=8.5,family='monospace')
    ax.text(x,y-0.85,note,ha='center',fontsize=8.5,color='gray',style='italic')

ax.text(5.5,1.0,'区分：环上反应需Lewis酸（FeBr₃等）\n侧链卤代需光照（自由基）',
    ha='center',fontsize=10,color='purple',
    bbox=dict(facecolor='#f3e5f5',boxstyle='round'))
ax.text(5.5,0.25,'苯甲酸 pKa≈4.2，比乙酸(4.75)稍强（苯环吸电子）',
    ha='center',fontsize=9,color='gray',style='italic')
save(fig,'ch7_side_chain.png')

# ════════════════════════════════════════════════════════════
# CH9 — Haloalkanes
# ════════════════════════════════════════════════════════════
print('\n=== CH9 ===')

# SN1 vs SN2 full comparison
fig, ax = plt.subplots(figsize=(13,6))
ax.axis('off'); ax.set_xlim(0,13); ax.set_ylim(0,6)
ax.set_title('SN1 vs SN2 全面对比（核心考点）', fontsize=14, fontweight='bold')

headers2 = ['对比项目','SN2（双分子）','SN1（单分子）']
rows_data = [
    ('底物',    '甲基>1°>2°（3°几乎不反应）','3°>>2°>>1°（甲基不反应）'),
    ('反应速率', 'r=k[RX][Nu]\n二级反应','r=k[RX]\n一级反应，与Nu无关'),
    ('亲核试剂', '强亲核试剂\n(HS⁻,I⁻,CN⁻,RO⁻)','弱亲核试剂也可\n(H₂O,ROH)'),
    ('立体化学', 'Walden翻转\n构型完全反转','外消旋化\n(两面进攻，略偏一侧)'),
    ('溶剂',    '极性非质子(DMF,DMSO,丙酮)\n增大亲核性','极性质子(H₂O,ROH)\n稳定碳正离子'),
    ('中间体',  '无！五配位过渡态','碳正离子！\n可发生重排'),
    ('离去基团', '好离去基团促进\nI>Br>Cl>F','好离去基团促进\nI>Br>Cl>F'),
]
header_y = 5.6
row_height = 0.7
col_xs = [0.5,4.5,9.0]
col_ws = [3.8,4.3,3.8]
# Header
for h,x,w in zip(headers2,col_xs,col_ws):
    r=mpatches.FancyBboxPatch((x-0.1,header_y-0.3),w,0.5,boxstyle='round,pad=0.05',
        facecolor='#1565C0',edgecolor='#1565C0')
    ax.add_patch(r)
    ax.text(x+w/2-0.1,header_y,h,ha='center',va='center',fontsize=9.5,color='white',fontweight='bold')
for i,(item,sn2,sn1) in enumerate(rows_data):
    y = header_y - (i+1)*row_height
    bg = '#F5F5F5' if i%2==0 else 'white'
    for j,(text,x,w) in enumerate(zip([item,sn2,sn1],col_xs,col_ws)):
        r=mpatches.FancyBboxPatch((x-0.1,y-row_height/2+0.05),w,row_height-0.1,
            boxstyle='round,pad=0.03',facecolor=bg,edgecolor='#BDBDBD',lw=0.5)
        ax.add_patch(r)
        col_text = '#1565C0' if j==1 else ('#C62828' if j==2 else 'black')
        ax.text(x+w/2-0.1,y,text,ha='center',va='center',fontsize=8,color=col_text)
save(fig,'ch9_sn1_sn2_compare.png')

# Four-way competition
fig, ax = plt.subplots(figsize=(12,6))
ax.axis('off'); ax.set_xlim(0,12); ax.set_ylim(0,6)
ax.set_title('SN1/SN2/E1/E2 四大竞争反应判断（最核心考点！）', fontsize=14, fontweight='bold')

ax.text(6,5.5,'判断逻辑树',ha='center',fontsize=11,fontweight='bold',color='purple')
# Decision tree
conditions = [
    (6,5.0,'底物结构？',None,None,'purple'),
    (2,4.2,'甲基/1°',6,5.0,'#1565C0'),
    (6,4.2,'2°',6,5.0,'#2E7D32'),
    (10,4.2,'3°',6,5.0,'#C62828'),
]
# 1° path
ax.text(0.8,3.5,'强Nu/弱碱\n→SN2为主',ha='center',fontsize=9.5,
    bbox=dict(facecolor='#E3F2FD',boxstyle='round',edgecolor='#1565C0'))
ax.text(3.2,3.5,'强碱/高温\n→E2为主',ha='center',fontsize=9.5,
    bbox=dict(facecolor='#E8F5E9',boxstyle='round',edgecolor='#2E7D32'))
# 2° path
ax.text(6,3.5,'强Nu极性非质子→SN2\n强碱→E2\n弱Nu质子溶剂→SN1/E1混合',ha='center',fontsize=9,
    bbox=dict(facecolor='#FFF9C4',boxstyle='round',edgecolor='#F57F17'))
# 3° path
ax.text(9.5,3.5,'强碱/高温→E2\n弱碱质子溶剂→SN1+E1\n(E2通常>SN1)',ha='center',fontsize=9,
    bbox=dict(facecolor='#FFEBEE',boxstyle='round',edgecolor='#C62828'))

# Summary rules
rules_table = [
    ('温度↑', '有利于消除(E)','有利于取代(S)时温度低'),
    ('碱性强', '有利于E2','弱亲核试剂利于SN1'),
    ('位阻大', '有利于E2','强Nu+无位阻→SN2'),
    ('极性非质子溶剂','增强Nu，利于SN2','质子溶剂稳定碳正离子→SN1'),
]
ax.text(1,2.3,'关键规律：',fontsize=10,fontweight='bold',color='black')
for i,(factor,fav,note) in enumerate(rules_table):
    y = 1.9 - i*0.45
    ax.text(1.2,y,f'• {factor} → {fav}',fontsize=8.5,color='black')
    ax.text(7.5,y,f'→ {note}',fontsize=8.5,color='gray',style='italic')

save(fig,'ch9_four_competition.png')

# Grignard reactions
fig, ax = plt.subplots(figsize=(12,5.5))
ax.axis('off'); ax.set_xlim(0,12); ax.set_ylim(0,5.5)
ax.set_title('Grignard试剂（RMgX）的制备与反应', fontsize=14, fontweight='bold')

# Preparation
ax.text(0.5,5.0,'【制备】RX + Mg → (乙醚) → RMgX',fontsize=11,family='monospace',fontweight='bold')
ax.text(0.5,4.5,'活性顺序: RI > RBr > RCl > RF',fontsize=10,color='gray',style='italic')
ax.text(0.5,4.0,'⚠ 无水！无CO₂！避免水和质子性物质',fontsize=10,color='red',fontweight='bold')

# Reactions
grignard_rxns = [
    (1.5,2.8,'+ 甲醛 (HCHO)','→ 伯醇 (RCH₂OH)','#1565C0'),
    (1.5,2.1,'+ 醛 (RCHO)','→ 仲醇 (RCHOHR\')\n增加一个碳','#2196F3'),
    (1.5,1.4,'+ 酮 (R\'COR\'\')',  '→ 叔醇 (R\'R\'\'COHR)\n增加一个碳','#42A5F5'),
    (6.5,2.8,'+ CO₂','→ (RCOOMgX) → H₃O⁺ → RCOOH\n增加一个碳→羧酸','#C62828'),
    (6.5,2.1,'+ 环氧乙烷','→ RCH₂CH₂OH\n增加两个碳','#E53935'),
    (6.5,1.4,'+ H₂O/醇/酸\n(含活泼H)',  '→ R-H\n(烃)\n破坏Grignard！','#FF9800'),
]
for x,y,reag,prod,col in grignard_rxns:
    r=mpatches.FancyBboxPatch((x-0.3,y-0.3),4.8,0.55,boxstyle='round,pad=0.05',
        facecolor=col,alpha=0.1,edgecolor=col,lw=1)
    ax.add_patch(r)
    ax.text(x,y+0.1,f'RMgX {reag}',fontsize=8.5,family='monospace',color=col)
    ax.text(x+4.5,y+0.1,prod,fontsize=8.5,color='black')

ax.text(6,0.5,'Grignard是构建C-C键的最重要方法之一！设计合成时优先考虑',
    ha='center',fontsize=10,color='purple',style='italic',
    bbox=dict(facecolor='lightyellow',boxstyle='round'))
save(fig,'ch9_grignard_reactions.png')

# Diels-Alder reaction example
fig, ax = plt.subplots(figsize=(10,5))
ax.axis('off'); ax.set_xlim(0,10); ax.set_ylim(0,5)
ax.set_title('Diels-Alder反应详解——endo规则与区域化学', fontsize=14, fontweight='bold')

ax.text(5,4.5,'【endo规则】过渡态中，亲二烯体取代基与二烯体互相靠近（"内向"）',
    ha='center',fontsize=10,color='#1565C0',fontweight='bold')
ax.text(5,4.0,'→ endo产物动力学优先（次级轨道相互作用稳定）',ha='center',fontsize=9.5,color='#1565C0')
ax.text(5,3.5,'→ exo产物更稳定（热力学），但通常动力学控制',ha='center',fontsize=9.5)

ax.text(5,3.0,'【区域化学】不对称取代时，遵循"邻位"或"对位"规则',
    ha='center',fontsize=10,color='#C62828',fontweight='bold')
ax.text(5,2.5,'二烯体1位取代+亲二烯体：1,2-产物（邻）or 1,4产物（对）？',ha='center',fontsize=9.5)

ax.text(5,1.9,'【立体化学】',ha='center',fontsize=10,fontweight='bold',color='#2E7D32')
ax.text(5,1.4,'协同反应（一步）→ 顺式加成（syn）\n亲二烯体上的取代基关系在产物中保留',ha='center',fontsize=9.5,color='#2E7D32')

ax.text(5,0.6,'【活性要求】\n二烯体：必须s-cis构象 + 富电子（供电子基）更活泼\n亲二烯体：缺电子（吸电子基EWG：CHO,NO₂,CN,C=O）更活泼',
    ha='center',fontsize=9,style='italic',color='gray',
    bbox=dict(facecolor='lightyellow',boxstyle='round'))
save(fig,'da_reaction_example.png')

print('\n✅ All images generated!')
