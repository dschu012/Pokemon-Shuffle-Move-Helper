from pathlib import Path


BARRIER_PREFIX = "Barrier_"
LAST_BOARD_IMAGE_PATH = r"last_board.png"
LAST_SCREEN_IMAGE_PATH = r"last_screen.png"
IMAGES_BARRIER_PATH = r"assets\icons_barrier"
IMAGES_EXTRA_PATH = r"assets\icons_extra"
IMAGES_PATH = r"assets\icons_processed"
ASSETS_PATH = r"assets"
BARRIER_TYPE_REAL = "Real"
BARRIER_TYPE_FAKE = "Fake"

GRADING_TOTAL_SCORE = "grading.score"
GRADING_MEGA_PROGRESS = "grading.megaprogress"
GRADING_WEEKEND_MEOWTH = "WeekendMeowth"

move_strategy = {
    "grading.score": "Total Score",
    "grading.totalblocks": "Total Blocks",
    "grading.disruptions": "Disruptions",
    "grading.mindisruptions": "Low Disrupt.",
    "grading.combos": "Combos",
    "grading.noneorall": "None or All",
    "grading.megaprogress": "Mega Progress",
    "grading.coordinate": "Coordinates",
    "WeekendMeowth": "WeekendMeowth"
}

move_stages = {
    "NORMAL": "NORMAL",
    "FIRE": "FIRE",
    "WATER": "WATER",
    "GRASS": "GRASS",
    "ELECTRIC": "ELECTRIC",
    "ICE": "ICE",
    "FIGHTING": "FIGHTING",
    "POISON": "POISON",
    "GROUND": "GROUND",
    "FLYING": "FLYING",
    "PSYCHIC": "PSYCHIC",
    "BUG": "BUG",
    "ROCK": "ROCK",
    "GHOST": "GHOST",
    "DRAGON": "DRAGON",
    "DARK": "DARK",
    "STEEL": "STEEL",
    "FAIRY": "FAIRY",
    "NONE": "NONE",
    "SP_084": "MEOWTH COIN MANIA"
}
downscale_res = (128, 128)




CURRENT_HEARTS_LIST = [
    Path(r"assets\auto_loop\heart_5.png"),
    Path(r"assets\auto_loop\heart_4.png"),
    Path(r"assets\auto_loop\heart_3.png"),
    Path(r"assets\auto_loop\heart_2.png"),
    Path(r"assets\auto_loop\heart_1.png"),
    Path(r"assets\auto_loop\heart_0.png"),
]

CURRENT_STAGE_IMAGE = r"assets\auto_loop\current_stage.png"
CONTINUE_IMAGE_IMAGE = r"assets\auto_loop\continue_image.png"
START_BUTTON_IMAGE = r"assets\auto_loop\start_button.png"
OK_BUTTON_IMAGE = r"assets\auto_loop\ok_button.png"
OK_BUTTON2_IMAGE = r"assets\auto_loop\ok_button2.png"
TO_MAP_BUTTON_IMAGE = r"assets\auto_loop\to_map_button.png"
ACTIVE_BOARD_IMAGE = r"assets\auto_loop\active_board.png"