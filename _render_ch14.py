"""Render mechanism SVGs for ch14 胺 (含氮化合物).

Writes SVG (+ PNG) into 复习全站/img/ch14_*.svg.

  python _render_ch14.py
"""
from __future__ import annotations

import io
import sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", errors="replace")
sys.path.insert(0, r"C:/Users/FXY/.claude/skills/organic-render")
from render import render_reaction, render_molecule  # noqa: E402

HERE = Path(__file__).resolve().parent
IMG = HERE / "img"
IMG.mkdir(exist_ok=True)

# Unicode sub/superscript -> ASCII fallback (font glyphs missing on some Windows fonts).
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
    out = IMG / f"{name}.png"
    try:
        render_reaction(f"{before}>>{after}", out, size=size, reagent=_clean(label))
        print(f"  OK  {name}")
    except Exception as e:
        print(f"  ERR {name}: {e}")
        raise


def mol(name: str, smiles: str, legend: str = "", size=(380, 240)) -> None:
    out = IMG / f"{name}.png"
    try:
        render_molecule(smiles, out, size=size, legend=_clean(legend))
        print(f"  OK  {name}")
    except Exception as e:
        print(f"  ERR {name}: {e}")
        raise


# ============================================================
# ch14  胺 (含氮化合物)
# ============================================================

def diazotization() -> None:
    """重氮化: 苯胺 + NaNO2/HCl(0-5C) → 苯重氮盐 (NO+ 机理)."""
    print("[ch14] 重氮化")
    # NO+ 生成
    step("ch14_diazo_s1", "O[N+]=O.Cl", "[N+]=O.O.[Cl-]",
         "Step 1: NaNO2 + HCl → HNO2 → 亲电的 NO+ (亚硝酰正离子)")
    # 苯胺 N 进攻 NO+ → N-亚硝胺 (N-nitroso)
    step("ch14_diazo_s2", "Nc1ccccc1.[N+]=O", "O=NNc1ccccc1",
         "Step 2: 苯胺 N 孤对进攻 NO+ → N-亚硝基苯胺")
    # 互变 + 脱水 → 重氮盐
    step("ch14_diazo_s3", "O=NNc1ccccc1", "[N+](=Nc1ccccc1)O",
         "Step 3: 互变异构 → 重氮酸 (Ar-N=N-OH)")
    step("ch14_diazo_s4", "[N+](=Nc1ccccc1)O", "[N+](#N)c1ccccc1.O",
         "Step 4: H+ 质子化 + 脱水 → 芳基重氮盐 Ar-N2+ (0-5C 稳定)")
    # 总反应
    step("ch14_diazo_overall", "Nc1ccccc1", "[N+](#N)c1ccccc1",
         "总反应: 苯胺 ──NaNO2/HCl, 0-5C──► 苯重氮盐 (PhN2+ Cl-)")


def sandmeyer() -> None:
    """Sandmeyer: ArN2+ + CuX → ArX (放 N2)."""
    print("[ch14] Sandmeyer")
    diazo = "[N+](#N)c1ccccc1"
    step("ch14_sandmeyer_cucl", diazo, "Clc1ccccc1.[N]#[N]",
         "Sandmeyer (CuCl): ArN2+ → 氯苯 + N2↑")
    step("ch14_sandmeyer_cubr", diazo, "Brc1ccccc1.[N]#[N]",
         "Sandmeyer (CuBr): ArN2+ → 溴苯 + N2↑")
    step("ch14_sandmeyer_cucn", diazo, "N#Cc1ccccc1.[N]#[N]",
         "Sandmeyer (CuCN): ArN2+ → 苯甲腈 + N2↑ (引入 -CN)")
    # 其它放氮去向: KI / H3PO2 / H2O
    step("ch14_diazo_ki", diazo, "Ic1ccccc1.[N]#[N]",
         "KI (不需 Cu): ArN2+ → 碘苯 + N2↑")
    step("ch14_diazo_hydrolysis", diazo, "Oc1ccccc1.[N]#[N]",
         "H3O+ / H2O, Δ (水解): ArN2+ → 苯酚 + N2↑")
    step("ch14_diazo_h3po2", diazo, "c1ccccc1.[N]#[N]",
         "H3PO2 (次磷酸, 脱氨): ArN2+ → 苯 + N2↑ (NH2 用完即除)")


def azo_coupling() -> None:
    """偶联: ArN2+ + 酚/芳胺 → 偶氮染料 (留 N2, EAS)."""
    print("[ch14] 偶联")
    # 重氮盐 + 苯酚(碱性) → 对羟基偶氮苯
    step("ch14_coupling_phenol",
         "[N+](#N)c1ccccc1.Oc1ccccc1",
         "Oc1ccc(/N=N/c2ccccc2)cc1",
         "偶联 (弱碱中, 与酚): ArN2+ 作亲电体进攻对位 → 对羟基偶氮苯 (橙黄染料)")
    # 重氮盐 + N,N-二甲基苯胺(弱酸) → 对二甲氨基偶氮苯 (甲基橙骨架)
    step("ch14_coupling_amine",
         "[N+](#N)c1ccccc1.CN(C)c1ccccc1",
         "CN(C)c1ccc(/N=N/c2ccccc2)cc1",
         "偶联 (弱酸中, 与芳胺): → 对二甲氨基偶氮苯 (甲基橙骨架)")
    mol("ch14_azo_chromophore", "c1ccc(/N=N/c2ccccc2)cc1",
        "偶氮基 -N=N- 是发色团: 与两侧芳环共轭 → 有颜色")


def reductive_amination() -> None:
    """还原胺化: 醛酮 + 胺 → 亚胺 → 还原 → 胺."""
    print("[ch14] 还原胺化")
    # 丙酮 + 甲胺 → 半缩胺醇 → 亚胺 → 异丙基甲胺
    step("ch14_redamin_s1", "CC(C)=O.NC", "CC(C)(O)NC",
         "Step 1: 醛酮 + 1° 胺 亲核加成 → 半缩胺醇 (氨基醇)")
    step("ch14_redamin_s2", "CC(C)(O)NC", "CC(C)=NC.O",
         "Step 2: -H2O → 亚胺 (Schiff 碱, C=N)")
    step("ch14_redamin_s3", "CC(C)=NC", "CC(C)NC",
         "Step 3: NaBH3CN (或 H2/Ni) 还原 C=N → N-甲基异丙胺 (2° 胺)")
    step("ch14_redamin_overall", "CC(C)=O.NC", "CC(C)NC.O",
         "总反应: 丙酮 + 甲胺 ──NaBH3CN──► N-甲基异丙胺 (控级数, 不过烷基化)")


def hofmann_exhaustive() -> None:
    """Hofmann 彻底甲基化 + Hofmann 消除 (择多反 Saytzeff)."""
    print("[ch14] Hofmann 甲基化 + 消除")
    # 2-丁胺 → 季铵盐 → 季铵碱 → 消除
    amine = "CCC(C)N"
    step("ch14_hofmann_s1", amine, "CCC(C)[N+](C)(C)C.[I-]",
         "Step 1: 过量 CH3I 穷尽甲基化 → 季铵盐 [R-N+(CH3)3] I-")
    step("ch14_hofmann_s2", "CCC(C)[N+](C)(C)C.[I-]",
         "CCC(C)[N+](C)(C)C.[OH-]",
         "Step 2: Ag2O / H2O 把 I- 换成 OH- → 季铵碱 (强碱, 含游离 OH-)")
    step("ch14_hofmann_s3", "CCC(C)[N+](C)(C)C.[OH-]",
         "CCC=C.CN(C)C.O",
         "Step 3: Δ 加热 E2 消除 → 1-丁烯 (Hofmann 取向, 少取代) + 三甲胺 + H2O")
    # 取向对比: Hofmann vs Saytzeff
    mol("ch14_hofmann_product", "CCC=C",
        "Hofmann 主产物: 1-丁烯 (末端烯, 少取代) — 因 -NR3+ 又大又带正电")
    mol("ch14_saytzeff_minor", "CC=CC",
        "Saytzeff 次产物: 2-丁烯 (多取代) — 在季铵碱热解中反而是次要")


def gabriel() -> None:
    """Gabriel 合成纯 1° 胺."""
    print("[ch14] Gabriel")
    # 邻苯二甲酰亚胺 → K 盐 → N-烷基化 → 水解
    phth = "O=C1c2ccccc2C(=O)N1"
    step("ch14_gabriel_s1", phth, "O=C1c2ccccc2C(=O)[N-]1.[K+]",
         "Step 1: 邻苯二甲酰亚胺 + KOH → 钾盐 (N- 亲核, 共振稳定)")
    step("ch14_gabriel_s2", "O=C1c2ccccc2C(=O)[N-]1.CCCCBr",
         "O=C1c2ccccc2C(=O)N1CCCC.[Br-]",
         "Step 2: + R-X (SN2) → N-烷基邻苯二甲酰亚胺 (只接一个 R)")
    step("ch14_gabriel_s3", "O=C1c2ccccc2C(=O)N1CCCC",
         "NCCCC.O=C(O)c1ccccc1C(=O)O",
         "Step 3: 水解 (H3O+ 或 N2H4) → 纯 1° 胺 (正丁胺) + 邻苯二甲酸")
    step("ch14_gabriel_overall", "O=C1c2ccccc2C(=O)N1", "NCCCC",
         "总思路: 酰亚胺 N 只接一个 R → 水解 → 纯 1° 胺 (杜绝多烷基化)")


def preparation() -> None:
    """制备: 还原硝基/腈/酰胺."""
    print("[ch14] 制备 (还原法)")
    step("ch14_prep_nitro", "O=[N+]([O-])c1ccccc1", "Nc1ccccc1",
         "硝基还原: 硝基苯 ──Fe/HCl 或 Sn/HCl 或 H2/Ni──► 苯胺 (芳胺主路)")
    step("ch14_prep_nitrile", "CCCC#N", "CCCCCN",
         "腈还原 (增 1 碳): 丁腈 ──LiAlH4 或 H2/Ni──► 戊胺 (RCH2NH2)")
    step("ch14_prep_amide", "CCCC(N)=O", "CCCCN",
         "酰胺还原 (不增碳): 丁酰胺 ──LiAlH4──► 丁胺 (羰基碳变 CH2)")


def hinsberg() -> None:
    """Hinsberg 鉴别 1°/2°/3° 胺 (苯磺酰氯)."""
    print("[ch14] Hinsberg")
    # 1° 胺 + 苯磺酰氯 → N-单取代磺酰胺 (N-H 酸性, 溶于 NaOH)
    step("ch14_hinsberg_1",
         "CCCCN.O=S(=O)(Cl)c1ccccc1",
         "CCCCNS(=O)(=O)c1ccccc1",
         "1° 胺: → N-H 磺酰胺 (N-H 受两个吸电子拉变酸) → 溶于 NaOH (清亮)")
    # 2° 胺 → N,N-二取代磺酰胺 (无 N-H, 不溶 NaOH)
    step("ch14_hinsberg_2",
         "CCNCC.O=S(=O)(Cl)c1ccccc1",
         "CCN(CC)S(=O)(=O)c1ccccc1",
         "2° 胺: → 无 N-H 磺酰胺 → 不溶 NaOH (沉淀/油状)")
    mol("ch14_hinsberg_3", "CCN(CC)CC",
        "3° 胺: N 无 H, 不与苯磺酰氯成磺酰胺 → 不反应 (静置回收)")


def basicity() -> None:
    """碱性排序的结构基础: 苯胺孤对离域 vs 脂肪胺 +I."""
    print("[ch14] 碱性结构基础")
    mol("ch14_basicity_aniline", "Nc1ccccc1",
        "苯胺: N 孤对进入苯环共轭离域 → 不愿给质子 → 碱性最弱")
    mol("ch14_basicity_dimethylamine", "CNC",
        "二甲胺 (2°): 烷基 +I 给电子 + 铵正离子溶剂化适中 → 水溶液中最强")
    mol("ch14_basicity_pNO2aniline", "Nc1ccc([N+](=O)[O-])cc1",
        "对硝基苯胺: -NO2 吸电子再抽走孤对 → 比苯胺还弱")


ALL = {
    "diazotization": diazotization,
    "sandmeyer": sandmeyer,
    "azo_coupling": azo_coupling,
    "reductive_amination": reductive_amination,
    "hofmann_exhaustive": hofmann_exhaustive,
    "gabriel": gabriel,
    "preparation": preparation,
    "hinsberg": hinsberg,
    "basicity": basicity,
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
