import sys, math, datetime
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from ztdata import STAGES, STAGE_MEANING, CORE, APPENDIX, EXAMPLE
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.chart import BarChart, Reference
from openpyxl.comments import Comment

FONT = "Arial"
NAVY = "1F2A44"; INK = "1A1F2B"; MUTED = "5B6676"
INPUT_FILL = PatternFill("solid", fgColor="FFF2CC")
HEAD_FILL = PatternFill("solid", fgColor=NAVY)
SUB_FILL = PatternFill("solid", fgColor="E6EAF2")
CALC_FILL = PatternFill("solid", fgColor="F4F6F9")
thin = Side(style="thin", color="D5DAE3")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
WRAP = Alignment(wrap_text=True, vertical="top")
WRAPC = Alignment(wrap_text=True, vertical="top", horizontal="center")

def f(size=10, bold=False, color=INK, italic=False):
    return Font(name=FONT, size=size, bold=bold, color=color, italic=italic)

def head(ws, row, headers, widths=None):
    for c, h in enumerate(headers, 1):
        cell = ws.cell(row=row, column=c, value=h)
        cell.font = f(10, True, "FFFFFF"); cell.fill = HEAD_FILL; cell.alignment = WRAPC; cell.border = BORDER
    if widths:
        for c, w in enumerate(widths, 1):
            ws.column_dimensions[ws.cell(row=row, column=c).column_letter].width = w
    ws.row_dimensions[row].height = 30

def lines(text, width):
    if not text: return 1
    return max(1, math.ceil(len(str(text)) / max(1, width * 1.05)))

def build(example, path):
    wb = Workbook()
    start = wb.active; start.title = "Start here"
    st = wb.create_sheet("Settings")
    asm = wb.create_sheet("Assessment")
    apx = wb.create_sheet("Appendix A Payments")
    summ = wb.create_sheet("Summary")
    mm = wb.create_sheet("Maturity map")
    rm = wb.create_sheet("Roadmap")
    rs = wb.create_sheet("Roadmap steps")
    for ws in wb.worksheets:
        ws.sheet_view.showGridLines = False

    # ---------------- Settings ----------------
    st.column_dimensions["A"].width = 40; st.column_dimensions["B"].width = 34; st.column_dimensions["C"].width = 90
    st["A1"] = "Settings"; st["A1"].font = f(16, True, NAVY)
    st["A2"] = "Yellow cells are inputs. Everything else in the workbook reads from here."; st["A2"].font = f(10, color=MUTED)
    rows = [
        (3, "Organisation", "Example organisation (illustrative values)" if example else None),
        (4, "Assessment date", datetime.date(2026, 10, 12) if example else None),
        (5, "Assessed by", "Security architecture" if example else None),
        (6, "Default target stage", "Advanced"),
        (8, "Include Appendix A (payments) in the roadmap", "No"),
        (9, "Delay low-priority steps by (waves)", 1),
    ]
    for r, label, val in rows:
        st.cell(row=r, column=1, value=label).font = f(10, True)
        c = st.cell(row=r, column=2, value=val); c.fill = INPUT_FILL; c.font = f(10, color="0000FF"); c.border = BORDER
    st["B4"].number_format = "yyyy-mm-dd"
    st["A7"] = "Default target score (calculated)"; st["A7"].font = f(10, True)
    st["B7"] = "=IFERROR(MATCH(B6,$A$12:$A$15,0),3)"; st["B7"].font = f(10); st["B7"].fill = CALC_FILL; st["B7"].border = BORDER
    st["C6"] = "Used wherever a function has no target override. CISA expects most organisations to aim for Advanced first; Optimal only where the risk justifies it."
    st["C8"] = "Yes adds Appendix A steps to the roadmap. Appendix scores never change the core maturity figures."
    st["C9"] = "Low-priority functions start one wave later by default. Set 0 to treat them like Medium."
    for a in ("C6", "C8", "C9"): st[a].font = f(9, color=MUTED); st[a].alignment = WRAP

    st["A11"] = "Stage"; st["B11"] = "Score"; st["C11"] = "What the stage means (paraphrased from CISA ZTMM v2.0)"
    for c in ("A11", "B11", "C11"):
        st[c].font = f(10, True, "FFFFFF"); st[c].fill = HEAD_FILL; st[c].border = BORDER
    for i, (s, m) in enumerate(zip(STAGES, STAGE_MEANING)):
        r = 12 + i
        st.cell(row=r, column=1, value=s).font = f(10, True)
        st.cell(row=r, column=2, value=i + 1).font = f(10)
        c = st.cell(row=r, column=3, value=m); c.font = f(10); c.alignment = WRAP
        for col in range(1, 4): st.cell(row=r, column=col).border = BORDER
        st.row_dimensions[r].height = 28

    st["A18"] = "Wave number"; st["B18"] = "Wave label (editable)"; st["C18"] = "Meaning"
    for c in ("A18", "B18", "C18"):
        st[c].font = f(10, True, "FFFFFF"); st[c].fill = HEAD_FILL; st[c].border = BORDER
    waves = [("Wave 1: 0-6 months", "Start now. Foundations and high-priority first steps."),
             ("Wave 2: 6-12 months", "Second steps, and steps waiting on wave 1 prerequisites."),
             ("Wave 3: 12-24 months", "Larger programmes and steps with several prerequisites."),
             ("Wave 4: 24 months +", "Horizon items. Anything further out is also placed here.")]
    for i, (lab, mean) in enumerate(waves):
        r = 19 + i
        st.cell(row=r, column=1, value=i).font = f(10)
        c = st.cell(row=r, column=2, value=lab); c.fill = INPUT_FILL; c.font = f(10, color="0000FF")
        st.cell(row=r, column=3, value=mean).font = f(10)
        for col in range(1, 4): st.cell(row=r, column=col).border = BORDER

    st["A25"] = "Priority"; st["B25"] = "Sort rank"
    for c in ("A25", "B25"):
        st[c].font = f(10, True, "FFFFFF"); st[c].fill = HEAD_FILL; st[c].border = BORDER
    for i, p in enumerate(["High", "Medium", "Low"]):
        st.cell(row=26 + i, column=1, value=p).font = f(10); st.cell(row=26 + i, column=2, value=i + 1).font = f(10)
        for col in (1, 2): st.cell(row=26 + i, column=col).border = BORDER

    STG = "Settings!$A$12:$A$15"; DEFT = "Settings!$B$7"; INCL = "Settings!$B$8"; LOWD = "Settings!$B$9"
    WLAB = "Settings!$B$19:$B$22"; PRI = "Settings!$A$26:$A$28"

    dv_stage_s = DataValidation(type="list", formula1=STG, allow_blank=True); st.add_data_validation(dv_stage_s); dv_stage_s.add("B6")
    dv_yn_s = DataValidation(type="list", formula1='"Yes,No"', allow_blank=False); st.add_data_validation(dv_yn_s); dv_yn_s.add("B8")
    dv_num = DataValidation(type="whole", operator="between", formula1="0", formula2="3"); st.add_data_validation(dv_num); dv_num.add("B9")

    # ---------------- Assessment sheets ----------------
    headers = ["Area", "ID", "Function", "Question", "Traditional", "Initial", "Advanced", "Optimal",
               "Current stage", "Target override", "Priority", "Applicable", "Owner", "Evidence and notes",
               "Current score", "Target score", "Gap", "Status", "Next step to the following stage", "Next step lands in"]
    widths = [16, 7, 22, 30, 30, 30, 30, 30, 13, 13, 10, 11, 16, 30, 8, 8, 6, 18, 48, 18]
    owners = {"Identity": "IAM lead", "Devices": "End-user computing", "Networks": "Network security",
              "Applications and workloads": "Application security", "Data": "Data protection",
              "Cross-cutting capabilities": "CISO office", "Appendix A: Treasury and payments": "Treasury operations"}

    loc = {}   # id -> (sheet title, row)
    fn_index = {}
    RS_N = 151

    def write_assessment(ws, title, banner, groups):
        ws["A1"] = title; ws["A1"].font = f(16, True, NAVY)
        ws["A2"] = banner; ws["A2"].font = f(10, True, "9C5700" if example else MUTED)
        ws["A3"] = "Yellow columns I to N are inputs. Pick the stage that best matches today, with evidence. Leave Target override blank to use the default on Settings."
        ws["A3"].font = f(9, color=MUTED)
        head(ws, 4, headers, widths)
        r = 5
        for area, fns in groups:
            for fn in fns:
                vals = [area, fn["id"], fn["name"], fn["q"]] + fn["stages"]
                for c, v in enumerate(vals, 1):
                    cell = ws.cell(row=r, column=c, value=v)
                    cell.font = f(9 if c >= 5 else 10, bold=(c == 3)); cell.alignment = WRAP; cell.border = BORDER
                cur = tgt = pri = own = note = None
                if example and fn["id"] in EXAMPLE:
                    cur, tgt, pri = EXAMPLE[fn["id"]]; own = owners[area]
                elif not example and fn["id"] == "ID-1":
                    cur, pri, own = "Initial", "High", "IAM lead"
                    note = "EXAMPLE ROW: replace with your own rating and evidence (e.g. MFA enforced for all staff via Conditional Access; FIDO2 only for admins)."
                inputs = [cur, tgt, pri or "Medium", "Yes", own, note]
                for c, v in enumerate(inputs, 9):
                    cell = ws.cell(row=r, column=c, value=v)
                    cell.fill = INPUT_FILL; cell.font = f(10, color="0000FF"); cell.border = BORDER
                    cell.alignment = WRAP if c == 14 else Alignment(vertical="top")
                RSs = "'Roadmap steps'"
                forms = {
                    15: f'=IF(OR(L{r}="No",I{r}=""),0,IFERROR(MATCH(I{r},{STG},0),0))',
                    16: f'=IF(O{r}=0,0,IF(J{r}="",{DEFT},IFERROR(MATCH(J{r},{STG},0),{DEFT})))',
                    17: f'=MAX(0,P{r}-O{r})',
                    18: f'=IF(L{r}="No","Not applicable",IF(I{r}="","Not rated",IF(Q{r}=0,"At or above target","Gap of "&Q{r}&IF(Q{r}=1," stage"," stages"))))',
                    19: f'=IF(O{r}=0,"",IF(O{r}>=4,"At Optimal: sustain and monitor.",IFERROR(INDEX({RSs}!$H$5:$H${RS_N},MATCH(B{r}&"|"&(O{r}+1),{RSs}!$A$5:$A${RS_N},0)),"")))',
                    20: f'=IF(O{r}=0,"",IFERROR(INDEX({RSs}!$V$5:$V${RS_N},MATCH(B{r}&"|"&(O{r}+1),{RSs}!$A$5:$A${RS_N},0)),""))',
                }
                for c, fm in forms.items():
                    cell = ws.cell(row=r, column=c, value=fm)
                    cell.font = f(10 if c < 19 else 9); cell.fill = CALC_FILL; cell.border = BORDER
                    cell.alignment = WRAP if c >= 18 else Alignment(vertical="top", horizontal="center")
                n = max(lines(fn["name"], 22), lines(fn["q"], 30), *[lines(s, 30) for s in fn["stages"]],
                        max(lines(x, 48) for x in fn["next"]), lines(note, 30))
                ws.row_dimensions[r].height = max(30, 12.5 * n + 4)
                loc[fn["id"]] = (ws.title, r); fn_index[fn["id"]] = (area, fn)
                r += 1
        last = r - 1
        dv_stage = DataValidation(type="list", formula1=STG, allow_blank=True, showErrorMessage=True,
                                  error="Choose Traditional, Initial, Advanced or Optimal.")
        dv_pri = DataValidation(type="list", formula1='"High,Medium,Low"', allow_blank=False)
        dv_yn = DataValidation(type="list", formula1='"Yes,No"', allow_blank=False)
        for dv in (dv_stage, dv_pri, dv_yn): ws.add_data_validation(dv)
        dv_stage.add(f"I5:J{last}"); dv_pri.add(f"K5:K{last}"); dv_yn.add(f"L5:L{last}")
        ws.freeze_panes = "D5"
        ws.auto_filter.ref = f"A4:T{last}"
        # status colouring
        ws.conditional_formatting.add(f"R5:R{last}", FormulaRule(formula=[f'LEFT($R5,3)="Gap"'], fill=PatternFill("solid", fgColor="FBE3D6"), font=Font(name=FONT, color="9C3B12", bold=True)))
        ws.conditional_formatting.add(f"R5:R{last}", FormulaRule(formula=[f'$R5="At or above target"'], fill=PatternFill("solid", fgColor="E2EFDA"), font=Font(name=FONT, color="2E6B30")))
        # highlight the chosen current stage descriptor
        for i, colL in enumerate("EFGH"):
            ws.conditional_formatting.add(f"{colL}5:{colL}{last}", FormulaRule(formula=[f"$O5={i+1}"], fill=PatternFill("solid", fgColor="C9D4F2"), font=Font(name=FONT, size=9, bold=True, color=NAVY)))
            ws.conditional_formatting.add(f"{colL}5:{colL}{last}", FormulaRule(formula=[f"AND($O5>0,{i+1}>$O5,{i+1}<=$P5)"], fill=PatternFill("solid", fgColor="FFF7E0")))
        ws.page_setup.orientation = "landscape"; ws.page_setup.fitToWidth = 1; ws.page_setup.fitToHeight = 0
        ws.sheet_properties.pageSetUpPr.fitToPage = True
        return last

    banner_core = ("ILLUSTRATIVE EXAMPLE VALUES, not a real assessment. Use the blank workbook for your own."
                   if example else "Rate each function against CISA ZTMM v2.0. Row ID-1 holds an example rating: replace it.")
    last_core = write_assessment(asm, "Assessment: CISA Zero Trust Maturity Model v2.0", banner_core, CORE)
    last_apx = write_assessment(apx, "Appendix A: Treasury and payments overlay",
                                ("ILLUSTRATIVE EXAMPLE VALUES. " if example else "") +
                                "Optional. Not part of CISA ZTMM; scored separately and included in the roadmap only if Settings says Yes.",
                                [APPENDIX])
    # stage-descriptor legend
    for ws in (asm, apx):
        ws["E3"] = "Blue cell = current stage. Pale yellow = stages between current and target."
        ws["E3"].font = f(9, True, NAVY)

    # ---------------- Roadmap steps (calculation) ----------------
    rs["A1"] = "Roadmap steps (calculation sheet)"; rs["A1"].font = f(16, True, NAVY)
    rs["A2"] = ("One row per function per stage move. A step is in scope when the function is applicable, rated, and the stage lies above current and at or below target. "
                "Wave = stage moves already needed for this function, plus the low-priority delay, but never before the previous stage of the same function or before a prerequisite reaches the same stage (or its own target, if lower).")
    rs["A2"].font = f(9, color=MUTED); rs["A2"].alignment = WRAP; rs.merge_cells("A2:Y2"); rs.row_dimensions[2].height = 42
    rhead = ["Key", "ID", "Area", "Function", "From", "To", "To score", "Action", "Current score", "Target score",
             "Applicable", "Priority", "Included", "In scope", "Base wave", "After previous stage", "Prerequisite 1",
             "Wait for prerequisite 1", "Prerequisite 2", "Wait for prerequisite 2", "Wave", "Wave label", "Waiting on", "Sort key", "Owner"]
    rwidths = [9, 7, 16, 22, 11, 11, 7, 50, 8, 8, 9, 9, 9, 9, 8, 9, 10, 10, 10, 10, 7, 20, 14, 10, 16]
    head(rs, 4, rhead, rwidths)
    rows_list = []
    for area, fns in CORE + [APPENDIX]:
        for fn in fns:
            for s in (2, 3, 4):
                rows_list.append((area, fn, s))
    assert len(rows_list) == RS_N - 4, len(rows_list)
    R = f"$5:$"  # unused
    for i, (area, fn, s) in enumerate(rows_list):
        r = 5 + i
        sh, ar = loc[fn["id"]]; shq = f"'{sh}'"
        is_apx = fn["id"].startswith("PA-")
        deps = fn["deps"] + [None, None]
        static = [f'{fn["id"]}|{s}', fn["id"], area, fn["name"], STAGES[s - 2], STAGES[s - 1], s, fn["next"][s - 2]]
        for c, v in enumerate(static, 1):
            cell = rs.cell(row=r, column=c, value=v); cell.font = f(9); cell.border = BORDER
            cell.alignment = WRAP if c in (4, 8) else Alignment(vertical="top")
        rng = lambda col: f"${col}$5:${col}${RS_N}"
        def depf(dcol, d):
            if not d:
                return "=0"
            dsh, drow = loc[d]; dq = f"'{dsh}'"
            dc, dt, da = f"{dq}!$O${drow}", f"{dq}!$P${drow}", f"{dq}!$L${drow}"
            dinc = f'{INCL}' if d.startswith("PA-") else '"Yes"'
            return (f'=IF(OR(N{r}<>"Yes",{dc}=0,{da}="No",{dc}>=MIN(G{r},{dt}),{dinc}<>"Yes"),0,'
                    f'IFERROR(INDEX({rng("U")},MATCH({dcol}{r}&"|"&MIN(G{r},{dt}),{rng("A")},0))+1,0))')
        forms = {
            9: f"={shq}!$O${ar}",
            10: f"={shq}!$P${ar}",
            11: f"={shq}!$L${ar}",
            12: f'=IF({shq}!$K${ar}="","Medium",{shq}!$K${ar})',
            13: f"={INCL}" if is_apx else "Yes",
            14: f'=IF(AND(M{r}="Yes",K{r}<>"No",I{r}>0,G{r}>I{r},G{r}<=J{r}),"Yes","No")',
            15: f'=IF(N{r}="Yes",(G{r}-I{r}-1)+IF(L{r}="Low",{LOWD},0),"")',
            16: f'=IF(N{r}<>"Yes","",IF(G{r}-1>I{r},IFERROR(INDEX({rng("U")},MATCH(B{r}&"|"&(G{r}-1),{rng("A")},0))+1,0),0))',
            17: deps[0] or "",
            18: depf("Q", deps[0]),
            19: deps[1] or "",
            20: depf("S", deps[1]),
            21: f'=IF(N{r}="Yes",MIN(MAX(Settings!$A$19:$A$22),MAX(O{r},P{r},R{r},T{r})),"")',
            22: f'=IF(U{r}="","",INDEX({WLAB},U{r}+1))',
            23: f'=IF(N{r}<>"Yes","",TRIM(IF(R{r}>MAX(O{r},P{r}),Q{r},"")&" "&IF(T{r}>MAX(O{r},P{r}),S{r},"")))',
            24: f'=IF(N{r}="Yes",U{r}*10000+MATCH(L{r},{PRI},0)*1000+ROW(),"")',
            25: f'=IF({shq}!$M${ar}="","",{shq}!$M${ar})',
        }
        for c, v in forms.items():
            cell = rs.cell(row=r, column=c, value=v); cell.font = f(9); cell.border = BORDER
            cell.alignment = Alignment(vertical="top", horizontal="center") if c not in (22, 23, 25) else Alignment(vertical="top", wrap_text=True)
            if c != 17 and c != 19: cell.fill = CALC_FILL
        rs.row_dimensions[r].height = max(24, 12 * max(lines(fn["next"][s - 2], 50), lines(fn["name"], 22)) + 4)
    rs.freeze_panes = "E5"
    rs.auto_filter.ref = f"A4:Y{RS_N}"
    rs.conditional_formatting.add(f"N5:N{RS_N}", CellIsRule(operator="equal", formula=['"Yes"'], fill=PatternFill("solid", fgColor="E2EFDA")))

    # ---------------- Roadmap (ordered plan) ----------------
    rm["A1"] = "Zero trust improvement roadmap"; rm["A1"].font = f(16, True, NAVY)
    rm["A2"] = ("Generated from the Assessment. Ordered by wave, then priority, then framework order. Each row moves one function up one stage. "
                "'Waiting on' names prerequisites that pushed the step later. Edit ratings, targets or priorities, not this sheet.")
    rm["A2"].font = f(9, color=MUTED); rm["A2"].alignment = WRAP; rm.merge_cells("A2:J2"); rm.row_dimensions[2].height = 30
    phead = ["#", "Wave", "Area", "ID", "Function", "Move", "Action", "Priority", "Owner", "Waiting on", "Sort key", "Step row", "Wave no.", "k"]
    pwidths = [5, 20, 18, 7, 24, 24, 60, 9, 18, 14, 8, 8, 8, 5]
    head(rm, 4, phead, pwidths)
    RSq = "'Roadmap steps'"
    for k in range(1, RS_N - 3):
        r = 4 + k
        rng = lambda col: f"{RSq}!${col}$5:${col}${RS_N}"
        forms = {
            14: k,
            11: f'=IFERROR(SMALL({rng("X")},N{r}),"")',
            12: f'=IF(K{r}="","",MATCH(K{r},{rng("X")},0))',
            13: f'=IF(L{r}="","",INDEX({rng("U")},L{r}))',
            1: f'=IF(L{r}="","",N{r})',
            2: f'=IF(L{r}="","",INDEX({rng("V")},L{r}))',
            3: f'=IF(L{r}="","",INDEX({rng("C")},L{r}))',
            4: f'=IF(L{r}="","",INDEX({rng("B")},L{r}))',
            5: f'=IF(L{r}="","",INDEX({rng("D")},L{r}))',
            6: f'=IF(L{r}="","",INDEX({rng("E")},L{r})&" to "&INDEX({rng("F")},L{r}))',
            7: f'=IF(L{r}="","",INDEX({rng("H")},L{r}))',
            8: f'=IF(L{r}="","",INDEX({rng("L")},L{r}))',
            9: f'=IF(L{r}="","",INDEX({rng("Y")},L{r}))',
            10: f'=IF(L{r}="","",INDEX({rng("W")},L{r}))',
        }
        for c, v in forms.items():
            cell = rm.cell(row=r, column=c, value=v); cell.font = f(9, bold=(c in (2, 5))); cell.border = BORDER
            cell.alignment = Alignment(vertical="top", wrap_text=True)
        rm.row_dimensions[r].height = 40
    for colL in ("K", "L", "M", "N"):
        rm.column_dimensions[colL].hidden = True
    wave_fills = ["DCE6F7", "EAF0FA", "F3F5F9", "FAFAFB"]
    for w, col in enumerate(wave_fills):
        rm.conditional_formatting.add(f"A5:J{RS_N}", FormulaRule(formula=[f'AND($M5<>"",$M5={w})'], fill=PatternFill("solid", fgColor=col)))
    rm.conditional_formatting.add(f"H5:H{RS_N}", CellIsRule(operator="equal", formula=['"High"'], font=Font(name=FONT, size=9, bold=True, color="9C3B12")))
    rm.freeze_panes = "A5"
    rm.auto_filter.ref = f"A4:J{RS_N}"
    rm.page_setup.orientation = "landscape"; rm.page_setup.fitToWidth = 1; rm.page_setup.fitToHeight = 0
    rm.sheet_properties.pageSetUpPr.fitToPage = True

    # ---------------- Maturity map ----------------
    mm["A1"] = "Maturity map"; mm["A1"].font = f(16, True, NAVY)
    mm["A2"] = "● stage reached today     ○ stage between today and target     blank = beyond target, or not rated"
    mm["A2"].font = f(10, True, NAVY)
    head(mm, 4, ["Area", "ID", "Function", "Traditional", "Initial", "Advanced", "Optimal", "Status"], [26, 7, 34, 12, 12, 12, 12, 22])
    r = 5
    for area, fns in CORE + [APPENDIX]:
        for fn in fns:
            sh, ar = loc[fn["id"]]; shq = f"'{sh}'"
            mm.cell(row=r, column=1, value=area); mm.cell(row=r, column=2, value=fn["id"]); mm.cell(row=r, column=3, value=fn["name"])
            for k in range(1, 5):
                mm.cell(row=r, column=3 + k, value=f'=IF({shq}!$O${ar}=0,"",IF({k}<={shq}!$O${ar},2,IF({k}<={shq}!$P${ar},1,0)))')
                mm.cell(row=r, column=3 + k).number_format = '[=2]"●";[=1]"○";""'
                mm.cell(row=r, column=3 + k).alignment = Alignment(horizontal="center", vertical="center")
            mm.cell(row=r, column=8, value=f"={shq}!$R${ar}")
            for c in range(1, 9):
                mm.cell(row=r, column=c).border = BORDER
                if c not in (4, 5, 6, 7): mm.cell(row=r, column=c).font = f(10, bold=(c == 3))
            r += 1
    mm_last = r - 1
    mm.conditional_formatting.add(f"D5:G{mm_last}", CellIsRule(operator="equal", formula=["2"], fill=PatternFill("solid", fgColor="2F4A9E"), font=Font(name=FONT, color="FFFFFF", bold=True)))
    mm.conditional_formatting.add(f"D5:G{mm_last}", CellIsRule(operator="equal", formula=["1"], fill=PatternFill("solid", fgColor="FFE8B3"), font=Font(name=FONT, color="7A5200", bold=True)))
    mm.freeze_panes = "D5"

    # ---------------- Summary ----------------
    summ.column_dimensions["A"].width = 38
    for colL, w in zip("BCDEFGH", [12, 10, 14, 14, 16, 14, 16]):
        summ.column_dimensions[colL].width = w
    summ["A1"] = "Zero trust maturity summary"; summ["A1"].font = f(18, True, NAVY)
    summ["A2"] = '=IF(Settings!$B$3="","Organisation not set (Settings)",Settings!$B$3)&IF(Settings!$B$4="",""," · assessed "&TEXT(Settings!$B$4,"yyyy-mm-dd"))'
    summ["A2"].font = f(11, color=MUTED)
    A_rng, O_rng, P_rng, Q_rng = (f"Assessment!${c}$5:${c}${last_core}" for c in "AOPQ")
    X_rng = f"'Appendix A Payments'!"
    kpis = [
        ("Overall maturity, core pillars (1 to 4)", f'=IFERROR(AVERAGEIF({O_rng},">0"),0)', "0.0"),
        ("Stage fully reached (overall)", f'=IF(B4=0,"Not rated",INDEX({STG},INT(B4)))', None),
        ("Average target", f'=IFERROR(AVERAGEIF({O_rng},">0",{P_rng}),0)', "0.0"),
        ("Functions rated (of 40)", f'=COUNTIF({O_rng},">0")', "0"),
        ("Functions below target", f'=COUNTIF({Q_rng},">0")', "0"),
        ("Roadmap steps in scope", f"=COUNTIF('Roadmap steps'!$N$5:$N${RS_N},\"Yes\")", "0"),
    ]
    for i, (lab, fm, nf) in enumerate(kpis):
        r = 4 + i
        summ.cell(row=r, column=1, value=lab).font = f(10, True)
        c = summ.cell(row=r, column=2, value=fm); c.font = f(12, True, NAVY); c.border = BORDER
        if nf: c.number_format = nf
    summ["C4"] = "Average of rated, applicable functions. Unrated and not-applicable functions are excluded."
    summ["C4"].font = f(9, color=MUTED)

    summ["A11"] = "By area"; summ["A11"].font = f(12, True, NAVY)
    head(summ, 12, ["Area", "Functions", "Rated", "Average current", "Average target", "Functions below target", "Stage moves to close", "Stage fully reached"])
    summ.column_dimensions["A"].width = 38
    areas = [a for a, _ in CORE]
    for i, area in enumerate(areas + [APPENDIX[0]]):
        r = 13 + i
        is_apx = (area == APPENDIX[0])
        sh = "'Appendix A Payments'" if is_apx else "Assessment"
        last = last_apx if is_apx else last_core
        A_, O_, P_, Q_ = (f"{sh}!${c}$5:${c}${last}" for c in "AOPQ")
        label = "Appendix A: payments (not in overall)" if is_apx else area
        vals = [label,
                f'=COUNTIF({A_},"{area}")',
                f'=COUNTIFS({A_},"{area}",{O_},">0")',
                f'=IFERROR(AVERAGEIFS({O_},{A_},"{area}",{O_},">0"),0)',
                f'=IFERROR(AVERAGEIFS({P_},{A_},"{area}",{O_},">0"),0)',
                f'=COUNTIFS({A_},"{area}",{Q_},">0")',
                f'=SUMIFS({Q_},{A_},"{area}")',
                f'=IF(D{r}=0,"Not rated",INDEX({STG},INT(D{r})))']
        for c, v in enumerate(vals, 1):
            cell = summ.cell(row=r, column=c, value=v); cell.font = f(10, bold=(c == 1), italic=is_apx); cell.border = BORDER
            if c in (4, 5): cell.number_format = '0.0;-0.0;"-"'
            if c > 1: cell.alignment = Alignment(horizontal="center")
    summ.conditional_formatting.add("F13:F19", CellIsRule(operator="greaterThan", formula=["0"], font=Font(name=FONT, bold=True, color="9C3B12")))

    summ["A22"] = "Roadmap by wave"; summ["A22"].font = f(12, True, NAVY)
    head(summ, 23, ["Wave", "Steps", "High priority", "Medium", "Low"])
    summ.column_dimensions["A"].width = 38
    for w in range(4):
        r = 24 + w
        U = f"'Roadmap steps'!$U$5:$U${RS_N}"; L_ = f"'Roadmap steps'!$L$5:$L${RS_N}"
        vals = [f"=Settings!$B${19+w}", f"=COUNTIF({U},{w})", f'=COUNTIFS({U},{w},{L_},"High")',
                f'=COUNTIFS({U},{w},{L_},"Medium")', f'=COUNTIFS({U},{w},{L_},"Low")']
        for c, v in enumerate(vals, 1):
            cell = summ.cell(row=r, column=c, value=v); cell.font = f(10, bold=(c == 1)); cell.border = BORDER
            if c > 1: cell.alignment = Alignment(horizontal="center")

    ch = BarChart(); ch.type = "bar"; ch.grouping = "clustered"
    ch.title = "Average maturity by area (1 Traditional, 2 Initial, 3 Advanced, 4 Optimal)"
    ch.y_axis.scaling.min = 0; ch.y_axis.scaling.max = 4; ch.y_axis.majorUnit = 1
    ch.y_axis.delete = False; ch.x_axis.delete = False
    ch.x_axis.scaling.orientation = "maxMin"
    data = Reference(summ, min_col=4, max_col=5, min_row=12, max_row=19)
    cats = Reference(summ, min_col=1, min_row=13, max_row=19)
    ch.add_data(data, titles_from_data=True); ch.set_categories(cats)
    ch.series[0].graphicalProperties.solidFill = "2F4A9E"; ch.series[0].graphicalProperties.line.solidFill = "2F4A9E"
    ch.series[1].graphicalProperties.solidFill = "F2B544"; ch.series[1].graphicalProperties.line.solidFill = "F2B544"
    ch.height = 9.5; ch.width = 20; ch.legend.position = "b"
    summ.add_chart(ch, "A30")

    # ---------------- Start here ----------------
    start.column_dimensions["A"].width = 3; start.column_dimensions["B"].width = 26; start.column_dimensions["C"].width = 100
    start["B1"] = "Zero Trust Maturity Workbook"; start["B1"].font = f(20, True, NAVY)
    start["B2"] = ("Self-assessment against the CISA Zero Trust Maturity Model v2.0, with a generated improvement roadmap. "
                   "No macros, no external links. " + ("THIS COPY HOLDS ILLUSTRATIVE EXAMPLE VALUES." if example else "Blank copy: one example row (ID-1)."))
    start["B2"].font = f(10, color="9C5700" if example else MUTED, bold=example); start.merge_cells("B2:C2")
    blocks = [
        ("How to use", None),
        ("1. Settings", "Enter organisation, date and the default target stage (Advanced unless you have a reason). Choose whether Appendix A joins the roadmap."),
        ("2. Assessment", "For each of the 40 functions, read the four stage descriptions and pick the one that matches today in Current stage. Record evidence and an owner. Set Target override where a function needs a different target from the default; mark Applicable = No if it does not apply. Set Priority (High, Medium, Low)."),
        ("3. Appendix A Payments", "Optional overlay for treasury and payments (SWIFT, bank portals, beneficiary changes). Scored the same way but kept out of the core maturity figures."),
        ("4. Summary", "Overall and per-area maturity, the gap to target, a chart, and how the roadmap spreads across waves."),
        ("5. Maturity map", "Every function on one page: where you are and how far you plan to go."),
        ("6. Roadmap", "The ordered list of improvement steps. Filter it by area, owner or wave. Each row moves one function up one stage."),
        ("Cell colours", None),
        ("Yellow, blue text", "Inputs you edit."),
        ("Grey", "Formulas. Do not overwrite; they feed the summary and roadmap."),
        ("How the roadmap is built", None),
        ("Steps", "Every stage between a function's current stage and its target becomes a step, with the action from the question bank."),
        ("Waves", "A function's first step goes in wave 1, its next in wave 2, and so on. Low priority starts one wave later (set on Settings)."),
        ("Prerequisites", "Some functions depend on others (e.g. device-based resource access needs device compliance and strong authentication). A step waits until each prerequisite reaches the same stage, or its own target if lower. 'Waiting on' shows when that happened."),
        ("Limits", "Waves are a sequencing aid, not a plan with costs or capacity. Anything beyond four waves lands in the last one. Review the order with the owners before committing to dates."),
        ("Sources and caveats", None),
        ("Framework", "CISA Zero Trust Maturity Model v2.0 (April 2023): five pillars (Identity, Devices, Networks, Applications and Workloads, Data), three cross-cutting capabilities, four stages. https://www.cisa.gov/zero-trust-maturity-model"),
        ("Wording", "Stage descriptions are paraphrased summaries written for this workbook, and the improvement actions are design recommendations, not CISA text. Check the CISA document for the full criteria before reporting results externally."),
        ("Related", "NIST SP 800-207 Zero Trust Architecture (https://csrc.nist.gov/pubs/sp/800/207/final). NSA Zero Trust Implementation Guidelines 2026 for detailed activity sequencing. Microsoft Zero Trust Assessment and Workshop (https://microsoft.github.io/zerotrustassessment/) for automated M365/Entra configuration checks: vendor material, use alongside, not as the framework."),
        ("Appendix A anchors", "SWIFT CSCF v2026 controls 2.4A (back-office data flow security) and 2.9 (transaction business controls); PSD2 dynamic linking; HKMA guidance on device-based authentication."),
    ]
    r = 4
    for k, v in blocks:
        if v is None:
            r += 1
            start.cell(row=r, column=2, value=k).font = f(12, True, NAVY)
        else:
            a = start.cell(row=r, column=2, value=k); a.font = f(10, True); a.alignment = WRAP
            b = start.cell(row=r, column=3, value=v); b.font = f(10); b.alignment = WRAP
            start.row_dimensions[r].height = max(16, 13.5 * lines(v, 100) + 3)
            if k.startswith("Yellow"):
                a.fill = INPUT_FILL; a.font = f(10, True, "0000FF")
            if k == "Grey":
                a.fill = CALC_FILL
        r += 1

    wb.active = 0
    wb.save(path)

if __name__ == "__main__":
    out = sys.argv[1]
    build(False, f"{out}/Zero-Trust-Maturity-Workbook.xlsx")
    build(True, f"{out}/Zero-Trust-Maturity-Workbook-example.xlsx")
    print("ok")
