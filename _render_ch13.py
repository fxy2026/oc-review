"""Mechanism renderer for ch13 羧酸衍生物 (carboxylic acid derivatives).

Generates SVG step images into 复习全站/img/ch13_*.svg.
Run:  python _render_ch13.py
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


def step(name: str, before: str, after: str, label: str, size=(900, 240)) -> None:
    out = IMG / f"{name}.svg"
    try:
        render_reaction(f"{before}>>{after}", out.with_suffix(".png"),
                        size=size, reagent=_clean(label))
        print(f"  OK  {name}")
    except Exception as e:
        print(f"  ERR {name}: {e}")
        raise


def mol(name: str, smiles: str, legend: str = "", size=(380, 240)) -> None:
    out = IMG / f"{name}.svg"
    try:
        render_molecule(smiles, out.with_suffix(".png"), size=size, legend=_clean(legend))
        print(f"  OK  {name}")
    except Exception as e:
        print(f"  ERR {name}: {e}")
        raise


# ============================================================
# 1) 亲核酰基取代通用机理 (加成-消除, 经四面体中间体)
#    以乙酰氯 + 甲醇 -> 乙酸甲酯 为例 (酰氯醇解)
# ============================================================
def nas_general() -> None:
    print("[ch13] 亲核酰基取代通用 (NAS)")
    # 乙酰氯
    acyl = "CC(=O)Cl"
    # 甲醇亲核加成 -> 四面体中间体 (氧负, sp3 C 同时连 Cl/OMe/OH)
    tet = "C[C]([O-])(Cl)[OH+]C"     # 四面体中间体(质子化的醇氧, 负氧)
    # 消除 Cl- -> 质子化的酯
    prot_ester = "CC(=[OH+])OC"
    ester = "CC(=O)OC"
    step("ch13_nas_s1", acyl, tet,
         "Step 1 加成: Nu(CH₃OH) 进攻羰基 C → 四面体中间体 (sp³, 氧带负电)")
    step("ch13_nas_s2", tet, prot_ester,
         "Step 2 消除: 离去基 Cl⁻ 离去, 重建 C=O")
    step("ch13_nas_s3", prot_ester, ester,
         "Step 3: 去质子 → 乙酸甲酯 (净: Cl 被 OCH₃ 取代)")
    # 通用结论分子图
    mol("ch13_tetrahedral", "C[C]([O-])(Cl)OC",
        "四面体中间体: 羰基 C 由 sp² → sp³, 决速步")


# ============================================================
# 2) 酯碱性水解 BAC2 (碱-酰氧-双分子)
#    乙酸乙酯 + OH- -> 乙酸根 + 乙醇
# ============================================================
def ester_bac2() -> None:
    print("[ch13] 酯碱性水解 BAC2")
    ester = "CC(=O)OCC"
    tet = "C[C]([O-])(O)OCC"          # 四面体中间体: OH- 加成
    acid = "CC(=O)O"                  # 酸 (随后被碱夺质子)
    carboxylate = "CC(=O)[O-]"        # 羧酸根 (不可逆: 拉平衡)
    step("ch13_bac2_s1", ester, tet,
         "Step 1: OH⁻ 进攻羰基 C → 四面体中间体 (B=碱, AC=酰氧断裂, 2=双分子)")
    step("ch13_bac2_s2", tet, acid + ".CCO",
         "Step 2: EtO⁻ 离去 → 乙酸 + 乙醇 (断的是酰氧 C–O 键)")
    step("ch13_bac2_s3", acid, carboxylate,
         "Step 3: 碱夺羧酸质子 → 羧酸根 (此步不可逆, 把皂化拉到底)")


# ============================================================
# 3) Claisen 酯缩合
#    2 乙酸乙酯 --EtONa--> 乙酰乙酸乙酯
# ============================================================
def claisen() -> None:
    print("[ch13] Claisen 酯缩合")
    ester = "CC(=O)OCC"
    enolate = "[CH2-]C(=O)OCC"            # α-碳负离子(烯醇负)
    tet = "CC([O-])(OCC)CC(=O)OCC"        # 进攻另一分子乙酸乙酯羰基后的四面体中间体
    keto_ester = "CC(=O)CC(=O)OCC"        # 乙酰乙酸乙酯
    final_anion = "CC(=O)[CH-]C(=O)OCC"   # 产物去质子(锁平衡)
    step("ch13_claisen_s1", ester, enolate,
         "Step 1: EtO⁻ 拔 α-H → 酯的 α-碳负离子 (烯醇负离子)")
    step("ch13_claisen_s2", enolate + "." + ester, tet,
         "Step 2: 碳负离子进攻另一分子酯的羰基 C → 四面体中间体")
    step("ch13_claisen_s3", tet, keto_ester,
         "Step 3: 消除 EtO⁻ → 乙酰乙酸乙酯 (β-酮酸酯)")
    step("ch13_claisen_s4", keto_ester, final_anion,
         "Step 4: EtO⁻ 夺产物活泼 α-H → 稳定烯醇负盐 (此步把平衡拉向产物!)")


# ============================================================
# 4) 丙二酸酯合成法 -> 造支链羧酸
#    丙二酸二乙酯 -> 烷基化 -> 水解脱羧 -> RCH2COOH
# ============================================================
def malonic() -> None:
    print("[ch13] 丙二酸酯合成法")
    malonate = "CCOC(=O)CC(=O)OCC"          # 丙二酸二乙酯
    anion = "CCOC(=O)[CH-]C(=O)OCC"         # 拔 α-H 得碳负离子
    alkylated = "CCOC(=O)C(CCC)C(=O)OCC"    # + 1-溴丙烷 -> C 上接丙基
    diacid = "OC(=O)C(CCC)C(=O)O"           # 水解得二酸
    product = "CCCCC(=O)O"                  # 脱羧 -> 戊酸 (2-丙基乙酸=戊酸)
    step("ch13_malonic_s1", malonate, anion,
         "Step 1: EtONa 拔活泼亚甲基 H → 碳负离子 (两酯共振稳定)")
    step("ch13_malonic_s2", anion, alkylated,
         "Step 2: + R–X (1-溴丙烷, SN2) → 烷基化")
    step("ch13_malonic_s3", alkylated, diacid,
         "Step 3: H₃O⁺ 水解两个酯 → 取代丙二酸")
    step("ch13_malonic_s4", diacid, product,
         "Step 4: 加热脱羧 (β-二酸, 六元环过渡态) → 戊酸 RCH₂COOH")


# ============================================================
# 5) 乙酰乙酸酯合成法 -> 造甲基酮
#    乙酰乙酸乙酯 -> 烷基化 -> 水解脱羧 -> CH3COCH2R
# ============================================================
def acetoacetic() -> None:
    print("[ch13] 乙酰乙酸酯合成法")
    aae = "CC(=O)CC(=O)OCC"               # 乙酰乙酸乙酯
    anion = "CC(=O)[CH-]C(=O)OCC"         # 拔 α-H
    alkylated = "CC(=O)C(CC)C(=O)OCC"     # + 溴乙烷
    ketoacid = "CC(=O)C(CC)C(=O)O"        # 水解得 β-酮酸
    product = "CC(=O)CCC"                 # 脱羧 -> 2-戊酮
    step("ch13_aae_s1", aae, anion,
         "Step 1: EtONa 拔 α-H → 碳负离子 (酮+酯夹住, 强酸性 pKa≈11)")
    step("ch13_aae_s2", anion, alkylated,
         "Step 2: + CH₃CH₂Br (SN2) → α-烷基化")
    step("ch13_aae_s3", alkylated, ketoacid,
         "Step 3: 稀碱水解酯 → β-酮酸")
    step("ch13_aae_s4", ketoacid, product,
         "Step 4: 加热脱羧 (β-酮酸) → 2-戊酮 CH₃COCH₂R (甲基酮)")


# ============================================================
# 6) Hofmann 降解 (酰胺 -> 伯胺, 经异氰酸酯, 少一个碳)
#    丙酰胺 CH3CH2CONH2 -> 乙胺 CH3CH2NH2
# ============================================================
def hofmann_degradation() -> None:
    print("[ch13] Hofmann 降解")
    amide = "CCC(N)=O"                    # 丙酰胺
    nbromo = "CCC(=O)NBr"                 # N-溴代酰胺
    nbromo_anion = "CCC(=O)[N-]Br"        # 去质子的 N-溴代酰胺负离子
    isocyanate = "CCN=C=O"               # 异氰酸酯 (R 迁移到 N, 失 Br-, 少碳关键!)
    carbamate_acid = "CCNC(=O)O"          # 加水得氨基甲酸
    amine = "CCN"                         # 乙胺 (脱羧)
    step("ch13_hof_s1", amide, nbromo,
         "Step 1: Br₂/NaOH 把 N–H 换成 N–Br → N-溴代酰胺")
    step("ch13_hof_s2", nbromo, nbromo_anion,
         "Step 2: OH⁻ 夺剩下的 N–H → N-溴代酰胺负离子")
    step("ch13_hof_s3", nbromo_anion, isocyanate,
         "Step 3 关键: R 基带电子对从 C 迁移到 N, Br⁻ 离去 → 异氰酸酯 (碳数 -1!)")
    step("ch13_hof_s4", isocyanate, carbamate_acid,
         "Step 4: 异氰酸酯 + H₂O → 氨基甲酸 (不稳)")
    step("ch13_hof_s5", carbamate_acid, amine,
         "Step 5: 氨基甲酸脱 CO₂ → 伯胺 (比原酰胺少 1 个碳)")


# ============================================================
# 7) Gabriel 合成 (纯伯胺)
#    邻苯二甲酰亚胺 K 盐 + RX -> 水解 -> 纯 1° 胺
# ============================================================
def gabriel() -> None:
    print("[ch13] Gabriel 合成")
    imide_k = "O=C1c2ccccc2C(=O)[N-]1"          # 邻苯二甲酰亚胺负离子(K盐)
    n_alkyl = "O=C1c2ccccc2C(=O)N1CCCC"          # N-烷基化(接丁基)
    amine = "NCCCC"                              # 水解(或肼解)得正丁胺
    phthalic = "O=C(O)c1ccccc1C(=O)O"            # 邻苯二甲酸副产物
    step("ch13_gabriel_s1", imide_k, n_alkyl,
         "Step 1: 酰亚胺 N⁻ + R–X (1-溴丁烷, SN2) → N-烷基邻苯二甲酰亚胺")
    step("ch13_gabriel_s2", n_alkyl, amine + "." + phthalic,
         "Step 2: 水解(或 N₂H₄ 肼解) → 纯净伯胺 + 邻苯二甲酸 (只接一个 R, 不多烷基化)")


# ============================================================
# 8) 相对活性 + 相互转化网络 (展示四个衍生物 + 腈)
# ============================================================
def reactivity() -> None:
    print("[ch13] 相对活性 / 五类化合物")
    mol("ch13_acyl_chloride", "CC(=O)Cl", "酰氯 RCOCl (最活泼, 离去基 Cl⁻ 最好)")
    mol("ch13_anhydride", "CC(=O)OC(C)=O", "酸酐 (RCO)₂O (次活泼, 离去基 RCOO⁻)")
    mol("ch13_ester", "CC(=O)OCC", "酯 RCOOR' (中等, 离去基 RO⁻)")
    mol("ch13_amide", "CC(N)=O", "酰胺 RCONH₂ (最钝, N 共轭供电最强)")
    mol("ch13_nitrile", "CC#N", "腈 R–C≡N (水解得羧酸/酰胺, 还原得 1° 胺)")


# ============================================================
# 9) SOCl2 制酰氯 + 酰氯反应网络 (单步示意图)
# ============================================================
def acyl_network() -> None:
    print("[ch13] SOCl₂ + 酰氯网络")
    step("ch13_socl2", "CC(=O)O", "CC(=O)Cl",
         "SOCl₂: 羧酸 → 酰氯 (副产 SO₂↑ + HCl↑, 易除)")
    step("ch13_acyl_to_anhydride", "CC(=O)Cl.CC(=O)[O-]", "CC(=O)OC(C)=O",
         "酰氯 + 羧酸根 → 酸酐")
    step("ch13_acyl_to_ester", "CC(=O)Cl.OCC", "CC(=O)OCC",
         "酰氯 + 醇 (加吡啶中和 HCl) → 酯 (不可逆, 比酯化更彻底)")
    step("ch13_acyl_to_amide", "CC(=O)Cl.N", "CC(N)=O",
         "酰氯 + 氨/胺 → 酰胺")
    step("ch13_acyl_to_ketone", "CC(=O)Cl.[CH3][Cu][CH3]", "CC(C)=O",
         "酰氯 + R₂CuLi (二烃基铜锂) → 酮 (停在酮, 不过加成)")


# ============================================================
# 10) 还原: 酯/酰胺/腈 还原对比
# ============================================================
def reduction() -> None:
    print("[ch13] 还原对比")
    step("ch13_red_ester", "CCC(=O)OCC", "CCCO.CCO",
         "酯 + LiAlH₄ → 1° 醇 (+ R'OH); NaBH₄ 不还原酯")
    step("ch13_red_acylcl_aldehyde", "CCC(=O)Cl", "CCC=O",
         "酰氯 + LiAlH(OtBu)₃ 或 Rosenmund(Pd/BaSO₄,H₂) → 醛 (停在醛)")
    step("ch13_red_amide", "CCC(N)=O", "CCCN",
         "酰胺 + LiAlH₄ → 胺 (羰基 → CH₂, 不增碳)")
    step("ch13_red_nitrile", "CCC#N", "CCCCN",
         "腈 + LiAlH₄ (或 H₂/Ni) → 1° 胺 RCH₂NH₂ (增 1 个碳)")


ALL = {
    "nas_general": nas_general,
    "ester_bac2": ester_bac2,
    "claisen": claisen,
    "malonic": malonic,
    "acetoacetic": acetoacetic,
    "hofmann_degradation": hofmann_degradation,
    "gabriel": gabriel,
    "reactivity": reactivity,
    "acyl_network": acyl_network,
    "reduction": reduction,
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
