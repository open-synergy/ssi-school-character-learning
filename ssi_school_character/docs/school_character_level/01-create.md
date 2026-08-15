# Create Character Level

> **Module:** ssi_school_character\
> **Model:** `school_character_level`\
> **Menu:** School > Configuration > Character Learning > Character Levels\
> **Actor:** Character Learning / User\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** At least one **Character Scale** (`school_character_scale`) exists.
- **Access:** User is in group **Character Learning / User**.

## Flow

1. Open the **School > Configuration > Character Learning > Character Levels** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name** and **Code**.
   - **Scale**: the character scale this level belongs to.
   - **Sequence**: the ascending order of this level within its scale (defaults to
     `10`).
4. Optionally fill in **Description**.
5. Click **Save**.

## Post-Condition

- A new Character Level record is created and active, ordered within its scale by
  **Sequence**.
