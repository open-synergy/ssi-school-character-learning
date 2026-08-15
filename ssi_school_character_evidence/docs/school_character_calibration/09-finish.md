# Finish Character Teacher Calibration

> **Module:** ssi_school_character_evidence\
> **Model:** `school_character_calibration`\
> **Menu:** School ‣ Character Learning ‣ Measurement ‣ Character Teacher Calibrations\
> **Actor:** Character Calibration Officer\
> **State:** `open` → `done`\
> **Requires:** > `05-approve`

## Pre-Condition

- **Record:** Status is **Open**.
- **Config:** An active `policy.template` grants `done_ok` to the actor's group.
- **Access:** User is in group **Character Calibration Officer**.

## Flow

1. Open the **School ‣ Character Learning ‣ Measurement ‣ Character Teacher
   Calibrations** menu.
2. Open the record to finish.
3. Click the **Done** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Done**.
