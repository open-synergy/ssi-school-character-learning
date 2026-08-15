# Finish Character Curriculum Map

> **Module:** ssi_school_character_curriculum\
> **Model:** `school_character_curriculum`\
> **Menu:** School ‣ Character Learning ‣ Curriculum ‣ Character Curriculum Maps\
> **Actor:** Character Curriculum Officer\
> **State:** `open` → `done`\
> **Requires:** > `05-approve`

## Pre-Condition

- **Record:** Status is **Open**.
- **Config:** An active `policy.template` grants `done_ok` to the actor's group.
- **Access:** User is in group **Character Curriculum Officer**.

## Flow

1. Open the **School ‣ Character Learning ‣ Curriculum ‣ Character Curriculum Maps**
   menu.
2. Open the record to finish.
3. Click the **Done** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Done**.
