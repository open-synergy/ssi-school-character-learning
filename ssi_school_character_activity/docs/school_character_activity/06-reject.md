# Reject Character Learning Activity

> **Module:** ssi_school_character_activity\
> **Model:** `school_character_activity`\
> **Menu:** School ‣ Character Learning ‣ Activity ‣ Character Learning Activities\
> **Actor:** Character Activity Approver\
> **State:** `confirm` → `reject`\
> **Requires:** > `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `policy.template` grants `reject_ok` for state `confirm` to the
  actor's group.
- **Access:** User is in group **Character Activity Approver**.

## Flow

1. Open the **School ‣ Character Learning ‣ Activity ‣ Character Learning Activities**
   menu.
2. Open the record to reject.
3. Click the **Reject** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The status changes to **Reject**.
