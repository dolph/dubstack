======================
OpenStack Echo Service
======================

Echo Service illustrates the simplest possible OpenStack service.

It is a WSGI app with a useless feature, logging, tests, extensible backends, and exception handling.

KVS Backend
===========

A simple backend interface meant to be further backended on anything that can
support primary key lookups, the most trivial implementation being an in-memory
dict.

Supports all features of the general data model.
