# Components and Interfaces

* this document will likely need to evolve from a flat document to an overview and a set of documents
  * one for each component?
  * current and proposed details?

## Purpose and Goals

* this is a template, can be edited
* agreed common language for components

* looking for precision in describing what we have and how it works, as a starting point for useful techincal discussion

* at the beginning this template can be used to map current components into a modular view
* as requirements dictate, this template can be used to build components as modules
  * feature gaps, capability enhancements or extension points
  * new modules may evolve from the existing code or be started fresh in a copy-and-paste manner from existing code

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

* Release management
  * how to coordinate releases of stable code
  * small sub-committee tasked to do the necessary checks and balances
  * how to manage the 'selecting and joining' of components into a release

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

### Output Formatter
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
* links to/from CMI

### Remote access / Task descriptor

### Managed Replica
Managed Replica Service: Client and server model with tracking

Proposal state: Mature. The plan has been considered in the context of business and user requirements.
Implementation state: Embyronic. Further detail requiried around functions and implementation specifics.

Server:
* tracks sub-cubes through linked data / provenance methods
* answer queries about holdings
* return a dry-run of results from a sub-cube request (list data and database)
* return results from a sub-cube request in the native format of the server (data and database)

Client
* connect to a server
* request holdings from a server
* request a sub-cube (including dry-run)
* translate results into local environment (data and database)
  * requires an extensible framework for multiple types of translations
* request an update to a sub-cube

Tracking
* implement a lean linked data model
* server tracks sub-cubes
  * push notifications of data/database updates to clients of relevant sub-cubes
* client requests update to sub-cube
* a sub-cube can be sub-cubed
  * linked data model links sub-sub-cube to server
  * a sub-cube always knows its parent cube

### User Interfaces

### Applications and Examples
* some apps can move to analytics once mature
