# Create Character Indicator

> **Module:** ssi_school_character\
> **Model:** `school_character_indicator`\
> **Menu:** School > Configuration > Character Learning > Character Indicators\
> **Actor:** Character Learning / User\
> **State:** `—` → `draft`

## Pre-Condition

- **Data:** At least one **Character Construct** (`school_character_construct`) exists.
- **Access:** User is in group **Character Learning / User**.

## Flow

1. Open the **School > Configuration > Character Learning > Character Indicators** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields: **Name**, **Code**, **Construct**.
4. Optionally fill in **Sub-construct**, **Grade Type**, **Grade**, **Indicator Type**
   (defaults to Positive Indicator), **RBT Level**, **DOK Level**, **SOLO Level**, and
   **Description**.
5. Click **Save**.

## Post-Condition

- A new Character Indicator record is created and active.
