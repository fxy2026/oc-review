"""Mechanism renderer for the 有机化学复习站.

Generates PNG+SVG step images for every mechanism in every chapter,
written into 复习全站/img/. Run from the directory:

  python _render_mechanisms.py

Each mechanism is a list of (step_id, before_smiles, after_smiles, label).
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


# Unicode sub/superscript -> ASCII fallback (font glyphs missing on Windows fonts).
_SUB = str.maketrans({
    "₀": "0", "₁": "1", "₂": "2", "₃": "3", "₄": "4",
    "₅": "5", "₆": "6", "₇": "7", "₈": "8", "₉": "9",
    "⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4",
    "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9",
    "⁺": "+", "⁻": "-",
})

def _clean(label: str) -> str:
    return label.translate(_SUB)


def step(name: str, before: str, after: str, label: str, size=(820, 220)) -> None:
    out = IMG / f"{name}.png"
    try:
        render_reaction(f"{before}>>{after}", out, size=size, reagent=_clean(label))
        print(f"  OK  {name}")
    except Exception as e:
        print(f"  ERR {name}: {e}")
        raise


def mol(name: str, smiles: str, legend: str = "", size=(360, 220)) -> None:
    out = IMG / f"{name}.png"
    try:
        render_molecule(smiles, out, size=size, legend=_clean(legend))
        print(f"  OK  {name}")
    except Exception as e:
        print(f"  ERR {name}: {e}")
        raise


# ============================================================
# ch10  醇/酚/醚
# ============================================================

def ch10_pinacol() -> None:
    """频哪醇 → 频哪酮 (4 步) + 立体之谜简化."""
    print("[ch10] Pinacol")
    pinacol = "OC(C)(C)C(O)(C)C"
    prot   = "[OH2+]C(C)(C)C(O)(C)C"
    cat1   = "[C+](C)(C)C(O)(C)C"
    oxoc   = "CC(C)(C)C(C)=[OH+]"
    keto   = "CC(C)(C)C(C)=O"
    step("ch10_pinacol_s1", pinacol, prot, "Step 1: H⁺ 质子化 OH")
    step("ch10_pinacol_s2", prot, cat1, "Step 2: − H₂O → 3° C⁺")
    step("ch10_pinacol_s3", cat1, oxoc, "Step 3: 1,2-CH₃ 迁移 → 氧鎓离子")
    step("ch10_pinacol_s4", oxoc, keto, "Step 4: − H⁺ → 频哪酮 C=O")
    # 立体之谜 (cis 缩环 / trans 仅 CH3 迁移)
    cis_diol  = "O[C@]1(C)CCCCC1(O)C"       # 1,2-cis-环己二醇 (示意, 简化)
    trans_diol = "O[C@@]1(C)CCCCC1(O)C"
    # 简化处理: 用对比标签的两个底物图
    mol("ch10_pinacol_cis_diol", cis_diol, "cis-1,2-二甲基-1,2-环己二醇 (题4(13) 模型)")
    mol("ch10_pinacol_trans_diol", trans_diol, "trans-1,2-二甲基-1,2-环己二醇 (题4(14) 模型)")


def ch10_wagner_meerwein() -> None:
    """3-甲基-2-丁醇 + HBr 经 1,2-H 迁移."""
    print("[ch10] Wagner-Meerwein 1,2-H")
    sub  = "CC(C)C(O)C"
    prot = "CC(C)C([OH2+])C"
    cat2 = "CC(C)[CH+]C"       # 2° cation
    cat3 = "C[C+](C)CC"        # 3° cation after H shift
    prod = "C[C](C)(Br)CC"     # tert-butyl bromide style
    step("ch10_wm_s1", sub, prot, "Step 1: H⁺ 质子化 OH")
    step("ch10_wm_s2", prot, cat2, "Step 2: − H₂O → 2° C⁺")
    step("ch10_wm_s3", cat2, cat3, "Step 3: 1,2-H 迁移 → 3° C⁺ (更稳)")
    step("ch10_wm_s4", cat3, prod, "Step 4: Br⁻ 进攻 → 2-溴-2-甲基丁烷")


def ch10_claisen() -> None:
    """烯丙基苯醚 → 邻烯丙基苯酚 (6 元环椅式过渡态)."""
    print("[ch10] Claisen 重排")
    ether = "C=CCOc1ccccc1"
    # 二烯酮中间体: 2-烯丙基-2,4-环己二烯-1-酮
    dien  = "O=C1C(CC=C)C=CC=C1"
    phenol = "C=CCc1ccccc1O"
    step("ch10_claisen_s1", ether, dien, "Step 1: [3,3]-σ 重排 (椅式过渡态), 烯丙基跨 O 跳邻位")
    step("ch10_claisen_s2", dien, phenol, "Step 2: 酮-烯醇互变 → 邻烯丙基苯酚 (恢复芳香性)")


def ch10_sn1_prime() -> None:
    """3-丁烯-2-醇 + HBr → 烯丙基共振 → 双产物."""
    print("[ch10] SN1' 烯丙基重排")
    sub  = "CC(O)C=C"
    prot = "CC([OH2+])C=C"
    cat  = "C[CH+]C=C"
    cat_reson = "CC=C[CH2+]"
    prod1 = "CC(Br)C=C"
    prod2 = "CC=CCBr"
    step("ch10_sn1p_s1", sub, prot, "Step 1: H⁺ 质子化 OH")
    step("ch10_sn1p_s2", prot, cat, "Step 2: − H₂O → 烯丙基 C⁺")
    step("ch10_sn1p_s3", cat, cat_reson, "Step 3: 烯丙基共振 (正电分到双键另一端)")
    step("ch10_sn1p_s4a", cat, prod1, "Step 4a: Br⁻ 进攻 C2 → 3-溴-1-丁烯 (SN1)")
    step("ch10_sn1p_s4b", cat_reson, prod2, "Step 4b: Br⁻ 进攻 C4 → 1-溴-2-丁烯 (SN1')")


def ch10_williamson() -> None:
    """RO⁻ + 1° R-X SN2 + 分子内关环."""
    print("[ch10] Williamson")
    # 链式: 苯酚钠 + 烯丙基氯
    s1_a = "[O-]c1ccccc1"
    s1_b = "ClCC=C"
    s1_p = "C(=C)COc1ccccc1"
    step("ch10_will_s1", f"{s1_a}.{s1_b}", s1_p,
         "SN2 (链式): 苯酚 O⁻ 进攻 C，Cl⁻ 离去")
    # 分子内: 4-氯-1-丁醇 + NaOH → THF
    s2_a = "OCCCCCl"
    s2_p = "C1CCCO1"
    step("ch10_will_s2", s2_a, s2_p,
         "分子内 SN2: 醇先脱质子，O⁻ 反咬 → 五元环 THF (NaOH)")


def ch10_lucas() -> None:
    """Lucas: 3° 醇 + HCl/ZnCl2 (SN1, 立即浑浊)."""
    print("[ch10] Lucas SN1")
    sub  = "CC(C)(C)O"
    prot = "CC(C)(C)[OH2+]"
    cat  = "C[C+](C)C"
    prod = "CC(C)(Cl)C"
    step("ch10_lucas_s1", sub, prot, "Step 1: H⁺/ZnCl₂ 质子化 OH")
    step("ch10_lucas_s2", prot, cat, "Step 2: − H₂O → 3° C⁺ (稳定 → 快)")
    step("ch10_lucas_s3", cat, prod, "Step 3: Cl⁻ 进攻 → 叔丁基氯")


def ch10_phenol_br2() -> None:
    """酚 + Br2: H2O 中三溴 / CS2 中单溴."""
    print("[ch10] 酚 + Br₂ 溶剂效应")
    phenol = "Oc1ccccc1"
    tribromo = "Oc1c(Br)cc(Br)cc1Br"
    monobromo = "Oc1ccc(Br)cc1"
    step("ch10_phenolBr2_H2O", phenol, tribromo,
         "在 H₂O 中: 苯酚电离成酚氧负离子 (强活化) → 2,4,6-三溴", size=(820, 220))
    step("ch10_phenolBr2_CS2", phenol, monobromo,
         "在 CS₂ 中: 不电离，苯酚活化弱 → 主要对位单溴", size=(820, 220))
    # 共振稳定性
    mol("ch10_phenoxide_reson_1", "[O-]c1ccccc1", "酚氧负离子 (1)")
    mol("ch10_phenoxide_reson_2", "O=C1C=CCC=C1", "邻位共振 (示意)")
    mol("ch10_phenoxide_reson_3", "O=C1C=CC=CC1", "对位共振 (示意)")


# ============================================================
# ch9  卤代烃 — SN/E + Grignard
# ============================================================

def ch9_sn2() -> None:
    """SN2 背面进攻 + Walden 反转 (用 (S)-2-溴丁烷 + OH-)."""
    print("[ch9] SN2")
    # (S)-2-bromobutane + OH- → (R)-2-butanol + Br-
    sub_attack = "CC[C@@H](C)Br.[OH-]"
    prod = "CC[C@H](C)O.[Br-]"
    step("ch9_sn2_overall", sub_attack, prod,
         "SN2 一步完成：OH- 从背面进攻，Br- 同时离去 → Walden 反转 (S→R)", size=(900, 220))
    # 进攻倾向: 1° > 2° > 3°
    mol("ch9_sn2_methyl", "CBr", "甲基: 位阻最小, 反应最快")
    mol("ch9_sn2_neopentyl", "CC(C)(C)CBr", "新戊基: 1° 但 β-位拥挤, 极慢")


def ch9_sn1() -> None:
    """SN1 3 步 + 消旋 (用 3° 卤代物)."""
    print("[ch9] SN1")
    # 2-bromo-2-methylbutane → 2-methyl-2-butanol
    sub = "CC(Br)(C)CC"
    cat = "C[C+](C)CC"
    prod = "CC(O)(C)CC"
    step("ch9_sn1_s1", sub, cat, "Step 1: C-Br 异裂 → 3° C+ (慢, 决速)")
    step("ch9_sn1_s2", cat, prod, "Step 2: H2O 从平面两面都能进攻 → 消旋 (快)")
    # 消旋示意
    mol("ch9_sn1_planar_cat", cat, "3° 碳正离子: sp2 平面构型")


def ch9_e2() -> None:
    """E2 反式共平面 anti-periplanar."""
    print("[ch9] E2")
    # 2-bromobutane + OH- → 2-butene (Zaitsev)
    sub = "CC(Br)CC.[OH-]"
    prod = "CC=CC"
    step("ch9_e2_overall", sub, prod,
         "E2 一步完成：碱夺 β-H, C-Br 同时离去 (要求 H 与 Br anti-periplanar)", size=(900, 220))
    # Zaitsev vs Hofmann
    mol("ch9_e2_zaitsev", "CC=CC", "Zaitsev: 2-丁烯 (取代多, 更稳)")
    mol("ch9_e2_hofmann", "CCC=C", "Hofmann: 1-丁烯 (取代少, 用大位阻碱时给出)")


def ch9_e1() -> None:
    """E1 2 步 + Saytzeff 倾向."""
    print("[ch9] E1")
    sub = "CC(Br)(C)CC"
    cat = "C[C+](C)CC"
    prod = "C=C(C)CC"        # Saytzeff: 2-methyl-2-butene 实际更稳但简化用 isobutylene-like
    prod2 = "CC(=C)CC"       # actually same: 2-methyl-1-butene Hofmann
    step("ch9_e1_s1", sub, cat, "Step 1: C-Br 异裂 → 3° C+ (与 SN1 共享)")
    step("ch9_e1_s2", cat, "CC=C(C)C", "Step 2: 失 β-H → 2-甲基-2-丁烯 (Zaitsev, 主)")
    step("ch9_e1_s2b", cat, "CC(C)=CC", "Step 2 alt: 失另一 β-H (次)")
    # 超共轭示意
    mol("ch9_hyperconjugation", "C[C+](C)CC",
        "超共轭: β-H 的 C-H 键与空 p 轨道部分重叠 → 稳定 3° C+")


def ch9_grignard() -> None:
    """Grignard 试剂的形成 + 与 CO2、酮反应."""
    print("[ch9] Grignard")
    # 形成
    step("ch9_grig_form", "CCCBr.[Mg]", "CCC[Mg]Br",
         "Grignard 生成: Mg 插入 C-Br (干乙醚, 无水无氧)")
    # 与 CO2
    step("ch9_grig_co2", "CCC[Mg]Br.O=C=O", "CCCC(=O)O[Mg]Br",
         "Grignard + CO2 → 羧酸盐 (加 1 个 C)")
    # 与酮
    step("ch9_grig_ketone", "CCC[Mg]Br.O=C(C)C", "CCCC(O)(C)C",
         "Grignard + 丙酮 → 3° 醇 (加碳骨架)")
    # 与环氧
    step("ch9_grig_epoxide", "CCC[Mg]Br.C1CO1", "CCCCCO",
         "Grignard + 环氧乙烷 → 醇 (加 2 个 C, 武大重点!)")


def ch9_corey_house() -> None:
    """Corey-House 偶联 R2CuLi + R'X → R-R'."""
    print("[ch9] Corey-House")
    # Gilman 试剂生成
    step("ch9_ch_gilman", "CC[Li].CC[Li].[Cu]I", "CC[Cu-]CC.[Li+].[I-]",
         "Gilman 试剂生成: 2 RLi + CuI → R2CuLi")
    # 偶联
    step("ch9_ch_couple", "CC[Cu-]CC.CCBr", "CCCC",
         "Corey-House 偶联: R2CuLi + R'-X → R-R' (新 C-C 键)")


# ============================================================
# ch7  芳烃 — EAS
# ============================================================

def ch7_eas_general() -> None:
    """EAS 通用机理: σ 复合物 (Wheland 中间体). 用 Br+ 当通用 E+."""
    print("[ch7] EAS general")
    # Wheland: cyclohexadienyl cation with sp3 C bearing E and H
    step("ch7_eas_s1", "c1ccccc1.[Br+]", "[CH+]1C=CC=CC1Br",
         "Step 1: 苯 + E+ (这里以 Br+ 代表) → σ 复合物 (Wheland 中间体, 失去芳香性)")
    step("ch7_eas_s2", "[CH+]1C=CC=CC1Br", "Brc1ccccc1",
         "Step 2: 失去 H+ → 取代苯 (恢复芳香性)")
    # 能量图示意 - 用三个分子标签近似
    mol("ch7_eas_energy_min1", "c1ccccc1", "起点: 苯 (低能, 芳香)")
    mol("ch7_eas_energy_max", "[CH+]1C=CC=CC1Br", "TS / 中间体: σ 复合物 (高能, 非芳香)")
    mol("ch7_eas_energy_min2", "Brc1ccccc1", "终点: 取代苯 (低能, 重获芳香)")


def ch7_nitration() -> None:
    """硝化 — NO2+ 生成 + 进攻."""
    print("[ch7] nitration")
    # NO2+ 生成: HNO3 + H2SO4 → NO2+ + HSO4- + H2O
    step("ch7_nit_gen", "O[N+](=O)[O-].OS(=O)(=O)O", "[N+](=O)=O.OS(=O)(=O)[O-].O",
         "Step 1: HNO3 + H2SO4 → NO2+ + HSO4- + H2O (硝酰阳离子生成)")
    # benzene + NO2+ → arenium
    step("ch7_nit_arenium", "c1ccccc1.[N+](=O)=O",
         "[CH+]1C=CC=CC1[N+](=O)[O-]",
         "Step 2: 苯进攻 NO2+ → σ 复合物")
    # arenium → nitrobenzene + H+
    step("ch7_nit_loseH", "[CH+]1C=CC=CC1[N+](=O)[O-]",
         "O=[N+]([O-])c1ccccc1",
         "Step 3: HSO4- 拿走 H+ → 硝基苯")


def ch7_halogenation() -> None:
    """卤代 — Cl2/FeCl3."""
    print("[ch7] halogenation")
    step("ch7_hal_gen", "ClCl.[Fe](Cl)(Cl)Cl", "[Cl+].[Fe-](Cl)(Cl)(Cl)Cl",
         "Step 1: FeCl3 极化 Cl-Cl → 类似 Cl+ 的强亲电体")
    step("ch7_hal_arenium", "c1ccccc1.[Cl+]", "[CH+]1C=CC=CC1Cl",
         "Step 2: 苯进攻 Cl+ → σ 复合物")
    step("ch7_hal_prod", "[CH+]1C=CC=CC1Cl", "Clc1ccccc1",
         "Step 3: 失 H+ → 氯苯")


def ch7_sulfonation() -> None:
    """磺化 — 可逆!"""
    print("[ch7] sulfonation")
    step("ch7_sul_overall", "c1ccccc1.O=S(=O)=O", "OS(=O)(=O)c1ccccc1",
         "苯 + SO3 (浓 H2SO4 给出) → 苯磺酸 (可逆: 加热稀酸又退回)")
    # 可逆性的应用: 占位保护
    mol("ch7_sul_blocking",
        "OS(=O)(=O)c1ccc(C)cc1",
        "占位例: 甲苯先磺化保护对位, 再做邻位取代")


def ch7_fc_alkyl() -> None:
    """Friedel-Crafts 烷基化 (重排陷阱)."""
    print("[ch7] FC alkylation")
    # 用 1-氯丙烷: 先生成 1° C+ → 重排到 2°
    step("ch7_fca_gen1", "CCCCl.[Al](Cl)(Cl)Cl", "CC[CH2+].[Al-](Cl)(Cl)(Cl)Cl",
         "Step 1: AlCl3 帮 RX 离子化 → 1° C+ (不稳)")
    step("ch7_fca_rearr", "CC[CH2+]", "C[CH+]C",
         "Step 2: 1,2-H 迁移 → 2° C+ (更稳, 此步导致主产物是异丙基苯)")
    step("ch7_fca_attack", "c1ccccc1.C[CH+]C", "CC(C)c1ccccc1",
         "Step 3: 苯进攻 2° C+ → 异丙基苯 (主产物, 不是正丙基!)")


def ch7_fc_acyl() -> None:
    """F-C 酰基化 (酰基不重排)."""
    print("[ch7] FC acylation")
    step("ch7_fcac_gen", "CC(=O)Cl.[Al](Cl)(Cl)Cl", "C[C+]=O.[Al-](Cl)(Cl)(Cl)Cl",
         "Step 1: AlCl3 + RCOCl → 酰基阳离子 RC(=O)+ (共振 R-C≡O+ 稳定, 不重排)")
    step("ch7_fcac_attack", "c1ccccc1.C[C+]=O", "CC(=O)c1ccccc1",
         "Step 2: 苯进攻 RC(=O)+ → 芳酮 (单取代, 因 -COR 钝化, 不会过多取代)")
    mol("ch7_fcac_resonance", "C[C+]=O",
        "酰基阳离子的共振形式: C=O+ ↔ C+-O (氧上孤对稳定正电, 不必重排)")


def ch7_orient() -> None:
    """定位效应 — 共振结构对比."""
    print("[ch7] 定位效应")
    # 甲苯 (邻/对位活化) 的 σ 复合物
    mol("ch7_orient_toluene_o",
        "[CH+]1C=CC=CC1(C)[N+](=O)[O-]",
        "甲苯邻位进攻 σ 复合物: + 可分到 CH3 邻碳, 受 +I 稳定")
    mol("ch7_orient_toluene_p",
        "O=[N+]([O-])C1C=CC(C)=C[CH+]1",
        "甲苯对位进攻 σ 复合物: + 可分到 CH3 同碳, 受 +I 稳定 (最稳)")
    mol("ch7_orient_toluene_m",
        "O=[N+]([O-])C1[CH+]C=CC=C1C",
        "甲苯间位进攻 σ 复合物: + 分不到 CH3 上, 无 +I 稳定 (次产物)")
    # 硝基苯 (邻/对位钝化, 间位定位)
    mol("ch7_orient_nb_m",
        "O=[N+]([O-])C1=CC(=CC=C1)[N+](=O)[O-]",
        "硝基苯间位取代: + 远离 NO2 → 钝化最少 (主产物)")


def ch7_birch() -> None:
    """Birch 还原 (Na/NH3液体 + 醇)."""
    print("[ch7] Birch")
    # 苯 → 1,4-环己二烯
    step("ch7_birch_overall", "c1ccccc1", "C1C=CCC=C1",
         "Birch: Na/NH3液 + EtOH → 1,4-环己二烯 (打破芳香性, 但留两个双键)")
    # 自由基阴离子中间体示意
    mol("ch7_birch_radical_anion", "[CH-]1[CH]C=CC=C1",
        "中间体: 单电子还原给自由基阴离子 (与 Na 给出的电子结合)")


# ============================================================
# ch5  烯烃加成
# ============================================================

def ch5_electrophilic_general() -> None:
    """亲电加成通用 (用 CH3-CH=CH2 + HBr)."""
    print("[ch5] 亲电加成 general")
    sub = "CC=C"
    cat = "C[CH+]C"        # 2° (Markovnikov)
    prod = "CC(Br)C"
    step("ch5_eag_s1", sub, cat, "Step 1: H+ 加到末端 C → 2° C+ (Markovnikov: + 留在多 C 那侧)")
    step("ch5_eag_s2", cat, prod, "Step 2: Br- 进攻 C+ → 2-溴丙烷")
    # Markovnikov 选择性对比
    mol("ch5_markov_2cation", "C[CH+]C", "2° C+ (Markov 主产物路径)")
    mol("ch5_markov_1cation", "CC[CH2+]", "1° C+ (反 Markov, 不稳定, 几乎不走)")


def ch5_cation_rearrange() -> None:
    """烯烃加成中的碳正离子重排 (3,3-二甲基-1-丁烯 + HCl)."""
    print("[ch5] 烯烃碳正离子重排")
    sub = "C=CC(C)(C)C"
    cat2 = "C[CH+]C(C)(C)C"
    cat3 = "CC(C)[C+](C)C"
    prod = "CC(C)C(C)(Cl)C"
    step("ch5_alkrearr_s1", sub, cat2, "Step 1: H+ 加成 → 2° C+ (按 Markov)")
    step("ch5_alkrearr_s2", cat2, cat3, "Step 2: 1,2-CH3 迁移 → 3° C+ (更稳)")
    step("ch5_alkrearr_s3", cat3, prod, "Step 3: Cl- 进攻 → 2-氯-2,3-二甲基丁烷 (重排产物)")


def ch5_bromonium() -> None:
    """溴鎓离子 anti 加成."""
    print("[ch5] 溴鎓离子")
    # 乙烯 + Br2 → 溴鎓 → 1,2-二溴乙烷
    step("ch5_brm_s1", "C=C.BrBr", "[Br+]1CC1.[Br-]",
         "Step 1: Br2 极化 → Br+ 桥接给 3 元环溴鎓离子, Br- 离开")
    step("ch5_brm_s2", "[Br+]1CC1.[Br-]", "BrCCBr",
         "Step 2: Br- 从背面进攻 (anti) → 1,2-二溴乙烷")
    # 立体后果: 顺/反丁烯给不同产物
    step("ch5_brm_cis", "C/C=C\\C.BrBr", "C[C@H](Br)[C@@H](C)Br",
         "顺-2-丁烯 + Br2 → (2R,3R)+(2S,3S) 一对消旋 (anti 加成)")
    step("ch5_brm_trans", "C/C=C/C.BrBr", "C[C@H](Br)[C@H](C)Br",
         "反-2-丁烯 + Br2 → meso 化合物 (anti 加成)")


def ch5_halohydrin() -> None:
    """卤水加成 (Br2/H2O) → Markov 卤醇."""
    print("[ch5] 卤水加成")
    step("ch5_hh_s1", "CC=C.BrBr", "CC1C[Br+]1.[Br-]",
         "Step 1: 溴鎓离子 (3 元环), 但取代多的 C 部分正电荷更多")
    step("ch5_hh_s2", "CC1C[Br+]1.O", "OC(C)CBr",
         "Step 2: H2O 进攻取代多的 C (更稳的 C+ 中心) → 1-溴-2-丙醇 (Markov)")


def ch5_peroxide() -> None:
    """过氧化物效应 — 反 Markov 自由基机理."""
    print("[ch5] 过氧化物效应")
    # 引发
    step("ch5_per_init1", "[O]O", "[O].[O]",
         "引发: ROOR → 2 RO• (光/热)")
    step("ch5_per_init2", "[O].Br", "[OH].[Br]",
         "引发: RO• + HBr → ROH + Br• (Br• 是真正的链转移体)")
    # 增长 1: Br• 加到末端 (生成更稳的 2° 自由基)
    step("ch5_per_prop1", "CC=C.[Br]", "C[CH][CH2]Br",
         "增长 1: Br• 加到 CH2 端 → 2° 自由基 (反 Markov!)")
    step("ch5_per_prop2", "C[CH][CH2]Br.Br", "CCCBr.[Br]",
         "增长 2: 自由基从 HBr 抢 H → 1-溴丙烷 + Br• (链循环)")


def ch5_hydroboration() -> None:
    """硼氢化-氧化 (syn, 反 Markov)."""
    print("[ch5] 硼氢化-氧化")
    # BH3 加到端烯
    step("ch5_hb_s1", "CC=C.B", "CCCB",
         "Step 1: BH3 协同 syn 加成, B 加到位阻小的端 C → 反 Markov 位置")
    step("ch5_hb_s2", "CCCB.OO.[OH-]", "CCCO.OB.[O-]",
         "Step 2: H2O2/NaOH 把 C-B 换成 C-OH (构型保留, 经过 -OO- 迁移)")
    mol("ch5_hb_overall_concerted", "C=C.B",
        "BH3 的协同 4 中心过渡态 (B-H 同步加到 C=C 两端)")


def ch5_ozonolysis() -> None:
    """臭氧化."""
    print("[ch5] 臭氧化")
    # 烯 + O3 → molozonide (1,2,3-trioxolane)
    step("ch5_ozo_s1", "CC=CC.O=[O+][O-]", "CC1OOOC1C",
         "Step 1: 烯 + O3 → 初级臭氧物 (molozonide, 1,2,3-三氧戊环, 不稳)")
    step("ch5_ozo_s2", "CC1OOOC1C", "CC1OOC(C)O1",
         "Step 2: 重排 → 次级臭氧物 (ozonide, 1,2,4-三氧戊环)")
    step("ch5_ozo_red", "CC1OOC(C)O1.[Zn]", "CC=O.CC=O",
         "Step 3: Zn/AcOH 还原裂解 → 2 个醛/酮 (两端断, 双键变 C=O)")
    step("ch5_ozo_ox", "CC1OOC(C)O1.OO", "CC(=O)O.CC(=O)O",
         "Step 3 alt: H2O2 氧化裂解 → 2 个羧酸")


def ch5_epoxidation() -> None:
    """mCPBA 环氧化 (syn, 蝴蝶过渡态)."""
    print("[ch5] 环氧化")
    step("ch5_epox_overall",
         "CC=CC.OC(=O)c1cccc(Cl)c1OO", "CC1OC1C.OC(=O)c1cccc(Cl)c1O",
         "Step 1: mCPBA 协同 syn 加成 → 环氧化合物 + 间氯苯甲酸",
         size=(950, 240))


def ch5_nbs() -> None:
    """NBS 烯丙位溴代."""
    print("[ch5] NBS")
    # 微量 Br• 引发
    step("ch5_nbs_s1", "C=CCC.[Br]", "C=C[CH]C.Br",
         "Step 1: Br• 抢 烯丙位 H → 烯丙基自由基 (共振稳定)")
    step("ch5_nbs_s2", "C=C[CH]C.BrBr", "C=CC(Br)C.[Br]",
         "Step 2: 烯丙基自由基 + Br2 → 烯丙基溴 + Br• (NBS 持续低浓度释放 Br2)")
    mol("ch5_nbs_radical_reson", "C=C[CH]C",
        "烯丙基自由基有 2 个共振端 (双键可在原位或迁移)")


# ============================================================
# ch6  炔烃 + 共轭
# ============================================================

def ch6_alkyne_hx() -> None:
    """炔烃 + HX (vinyl cation, Markov)."""
    print("[ch6] 炔烃 HX")
    step("ch6_alk_hx_s1", "CC#C.Br", "C[C+]=C.[Br-]",
         "Step 1: H+ 加到末端 → 乙烯基阳离子 (vinyl C+, 比烷基 C+ 不稳, 所以炔比烯加慢)")
    step("ch6_alk_hx_s2", "C[C+]=C.[Br-]", "CC(Br)=C",
         "Step 2: Br- 进攻 → 2-溴丙烯 (烯式卤代物, Markov 位置)")
    step("ch6_alk_hx_s3", "CC(Br)=C.Br", "CC(Br)(Br)C",
         "Step 3 (过量 HBr): 第二份 HBr 加成, 同侧 → 2,2-二溴丙烷 (gem-二卤)")


def ch6_lindlar_birch() -> None:
    """Lindlar 顺式 vs Na/NH3 反式还原."""
    print("[ch6] Lindlar / Na-NH3")
    step("ch6_lin_lindlar", "CC#CC", "C/C=C\\C",
         "Lindlar (Pd/CaCO3, 毒化): 顺式还原 → 顺-2-丁烯 (吸附在催化剂表面, 两 H 同侧加)")
    step("ch6_lin_birch", "CC#CC", "C/C=C/C",
         "Na/NH3液 (溶剂电子还原): 反式还原 → 反-2-丁烯 (经过自由基阴离子, 更稳的反式 = 主)")


def ch6_diels_alder() -> None:
    """Diels-Alder [4+2]."""
    print("[ch6] D-A")
    # 1,3-butadiene + ethylene
    step("ch6_da_basic", "C=CC=C.C=C", "C1CCC=CC1",
         "D-A [4+2]: 1,3-丁二烯 + 乙烯 → 环己烯 (6 元环过渡态, 协同, 无中间体)")
    # 富电子双烯 + 缺电子亲双烯
    step("ch6_da_rich",
         "C=CC=C.O=C(/C=C/C)OC", "CC1CC=CCC1C(=O)OC",
         "推电子双烯 + 拉电子亲双烯 (e.g. 丙烯酸酯) → 快")
    mol("ch6_da_endo",
        "O=C1OC(=O)[C@@H]2CCC=C[C@@H]12",
        "endo 规则: 拉电子取代基朝向π系统内侧 (动力学产物)")
    mol("ch6_da_diene_s_cis", "C=CC=C",
        "双烯须能采取 s-cis 构象才能反应 (s-trans 不能)")


def ch6_1_2_vs_1_4() -> None:
    """1,2- vs 1,4-加成 (动力学 / 热力学)."""
    print("[ch6] 1,2 vs 1,4")
    step("ch6_da_12",
         "C=CC=C.Br", "C=CC(Br)C",
         "1,2-加成: -40°C 低温, 动力学产物 (Br- 进攻较稳烯丙基 C+ 的近端)")
    step("ch6_da_14",
         "C=CC=C.Br", "BrCC=CC",
         "1,4-加成: 40°C 高温, 热力学产物 (重排得内双键, 更稳)")


# ============================================================
# ch3  烷烃 — 自由基链反应
# ============================================================

def ch3_radical_chain() -> None:
    """CH4 + Cl2 自由基链反应."""
    print("[ch3] 自由基链反应")
    step("ch3_rad_init", "ClCl", "[Cl].[Cl]",
         "引发: Cl-Cl + hv → 2 Cl• (光解, 高能量)")
    step("ch3_rad_prop1", "C.[Cl]", "[CH3].Cl",
         "增长 1: CH4 + Cl• → •CH3 + HCl (抢 H, 主导链)")
    step("ch3_rad_prop2", "[CH3].ClCl", "CCl.[Cl]",
         "增长 2: •CH3 + Cl2 → CH3Cl + Cl• (循环回到 Cl•)")
    step("ch3_rad_term1", "[Cl].[Cl]", "ClCl",
         "终止 a: 2 Cl• → Cl2")
    step("ch3_rad_term2", "[CH3].[CH3]", "CC",
         "终止 b: 2 •CH3 → C2H6 (乙烷, 副产物之一)")
    step("ch3_rad_term3", "[CH3].[Cl]", "CCl",
         "终止 c: •CH3 + Cl• → CH3Cl")
    # 选择性
    mol("ch3_rad_3deg", "C[C](C)C", "3° 自由基: 最稳定 (取代越多越稳)")
    mol("ch3_rad_2deg", "C[CH]C", "2° 自由基")
    mol("ch3_rad_1deg", "C[CH2]", "1° 自由基: 最不稳")


# ============================================================
# ch2  共振 + 共轭
# ============================================================

def ch2_resonance() -> None:
    """常见共振对子."""
    print("[ch2] 共振")
    # 烯丙基 C+
    step("ch2_reson_allyl",
         "[CH2+]C=C", "C=C[CH2+]",
         "烯丙基阳离子共振: 正电跨越双键, 分到两端 (等价共振)")
    # 苄基 C+
    step("ch2_reson_benzyl",
         "[CH2+]c1ccccc1", "C1=CC=CC=C1[CH2+]",
         "苄基阳离子共振: 正电分到苯环邻/对位 (4 个共振形式)")
    # 羰基
    step("ch2_reson_carbonyl",
         "CC(=O)C", "C[C+]([O-])C",
         "羰基共振: C=O ↔ C+-O- (carbonyl 极性的本质, C 部分正电)")
    # 烯醇负离子
    step("ch2_reson_enolate",
         "[CH2-]C(=O)C", "C=C([O-])C",
         "丙酮烯醇负离子共振: 负电跨 C=C-O, 主要分到 O 上 (更稳)")
    # 苯酚负离子 5 个形式
    mol("ch2_phenoxide_main", "[O-]c1ccccc1", "苯酚负离子: 负电在 O")
    mol("ch2_phenoxide_o1", "O=C1C=CC=C[CH-]1", "共振: 负电分到邻位 C")
    mol("ch2_phenoxide_p", "O=C1C=C[CH-]C=C1", "共振: 负电分到对位 C")


def ch2_conjugation() -> None:
    """共轭二烯 — 离域示意."""
    print("[ch2] 共轭")
    mol("ch2_butadiene_s_cis", "C=CC=C", "1,3-丁二烯 (共轭, 单键有部分双键性)")
    mol("ch2_isolated_diene", "C=CCC=C", "1,4-戊二烯 (孤立双键, 中间 sp3, 不共轭)")
    mol("ch2_cumulated", "C=C=C", "丙二烯 (累积双键, 中间 sp, 双键互相垂直)")


# ============================================================
# ch4  立体化学
# ============================================================

def ch4_stereo_examples() -> None:
    """R/S 实例 + Fischer 互转."""
    print("[ch4] 立体化学")
    mol("ch4_R_lactic", "OC(=O)[C@@H](O)C", "(R)-乳酸 (CIP: OH > COOH > CH3 > H, 顺时针)")
    mol("ch4_S_lactic", "OC(=O)[C@H](O)C", "(S)-乳酸 (逆时针)")
    mol("ch4_meso_tartaric", "OC(=O)[C@H](O)[C@@H](O)C(=O)O",
        "酒石酸 meso 形: 含两个手性碳但有对称面 → 无旋光")
    mol("ch4_R_R_tartaric", "OC(=O)[C@@H](O)[C@@H](O)C(=O)O",
        "(R,R)-酒石酸: 与 (S,S) 互为对映体")


# ============================================================
# ch1  弯箭头 — 用 RDKit 不好画, 留作 SVG overlay 由 HTML 直接做
# ============================================================
# (no python rendering; HTML 直接 SVG)


ALL = {
    "ch10_pinacol": ch10_pinacol,
    "ch10_wm": ch10_wagner_meerwein,
    "ch10_claisen": ch10_claisen,
    "ch10_sn1p": ch10_sn1_prime,
    "ch10_williamson": ch10_williamson,
    "ch10_lucas": ch10_lucas,
    "ch10_phenol_br2": ch10_phenol_br2,
    # ch9
    "ch9_sn2": ch9_sn2,
    "ch9_sn1": ch9_sn1,
    "ch9_e2": ch9_e2,
    "ch9_e1": ch9_e1,
    "ch9_grignard": ch9_grignard,
    "ch9_corey_house": ch9_corey_house,
    # ch7
    "ch7_eas_general": ch7_eas_general,
    "ch7_nitration": ch7_nitration,
    "ch7_halogenation": ch7_halogenation,
    "ch7_sulfonation": ch7_sulfonation,
    "ch7_fc_alkyl": ch7_fc_alkyl,
    "ch7_fc_acyl": ch7_fc_acyl,
    "ch7_orient": ch7_orient,
    "ch7_birch": ch7_birch,
    # ch5
    "ch5_electrophilic_general": ch5_electrophilic_general,
    "ch5_cation_rearrange": ch5_cation_rearrange,
    "ch5_bromonium": ch5_bromonium,
    "ch5_halohydrin": ch5_halohydrin,
    "ch5_peroxide": ch5_peroxide,
    "ch5_hydroboration": ch5_hydroboration,
    "ch5_ozonolysis": ch5_ozonolysis,
    "ch5_epoxidation": ch5_epoxidation,
    "ch5_nbs": ch5_nbs,
    # ch6
    "ch6_alkyne_hx": ch6_alkyne_hx,
    "ch6_lindlar_birch": ch6_lindlar_birch,
    "ch6_diels_alder": ch6_diels_alder,
    "ch6_1_2_vs_1_4": ch6_1_2_vs_1_4,
    # ch3
    "ch3_radical_chain": ch3_radical_chain,
    # ch2
    "ch2_resonance": ch2_resonance,
    "ch2_conjugation": ch2_conjugation,
    # ch4
    "ch4_stereo_examples": ch4_stereo_examples,
}


if __name__ == "__main__":
    targets = sys.argv[1:] or list(ALL)
    for key in targets:
        fn = ALL.get(key)
        if not fn:
            print(f"Unknown target: {key}")
            continue
        fn()
    print(f"\nAll done. Images in: {IMG}")
