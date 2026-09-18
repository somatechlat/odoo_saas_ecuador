# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
# Copyright 2026 Somatech.dev
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

{
    "name": "Ecuador - Customs (Imports/Exports)",
    "version": "18.0.1.0.0",
    "category": "Operations/Customs",
    "summary": "DAU, Tariff Codes, FODINFA, Import IVA",
    "description": """
Ecuadorian Customs Localization
===============================

Complete customs management for Ecuador (SENAE):

* Declaración Aduanera Única (DAU)
* Tariff Headings (Partidas Arancelarias / HS Codes)
* Import Tax Calculations:
  - Ad Valorem (0-40% based on tariff)
  - FODINFA (0.5% on CIF)
  - IVA Import (15% on CIF + duties)
  - ISD (5% on payments abroad)
* ECUAPASS integration support
* Customs regime tracking

**Regulatory Compliance**: SENAE 2026
    """,
    "author": "Somatech.dev, Odoo Community Association (OCA)",
    "website": "https://github.com/somatechlat/odoo_saas_ecuador",
    "license": "LGPL-3",
    "depends": ["stock", "account", "purchase", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "data/l10n_ec_customs_data.xml",
        "views/l10n_ec_customs_views.xml",
    ],
    "images": ["static/description/banner.png"],
    "installable": True,
    "application": False,
}
