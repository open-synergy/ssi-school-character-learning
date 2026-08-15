# Confirm Character Teacher Calibration

> **Module:** ssi_school_character_evidence\
> **Model:** `school_character_calibration`\
> **Menu:** School ‣ Character Learning ‣ Measurement ‣ Character Teacher Calibrations\
> **Actor:** Character Calibration Officer\
> **State:** `draft` → `confirm`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for this model grants `confirm_ok` for state
  `draft` to the actor's group.
- **Config:** An active `approval.template` for this model matches this record and has
  at least one approver level.
- **Config:** An active `sequence.template` exists for this model.
- **Access:** User is in group **Character Calibration Officer**.

## Flow

1. Open the **School ‣ Character Learning ‣ Measurement ‣ Character Teacher
   Calibrations** menu.
2. Open the record to confirm.
3. Click the **Confirm** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Waiting for Approval**.
- Approval records are created for each approver level defined by the approval template.
