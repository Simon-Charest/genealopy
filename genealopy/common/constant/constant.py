from common.datetime_ import datetime_

__author__ = 'SLCIT, Inc.'
__email__ = 'simoncharest@gmail.com'
__copyright__ = f'Copyright © {datetime_.get_years(2020)} {__author__} <{__email__}>. All rights reserved.'
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
    'Gilles Charest': {},
    'Gilles Deguire': {'email': 'deguire@mesancetres.ca', 'organization': 'Mes ancêtres', 'website': 'http://www.mesancetres.ca/'},
    'Louise Charest': {'email': 'charestl53@videotron.ca'},
    'Marc Charest': {'email': 'marc@lourobin.com'},
    'Michel Charest': {'email': 'mic6349@gmail.com'},
    'Pierre Charest': {'email': 'charestp@videotron.ca', 'organization': '9116-8872 Québec inc.', 'website': 'https://www.myheritage.fr/site-205814691/charest'},
    'Richard Côté': {'email': 'richardcoste@sogetel.net', 'organization': "Le Centre de généalogie francophone d'Amérique", 'website': 'http://www.genealogie.org/login/'},
    'Suzanne Coderre': {'email': 'suzanne1809@gmail.com'},
    'The Charest Family': {}
}
__license__ = 'GNU'
__maintainer__ = 'Simon Charest'
__status__ = 'Developement'
__version__ = '2.0.0'

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

# Data files
DATA_DIRECTORY = 'data/'
INPUT_DIRECTORY = f'{DATA_DIRECTORY}input/'
OUTPUT_DIRECTORY = f'{DATA_DIRECTORY}output/'
ALL_FILENAMES = [f'{INPUT_DIRECTORY}**/*.json']
INPUT_FILENAMES = map(lambda filename: INPUT_DIRECTORY + str(filename), [
        # Laguë
        'Laguë/far_ascendance/*.json',  # Marie-Anne Lucas dit Francoeur's ascendance
        'Laguë/*.json',  # Suzanne Laguë's ascendance
        'Laguë/descendance/*.json',

        # Charest
        'Charest/far_ascendance/*.json',  # Delphis Charest's ascendance
        'Charest/tanguay_charest_siblings/*.json',  # Delphis Charest's siblings
        'Charest/dion_charette_ascendance/*.json',  # Aurèle Charette (Charest-Charette)'s ascendance
        'Charest/little_cousins/*.json',  # Clément Charest siblings' descendance
        'Charest/little_cousin_descendance/*.json',  # Clément Charest siblings' descendance
        'Tremblay/*.json',  # Rita Lacombe Tremblay's ascendance
        'Charest/*.json',
        'Charest/descendance/*.json',

        # Laguë-Charest
        '0?_lague_charest.json'
    ]
)
OUTPUT_FILENAME = f'{OUTPUT_DIRECTORY}data.txt'

# Encryption
SECURITY_DIRECTORY = f'{DATA_DIRECTORY}security/'
KEY_FILENAME = f'{SECURITY_DIRECTORY}key.txt'
SALT_FILENAME = f'{SECURITY_DIRECTORY}salt.txt'

# Visuals
GRAPH_DIRECTORY = f'{DATA_DIRECTORY}graph/'
GRAPH_FILENAME = f'{GRAPH_DIRECTORY}{__project__.lower()}.gv'
GRAPH_FORMAT = 'png'
RANK_DIRECTION = 'TB'  # TB, LR, BT or RL
SHAPE = 'box'
STYLE = 'filled'
NAME_UNKNOWN = '(inconnu)'

# Filters
GENDER = ['M', 'F']
RELATIONSHIP = ['grandfather', 'father', 'grandmother', 'mother', 'union']

# Colors
DARKEN_INCOMPLETE = True
FEMALE_COLOR = 'pink'
FEMALE_INCOMPLETE_COLOR = 'deeppink'
MALE_COLOR = 'lightblue'
MALE_INCOMPLETE_COLOR = 'deepskyblue'
UNDEFINED_COLOR = 'grey'
SEARCH_COLOR = 'orange'
PARENT_LINK_STYLE = 'solid'
UNDEFINED_LINK_STYLE = 'dashed'

# Debugging
DEBUG = False
