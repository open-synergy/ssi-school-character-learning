# Create Character Rubric

> **Module:** ssi_school_character
> **Model:** `school_character_rubric`
> **Menu:** School > Configuration > Character Learning > Character Rubrics
> **Actor:** Character Learning / User
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** At least one **Character Construct** (`school_character_construct`) and one
  **Character Scale** (`school_character_scale`) exist.
- **Access:** User is in group **Character Learning / User**.

## Flow

1. Open the **School > Configuration > Character Learning > Character Rubrics** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields: **Name**, **Code**, **Construct**, **Scale**.
4. On the **Descriptors** tab, add one descriptor line per scale level: **Level**,
   **Descriptor**, **Criteria**.
5. Click **Save**.

## Post-Condition

- A new Character Rubric record is created and active.
