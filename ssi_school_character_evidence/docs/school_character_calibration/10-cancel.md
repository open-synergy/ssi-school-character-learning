# Cancel Character Teacher Calibration

> **Module:** ssi_school_character_evidence\
> **Model:** `school_character_calibration`\
> **Menu:** School ‣ Character Learning ‣ Measurement ‣ Character Teacher Calibrations\
> **Actor:** Character Calibration Officer\
> **State:** `draft` | `confirm` | `open` → `cancel`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status allows cancellation (**Draft**, **Waiting for Approval**, or
  **Open**).
- **Config:** An active `policy.template` grants `cancel_ok` for that state to the
  actor's group.
- **Access:** User is in group **Character Calibration Officer**.

## Flow

1. Open the **School ‣ Character Learning ‣ Measurement ‣ Character Teacher
   Calibrations** menu.
2. Open the record to cancel.
3. Click the **Cancel** button.
4. In the wizard that appears, select the **Cancellation Reason**.
5. Click **Confirm**.
6. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Cancelled**.
