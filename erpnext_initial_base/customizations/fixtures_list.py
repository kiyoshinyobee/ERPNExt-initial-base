from .fixtures.client_script import client_script_fixtures
from .fixtures.custom_docperm import custom_docperm_fixtures
from .fixtures.property_setter import property_setter_fixtures
from .fixtures.role import role_fixtures
from .fixtures.role_profile import role_profile_fixtures


# Please be carefull with the order of the fixtures
fixtures_list = role_fixtures + \
    role_profile_fixtures + \
    custom_docperm_fixtures + \
    client_script_fixtures + \
    property_setter_fixtures
