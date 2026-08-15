# Finish Character Growth Report

> **Module:** ssi_school_character_growth_report\
> **Model:** > `school_character_growth_report`\
> **Menu:** School ‣ Character Learning ‣ Growth Report ‣ Character Growth Reports\
> **Actor:** Character Growth Report User\
> **State:** > `open` → `done`\
> **Requires:** `05-approve`

## Pre-Condition

- **Record:** Status is **Open**.
- **Config:** An active `policy.template` grants `done_ok` for state `open` to the
  actor's group.
- **Access:** User is in group **Character Growth Report User**.

## Flow

1. Open the **School ‣ Character Learning ‣ Growth Report ‣ Character Growth Reports**
   menu.
2. Open the record to finish.
3. Click the **Done** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The status changes to **Done**.
