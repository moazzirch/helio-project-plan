"""Checks that the project schedule and registers are internally consistent."""
import csv
import sys
from pathlib import Path

DOCS = Path(__file__).resolve().parent.parent / "docs"
errors = []


def load(name):
    with open(DOCS / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# Schedule: unique IDs, valid weeks, predecessors exist and finish before the task starts
schedule = load("schedule.csv")
tasks = {}
for row in schedule:
    tid = row["id"]
    if tid in tasks:
        errors.append(f"schedule: duplicate id {tid}")
    start, end = int(row["start_week"]), int(row["end_week"])
    if not (1 <= start <= end <= 18):
        errors.append(f"schedule: task {tid} has invalid weeks {start}-{end}")
    tasks[tid] = row
for tid, row in tasks.items():
    preds = [p for p in row["predecessors"].split(";") if p]
    note = row["dependency_note"]
    for p in preds:
        if p not in tasks:
            errors.append(f"schedule: task {tid} depends on unknown task {p}")
            continue
        if not note and int(tasks[p]["end_week"]) >= int(row["start_week"]):
            errors.append(f"schedule: task {tid} starts before predecessor {p} finishes")

# Risk register: valid ranges and EMV = probability x impact
risks = load("risk_register.csv")
total_initial = total_residual = 0.0
for r in risks:
    p, rp = float(r["probability"]), float(r["residual_probability"])
    impact, emv, score = float(r["impact_aud"]), float(r["initial_emv"]), int(r["impact_score"])
    if not (0 < p <= 1 and 0 <= rp <= p):
        errors.append(f"risk: {r['id']} has invalid probabilities")
    if not 1 <= score <= 5:
        errors.append(f"risk: {r['id']} impact score must be 1-5")
    if abs(p * impact - emv) > 1:
        errors.append(f"risk: {r['id']} EMV {emv} does not equal probability x impact")
    if not r["owner"].strip():
        errors.append(f"risk: {r['id']} has no owner")
    total_initial += emv
    total_residual += rp * impact

# Issue register: every issue has an owner and target
for i in load("issue_register.csv"):
    if not i["owner"].strip() or not i["target"].strip():
        errors.append(f"issue: {i['id']} needs an owner and target")

if errors:
    print("Validation failed:")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print(f"OK: {len(tasks)} schedule tasks, {len(risks)} risks checked.")
print(f"Total initial EMV: AUD {total_initial:,.0f}; residual EMV: AUD {total_residual:,.0f}")
