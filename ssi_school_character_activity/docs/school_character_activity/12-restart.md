# Restart Character Learning Activity

> **Module:** ssi_school_character_activity\
> **Model:** `school_character_activity`\
> **Menu:** School ‣ Character Learning ‣ Activity ‣ Character Learning Activities\
> **Actor:** Character Activity User\
> **State:** `cancel` → `draft`\
> **Requires:** > `10-cancel`

## Pre-Condition

- **Record:** Status is **Cancel**.
- **Config:** An active `policy.template` grants `restart_ok` for state `cancel` to the
  actor's group.
- **Access:** User is in group **Character Activity User**.

## Flow

1. Open the **School ‣ Character Learning ‣ Activity ‣ Character Learning Activities**
   menu.
2. Open the record to restart.
3. Click the **Restart** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The status changes back to **Draft**.
