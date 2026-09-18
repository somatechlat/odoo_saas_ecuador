# -*- coding: utf-8 -*-
{
    "name": "Ecuador - Loans & IESS Extension",
    "version": "18.0.1.0.0",
    "category": "Human Resources",
    "summary": "Manage Company Loans and IESS Deductions",
    "description": """
Ecuador Loans
=============

1. **IESS Import**: Wizard to upload CSV/TXT from IESS for Quirografario/Hipotecario loans.
2. **Loan Management**: Track installments and status.
3. **Payslip Integration**: Automatically deducts due installments from the employee's payslip.
    """,
    "author": "Somatech.dev",
    "depends": ["l10n_ec_hr_payroll", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "views/loan_views.xml",
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}
