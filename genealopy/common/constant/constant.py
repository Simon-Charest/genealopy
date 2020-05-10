from common.datetime_ import datetime

__author__ = 'SLCIT, Inc.'
__email__ = 'simoncharest@gmail.com'
__copyright__ = f'Copyright © {datetime.get_years(2020)} {__author__} <{__email__}>. All rights reserved.'
__project__ = 'Genealopy'
__credits__ = {
    'Simon Charest': {
        'organization': [f'{__author__}', 'Retronic Design'],
        'email': [f'{__email__}', 'simoncharest@retronicdesign.com'],
        'Facebook': 'https://www.facebook.com/simon.charest/',
        'GitHub': 'https://github.com/Simon-Charest',
        'LinkedIn': 'https://www.linkedin.com/in/simoncharest/',
        'Twitter': 'https://twitter.com/scharest'
    },
    'Francis-Olivier Gradel, Eng.': {
        'organization': 'Retronic Design',
        'product': 'DB9 to USB Game Controller Adapter',
        'email': 'info@retronicdesign.com',
        'eBay': 'https://www.ebay.com/usr/retronicdesign',
        'Facebook': 'https://www.facebook.com/retronicdesign',
        'LinkedIn': 'https://ca.linkedin.com/in/francis-gradel-ing-b620591a',
        'Twitter': 'https://twitter.com/fogradel',
        'Website': 'retronicdesign.com',
        'AtariAge': 'https://atariage.com/forums/profile/37766-nitz1976/'
       },
    'Michel Charest': {},
    'Louise Charest': {},
    'Pierre Charest': {}
}
__license__ = 'GNU'
__maintainer__ = 'Simon Charest'
__status__ = 'Developement'
__version__ = '2.0.0'

ABOUT = f'{__project__}\n' \
        f'Version {__version__}\n' \
        f'{__copyright__}\n' \
        f'\n' \
        f'The {__project__} and its software are the propriety of ' \
        f'{__author__}.\n' \
        f'This software is open-source and provided free of charge.\n' \
        f'\n' \
        f'This product is license under the {__license__} License Terms.'
DATA = 'data/data.json'
DEBUG = True
SOURCES = {
    "Famille Gradel": {
        'owner': 'Francis Gradel',
        'email': 'info@retronicdesign.com',
        'hyperlink': 'https://www.retronicdesign.com/genealogie/individual.php?ged=gradel&pid='
    },
    "Le Centre de généalogie francophone d'Amérique": {
        'brief_summary': 'Familles Côté, Tremblay (02-2019)',
        'detailed description': 'Une magnifique banque de données sur plus de 600,000 individus.',
        'owner': 'Richard Côté',
        'email': 'richardcoste@sogetel.net',
        'hyperlink': 'http://www.genealogie.org/bcentrale/liste.asp?code_owner=214&code_individu='
    }
}
