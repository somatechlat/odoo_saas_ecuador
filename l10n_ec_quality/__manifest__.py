# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
# Copyright 2026 Somatech.dev
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

{
    "name": "Ecuador - Control de Calidad",
    "version": "18.0.1.0.0",
    "category": "Manufacturing/Quality",
    "summary": "Control de calidad para Ecuador - Ley Calidad Art. 31-40, ARCSA Res. 067",
    "description": """
Ecuador Quality Control Module (Community Alternative)
=======================================================

Provides quality control functionality required by Ecuador law:

* Ley del Sistema Ecuatoriano de Calidad Art. 31-40
* ARCSA Resolución 067 - BPM obligatorio
* NTE INEN ISO 9001 compliance tracking
* NTE INEN ISO 22000 food safety

Features:
- Quality control points on manufacturing
- Quality alerts and notifications
- Quality check templates
- BPM compliance tracking
- Certificate management
    """,
    "author": "Somatech.dev",
    "website": "https://github.com/somatechlat/odoo_saas_ecuador",
    "license": "LGPL-3",
    "depends": ["mrp", "stock", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/quality_views.xml",
    ],
    "installable": True,
    "application": False,
}
