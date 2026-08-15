# Finish Character Learning Activity

> **Module:** ssi_school_character_activity
> **Model:** `school_character_activity`
> **Menu:** School ‣ Character Learning ‣ Activity ‣ Character Learning Activities
> **Actor:** Character Activity User
> **State:** `open` → `done`
> **Requires:** `05-approve`

## Pre-Condition

- **Record:** Status is **Open**.
- **Config:** An active `policy.template` grants `done_ok` for state `open` to
  the actor's group.
- **Access:** User is in group **Character Activity User**.

## Flow

1. Open the **School ‣ Character Learning ‣ Activity ‣ Character Learning Activities**
   menu.
2. Open the record to finish.
3. Click the **Done** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The status changes to **Done**.
