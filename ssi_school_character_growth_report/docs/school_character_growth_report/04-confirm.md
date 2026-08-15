# Confirm Character Growth Report

> **Module:** ssi_school_character_growth_report\
> **Model:** > `school_character_growth_report`\
> **Menu:** School ‣ Character Learning ‣ Growth Report ‣ Character Growth Reports\
> **Actor:** Character Growth Report User\
> **State:** > `draft` → `confirm`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for this model grants `confirm_ok` for state
  `draft` to the actor's group.
- **Access:** User is in group **Character Growth Report User**.

## Flow

1. Open the **School ‣ Character Learning ‣ Growth Report ‣ Character Growth Reports**
   menu.
2. Open the record to confirm.
3. Click the **Confirm** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The status changes to **Waiting for Approval**.
