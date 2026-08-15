# Create Character Anchor

> **Module:** ssi_school_character\
> **Model:** `school_character_anchor`\
> **Menu:** School > Configuration > Character Learning > Character Anchors\
> **Actor:** Character Learning / User\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** At least one **Character Construct** (`school_character_construct`) exists.
- **Data:** At least one **Character Level** (`school_character_level`) exists.
- **Access:** User is in group **Character Learning / User**.

## Flow

1. Open the **School > Configuration > Character Learning > Character Anchors** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields:
   - **Construct**: the character construct this anchor example calibrates.
   - **Level**: the scale level this anchor example represents.
4. On the **Anchor** tab, optionally fill in **Grade Type**, **Source Type**, and the
   **Sample** text describing the concrete performance sample.
5. Click **Save**.

## Post-Condition

- A new Character Anchor record is created and active.
