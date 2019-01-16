from django.conf import settings

BUTTON_TEXT_SAVE = getattr(
    settings,
    'BOOKMARKS_BUTTON_TEXT_SAVE',
    'Salva nei Bookmark',
)

BUTTON_TEXT_DELETE = getattr(
    settings,
    'BOOKMARKS_BUTTON_TEXT_DELETE',
    'Rimuovi dai Bookmark',
)

BOOKMARK_FORM_NAME = getattr(
    settings,
    'BOOKMARKS_BOOKMARK_FORM_NAME',
    'Nome',
)
