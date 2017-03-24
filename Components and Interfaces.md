# Components and Interfaces

## Purpose and Goals

* this is a template, can be edited
* agreed common language for components

* looking for precision in describing what we have and how it works, as a starting point for useful techincal discussion

* at the beginning this template can be used to map current components into a modular view
* as requirements dictate, this template can be used to build components as modules
  * feature gaps, capability enhancements or extension points
  * new modules may evolve from teh existing code or be started fresh in a copy-and-paste manner from existing code

## Outstanding questions

* Propose to build some of this documentation into readthedocs.
  * There is a developer section in readthdocs but there is no equivalent of this level of compoennts documentation in the readthedocs

* Transition questions
  * how to enable R&D vs production
  * there will be grey areas
  * what currently exists

* Components
  * what currently exists
  * how to add new ones
  * how to edit scope and interfaces

## Components and Interfaces
* high level purpose or scope statements can be taken from https://docs.google.com/document/d/1Bjt_mjT9SPUbOB5V-t5eQnc94XEQI__Co4lCqTQekkE/edit?usp=sharing

### Config

* datacube.conf
* params for ingest: input; storage unit; metadata; provenance

### Ingest / Index

### Drivers
* Index DB
* Storage

### Data Access
* Uses Driver

### Analytics
* Analytics
* Execution

### Output
* file write, various formats

### OGC
* WxS interfaces

### DB management
* consistency
* upgrade/update schema
* (links to Managed Replica)

### NCI / v1-ish workflows
* gridworkflow
* direct DB and file access
* use functions to inform AE/EE

### Remote access / Task descriptor

### Managed Replica

### User Interfaces

### Applications and Examples
* some apps can move to analytics once mature
