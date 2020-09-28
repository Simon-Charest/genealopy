from common.datetime_ import datetime

__author__ = 'SLCIT, Inc.'
__email__ = 'simoncharest@gmail.com'
__copyright__ = f'Copyright © {datetime.get_years(2020)} {__author__} <{__email__}>. All rights reserved.'
__project__ = 'Genealopy'
__credits__ = {
    'Simon Charest': {
        'organization': [f'{__author__}', 'SLCIT, Inc.'],
        'email': [f'{__email__}', 'simoncharest@gmail.com'],
        'Facebook': 'https://www.facebook.com/simon.charest/',
        'GitHub': 'https://github.com/Simon-Charest',
        'LinkedIn': 'https://www.linkedin.com/in/simoncharest/',
        'Twitter': 'https://twitter.com/scharest'
    },
    'Francis-Olivier Gradel, Eng.': {
        'organization': 'Retronic Design',
        'product': 'DB9 to USB Game Controller Adapter',
        'email': 'info@retronicdesign.com',
        'website': 'retronicdesign.com',
        'eBay': 'https://www.ebay.com/usr/retronicdesign',
        'Facebook': 'https://www.facebook.com/retronicdesign',
        'LinkedIn': 'https://ca.linkedin.com/in/francis-gradel-ing-b620591a',
        'Twitter': 'https://twitter.com/fogradel',
        'AtariAge': 'https://atariage.com/forums/profile/37766-nitz1976/',
        'Famille Gradel': 'https://www.retronicdesign.com/genealogie/'
       },
    'Michel Charest': {
        'email': 'mic6349@gmail.com'
    },
    'Louise Charest': {
        'email': 'charestl53@videotron.ca'
    },
    'Pierre Charest': {
        'organization': '9116-8872 Québec inc.',
        'email': 'charestp@videotron.ca'
    },
    'Suzanne Coderre': {
        'email': 'suzanne1809@gmail.com'
    },
    'The Charest Family': {},
    'Gilles Deguire': {
        'organization': 'Mes ancêtres',
        'email': 'deguire@mesancetres.ca',
        'website': 'http://www.mesancetres.ca/'
    },
    'Richard Côté': {
        'organization': "Le Centre de généalogie francophone d'Amérique",
        'email': 'richardcoste@sogetel.net',
        'website': 'http://www.genealogie.org/login/'
    }
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
RANK_DIRECTION = 'TB'  # TB, LR, BT or RL
DATA = [
    'data/Charest/far_ascendance/*.json',  # Delphis Charest's ascendance
    'data/Charest/tanguay_charest_siblings/*.json',  # Delphis Charest's siblings
    'data/Charest/dion_charette_ascendance/*.json',  # Aurèle Charette (Charest-Charette)'s ascendance
    'data/Charest/little_cousins/*.json',  # Clément Charest siblings' descendance
    'data/Charest/little_cousin_descendance/*.json',  # Clément Charest siblings' descendance
    'data/Tremblay/*.json',  # Rita Lacombe Tremblay's ascendance
    'data/Charest/*.json',
    'data/Laguë/*.json',  # Suzanne Laguë's ascendance
    'data/0?_lague_charest.json',
    'data/Charest/descendance/*.json'
]
SHAPE = 'box'
STYLE = 'filled'
GENDER = ['M', 'F']
RELATIONSHIP = ['father', 'mother', 'union']
FEMALE_COLOR = 'pink'
FEMALE_INCOMPLETE_COLOR = 'deeppink'
MALE_COLOR = 'lightblue'
MALE_INCOMPLETE_COLOR = 'deepskyblue'
UNDEFINED_COLOR = 'grey'
PARENT_LINK_STYLE = 'solid'
UNDEFINED_LINK_STYLE = 'dashed'
NAME_UNKNOWN = '(inconnu)'
HIGHLIGHT_INCOMPLETE = True
DEBUG = False
SEARCH_COLOR = 'yellow'

"""
Filenames examples:
    ma01_dubreuil_lague.json   : first-degree (01) ascendant (a) of the mother's side (m) of the family
    fa01_tremblay_charest.json : first-degree (01) ascendant (a) of the father's side (f) of the family
    00_lague_charest.json      : Root (00) of both sides of the family
    m00_dubreuil_lague.json    : Root (00) of the mother's side (m) of the family
    f00_tremblay_charest.json  : Root (00) of the father's side (f) of the family
    md01_dubreuil_lague.json   : first-degree (01) descendant (d) of the mother's side (m) of the family
    fd01_charest_drouin.json   : first-degree (01) descendant (d) of the father's side (f) of the family
"""
