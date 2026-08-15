# Confirm Character Learning Activity

> **Module:** ssi_school_character_activity
> **Model:** `school_character_activity`
> **Menu:** School ‣ Character Learning ‣ Activity ‣ Character Learning Activities
> **Actor:** Character Activity User
> **State:** `draft` → `confirm`
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for this model grants `confirm_ok` for
  state `draft` to the actor's group.
- **Access:** User is in group **Character Activity User**.

## Flow

1. Open the **School ‣ Character Learning ‣ Activity ‣ Character Learning Activities**
   menu.
2. Open the record to confirm.
3. Click the **Confirm** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The status changes to **Waiting for Approval**.
