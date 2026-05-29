"""Mechanism renderer for ch12 羧酸 (carboxylic acids).

Writes PNG+SVG step images into 复习全站/img/ as ch12_*.

  python _render_ch12.py
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

def _clean(s: str) -> str:
    return s.translate(_SUB)

def step(name: str, before: str, after: str, label: str, size=(860, 230)) -> None:
    out = IMG / f"{name}.png"
    try:
        render_reaction(f"{before}>>{after}", out, size=size, reagent=_clean(label))
        print(f"  OK  {name}")
    except Exception as e:
        print(f"  ERR {name}: {e}")
        raise

def mol(name: str, smiles: str, legend: str = "", size=(380, 230)) -> None:
    out = IMG / f"{name}.png"
    try:
        render_molecule(smiles, out, size=size, legend=_clean(legend))
        print(f"  OK  {name}")
    except Exception as e:
        print(f"  ERR {name}: {e}")
        raise


# ============================================================
# A. 反应总览图
# ============================================================
def overview() -> None:
    print("[ch12] overview reactions")
    # 成盐
    step("ch12_salt", "CC(=O)O.[OH-]", "CC(=O)[O-].O",
         "成盐: RCOOH + NaOH → RCOO⁻Na⁺ (溶于水, 强于碳酸可放 CO₂)")
    # Fischer 酯化 总览
    step("ch12_ester_overall", "CC(=O)O.OC", "CC(=O)OC.O",
         "Fischer 酯化总览: 乙酸 + 甲醇 ⇌(H⁺) 乙酸甲酯 + H₂O (可逆)")
    # 成酰氯 总览
    step("ch12_socl2_overall", "CCC(=O)O", "CCC(=O)Cl",
         "成酰氯: RCOOH + SOCl₂ → RCOCl + SO₂↑ + HCl↑")
    # 成酸酐 总览 (脱水)
    step("ch12_anh_overall", "CC(=O)O.CC(=O)O", "CC(=O)OC(C)=O.O",
         "成酸酐: 2 RCOOH ⟶(P₂O₅/Δ) (RCO)₂O + H₂O")
    # LiAlH4 还原
    step("ch12_lialh4", "CCCC(=O)O", "CCCCO",
         "还原: RCOOH ⟶(① LiAlH₄ ② H₃O⁺) RCH₂OH (1° 醇; NaBH₄ 不还原羧酸)")
    # HVZ 总览
    step("ch12_hvz_overall", "CCC(=O)O", "CC(Br)C(=O)O",
         "HVZ α-溴代: RCH₂COOH ⟶(① Br₂/P ② H₂O) R-CHBr-COOH")
    # 脱羧 总览
    step("ch12_decarb_overall", "CC(=O)CC(=O)O", "CC(C)=O.O=C=O",
         "脱羧: β-酮酸 ⟶(Δ) 酮 + CO₂↑ (β-C 上有 C=O/COOH 才易脱羧)")


# ============================================================
# B. Fischer 酯化 机理 (加成-消除, AAC2)
# ============================================================
def fischer() -> None:
    print("[ch12] Fischer 酯化 机理")
    acid    = "CC(=O)O"
    prot    = "CC(=[OH+])O"                  # 羰基 O 质子化
    tetneut = "CC(O)(O)[O+](C)[H]"           # 甲醇加成后中间体(质子在 OMe 的 O 上)
    tet     = "CC(O)(O)OC"                    # 四面体中间体(中性, 质子转移后)
    leave   = "CC(O)([OH2+])OC"              # 一个 OH 被质子化 → 变好离去基 (=离去的 H2O 含原羰基的 O)
    estprot = "CC(=[OH+])OC"                  # 失水后氧鎓离子
    ester   = "CC(=O)OC"
    step("ch12_fischer_s1", acid, prot,
         "Step 1: H⁺ 质子化羰基 O → 羰基 C 更缺电子 (亲电活化)")
    step("ch12_fischer_s2", f"{prot}.OC", tet,
         "Step 2: 甲醇 O 亲核加成到羰基 C + 质子转移 → 四面体中间体")
    step("ch12_fischer_s3", tet, leave,
         "Step 3: 原羧基的一个 OH 被质子化 → 变成 H₂O 这个好离去基")
    step("ch12_fischer_s4", leave, estprot,
         "Step 4: 消除 H₂O (¹⁸O 标记证明: 走掉的 O 来自原羧酸 C-OH, 羰基 O 留在酯里)")
    step("ch12_fischer_s5", estprot, ester,
         "Step 5: 失 H⁺ → 乙酸甲酯 (再生 H⁺ 催化剂, 全程可逆)")
    # 18O 示踪对照
    step("ch12_fischer_18O_proof", "CC(=O)O.[18OH]C", "CC(=O)[18O]C.O",
         "¹⁸O 示踪: 用 ¹⁸O 标记的醇, ¹⁸O 出现在酯里 → 断的是酰基 C-OH 键, 不是醇 O-H")


# ============================================================
# C. 成酰氯 (SOCl2) 机理
# ============================================================
def socl2() -> None:
    print("[ch12] SOCl₂ 成酰氯 机理")
    acid    = "CCC(=O)O"
    chloro  = "CCC(=O)OS(=O)Cl"              # 氯代亚硫酸酯 (混合酐式中间体)
    tet     = "CCC([O-])(Cl)OS(=O)[Cl]"      # Cl⁻ 加成的四面体中间体(示意)
    acl     = "CCC(=O)Cl"
    step("ch12_socl2_s1", f"{acid}.O=S(Cl)Cl", chloro,
         "Step 1: 羧基 O 进攻 SOCl₂ 的 S → 氯代亚硫酸酯 R-C(=O)-O-S(=O)Cl + HCl")
    step("ch12_socl2_s2", chloro, tet,
         "Step 2: 离去的 Cl⁻ 回头从背面进攻羰基 C → 四面体中间体")
    step("ch12_socl2_s3", tet, f"{acl}.O=S=O",
         "Step 3: -OSOCl 离去并碎成 SO₂↑+Cl⁻ → 酰氯 (副产物全为气体, 易纯化)")


# ============================================================
# D. HVZ α-溴代 机理 (经酰溴的烯醇)
# ============================================================
def hvz() -> None:
    print("[ch12] HVZ α-溴代 机理")
    acid    = "CCC(=O)O"
    acbr    = "CCC(=O)Br"                     # 酰溴 (P/Br2 先把少量酸变酰溴)
    enol    = "CC=C(O)Br"                     # 酰溴的烯醇式 (α-H 才活泼)
    brac    = "CC(Br)C(=O)Br"                 # α-溴代酰溴
    prod    = "CC(Br)C(=O)O"                  # 水解(或与原酸交换)得 α-溴酸
    step("ch12_hvz_s1", f"{acid}.[P]", acbr,
         "Step 1: P + Br₂ 生成 PBr₃, 把羧酸转成酰溴 RCH₂COBr (酰溴 α-H 比酸活泼得多)")
    step("ch12_hvz_s2", acbr, enol,
         "Step 2: 酰溴烯醇化 → 烯醇 (这是 HVZ 的关键: 只有烯醇能被 Br₂ 进攻)")
    step("ch12_hvz_s3", f"{enol}.BrBr", f"{brac}.Br",
         "Step 3: 烯醇 C=C 亲核进攻 Br₂ → α-溴代酰溴 + HBr")
    step("ch12_hvz_s4", f"{brac}.O", f"{prod}.Br",
         "Step 4: 水解(或与未反应的酸交换 Br) → α-溴代羧酸 (循环出酰溴继续反应)")


# ============================================================
# E. 脱羧 机理 (六元环过渡态) — β-酮酸 & 丙二酸
# ============================================================
def decarb() -> None:
    print("[ch12] 脱羧 六元环过渡态")
    # β-酮酸: 乙酰乙酸 → 丙酮 + CO2
    bka     = "CC(=O)CC(=O)O"                 # 乙酰乙酸 (3-氧代丁酸)
    enol    = "CC(O)=C.O=C=O"                 # 六元环 TS 直接给出烯醇 + CO2
    acetone = "CC(C)=O"
    step("ch12_decarb_s1", bka, enol,
         "Step 1: β-酮酸经六元环过渡态 — 羧基 O-H 的 H 跨环转给酮 O, C-C 断裂放 CO₂ → 丙酮烯醇式")
    step("ch12_decarb_s2", "CC(O)=C", acetone,
         "Step 2: 烯醇 → 酮 互变异构 → 丙酮 (最终产物)")
    # 丙二酸: 一元化后脱羧给乙酸
    malonic = "OC(=O)CC(=O)O"
    aaenol  = "C=C(O)O.O=C=O"                 # 乙酸的烯醇式 + CO2
    aa      = "CC(=O)O"
    step("ch12_decarb_mal_s1", malonic, aaenol,
         "丙二酸 Step 1: 一个 COOH 当作 β-位的羰基, 六元环 TS 脱一分子 CO₂ → 乙酸烯醇式")
    step("ch12_decarb_mal_s2", "C=C(O)O", aa,
         "丙二酸 Step 2: 烯醇 → 互变 → 乙酸 (只脱掉一个 COOH; 故丙二酸二乙酯合成法靠这步)")


# ============================================================
# F. 二元酸受热规律 (Blanc 规则)
# ============================================================
def diacid() -> None:
    print("[ch12] 二元酸受热")
    # 乙二酸/丙二酸 → 脱羧
    step("ch12_diacid_C2", "OC(=O)C(=O)O", "OC=O.O=C=O",
         "乙二酸(草酸,2C)/丙二酸(3C) 受热 → 脱羧 (失 CO₂): 草酸→甲酸+CO₂")
    step("ch12_diacid_C3", "OC(=O)CC(=O)O", "CC(=O)O.O=C=O",
         "丙二酸(3C) 受热 → 脱羧 → 乙酸 + CO₂")
    # 丁二酸/戊二酸 → 脱水成环酐 (5/6 元)
    step("ch12_diacid_C4", "OC(=O)CCC(=O)O", "O=C1CCC(=O)O1.O",
         "丁二酸(琥珀酸,4C) 受热 → 脱水成 五元环酐 (丁二酸酐)")
    step("ch12_diacid_C5", "OC(=O)CCCC(=O)O", "O=C1CCCC(=O)O1.O",
         "戊二酸(5C) 受热 → 脱水成 六元环酐 (戊二酸酐)")
    # 己二酸/庚二酸 → 脱水+脱羧成环酮
    step("ch12_diacid_C6", "OC(=O)CCCCC(=O)O", "O=C1CCCC1.O=C=O.O",
         "己二酸(6C)/庚二酸(7C) 受热(Ba(OH)₂/Δ) → 同时脱水脱羧成 环酮: 己二酸→环戊酮")


# ============================================================
# G. 鉴别用单分子
# ============================================================
def ident() -> None:
    print("[ch12] 鉴别用结构")
    mol("ch12_formic_acid", "OC=O", "甲酸 HCOOH: 有 -CHO 结构片段 → 能还原 Tollens 试剂(银镜)")
    mol("ch12_oxalic_acid", "OC(=O)C(=O)O", "草酸: 使 KMnO₄ 褪色(被氧化成 CO₂); 受热脱羧")
    mol("ch12_acetic_acid", "CC(=O)O", "乙酸: NaHCO₃ 中放 CO₂ 气泡 (羧酸通性, 区别于酚)")


if __name__ == "__main__":
    overview()
    fischer()
    socl2()
    hvz()
    decarb()
    diacid()
    ident()
    print(f"\nAll done. Images in: {IMG}")
