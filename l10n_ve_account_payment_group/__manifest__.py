# © 2016 ADHOC SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
{
    "name": "Account Payment with Multiple methods",
    "version": "14.0.1.0.0",
    "category": "Accounting",
    "website": "www.adhoc.com.ar",
    "author": "ADHOC SA, SINAPSYS GLOBAL SA || MASTERCORE SAS",
    "license": "AGPL-3",
    "application": False,
    'installable': True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": [
        "l10n_ve_account_financial_amount",
        # for fixes related to domains and company_id field on form view
        "l10n_ve_account_payment_fix",
    ],
    "data": [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizards/account_payment_group_invoice_wizard_view.xml',
        'wizards/res_config_settings_views.xml',
        'views/account_payment_view.xml',
        'views/account_move_line_view.xml',
        'views/account_payment_group_view.xml',
        'views/account_journal_dashboard_view.xml',
        'views/report_payment_group.xml',
        'data/mail_template_data.xml',
    ],
    "demo": [
    ],
}
