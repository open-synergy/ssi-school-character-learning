.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

===========================================
Character Observation & Teacher Calibration
===========================================

The measurement layer of the character-learning set. It records structured,
behaviour-based character evidence per student per construct, and the teacher
calibration sessions that keep inter-rater reliability high (ICLAD v2.3
Evidence System Bab 11 & 12, calibration Bab 18).

* **Character Observation** -- a transactional document that gathers the
  evidence recorded for one student against one character construct within an
  academic term. Each observation carries a set of evidence entries and an
  optional provisional level taken from the configured character scale.
* **Evidence entries** -- each entry is a single observed behaviour tied to
  the arena and (optionally) the activity it happened in, the observer, the
  indicator it evidences, its source type, its evidence quality, and the
  scale level it is matched to. A student's own reflection is recorded here
  as an ordinary entry with source type ``Reflection``.
* **Teacher Calibration** -- a transactional document for a calibration
  session: which constructs it covers, which teachers took part, which
  calibrated anchor examples were rated, and the level each participant
  assigned to each anchor (the rating lines), plus the overall agreement
  result.
* **Full approval workflow** -- both documents follow the standard SSI
  transactional lifecycle Draft -> Confirm -> Approve -> Open -> Done /
  Cancel, each with an automatically generated document number.

Data governance boundary (ICLAD Bab 17)
=======================================

This module enforces the non-negotiable character-evidence data governance
rules:

* It holds **no** link to any discipline, counseling, or safeguarding record.
* ``source_type`` is restricted to legitimate character-evidence sources:
  observation, reflection, artifact, peer, self, parent, community.
* ``evidence_quality`` carries an ``Invalid (Not Admissible)`` tier that
  documents, explicitly, that rumor, impression, counseling notes,
  psychological test results, and punishment data must NOT be used as
  character evidence. Such material may be recorded only to make the
  exclusion explicit; it never becomes valid evidence.


Installation
============

To install this module, you need to:

1.  Clone the branch 14.0 of the repository https://github.com/open-synergy/ssi-school-character-learning
2.  Add the path to this repository in your configuration (addons-path)
3.  Update the module list (Must be on developer mode)
4.  Go to menu *Apps -> Apps -> Main Apps*
5.  Search For *Character Observation & Teacher Calibration*
6.  Install the module


Work Instruction
================

* `Create Character Observation <docs/school_character_observation/index.html>`_
* `Edit Character Observation <docs/school_character_observation/index.html>`_
* `Delete Character Observation <docs/school_character_observation/index.html>`_
* `Confirm Character Observation <docs/school_character_observation/index.html>`_
* `Approve Character Observation <docs/school_character_observation/index.html>`_
* `Reject Character Observation <docs/school_character_observation/index.html>`_
* `Finish Character Observation <docs/school_character_observation/index.html>`_
* `Cancel Character Observation <docs/school_character_observation/index.html>`_
* `Restart Character Observation <docs/school_character_observation/index.html>`_
* `Create Character Teacher Calibration <docs/school_character_calibration/index.html>`_
* `Edit Character Teacher Calibration <docs/school_character_calibration/index.html>`_
* `Delete Character Teacher Calibration <docs/school_character_calibration/index.html>`_
* `Confirm Character Teacher Calibration <docs/school_character_calibration/index.html>`_
* `Approve Character Teacher Calibration <docs/school_character_calibration/index.html>`_
* `Reject Character Teacher Calibration <docs/school_character_calibration/index.html>`_
* `Finish Character Teacher Calibration <docs/school_character_calibration/index.html>`_
* `Cancel Character Teacher Calibration <docs/school_character_calibration/index.html>`_
* `Restart Character Teacher Calibration <docs/school_character_calibration/index.html>`_


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/open-synergy/ssi-school-character-learning/issues>`_. In case of
trouble, please check there if your issue has already been reported. If you
spotted it first, help us smash it by providing detailed and welcomed
feedback.


Credits
=======

Contributors
------------

* Andhitia Rama <andhitia.r@gmail.com>

Maintainer
----------

.. image:: https://simetri-sinergi.id/logo.png
   :alt: PT. Simetri Sinergi Indonesia
   :target: https://simetri-sinergi.id

This module is maintained by the PT. Simetri Sinergi Indonesia.
