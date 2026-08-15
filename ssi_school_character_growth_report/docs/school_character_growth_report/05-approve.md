# Approve Character Growth Report

> **Module:** ssi_school_character_growth_report
> **Model:** `school_character_growth_report`
> **Menu:** School ‣ Character Learning ‣ Growth Report ‣ Character Growth Reports
> **Actor:** Character Growth Report Officer
> **State:** `confirm` → `open` (via `approve_ok`, then automatic Open)
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `approval.template` for this model matches this record and
  routes it to the actor's group.
- **Config:** An active `policy.template` grants `approve_ok` for state `confirm`
  to the actor's group.
- **Access:** User is in group **Character Growth Report Officer**.

## Flow

1. Open the **School ‣ Character Learning ‣ Growth Report ‣ Character Growth
   Reports** menu.
2. Open the record to approve.
3. Click the **Approve** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Once the final approval level is reached, the record automatically transitions
  to status **Open** (there is no separate manual "Start"/"Open" button for this
  model).
- The document number is generated.
