# Activate Character Profile

> **Module:** `ssi_school_character`\
> **Model:** `school_character_profile`\
> **Menu:** School > Configuration > Character Learning > Character Profiles\
> **Actor:** user in group `Character Profile`\
> **Active:** `false` → `true`\
> **Requires:** `04-deactivate`

## Pre-Condition

- **Record:** The record is currently archived (inactive).
- **Access:** User is in group `Character Profile`.

## Flow

1. Open the **School > Configuration > Character Learning > Character Profiles** menu.
2. Open the **Filters** menu and enable **Archived**.
3. Select one or more records to reactivate (check the checkbox).
4. Click **Action** > **Unarchive**.

## Post-Condition

- The records are active again and appear in the default list view.
