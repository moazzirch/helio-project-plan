# HELIO: AI-Powered Chatbot for Customer Support Automation

Planning artefacts for the HELIO project plan (ITSU2006, Assessment 2, Option 3).

| File | Purpose |
|---|---|
| `docs/charter.md` | Project charter and scope baseline |
| `docs/schedule.csv` | WBS work packages, weeks, predecessors and leads (Table 6 of the report) |
| `docs/risk_register.csv` | Quantified risk register (Table 7) |
| `docs/issue_register.csv` | Issue log (Table 9) |
| `docs/architecture_decision.md` | Architecture decision record |
| `docs/change_control.md` | Change request and change management process |
| `docs/changes/CR-001.md` | Worked change request CR-001 |
| `.github/pull_request_template.md` | Checklist for every pull request |
| `.github/workflows/validate-registers.yml` | Runs the validation script on every push and pull request |
| `scripts/validate_registers.py` | Checks the schedule and registers for consistency |

## Working rules

- `main` is protected. Every change goes through a branch and a pull request approved by the other member.
- Each pull request links to a change ID or issue where relevant.
- Releases are tagged; the submitted version is `v1.0`.
