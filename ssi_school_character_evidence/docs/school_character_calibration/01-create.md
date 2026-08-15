# Create Character Teacher Calibration

> **Module:** ssi_school_character_evidence
> **Model:** `school_character_calibration`
> **Menu:** School ‣ Character Learning ‣ Measurement ‣ Character Teacher
>   Calibrations
> **Actor:** Character Calibration User
> **State:** `—` → `draft`

## Pre-Condition

- **Config:** An active `sequence.template` for this model is configured so the
  document number can be generated on Done.
- **Access:** User is in group **Character Calibration User**.

## Flow

1. Open the **School ‣ Character Learning ‣ Measurement ‣ Character Teacher
   Calibrations** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Document Date**: defaults to today. Change if needed.
4. On the **Scope** tab, select the **Constructs**, **Participants**, and
   **Anchors** covered by this calibration session.
5. On the **Ratings** tab, add one or more rating lines, each linking a
   **Participant**, an **Anchor**, and the **Assigned Level** that
   participant scored it at.
6. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
