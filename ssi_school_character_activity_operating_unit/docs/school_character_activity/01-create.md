# Create Character Learning Activity

> **Module:** ssi_school_character_activity_operating_unit
> **Extends:** ssi_school_character_activity — model `school_character_activity`,
> aksi `01-create`

## Additional Pre-Condition

- **Access:** User has an Operating Unit assigned (`user.operating_unit_ids` is not
  empty) if the user's group is scoped by the Operating Unit `ir.rule` below.

## Additional Fields

When this module is installed, the create form gains one field next to Company:

- **Operating Unit**: The operating unit this Character Learning Activity document
  belongs to. Not required by the field definition itself, but a document without an
  Operating Unit is invisible to users who are only granted the Operating Unit
  group (see Record Visibility below). Only visible when multiple operating units
  are configured (`operating_unit.group_multi_operating_unit`).

## Modified — Record Visibility

- The Character Learning Activity list/form is filtered by an `ir.rule` for users in
  the *Operating Unit* group: they can only read/write/create/unlink documents whose
  **Operating Unit** is one of the operating units assigned to them
  (`user.operating_unit_ids`). Users in the base module's Officer/Manager groups
  without this Operating Unit group are unaffected. This is not a Flow step.
