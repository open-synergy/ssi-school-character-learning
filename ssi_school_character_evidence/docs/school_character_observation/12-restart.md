# Restart Character Observation

> **Module:** ssi_school_character_evidence\
> **Model:** `school_character_observation`\
> **Menu:** School ‣ Character Learning ‣ Measurement ‣ Character Observations\
> **Actor:** Character Observation Officer\
> **State:** `cancel` | `reject` → `draft`\
> **Requires:** `10-cancel`

## Pre-Condition

- **Record:** Status is **Cancelled** or **Rejected**.
- **Config:** An active `policy.template` grants `restart_ok` for that state to the
  actor's group.
- **Access:** User is in group **Character Observation Officer**.

## Flow

1. Open the **School ‣ Character Learning ‣ Measurement ‣ Character Observations** menu.
2. Open the record to restart.
3. Click the **Restart** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- Status returns to **Draft**.
- All approval records are removed and the approval template is cleared. A later Confirm
  starts the approval process from the beginning.
