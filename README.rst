POS Branding (WaranCloud)
=========================

White-label Odoo Point of Sale module that replaces default Odoo branding with company and WaranCloud branding.

Features
--------

* **Navbar**: Dynamic company logo from `res.company.logo`
* **Loader screen**: WaranCloud logo (static SVG)
* **Saver screen**: WaranCloud logo (static SVG)
* **Receipt footer**: "Solution By WaranCloud" (replaces "Powered by Odoo")
* **Customer display** (desktop & mobile): "Solution By WaranCloud" (replaces "Powered by Odoo")

Installation
------------

1. Copy the `pos_branding` folder to your Odoo addons path
2. Update Apps list
3. Install "POS Branding (WaranCloud)"

Configuration
-------------

* Company logo is taken from the POS company's `res.company.logo` field
* WaranCloud SVG logo is included in the module (`static/src/img/warancloud_logo.svg`)

Requirements
------------

* point_of_sale (Odoo 19.0)

License
-------

LGPL-3