# Create Character Profile

> **Module:** ssi_school_character
> **Model:** `school_character_profile`
> **Menu:** School > Configuration > Character Learning > Character Profiles
> **Actor:** Character Learning / User
> **State:** `—` → `draft`

## Pre-Condition

- **Access:** User is in group **Character Learning / User**.

## Flow

1. Open the **School > Configuration > Character Learning > Character Profiles** menu.
2. Click the **New** button. **(14.0: "Create")**
3. Fill in the required fields: **Name**, **Code**.
4. On the **Profile** tab, optionally select **School** and fill in **Description**.
5. Click **Save**.

## Post-Condition

- A new Character Profile record is created and active. The **Constructs** tab lists any
  construct already linked to this profile (`school_character_construct.profile_id`);
  constructs are added from `school_character_construct/01-create.md`, not from here.
