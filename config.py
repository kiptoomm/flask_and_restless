"""
    Run Configuration
    ~~~~~~
    Defines runtime variables to
    support different environments

    :copyright: (c) 2017 by Kiptoo Magutt
"""

import os

# define configuration environment names
CONFIG_DEVELOPMENT = 'development'
CONFIG_DEVELOPMENT_FLEX = 'development-flex'
CONFIG_TESTING = 'testing'
CONFIG_STAGING = 'staging'
CONFIG_PRODUCTION = 'production'

# value of the 'FLASK_CONFIG' env var,
# should match any of the names above, one at a time
CONFIG_ENV_VAR_NAME = 'development' # os.environ['FLASK_CONFIG']

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments

    DEBUG = True
    TESTING = False

    CLOUDSQL_USER = 'root'
    CLOUDSQL_PASSWORD = 'testpassword'
    CLOUDSQL_DATABASE = 'flask_restless_db'

    CONFIG_NAME = CONFIG_DEVELOPMENT

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevConfigStd(Config):
    """
    Development configuration for the Google App Engine Standard Environment
    """

    CONFIG_NAME = CONFIG_DEVELOPMENT

    # this check is only necessary as far as logging is concerned. that is,
    # we don't want to unnecessarily print misleading messages or execute other code
    # if this is not the currently active config
    if CONFIG_ENV_VAR_NAME == CONFIG_NAME:
        print "current config name: ", CONFIG_NAME

        CLOUDSQL_CONNECTION_NAME = 'flask-and-restless:europe-west1:flask-restless-db'

        LOCAL_SQLALCHEMY_DATABASE_URI = (
            'mysql+mysqldb://{user}:{password}@127.0.0.1:3306/{database}').format(
            user=Config.CLOUDSQL_USER, password=Config.CLOUDSQL_PASSWORD, database=Config.CLOUDSQL_DATABASE)

        # When running on App Engine a unix socket is used to connect to the cloudsql
        # instance.
        live_host_name = 'localhost'
        LIVE_SQLALCHEMY_DATABASE_URI = (
            'mysql+mysqldb://{user}:{password}@{hostname}/{database}'
            '?unix_socket=/cloudsql/{connection_name}').format(
            user=Config.CLOUDSQL_USER, password=Config.CLOUDSQL_PASSWORD, hostname=live_host_name,
            database=Config.CLOUDSQL_DATABASE, connection_name=CLOUDSQL_CONNECTION_NAME)

        if os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
            SQLALCHEMY_DATABASE_URI = LIVE_SQLALCHEMY_DATABASE_URI
            print "********* running in the live standard env ********", SQLALCHEMY_DATABASE_URI
        else:
            SQLALCHEMY_DATABASE_URI = LOCAL_SQLALCHEMY_DATABASE_URI
            print "********* running in the local standard env ********", SQLALCHEMY_DATABASE_URI


class DevConfigFlex(Config):
    """
    Development configuration for the Google App Engine Flexible Environment
    """

    CONFIG_NAME = CONFIG_DEVELOPMENT_FLEX

    if CONFIG_ENV_VAR_NAME == CONFIG_NAME:
        print "current config name: ", CONFIG_NAME


class TestingConfig(Config):
    """
    Testing configurations
    """

    CONFIG_NAME = CONFIG_TESTING

    if CONFIG_ENV_VAR_NAME == CONFIG_NAME:
        print "current config name: ", CONFIG_NAME

        DEBUG = True
        #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://twende_test_user:test_password@localhost/twende_test'

        TESTING = True

class ProductionConfig(Config):
    """
    Production configurations
    """

    CONFIG_NAME = CONFIG_PRODUCTION

    if CONFIG_ENV_VAR_NAME == CONFIG_NAME:
        print "current config name: ", CONFIG_NAME

        DEBUG = False

app_config = {
    CONFIG_DEVELOPMENT: DevConfigStd,
    CONFIG_DEVELOPMENT_FLEX: DevConfigFlex,
    CONFIG_TESTING: TestingConfig,
    CONFIG_PRODUCTION: ProductionConfig
}
