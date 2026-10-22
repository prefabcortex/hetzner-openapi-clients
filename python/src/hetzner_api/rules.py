"""Rules of the spec, defined once (generated - do not edit by hand).

``*_RULES``: rules of named schemas; ``*_FIELDS``: rules of the fields of request
objects. Checked only with ``validation="strict"`` - see :mod:`hetzner_api._validation`.
"""

from typing import Final

from hetzner_api._validation import Check

__all__ = [
    "CREATE_LOAD_BALANCER_REQUEST_TARGET_FIELDS",
    "HEALTH_CHECK_HTTP_FIELDS",
    "LABELS_RULES",
    "LOAD_BALANCER_CREATE_PUBLIC_NET_FIELDS",
    "LOAD_BALANCER_SERVICE_HEALTH_CHECK2_FIELDS",
    "LOAD_BALANCER_SERVICE_HTTP_FIELDS",
    "LOAD_BALANCER_TARGET_LABEL_SELECTOR_FIELDS",
    "RR_SET_REQUEST_FIELDS",
    "RULE_FIELDS",
    "UPDATE_LOAD_BALANCER_SERVICE_HEALTH_CHECK_FIELDS",
    "UPDATE_LOAD_BALANCER_SERVICE_HTTP_FIELDS",
]


LABELS_RULES: Final[Check] = Check(
    values=Check(max_length=63, pattern="^([a-zA-Z0-9]([-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9])?)?$"),
    keys=Check(
        pattern="^((?=[^/]{1,253}/)[a-zA-Z0-9]([-a-zA-Z0-9]{0,61}[a-zA-Z0-9])?(\\.[a-zA-Z0-9]([-a-zA-Z0-9]{0,61}[a-zA-Z0-9])?)*/)?[a-zA-Z0-9]([-_.a-zA-Z0-9]{0,61}[a-zA-Z0-9])?$"
    ),
)


CREATE_LOAD_BALANCER_REQUEST_TARGET_FIELDS: Final[Check] = Check(
    fields=(
        ("label_selector", Check(fields_of=lambda: LOAD_BALANCER_TARGET_LABEL_SELECTOR_FIELDS)),
    )
)


HEALTH_CHECK_HTTP_FIELDS: Final[Check] = Check(
    fields=(
        ("domain", Check(max_length=128)),
        ("path", Check(min_length=1, max_length=256)),
        ("response", Check(max_length=256)),
        ("status_codes", Check(max_items=20)),
    )
)


LOAD_BALANCER_CREATE_PUBLIC_NET_FIELDS: Final[Check] = Check(
    fields=(
        ("ipv4", Check(minimum=1, maximum=9007199254740991)),
        ("ipv6", Check(minimum=1, maximum=9007199254740991)),
    )
)


LOAD_BALANCER_SERVICE_HEALTH_CHECK2_FIELDS: Final[Check] = Check(
    fields=(
        ("interval", Check(minimum=3, maximum=60)),
        ("timeout", Check(minimum=1, maximum=60)),
        ("retries", Check(minimum=1, maximum=5)),
        ("http", Check(fields_of=lambda: HEALTH_CHECK_HTTP_FIELDS)),
    )
)


LOAD_BALANCER_SERVICE_HTTP_FIELDS: Final[Check] = Check(
    fields=(
        ("cookie_name", Check(min_length=1, max_length=100)),
        ("cookie_lifetime", Check(minimum=30, maximum=86400)),
    )
)


LOAD_BALANCER_TARGET_LABEL_SELECTOR_FIELDS: Final[Check] = Check(
    fields=(("selector", Check(min_length=1, max_length=1000)),)
)


RR_SET_REQUEST_FIELDS: Final[Check] = Check(
    fields=(("ttl", Check(minimum=60, maximum=2147483647)), ("labels", LABELS_RULES))
)


RULE_FIELDS: Final[Check] = Check(fields=(("description", Check(max_length=255)),))


UPDATE_LOAD_BALANCER_SERVICE_HEALTH_CHECK_FIELDS: Final[Check] = Check(
    fields=(
        ("interval", Check(minimum=3, maximum=60)),
        ("timeout", Check(minimum=1, maximum=60)),
        ("retries", Check(minimum=1, maximum=5)),
        ("http", Check(fields_of=lambda: HEALTH_CHECK_HTTP_FIELDS)),
    )
)


UPDATE_LOAD_BALANCER_SERVICE_HTTP_FIELDS: Final[Check] = Check(
    fields=(
        ("cookie_name", Check(min_length=1, max_length=100)),
        ("cookie_lifetime", Check(minimum=30, maximum=86400)),
    )
)
