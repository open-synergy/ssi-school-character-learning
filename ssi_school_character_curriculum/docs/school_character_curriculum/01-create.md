# Create Character Curriculum Map

> **Module:** ssi_school_character_curriculum\
> **Model:** `school_character_curriculum`\
> **Menu:** School ‣ Character Learning ‣ Curriculum ‣ Character Curriculum Maps\
> **Actor:** Character Curriculum User\
> **State:** `—` → `draft`

## Pre-Condition

- **Config:** An active `sequence.template` for this model is configured so the document
  number can be generated on Done.
- **Data:** At least one **Character Profile** (`school_character_profile`) exists.
- **Data:** At least one **Academic Year** (`school_academic_year`) exists.
- **Access:** User is in group **Character Curriculum User**.

## Flow

1. Open the **School ‣ Character Learning ‣ Curriculum ‣ Character Curriculum Maps**
   menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Document Date**: defaults to today. Change if needed.
   - **Academic Year**: the academic year this map applies to.
   - **Character Profile**: the character profile this map is derived from.
   - **Pathway**: defaults to **Core**. Change to **Lite** or **Full** if needed.
4. Optionally fill in **Academic Term**, **School**, **Grade**, **Grade Class**.
5. On the **Curriculum Lines** tab, add one or more lines, each mapping a **Construct**
   to an **Arena**, a **Method**, a **Target Level**, and the **Capaian Pembelajaran**
   (learning outcome).
6. Click **Save**.

## Post-Condition

- A new record is created in **Draft** status.
