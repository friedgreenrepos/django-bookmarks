import re
from six.moves.urllib.parse import urlparse
from six.moves.urllib.parse import parse_qsl


def params_to_dict(params):
    params_dict = {}
    if params is not None:
        params_qsl = parse_qsl(params, keep_blank_values=True)
        params_dict = dict(params_qsl)
    return params_dict
