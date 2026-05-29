"""Mechanism renderer for ch11 醛和酮 of the 有机化学复习站.

Writes PNG+SVG step images into 复习全站/img/ as ch11_*.{png,svg}.
Mirrors the helper pattern of _render_mechanisms.py.

Run:  python _render_ch11.py
"""
from __future__ import annotations

import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, r"C:\Users\FXY\.claude\skills\organic-render")
from render import render_reaction, render_molecule  # noqa: E402

HERE = Path(__file__).resolve().parent
IMG = HERE / "img"
IMG.mkdir(exist_ok=True)

_SUB = str.maketrans({
    "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4",
    "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9",
    "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4",
    "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9",
    "⁺": "+", "⁻": "-",
})


def _clean(label: str) -> str:
    return label.translate(_SUB)


N_OK = 0
N_ERR = 0


def step(name: str, before: str, after: str, label: str, size=(900, 240)) -> None:
    global N_OK, N_ERR
    out = IMG / f"{name}.png"
    try:
        render_reaction(f"{before}>>{after}", out, size=size, reagent=_clean(label))
        print(f"  OK  {name}")
        N_OK += 1
    except Exception as e:
        print(f"  ERR {name}: {e}")
        N_ERR += 1


def mol(name: str, smiles: str, legend: str = "", size=(380, 240)) -> None:
    global N_OK, N_ERR
    out = IMG / f"{name}.png"
    try:
        render_molecule(smiles, out, size=size, legend=_clean(legend))
        print(f"  OK  {name}")
        N_OK += 1
    except Exception as e:
        print(f"  ERR {name}: {e}")
        N_ERR += 1


# ============================================================
# ch11  醛和酮
# ============================================================

def reactivity_order() -> None:
    """亲核加成活性 HCHO > RCHO > R2CO."""
    print("[ch11] 羰基亲核加成活性序")
    mol("ch11_react_hcho", "C=O", "甲醛 HCHO: 无烷基, 羰基碳最缺电子, 位阻最小 → 最活泼")
    mol("ch11_react_rcho", "CC=O", "乙醛 RCHO: 1 个烷基供电 + 位阻 → 居中")
    mol("ch11_react_r2co", "CC(C)=O", "丙酮 R₂CO: 2 个烷基供电 + 位阻大 → 较钝")


def hcn_addition() -> None:
    """HCN 亲核加成 → α-羟基腈 (氰醇)."""
    print("[ch11] HCN 亲核加成")
    # 丙酮 + HCN → 2-羟基-2-甲基丙腈 (丙酮氰醇)
    keto = "CC(C)=O"
    alkoxide = "CC(C)([O-])C#N"   # 加成后烷氧负离子
    prod = "CC(O)(C#N)C"          # 质子化得氰醇
    step("ch11_hcn_s1", keto, alkoxide,
         "Step 1: CN⁻ 亲核进攻羰基碳 → 四面体烷氧负离子 (决速)")
    step("ch11_hcn_s2", alkoxide, prod,
         "Step 2: 烷氧负离子被 HCN/H⁺ 质子化 → α-羟基腈 (氰醇, +1C)")


def bisulfite_addition() -> None:
    """NaHSO3 加成 → α-羟基磺酸钠 (白色结晶, 鉴别)."""
    print("[ch11] NaHSO₃ 加成")
    # 乙醛 + NaHSO3 → 1-羟基乙磺酸钠
    ald = "CC=O"
    prod = "CC(O)S(=O)(=O)[O-]"
    step("ch11_bisulfite", ald, prod,
         "醛/甲基酮 + NaHSO₃: 亲核 S 进攻羰基碳 → α-羟基磺酸钠 (白色结晶析出, 鉴别)")


def acetal_formation() -> None:
    """缩醛形成 (酸催化): 半缩醛 → 缩醛, 4 步."""
    print("[ch11] 缩醛形成")
    # 乙醛 + 2 CH3OH (干 HCl) → 半缩醛 → 缩醛
    ald = "CC=O"
    prot = "CC=[OH+]"                 # 羰基质子化
    hemi = "CC(O)OC"                  # 半缩醛
    oxocarb = "CC=[O+]C"             # 氧鎓离子 (失水后)
    acetal = "CC(OC)OC"             # 缩醛
    step("ch11_acetal_s1", ald, prot,
         "Step 1: H⁺ 质子化羰基 O → 活化羰基碳")
    step("ch11_acetal_s2", prot, hemi,
         "Step 2: 第 1 分子 ROH 的 O 进攻碳 + 失 H⁺ → 半缩醛 (hemiacetal)")
    step("ch11_acetal_s3", hemi, oxocarb,
         "Step 3: 半缩醛 OH 质子化脱 H₂O → 氧鎓离子 (共振稳定)")
    step("ch11_acetal_s4", oxocarb, acetal,
         "Step 4: 第 2 分子 ROH 进攻氧鎓 + 失 H⁺ → 缩醛 (acetal, 保护羰基)")


def aldol_dilute() -> None:
    """羟醛缩合 (稀碱低温): 烯醇负离子加成 → β-羟基醛, 3 步."""
    print("[ch11] 羟醛缩合 稀碱")
    # 2 乙醛 → 3-羟基丁醛
    ald = "CC=O"
    enolate = "[CH2-]C=O"            # 烯醇负离子 (碳负)
    enolate_o = "C=C[O-]"           # 共振 O 负
    aldol_alk = "CC([O-])CC=O"     # 加成后 β-烷氧负离子
    aldol = "CC(O)CC=O"            # 3-羟基丁醛
    step("ch11_aldol_s1", ald, enolate,
         "Step 1: 稀 OH⁻ 拔 α-H → 烯醇负离子 (碳负离子, 被羰基共振稳定)")
    step("ch11_aldol_s2", enolate, enolate_o,
         "共振: 负电分到 O 上 (C=C–O⁻, 更稳); 亲核位仍在 α-碳")
    step("ch11_aldol_s3", f"{enolate}.{ald}", aldol_alk,
         "Step 2: α-碳进攻另一分子羰基碳 → β-烷氧负离子")
    step("ch11_aldol_s4", aldol_alk, aldol,
         "Step 3: 质子化 → β-羟基丁醛 (3-羟基丁醛, 稀碱低温停在此)")


def aldol_conc() -> None:
    """羟醛缩合 (浓碱加热): β-羟基醛脱水 → α,β-不饱和醛."""
    print("[ch11] 羟醛缩合 浓碱脱水")
    aldol = "CC(O)CC=O"            # 3-羟基丁醛
    enal = "CC=CC=O"              # 2-丁烯醛 (巴豆醛)
    step("ch11_aldol_dehydrate", aldol, enal,
         "浓碱/Δ: β-羟基醛 E1cb 脱水 (拔 α-H → 赶 β-OH⁻) → 2-丁烯醛 (α,β-不饱和, C=C 与 C=O 共轭更稳)")


def aldol_crossed() -> None:
    """交叉羟醛: 苯甲醛(无 α-H) + 乙醛 → 肉桂醛."""
    print("[ch11] 交叉羟醛")
    # PhCHO + CH3CHO → 肉桂醛 PhCH=CH-CHO
    step("ch11_aldol_crossed", "O=Cc1ccccc1.CC=O", "O=C/C=C/c1ccccc1",
         "交叉羟醛: 苯甲醛无 α-H 只当亲电体, 乙醛供烯醇负离子 → 肉桂醛 PhCH=CH–CHO",
         size=(950, 240))


def cannizzaro() -> None:
    """Cannizzaro: 无 α-H 醛 + 浓碱 → 歧化 (醇 + 羧酸盐)."""
    print("[ch11] Cannizzaro")
    # 苯甲醛
    ald = "O=Cc1ccccc1"
    tetra = "[O-]C(O)c1ccccc1"     # OH⁻ 加成的四面体中间体
    # 歧化结果
    step("ch11_cannizzaro_s1", f"{ald}.[OH-]", tetra,
         "Step 1: OH⁻ 进攻一分子醛羰基 → 四面体烷氧负离子中间体")
    step("ch11_cannizzaro_s2", f"{tetra}.{ald}",
         "OCc1ccccc1.[O-]C(=O)c1ccccc1",
         "Step 2: 中间体 C–H 以 H⁻ 转移给另一分子醛 → 苯甲醇 + 苯甲酸根 (歧化)",
         size=(960, 240))


def haloform() -> None:
    """碘仿反应: 甲基酮 + 3 I2/NaOH → CHI3↓ + 羧酸盐, 3 步."""
    print("[ch11] 碘仿/卤仿")
    # 丙酮 → 三碘代丙酮 → 裂解
    keto = "CC(C)=O"
    tri = "O=C(C)C(I)(I)I"        # CH3 端三碘代 (1,1,1-三碘丙酮)
    cleave = "CC(=O)[O-].C(I)(I)I"  # 乙酸根 + 碘仿
    step("ch11_haloform_s1", keto, tri,
         "Step 1: 碱拔 α-H → 烯醇负离子, I₂ 逐个碘代甲基 → 三碘甲基酮 (–CI₃ 吸电子, 越代越快)")
    step("ch11_haloform_s2", tri, cleave,
         "Step 2: OH⁻ 进攻羰基碳, CI₃⁻ 离去 (稳定碳负) → 羧酸根 + CHI₃↓ 黄色沉淀",
         size=(960, 240))


def nabh4_reduction() -> None:
    """NaBH4 还原醛酮 → 醇 (不动酸酯)."""
    print("[ch11] NaBH₄ 还原")
    # 丁酮 → 2-丁醇
    step("ch11_nabh4", "CCC(C)=O", "CCC(O)C",
         "NaBH₄: H⁻ 进攻羰基碳 → 烷氧负离子, 后处理质子化 → 醇 (温和, 只还原醛酮, 不动 –COOH/–COOR)")


def lialh4_reduction() -> None:
    """LiAlH4 还原 酸/酯/醛酮 → 醇 (强)."""
    print("[ch11] LiAlH₄ 还原")
    step("ch11_lialh4", "CCC(=O)O", "CCCO",
         "LiAlH₄: 强还原剂, 把羧酸/酯/醛酮统统还原成醇 (丙酸 → 丙-1-醇); 遇水剧烈, 须无水醚")


def clemmensen() -> None:
    """Clemmensen: C=O → CH2 (Zn-Hg/浓HCl, 耐酸底物)."""
    print("[ch11] Clemmensen 还原")
    # 苯乙酮 → 乙苯
    step("ch11_clemmensen", "CC(=O)c1ccccc1", "CCc1ccccc1",
         "Clemmensen (Zn-Hg / 浓 HCl, Δ): 羰基 C=O 还原成 CH₂ (苯乙酮 → 乙苯); 用于耐酸不耐碱底物")


def wolff_kishner() -> None:
    """Wolff-Kishner: C=O → CH2 (NH2NH2/KOH/Δ, 耐碱底物)."""
    print("[ch11] Wolff-Kishner 还原")
    # 苯乙酮 → 乙苯 (经腙)
    keto = "CC(=O)c1ccccc1"
    hydrazone = "CC(=NN)c1ccccc1"
    prod = "CCc1ccccc1"
    step("ch11_wk_s1", keto, hydrazone,
         "Step 1: 酮 + H₂N–NH₂ → 腙 (hydrazone, C=N–NH₂)")
    step("ch11_wk_s2", hydrazone, prod,
         "Step 2: KOH / Δ (高沸醇) 放 N₂ → CH₂ (苯乙酮 → 乙苯); 用于耐碱不耐酸底物")


def wittig() -> None:
    """Wittig: 叶立德 + 羰基 → 烯, 经氧磷杂四元环."""
    print("[ch11] Wittig")
    # Ph3P=CH2 + 苯甲醛 → 苯乙烯
    ylide = "C=[P](c1ccccc1)(c1ccccc1)c1ccccc1"   # 亚甲基三苯基膦叶立德
    ald = "O=Cc1ccccc1"
    betaine = "[O-]C(c1ccccc1)C[P+](c1ccccc1)(c1ccccc1)c1ccccc1"  # 内鎓盐/甜菜碱
    step("ch11_wittig_s1", f"{ylide}.{ald}", betaine,
         "Step 1: 叶立德碳负进攻醛羰基碳 → 内鎓盐/氧磷四元环中间体 (betaine → oxaphosphetane)",
         size=(980, 240))
    step("ch11_wittig_s2", betaine, "C(=Cc1ccccc1)[H].O=P(c1ccccc1)(c1ccccc1)c1ccccc1",
         "Step 2: 四元环顺向裂解 → 烯 (苯乙烯) + 三苯氧膦 Ph₃P=O (定向成 C=C, 位置确定)",
         size=(980, 240))
    mol("ch11_wittig_ylide", "[CH2-][P+](c1ccccc1)(c1ccccc1)c1ccccc1",
        "叶立德 (ylide): Ph₃P⁺–CH₂⁻, 由 Ph₃P + RCH₂X → 鏻盐, 再强碱拔 α-H 生成")


def imine_oxime() -> None:
    """与含氮亲核体: 肟/腙/缩氨脲 (鉴别衍生物)."""
    print("[ch11] 与 N-亲核体 (肟/腙)")
    # 丙酮 + 羟胺 → 丙酮肟
    step("ch11_oxime", "CC(C)=O", "CC(C)=NO",
         "丙酮 + NH₂OH (羟胺) → 丙酮肟 C=N–OH (脱水); 2,4-DNP 同理给黄色腙沉淀, 鉴别羰基")
    step("ch11_dnp", "CC(C)=O", "CC(C)=NNc1ccc([N+](=O)[O-])cc1[N+](=O)[O-]",
         "醛酮 + 2,4-二硝基苯肼 (2,4-DNP) → 黄/橙红 2,4-二硝基苯腙↓ (验羰基存在)",
         size=(960, 240))


def mannich() -> None:
    """Mannich: 烯醇 + 亚胺离子 → β-氨基酮."""
    print("[ch11] Mannich")
    # 丙酮 + HCHO + 二甲胺 → 1-(二甲氨基)-3-丁酮  (Mannich 碱)
    iminium = "C=[N+](C)C"          # 亚甲基亚胺离子 (HCHO + HN(CH3)2)
    step("ch11_mannich_s1", "C=O.CNC", iminium,
         "Step 1: 甲醛 + 仲胺 (二甲胺) → 亚胺离子 CH₂=N⁺(CH₃)₂ (亲电体)")
    step("ch11_mannich_s2", f"CC(C)=O.{iminium}", "CC(=O)CCN(C)C",
         "Step 2: 酮的烯醇 α-碳进攻亚胺离子 → β-氨基酮 (Mannich 碱)",
         size=(960, 240))


def stork_enamine() -> None:
    """Stork 烯胺: 酮 + 仲胺 → 烯胺, 烷基化/酰基化 α-碳."""
    print("[ch11] Stork 烯胺")
    # 环己酮 + 吡咯烷 → 烯胺
    keto = "O=C1CCCCC1"
    enamine = "C1(=CCCCC1)N1CCCC1"  # 1-(1-环己烯基)吡咯烷
    step("ch11_enamine_s1", f"{keto}.C1CCNC1", enamine,
         "Step 1: 环己酮 + 仲胺 (吡咯烷) 脱水 → 烯胺 (enamine, C=C–N, α-碳带亲核性)",
         size=(960, 240))
    step("ch11_enamine_s2", enamine, "O=C1CCCCC1CC=C",
         "Step 2: 烯胺 α-碳进攻 R–X (如烯丙基溴) 烷基化, 水解还原羰基 → α-烷基环己酮",
         size=(960, 240))


def tollens_fehling() -> None:
    """氧化鉴别: Tollens 银镜 / Fehling 砖红."""
    print("[ch11] Tollens / Fehling")
    step("ch11_tollens", "CC=O", "CC(=O)[O-]",
         "Tollens [Ag(NH₃)₂]⁺: 醛 → 羧酸根 + 析出 Ag↓ (银镜); 酮不反应 → 区分醛酮")
    step("ch11_fehling", "CCC=O", "CCC(=O)[O-]",
         "Fehling (Cu²⁺ 酒石酸碱液): 脂肪醛 → 羧酸根 + 砖红 Cu₂O↓; 芳醛一般不灵")


ALL = {
    "reactivity": reactivity_order,
    "hcn": hcn_addition,
    "bisulfite": bisulfite_addition,
    "acetal": acetal_formation,
    "aldol_dilute": aldol_dilute,
    "aldol_conc": aldol_conc,
    "aldol_crossed": aldol_crossed,
    "cannizzaro": cannizzaro,
    "haloform": haloform,
    "nabh4": nabh4_reduction,
    "lialh4": lialh4_reduction,
    "clemmensen": clemmensen,
    "wolff_kishner": wolff_kishner,
    "wittig": wittig,
    "imine_oxime": imine_oxime,
    "mannich": mannich,
    "stork_enamine": stork_enamine,
    "tollens_fehling": tollens_fehling,
}


if __name__ == "__main__":
    targets = sys.argv[1:] or list(ALL)
    for key in targets:
        fn = ALL.get(key)
        if not fn:
            print(f"Unknown target: {key}")
            continue
        fn()
    print(f"\nDONE. OK={N_OK} ERR={N_ERR}. Images in: {IMG}")
