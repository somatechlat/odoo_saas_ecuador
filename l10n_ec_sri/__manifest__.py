# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
# Copyright 2026 Somatech.dev
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0).

{
    "name": "Ecuador SRI Electronic Invoicing",
    "version": "18.0.1.0.0",
    "category": "Accounting/Localizations/SRI",
    "summary": "Full SRI Electronic Invoicing Compliance (2025-2026)",
    "description": """
Ecuador SRI Integration Module
==============================

Complete SRI (Servicio de Rentas Internas) integration:

* SOAP Web Services (RecepcionComprobantesOffline, AutorizacionComprobantesOffline)
* Test and Production environments
* Certificate management (.p12)
* Error handling and retry logic
* Authorization status tracking
* RIDE report generation

**Endpoints**:
- Test: celcer.sri.gob.ec
- Production: cel.sri.gob.ec

**Regulatory Compliance**: SRI 2026
    """,
    "author": "Somatech.dev, Odoo Community Association (OCA)",
    "website": "https://github.com/somatechlat/odoo_saas_ecuador",
    "license": "LGPL-3",
    "depends": [
        "base",
        "account",
        "l10n_ec_base",
        "l10n_ec_edi",  # Base EDI module with field definitions
        "mail",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/ir_sequence_data.xml",
        "views/account_move_views.xml",
        "views/account_move_purchase_views.xml",
        "views/l10n_ec_retention_views.xml",
        "views/l10n_ec_retention_xml_template.xml",
    ],
    "assets": {
        "web.assets_backend": [
            # Future: Add status badges styling if needed
        ],
    },
    "external_dependencies": {
        "python": ["zeep", "cryptography", "lxml"],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "post_init_hook": "post_init_hook",
    "uninstall_hook": "uninstall_hook",
}
