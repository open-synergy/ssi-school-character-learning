.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
   :alt: License: AGPL-3

=========================
School Character Learning
=========================

Foundation module for documenting a school's character-learning program
end-to-end, based on the ICLAD v2.3 framework (*universal in method,
contextual in values*). It provides the full master data / configuration
layer -- the character construct architecture -- reused by the downstream
transactional modules (curriculum, activity, evidence, growth report).

The module is deliberately **neutral**: no school-specific value, scale, or
construct is hard-coded. Every school configures its own data. Concrete pilot
examples appear only as demo data.

Master data provided:

* **Character Scale & Character Level** -- configurable rating/level scales
  (for example a four-level mastery progression, or a status scale), each made
  up of ordered levels.
* **Character Profile** -- the top-level container of a school's core
  character values.
* **Character Family** -- a grouping of related constructs.
* **Character Construct** -- a single, precisely defined and bounded character
  trait, tied to a profile, family, scale, and pedagogical methods.
* **Character Sub-construct** -- a finer-grained facet of a construct.
* **Character Indicator** -- an observable behaviour (positive or
  non-indicator) evidencing a construct, tagged with cognitive-demand
  taxonomies (RBT, DOK, SOLO).
* **Character Rubric & Descriptor** -- a rubric tying a construct to a scale,
  with one descriptor per level.
* **Character Anchor** -- a calibrated example pinned to a construct and level.
* **Character Method** -- a pedagogical method in the school's repertoire.
* **Character Arena** -- a learning arena/program where character is formed and
  observed.


Work Instruction
================

* `Create Character Anchor <docs/school_character_anchor/index.html>`_
* `Edit Character Anchor <docs/school_character_anchor/index.html>`_
* `Delete Character Anchor <docs/school_character_anchor/index.html>`_
* `Deactivate Character Anchor <docs/school_character_anchor/index.html>`_
* `Activate Character Anchor <docs/school_character_anchor/index.html>`_
* `Create Character Arena <docs/school_character_arena/index.html>`_
* `Edit Character Arena <docs/school_character_arena/index.html>`_
* `Delete Character Arena <docs/school_character_arena/index.html>`_
* `Deactivate Character Arena <docs/school_character_arena/index.html>`_
* `Activate Character Arena <docs/school_character_arena/index.html>`_
* `Create Character Family <docs/school_character_family/index.html>`_
* `Edit Character Family <docs/school_character_family/index.html>`_
* `Delete Character Family <docs/school_character_family/index.html>`_
* `Deactivate Character Family <docs/school_character_family/index.html>`_
* `Activate Character Family <docs/school_character_family/index.html>`_
* `Create Character Method <docs/school_character_method/index.html>`_
* `Edit Character Method <docs/school_character_method/index.html>`_
* `Delete Character Method <docs/school_character_method/index.html>`_
* `Deactivate Character Method <docs/school_character_method/index.html>`_
* `Activate Character Method <docs/school_character_method/index.html>`_


Installation
============

To install this module, you need to:

1.  Clone the branch 14.0 of the repository https://github.com/open-synergy/ssi-school-character-learning
2.  Add the path to this repository in your configuration (addons-path)
3.  Update the module list (Must be on developer mode)
4.  Go to menu *Apps -> Apps -> Main Apps*
5.  Search For *School Character Learning*
6.  Install the module


Bug Tracker
===========

Bugs are tracked on `GitHub Issues
<https://github.com/open-synergy/ssi-school-character-learning/issues>`_. In case of trouble, please
check there if your issue has already been reported. If you spotted it first,
help us smash it by providing detailed and welcomed feedback.


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
