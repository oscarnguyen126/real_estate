{
    'name': 'Estate',
    'version': '1.0',
    'category': 'Sale',
    'sequence': 15,
    'summary': 'Real estate',
    'description': "",
    'depends': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_view.xml',
        'views/type.xml',
        'views/tags.xml',
        'views/offer.xml',


        'views/estate_menus.xml',
    ],
    'demo': [
    ],
    'installable': True,
    'application': True,
}