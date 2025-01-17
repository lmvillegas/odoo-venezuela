{
    "name": "Payment Groups with Accounting Documents",
    "version": "14.0.1.0.0",
    "author": "ADHOC SA, SINAPSYS GLOBAL SA || MASTERCORE SAS",
    "license": "AGPL-3",
    "category": "Accounting",
    "depends": [
        "l10n_latam_invoice_document",
        "l10n_ve_account_payment_group",
    ],
    "data": [
        'view/account_payment_group_view.xml',
        'view/account_payment_receiptbook_view.xml',
        'wizards/account_payment_group_invoice_wizard_view.xml',
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/decimal_precision_data.xml',
        'data/l10n_latam.document.type.csv',
    ],
    "demo": [
    ],
    'images': [
    ],
    'installable': True,
    'auto_install': True,
}
