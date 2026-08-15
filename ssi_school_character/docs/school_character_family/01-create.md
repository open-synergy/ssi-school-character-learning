# Create Character Family

> **Module:** ssi_school_character
> **Model:** `school_character_family`
> **Menu:** School > Configuration > Character Learning > Character Families
> **Actor:** Character Learning / User
> **State:** `—` → `draft`

## Pre-Condition

- **Access:** User is in group **Character Learning / User**.

## Flow

1. Open the **School > Configuration > Character Learning > Character Families** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Name**: name of the construct family/grouping.
   - **Code**: a meaningful, unique code. The `/` placeholder is rejected on save —
     leaving it as `/` raises an error.
4. On the **Family** tab, optionally fill in the **Description**.
5. Click **Save**.

## Post-Condition

- A new Character Family record is created and active.
