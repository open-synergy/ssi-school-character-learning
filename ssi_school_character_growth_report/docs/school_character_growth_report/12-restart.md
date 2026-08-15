# Restart Character Growth Report

> **Module:** ssi_school_character_growth_report\
> **Model:** > `school_character_growth_report`\
> **Menu:** School ‣ Character Learning ‣ Growth Report ‣ Character Growth Reports\
> **Actor:** Character Growth Report User\
> **State:** > `cancel` → `draft`\
> **Requires:** `10-cancel`

## Pre-Condition

- **Record:** Status is **Cancel**.
- **Config:** An active `policy.template` grants `restart_ok` for state `cancel` to the
  actor's group.
- **Access:** User is in group **Character Growth Report User**.

## Flow

1. Open the **School ‣ Character Learning ‣ Growth Report ‣ Character Growth Reports**
   menu.
2. Open the record to restart.
3. Click the **Restart** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The status changes back to **Draft**.
