# Reject Character Growth Report

> **Module:** ssi_school_character_growth_report
> **Model:** `school_character_growth_report`
> **Menu:** School ‣ Character Learning ‣ Growth Report ‣ Character Growth Reports
> **Actor:** Character Growth Report Officer
> **State:** `confirm` → `reject`
> **Requires:** `04-confirm`

## Pre-Condition

- **Record:** Status is **Waiting for Approval**.
- **Config:** An active `policy.template` grants `reject_ok` for state `confirm`
  to the actor's group.
- **Access:** User is in group **Character Growth Report Officer**.

## Flow

1. Open the **School ‣ Character Learning ‣ Growth Report ‣ Character Growth
   Reports** menu.
2. Open the record to reject.
3. Click the **Reject** button.
4. Click **OK** on the confirmation dialog.

## Post-Condition

- The status changes to **Reject**.
