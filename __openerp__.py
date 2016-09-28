{
    'name': 'Elmatica - Sales Customization',
    'category': 'Sales',
    'version': '0.1',
    'depends': ['base','product'],
    'data': [
	'product_view.xml',
	'sale_view.xml',
	#'po10_report.xml',
	#'po20_report.xml',
	#'po21_report.xml',
	#'shipping_label_report.xml',
	'security/ir.model.access.csv',
	'security/security.xml',
	'wizard/wizard_view.xml'
    ],
    'demo': [
    ],
    'qweb': [],
    # 'css': ['static/src/css/styles.css',],
    'installable': True,
}
