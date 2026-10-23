# core/exceptions.py
class TemplateError(Exception):
    """母艦の共通基底エラー"""
    pass

class FilmValidationError(TemplateError):
    """Film（YAML）の検証エラー"""
    pass
