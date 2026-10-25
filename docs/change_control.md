# Change Request and Change Management Process

Every change request (CR) records: unique ID; source and desired outcome; alternatives; effect on scope, cost, schedule, acceptance gates, privacy/security, accessibility and residual risk; project-manager recommendation; decision authority; linked repository activity; and final verification.

## Steps
1. **Log** the request as a GitHub issue with the `change-request` label.
2. **Assess** its impact on scope, cost, schedule, quality and risk.
3. **Decide:** the PM may approve low-risk changes within tolerance. Changes affecting personal information, acceptance criteria, major scope, more than AUD 10,000 or more than five working days go to the sponsor-led Change Control Board (CCB).
4. **Implement** on a branch and open a pull request linked to the CR.
5. **Verify:** checks pass and a peer approves the pull request.
6. **Close:** merge, update the baseline and record the release.

A request is not an instruction to implement. Baselines change only after approval, and earlier versions stay in the repository history.
