from genealopy.__init__ import __project__
from pathlib import Path

"""Filenames examples:
    ma01_dubreuil_lague.json    : first-degree (01) ascendant (a) of the mother's side (m) of the family
    fa01_tremblay_charest.json  : first-degree (01) ascendant (a) of the father's side (f) of the family
    00_lague_charest.json       : Root (00) of both sides of the family
    m00_dubreuil_lague.json     : Root (00) of the mother's side (m) of the family
    f00_tremblay_charest.json   : Root (00) of the father's side (f) of the family
    md01_dubreuil_lague.json    : first-degree (01) descendant (d) of the mother's side (m) of the family
    fd01_charest_drouin.json    : first-degree (01) descendant (d) of the father's side (f) of the family
"""

# Data files
DATA_PATH: Path = Path(__file__).parent.joinpath("data")
INPUT_PATH: Path = DATA_PATH.joinpath("input")
OUTPUT_PATH: Path = DATA_PATH.joinpath("output")
ALL_FILENAMES: list = [INPUT_PATH.joinpath("**/*.json")]
INPUT_FILENAMES: list = map(lambda filename: INPUT_PATH.joinpath(filename), [
        # Laguë
        # "Laguë/far_ascendance/*.json",  # Marie-Anne Lucas dit Francoeur's ascendance
        # "Laguë/*.json",  # Suzanne Laguë's ascendance
        # "Laguë/descendance/*.json",

        # Charest
        "Charest/far_ascendence/fa99_delorraine.json",  # Charest noble ascendence
        "Charest/far_ascendence/*.json",  # Delphis Charest's ascendence
        "Charest/tanguay_charest_siblings/*.json",  # Delphis Charest's siblings
        "Charest/dion_charette_ascendence/*.json",  # Aurèle Charette (Charest-Charette)'s ascendence
        "Charest/little_cousins/*.json",  # Clément Charest siblings" descendence
        "Charest/little_cousin_descendence/*.json",  # Clément Charest siblings" descendence
        "Tremblay/*.json",  # Rita Lacombe Tremblay's ascendence
        "Charest/*.json",
        "Charest/descendence/*.json",

        # Laguë-Charest
        "0?_lague_charest.json"
    ]
)
OUTPUT_FILENAME: Path = OUTPUT_PATH.joinpath("data.txt")

# Encryption
SECURITY_PATH: Path = DATA_PATH.joinpath("security")
KEY_FILENAME: Path = SECURITY_PATH.joinpath("key.txt")
SALT_FILENAME: Path = SECURITY_PATH.joinpath("salt.txt")

# Visuals
GRAPH_PATH: Path = DATA_PATH.joinpath("graph")
GRAPH_FILENAME: Path = GRAPH_PATH.joinpath(f"{__project__.lower()}.gv")
GRAPH_FORMAT: str = "png"
RANK_DIRECTION: str = "TB"  # TB, LR, BT or RL
SHAPE: str = "box"
STYLE: str = "filled"
NAME_UNKNOWN: str = "(inconnu)"

# Filters
GENDER: list = ["M", "F"]
RELATIONSHIP: list = ["grandfather", "father", "grandmother", "mother", "union"]

# Colors
DARKEN_INCOMPLETE: bool = True
FEMALE_COLOR: str = "pink"
FEMALE_INCOMPLETE_COLOR: str = "deeppink"
MALE_COLOR: str = "lightblue"
MALE_INCOMPLETE_COLOR: str = "deepskyblue"
UNDEFINED_COLOR: str = "grey"
SEARCH_COLOR: str = "orange"
PARENT_LINK_STYLE: str = "solid"
UNDEFINED_LINK_STYLE: str = "dashed"

# Debugging
DEBUG: bool = False
