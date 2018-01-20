from .default import Config


class DevelopmentConfig(Config):
    # enable debug mode
    DEBUG = True
    # follow 2 parameters my be false to enable PyCharm debugging (or any other IDE)
    USE_DEBUGGER = False
    USE_RELOADER = False
    # show where templates are loaded from
    # EXPLAIN_TEMPLATE_LOADING = True
