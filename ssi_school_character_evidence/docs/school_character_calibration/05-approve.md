# Approve Character Teacher Calibration

> **Module:** ssi_school_character_evidence
> **Model:** `school_character_calibration`
> **Menu:** School ‣ Character Learning ‣ Measurement ‣ Character Teacher
>   Calibrations
> **Actor:** Character Calibration Manager
> **State:** `confirm` → `open` (via `approve_ok`, then automatic Open)
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `policy.template` grants `approve_ok` to the actor's
  group.
- **Access:** User is registered as an approver on the approval level that is
  currently pending.
- **Access:** User is in group **Character Calibration Manager**.

## Flow

1. Open the **School ‣ Character Learning ‣ Measurement ‣ Character Teacher
   Calibrations** menu.
2. Open the record to approve.
3. Click the **Approve** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Once the final approval level is reached, the record automatically
  transitions to status **Open** (there is no separate manual "Start"/"Open"
  button for this model).
- The document number is generated.
