from datetime import timedelta


class BaseConfig():
    # SECRET_KEY = 'test'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)


class Development(BaseConfig):
    """开发环境"""
    ENV = 'development'
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)


class Production(BaseConfig):
    """开发环境"""
    ENV = 'production'
    PERMANENT_SESSION_LIFETIME = timedelta(days=2)

# 定义字典来记录 配置类型 和 配置子类  之间的映射关系
config_dict = {
    'dev': Development,
    'pro': Production
}