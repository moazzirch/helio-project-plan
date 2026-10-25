# ADR-001: Evidence-first answers with read-only integrations

**Status:** Accepted for planning baseline

## Context
A generic AI chatbot can produce fluent answers that are not backed by approved policy. Student-record systems hold personal information that must not be changed or exposed by the chatbot.

## Decision
- Answers come only from an approved, versioned knowledge base, and each answer shows its source and last-reviewed date (an "answer receipt").
- LMS/SMS connections are read-only and least-privilege. The model cannot update any record.
- Retrieved text is treated as untrusted input to reduce prompt-injection risk.
- High-stakes or low-confidence questions are handed to staff.
- A static FAQ and staff fallback is available if the model or vendor fails.

## Consequences
- Lower automated deflection at first, but stronger answer integrity.
- Personalised answers depend on passing the G2 privacy/vendor gate.
