# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
# Copyright 2026 Somatech.dev
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0)

{
    "name": "Ecuador - Activos Fijos",
    "version": "18.0.1.0.0",
    "category": "Accounting/Localizations/Assets",
    "summary": "Gestión de activos fijos para Ecuador - LORTI Art. 28",
    "description": """
Ecuador Asset Management Module (Community Alternative)
========================================================

Provides asset management and depreciation per Ecuador law:

* LORTI Art. 28 num. 6: Depreciación activos fijos
* SRI tablas de depreciación

Depreciation Rates (LORTI):
- Inmuebles: 5% anual (20 años)
- Maquinaria/Equipos: 10% anual (10 años)
- Vehículos: 20% anual (5 años)
- Equipos de cómputo: 33% anual (3 años)

Features:
- Asset registration and tracking
- Ecuador-compliant depreciation calculation
- Automatic journal entries
- Asset revaluation
- Asset disposal
    """,
    "author": "Somatech.dev",
    "website": "https://github.com/somatechlat/odoo_saas_ecuador",
    "license": "LGPL-3",
    "depends": ["account", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "data/asset_category_data.xml",
        "views/asset_views.xml",
    ],
    "installable": True,
    "application": False,
}
