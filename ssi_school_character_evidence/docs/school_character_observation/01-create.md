# Create Character Observation

> **Module:** ssi_school_character_evidence\
> **Model:** `school_character_observation`\
> **Menu:** School ‣ Character Learning ‣ Measurement ‣ Character Observations\
> **Actor:** Character Observation User\
> **State:** `—` → `draft`

## Pre-Condition

- **Config:** An active `sequence.template` for this model is configured so the document
  number can be generated on Done.
- **Data:** At least one `school_student` record exists.
- **Data:** At least one **Character Construct** (`school_character_construct`) exists.
- **Access:** User is in group **Character Observation User**.

## Flow

1. Open the **School ‣ Character Learning ‣ Measurement ‣ Character Observations** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Document Date**: defaults to today. Change if needed.
   - **Student**: the student this observation records evidence for.
   - **Construct**: the character construct being observed.
4. Optionally fill in **Subconstruct**, **Academic Year**, **Academic Term**,
   **Provisional Level**.
5. On the **Evidence Entries** tab, add one or more evidence lines, each recording a
   **Date**, **Activity**, **Arena**, **Indicator**, **Observer**, **Observed
   Behavior**, **Source Type**, and **Evidence Quality**.
6. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
