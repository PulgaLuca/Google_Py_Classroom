import re

def sanitize_filename(filename):
    """Rimuove caratteri non validi per il filesystem dai nomi dei file."""
    return re.sub(r'[\\/*?:"<>|]', '_', filename)
