# Finish Character Observation

> **Module:** ssi_school_character_evidence\
> **Model:** `school_character_observation`\
> **Menu:** School ‣ Character Learning ‣ Measurement ‣ Character Observations\
> **Actor:** Character Observation Officer\
> **State:** `open` → `done`\
> **Requires:** > `05-approve`

## Pre-Condition

- **Record:** Status is **Open**.
- **Config:** An active `policy.template` grants `done_ok` to the actor's group.
- **Access:** User is in group **Character Observation Officer**.

## Flow

1. Open the **School ‣ Character Learning ‣ Measurement ‣ Character Observations** menu.
2. Open the record to finish.
3. Click the **Done** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status changes to **Done**.
