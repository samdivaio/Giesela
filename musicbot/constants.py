import os.path

MAIN_VERSION = "4.3.5"
SUB_VERSION = "breadstick"
VERSION = MAIN_VERSION + "_" + SUB_VERSION

all_sub_versions = {
    "4.3.x": "Breadstick",
    "4.2.x": "Ice Cube",
    "4.1.x": "Gooma",
    "4.0.x": "New Reign",
    "3.9.x": "Giesenesis",
    "3.8.x": "Giezela",
    "3.7.x": "GieseLa La Land",
    "3.6.x": "Weebiesela",
    "3.5.x": "Veggiesela",
    "3.4.x": "Gunzulalela",
    "3.3.x": "Giselator",
    "3.2.x": "GG iesela",
    "3.1.x": "Age of Giesela",
    "3.0.x": "Giesela PLUS"
}

AUDIO_CACHE_PATH = "cache/audio_cache"
ABS_AUDIO_CACHE_PATH = os.path.join(os.getcwd(), AUDIO_CACHE_PATH)
DISCORD_MSG_CHAR_LIMIT = 2000
