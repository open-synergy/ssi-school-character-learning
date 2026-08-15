# Confirm Character Curriculum Map

> **Module:** ssi_school_character_curriculum\
> **Model:** `school_character_curriculum`\
> **Menu:** School ‣ Character Learning ‣ Curriculum ‣ Character Curriculum Maps\
> **Actor:** Character Curriculum Officer\
> **State:** `draft` → `confirm`\
> **Requires:** > `01-create`

## Pre-Condition

- **Record:** Status is **Draft**.
- **Config:** An active `policy.template` for this model grants `confirm_ok` for state
  `draft` to the actor's group.
- **Config:** An active `approval.template` for this model matches this record and has
  at least one approver level.
- **Config:** An active `sequence.template` exists for this model.
- **Access:** User is in group **Character Curriculum Officer**.

## Flow

1. Open the **School ‣ Character Learning ‣ Curriculum ‣ Character Curriculum Maps**
   menu.
2. Open the record to confirm.
3. Click the **Confirm** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Waiting for Approval**.
- Approval records are created for each approver level defined by the approval template.
