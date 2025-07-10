from pathlib import Path

HYPR_CONFIG_DIR = Path.home() / ".config" / "hypr"
AUTOGEN_CONF_DIR = HYPR_CONFIG_DIR / "conf.d" / "autogen"

WALLPAPER_DIR = Path.home() / "images" / "wallpapers"
ALLOWED_WALLPAPER_EXTENSIONS = [
    "*.jpg",
    "*.jpeg",
    "*.png",
    "*.gif",
    "*.bmp",
    "*.tiff",
    "*.webp",
]

WALLPAPER_CURRENT_PLAYLIST_PATH = Path.home() / ".cache" / "wallpaper-current-playlist"
WALLPAPER_PLAYLIST_PATH = WALLPAPER_DIR / "playlists.toml"
