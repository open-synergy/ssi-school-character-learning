# Cancel Character Learning Activity

> **Module:** ssi_school_character_activity\
> **Model:** `school_character_activity`\
> **Menu:** School ‣ Character Learning ‣ Activity ‣ Character Learning Activities\
> **Actor:** Character Activity User\
> **State:** any cancellable state → `cancel`\
> **Requires:** `01-create`

## Pre-Condition

- **Record:** Status is not already **Done** or **Cancel**.
- **Config:** An active `policy.template` grants `cancel_ok` for the current state to
  the actor's group.
- **Data:** At least one cancel reason record is configured.
- **Access:** User is in group **Character Activity User**.

## Flow

1. Open the **School ‣ Character Learning ‣ Activity ‣ Character Learning Activities**
   menu.
2. Open the record to cancel.
3. Click the **Cancel** button.
4. In the wizard that appears, select the **Reason**.
5. Click **Confirm**.

## Post-Condition

- The status changes to **Cancel**.
