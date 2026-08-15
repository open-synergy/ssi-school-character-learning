# Reject Character Curriculum Map

> **Module:** ssi_school_character_curriculum\
> **Model:** `school_character_curriculum`\
> **Menu:** School ‣ Character Learning ‣ Curriculum ‣ Character Curriculum Maps\
> **Actor:** Character Curriculum Manager\
> **State:** `confirm` → `reject`\
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `policy.template` grants `reject_ok` to the actor's group.
- **Access:** User is registered as an approver on the approval level that is currently
  pending.
- **Access:** User is in group **Character Curriculum Manager**.

## Flow

1. Open the **School ‣ Character Learning ‣ Curriculum ‣ Character Curriculum Maps**
   menu.
2. Open the record to reject.
3. Click the **Reject** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Rejected**.
