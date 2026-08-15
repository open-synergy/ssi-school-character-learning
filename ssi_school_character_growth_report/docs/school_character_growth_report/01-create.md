# Create Character Growth Report

> **Module:** ssi_school_character_growth_report\
> **Model:** > `school_character_growth_report`\
> **Menu:** School ‣ Character Learning ‣ Growth Report ‣ Character Growth Reports\
> **Actor:** Character Growth Report User\
> **State:** > `—` → `draft`

## Pre-Condition

- **Config:** An active `sequence.template` for this model is configured so the document
  number can be generated on Done.
- **Data:** At least one `school_student` record exists.
- **Access:** User is in group **Character Growth Report User**.

## Flow

1. Open the **School ‣ Character Learning ‣ Growth Report ‣ Character Growth Reports**
   menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Document Date**: defaults to today. Change if needed.
   - **Student**: the student this growth report profiles.
4. Optionally fill in **Academic Year**, **Academic Term**, **Homeroom Teacher**,
   **Calibration**, **Pathway**.
5. On the **Growth Lines** tab, add one or more lines, each linking a **Construct** to
   its **Achieved Level**, **Growth Narrative**, **Next Step**, and supporting
   **Evidence Entries**.
6. Optionally fill in the **Overall Narrative** tab.
7. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
