# Create Character Scale

> **Module:** ssi_school_character
> **Model:** `school_character_scale`
> **Menu:** School > Configuration > Character Learning > Character Scales
> **Actor:** Character Learning / User
> **State:** `—` → `draft`

## Pre-Condition

- **Access:** User is in group **Character Learning / User**.

## Flow

1. Open the **School > Configuration > Character Learning > Character Scales** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields: **Name** and **Code**.
4. On the **Levels** tab, add one or more level lines: **Code**, **Name**, and
   **Description** (see `school_character_level/01-create.md` for the standalone
   equivalent; levels may also be created inline here).
5. Click **Save**.

## Post-Condition

- A new Character Scale record is created and active, with its level lines (if any)
  saved as `school_character_level` records.
