Introduction
============

Acquisition can be evil.

If you have a Zope tree like this::

     |
     \-- Site1
     |
     \-- Site2

Acquisition allows a request to traverse to Site2 from Site1 with a URL like::

    http://Site1/Site2

Making it appear that Site2 is inside Site1.

This package prevents this behavior by adding verification during traversal.

Simply installing the package will isolate Plone sites that are in the root of the ZODB. If one or more sites are inside Zope folders, rather than at the ZODB root, you will need to take extra action to protect them. To do so, apply collective.siteisolation.interfaces.IObjectToIsolate to the enclosing folder (the one at the ZODB root). You may do this with code or via the "Interfaces" tab in the ZMI.

Only Plone sites are automatically protected. To protect non-Plone sites, apply marker interfaces collective.siteisolation.interfaces.IObjectToIsolate and collective.siteisolation.interfaces.IIsolatedObject to the sites you wish to protect. IObjectToIsolate only works for items in the ZODB root.

New sites are not isolated until after a restart.

Details
=======

The package makes use of two marker interfaces.

collective.siteisolation.interfaces.IIsolatedObject is detected during traversal. If found, the traversal will not be allowed to include objects marked with collective.siteisolation.interfaces.IObjectToIsolate.

To make this a little faster, IObjectToIsolate is only detected at the ZODB root when a list of objects to isolate is created on first traverse. That list is memoized for the life of the Zope instance, so adding new objects to isolate requires a restart.

Author
======

 * ICTS Team - KULeuven (https://admin.kuleuven.be/icts)
 * Jean-Francois Roche <jfroche at affinitic dot be>
