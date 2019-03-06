{
    'name' : "sunfire invoice",
    'summary' : "sunfire_invoice",
    'description' : """**********************""",
    'author' : "Sai Application",
    'website' : "http://www.saiaipl.com",
    'category' : 'Uncategorized',
    'version' : '11.0.1.0.0',
    'depends' : ['account','sale','account_invoicing','web','l10n_in','account_tax_python', 'product', 'analytic', 'web_planner', 'portal','sunfire_sales'],
    'data' : [
        'report/invc_menu.xml',
        'report/invoice_report.xml',
        'report/invoice_cust_template.xml',
        'report/invoice_with_out_unit_rate.xml',
        'views/account_invoice_inhe.xml',
        'views/res_company_view_inhe.xml',
	'views/account_supplier_invoice_form.xml',
        'report/invoice_outstanding_report.xml',
	'views/ref_template.xml'
            ],
    'installable': True,
    'auto_install': True,
    'application': True,
}
