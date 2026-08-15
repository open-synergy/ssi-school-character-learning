# Create Character Learning Activity

> **Module:** ssi_school_character_activity
> **Model:** `school_character_activity`
> **Menu:** School ‣ Character Learning ‣ Activity ‣ Character Learning Activities
> **Actor:** Character Activity User
> **State:** `—` → `draft`

## Pre-Condition

- **Config:** An active `sequence.template` for this model is configured so the
  document number can be generated on Done.
- **Data:** At least one `school_character_construct` record exists.
- **Access:** User is in group **Character Activity User**.

## Flow

1. Open the **School ‣ Character Learning ‣ Activity ‣ Character Learning Activities**
   menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Document Date**: defaults to today. Change if needed.
   - **Construct**: the character construct this activity develops.
4. Optionally fill in **Arena**, **Method**, **Curriculum Map**, **Grade Class**,
   **Teacher**, **Learning Objective (RBT)**, **RBT Level**, **DOK Level**,
   **SOLO Target**.
5. On the **Alignment** tab, add one or more alignment lines linking an
   **Indicator** to the activity's RBT/DOK/SOLO design.
6. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
