# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
# Copyright 2026 Somatech.dev
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

{
    "name": "Ecuador - Withholding Management (Retenciones)",
    "version": "18.0.1.0.0",
    "category": "Accounting/Localizations",
    "summary": "Vendor Bill Withholding, SRI Authorization, 5-Day Rule",
    "description": """
Ecuador Withholding Module (Retenciones)
========================================

Complete withholding management for Ecuador:

* Retention document (Comprobante de Retención)
* Income Tax withholdings (IR codes 303, 304, 312, etc.)
* IVA withholdings (codes 721, 723, 725, 727, 729, 731)
* 5-day rule enforcement (must issue within 5 days of invoice)
* SRI electronic transmission
* XML generation and XAdES signing

**Regulatory Compliance**: SRI 2026
    """,
    "author": "Somatech.dev, Odoo Community Association (OCA)",
    "website": "https://github.com/somatechlat/odoo_saas_ecuador",
    "license": "LGPL-3",
    "depends": [
        "l10n_ec_base",
        "l10n_ec_edi",
        "account",
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/l10n_ec_withholding.xml",
        "data/retention_codes_2026.xml",
        "data/retention_template.xml",
        "views/account_retention_views.xml",
        "wizard/retention_wizard_views.xml",
        "views/account_move_views_fixed.xml",
    ],
    "images": ["static/description/banner.png"],
    "installable": True,
    "application": False,
    "auto_install": False,
}
