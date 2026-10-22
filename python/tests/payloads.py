"""Example responses of the API (derived from the examples in the spec)."""

from typing import Final

from pydantic import JsonValue

ACTION: Final[JsonValue] = {
    "id": 42,
    "command": "start_resource",
    "status": "running",
    "started": "2016-01-30T23:55:00Z",
    "finished": "2016-01-30T23:55:00Z",
    "progress": 100,
    "resources": [{"id": 42, "type": "server"}],
    "error": {"code": "action_failed", "message": "Action failed"},
}


ACTION_LIST_RESPONSE: Final[JsonValue] = {
    "actions": [
        {
            "id": 42,
            "command": "start_resource",
            "status": "running",
            "started": "2016-01-30T23:55:00Z",
            "finished": "2016-01-30T23:55:00Z",
            "progress": 100,
            "resources": [{"id": 42, "type": "server"}],
            "error": {"code": "action_failed", "message": "Action failed"},
        }
    ]
}


ACTION_LIST_RESPONSE_WITH_META: Final[JsonValue] = {
    "actions": [
        {
            "id": 42,
            "command": "start_resource",
            "status": "running",
            "started": "2016-01-30T23:55:00Z",
            "finished": "2016-01-30T23:55:00Z",
            "progress": 100,
            "resources": [{"id": 42, "type": "server"}],
            "error": {"code": "action_failed", "message": "Action failed"},
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


ACTION_RESPONSE: Final[JsonValue] = {
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    }
}


CERTIFICATES_RESPONSE: Final[JsonValue] = {
    "certificates": [
        {
            "id": 42,
            "name": "my-resource",
            "labels": {"key": "example"},
            "type": "uploaded",
            "certificate": "-----BEGIN CERTIFICATE-----\n...",
            "created": "2016-01-30T23:55:00Z",
            "not_valid_before": "2019-01-08T10:00:00Z",
            "not_valid_after": "2019-07-08T09:59:59Z",
            "domain_names": ["example.com", "webmail.example.com", "www.example.com"],
            "fingerprint": "03:c7:55:9b:2a:d1:04:17:09:f6:d0:7f:18:34:63:d4:3e:5f",
            "status": {
                "issuance": "completed",
                "renewal": "scheduled",
                "error": {"code": "example", "message": "example"},
            },
            "used_by": [{"id": 4711, "type": "load_balancer"}],
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


CERTIFICATE_RESPONSE: Final[JsonValue] = {
    "certificate": {
        "id": 42,
        "name": "my-resource",
        "labels": {"key": "example"},
        "type": "uploaded",
        "certificate": "-----BEGIN CERTIFICATE-----\n...",
        "created": "2016-01-30T23:55:00Z",
        "not_valid_before": "2019-01-08T10:00:00Z",
        "not_valid_after": "2019-07-08T09:59:59Z",
        "domain_names": ["example.com", "webmail.example.com", "www.example.com"],
        "fingerprint": "03:c7:55:9b:2a:d1:04:17:09:f6:d0:7f:18:34:63:d4:3e:5f",
        "status": {
            "issuance": "completed",
            "renewal": "scheduled",
            "error": {"code": "example", "message": "example"},
        },
        "used_by": [{"id": 4711, "type": "load_balancer"}],
    }
}


CREATE_CERTIFICATE_RESPONSE: Final[JsonValue] = {
    "certificate": {
        "id": 42,
        "name": "my-resource",
        "labels": {"key": "example"},
        "type": "uploaded",
        "certificate": "-----BEGIN CERTIFICATE-----\n...",
        "created": "2016-01-30T23:55:00Z",
        "not_valid_before": "2019-01-08T10:00:00Z",
        "not_valid_after": "2019-07-08T09:59:59Z",
        "domain_names": ["example.com", "webmail.example.com", "www.example.com"],
        "fingerprint": "03:c7:55:9b:2a:d1:04:17:09:f6:d0:7f:18:34:63:d4:3e:5f",
        "status": {
            "issuance": "completed",
            "renewal": "scheduled",
            "error": {"code": "example", "message": "example"},
        },
        "used_by": [{"id": 4711, "type": "load_balancer"}],
    },
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


CREATE_FIREWALL_RESPONSE: Final[JsonValue] = {
    "firewall": {
        "id": 42,
        "name": "new-name",
        "labels": {"key": "example"},
        "created": "2016-01-30T23:55:00Z",
        "rules": [
            {
                "description": "example",
                "direction": "in",
                "source_ips": [
                    "192.0.2.2/32",
                    "192.0.2.0/24",
                    "2001:0db8:9a3b:ee58:5ca:990c:8bc9:c03b/128",
                ],
                "destination_ips": ["example"],
                "protocol": "tcp",
                "port": "80",
            }
        ],
        "applied_to": [
            {
                "type": "server",
                "server": {"id": 42},
                "label_selector": {"selector": "env=prod"},
                "applied_to_resources": [{"type": "server", "server": {"id": 42}}],
            }
        ],
    },
    "actions": [
        {
            "id": 42,
            "command": "start_resource",
            "status": "running",
            "started": "2016-01-30T23:55:00Z",
            "finished": "2016-01-30T23:55:00Z",
            "progress": 100,
            "resources": [{"id": 42, "type": "server"}],
            "error": {"code": "action_failed", "message": "Action failed"},
        }
    ],
}


CREATE_FLOATING_IP_RESPONSE: Final[JsonValue] = {
    "floating_ip": {
        "id": 42,
        "name": "my-resource",
        "description": "This describes my resource",
        "ip": "2001:db8::/64",
        "type": "ipv6",
        "server": 42,
        "dns_ptr": [{"ip": "2001:db8::1", "dns_ptr": "server.example.com"}],
        "home_location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "blocked": False,
        "protection": {"delete": False},
        "labels": {"key": "example"},
        "created": "2016-01-30T23:55:00Z",
    },
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


CREATE_LOAD_BALANCER_RESPONSE: Final[JsonValue] = {
    "load_balancer": {
        "id": 42,
        "name": "my-resource",
        "public_net": {
            "enabled": True,
            "ipv4": {"id": 42, "ip": "1.2.3.4", "blocked": False, "dns_ptr": "lb1.example.com"},
            "ipv6": {"id": 42, "ip": "1.2.3.4", "blocked": False, "dns_ptr": "lb1.example.com"},
        },
        "private_net": [{"network": 4711, "ip": "10.0.0.2"}],
        "location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "load_balancer_type": {
            "id": 1,
            "name": "lb11",
            "description": "LB11",
            "max_connections": 20000,
            "max_services": 5,
            "max_targets": 25,
            "max_assigned_certificates": 10,
            "deprecated": "2016-01-30T23:50:00Z",
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
            "prices": [
                {
                    "location": "fsn1",
                    "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                    "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                    "included_traffic": 654321,
                    "price_per_tb_traffic": {"net": "1.0000", "gross": "1.1900"},
                }
            ],
        },
        "protection": {"delete": False},
        "labels": {"key": "example"},
        "created": "2016-01-30T23:55:00Z",
        "services": [
            {
                "protocol": "tcp",
                "listen_port": 443,
                "destination_port": 80,
                "proxyprotocol": False,
                "health_check": {
                    "protocol": "http",
                    "port": 4711,
                    "interval": 15,
                    "timeout": 10,
                    "retries": 3,
                    "http": {
                        "domain": "example.com",
                        "path": "/",
                        "response": '{"status": "ok"}',
                        "status_codes": ["2??", "3??"],
                        "tls": False,
                    },
                },
            }
        ],
        "targets": [
            {
                "type": "server",
                "server": {"id": 80, "ip": "2001:db8::1"},
                "health_status": [
                    {
                        "listen_port": 443,
                        "status": "healthy",
                        "detail": "unexpected_http_status",
                        "http_status_code": 503,
                    }
                ],
                "use_private_ip": True,
            }
        ],
        "algorithm": {"type": "round_robin"},
        "outgoing_traffic": 1,
        "ingoing_traffic": 1,
        "included_traffic": 10000,
    },
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


CREATE_PLACEMENT_GROUP_RESPONSE: Final[JsonValue] = {
    "placement_group": {
        "id": 42,
        "name": "my-resource",
        "labels": {"key": "example"},
        "type": "spread",
        "created": "2016-01-30T23:55:00Z",
        "servers": [42],
    },
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


CREATE_PRIMARY_IP_RESPONSE: Final[JsonValue] = {
    "primary_ip": {
        "id": 42,
        "name": "my-resource",
        "labels": {"key": "example"},
        "created": "2016-01-30T23:55:00Z",
        "blocked": False,
        "location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "ip": "2001:db8::/64",
        "dns_ptr": [{"ip": "2001:db8::1", "dns_ptr": "server.example.com"}],
        "protection": {"delete": False},
        "type": "ipv6",
        "auto_delete": True,
        "assignee_type": "server",
        "assignee_id": 17,
    },
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


CREATE_SERVER_IMAGE_RESPONSE: Final[JsonValue] = {
    "image": {
        "id": 42,
        "type": "snapshot",
        "status": "available",
        "name": "ubuntu-24.04",
        "description": "Ubuntu 24.04 Standard 64 bit",
        "image_size": 2.3,
        "disk_size": 10,
        "created": "2016-01-30T23:55:00Z",
        "created_from": {"id": 1, "name": "Server"},
        "bound_to": 1,
        "os_flavor": "ubuntu",
        "os_version": "24.04",
        "rapid_deploy": False,
        "protection": {"delete": False},
        "deprecated": "2018-02-28T00:00:00Z",
        "deprecation": {
            "unavailable_after": "2023-09-01T00:00:00Z",
            "announced": "2023-06-01T00:00:00Z",
        },
        "deleted": "example",
        "labels": {"key": "example"},
        "architecture": "x86",
    },
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


CREATE_SERVER_RESPONSE: Final[JsonValue] = {
    "server": {
        "id": 42,
        "name": "my-resource",
        "status": "running",
        "created": "2016-01-30T23:55:00Z",
        "public_net": {
            "ipv4": {
                "id": 42,
                "ip": "1.2.3.4",
                "blocked": False,
                "dns_ptr": "server01.example.com",
            },
            "ipv6": {
                "id": 42,
                "ip": "2001:db8::/64",
                "blocked": False,
                "dns_ptr": [{"ip": "2001:db8::1", "dns_ptr": "server.example.com"}],
            },
            "floating_ips": [478],
            "firewalls": [{"id": 42, "status": "applied"}],
        },
        "private_net": [
            {
                "network": 4711,
                "ip": "10.0.0.2",
                "alias_ips": ["10.0.0.3", "10.0.0.4"],
                "mac_address": "86:00:ff:2a:7d:e1",
            }
        ],
        "server_type": {
            "id": 1,
            "name": "cpx22",
            "description": "CPX22",
            "cores": 2,
            "memory": 4,
            "disk": 80,
            "deprecated": False,
            "prices": [
                {
                    "location": "fsn1",
                    "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                    "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                    "included_traffic": 654321,
                    "price_per_tb_traffic": {"net": "1.0000", "gross": "1.1900"},
                }
            ],
            "storage_type": "local",
            "cpu_type": "shared",
            "category": "Shared vCPU",
            "architecture": "x86",
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
            "locations": [
                {
                    "id": 42,
                    "name": "fsn1",
                    "deprecation": {
                        "unavailable_after": "2023-09-01T00:00:00Z",
                        "announced": "2023-06-01T00:00:00Z",
                    },
                    "recommended": False,
                    "available": True,
                }
            ],
        },
        "location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "image": {
            "id": 42,
            "type": "snapshot",
            "status": "available",
            "name": "ubuntu-24.04",
            "description": "Ubuntu 24.04 Standard 64 bit",
            "image_size": 2.3,
            "disk_size": 10,
            "created": "2016-01-30T23:55:00Z",
            "created_from": {"id": 1, "name": "Server"},
            "bound_to": 1,
            "os_flavor": "ubuntu",
            "os_version": "24.04",
            "rapid_deploy": False,
            "protection": {"delete": False},
            "deprecated": "2018-02-28T00:00:00Z",
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
            "deleted": "example",
            "labels": {"key": "example"},
            "architecture": "x86",
        },
        "iso": {
            "id": 42,
            "name": "FreeBSD-11.0-RELEASE-amd64-dvd1",
            "description": "FreeBSD 11.0 x64",
            "type": "public",
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
            "architecture": "x86",
        },
        "rescue_enabled": False,
        "locked": False,
        "backup_window": "22-02",
        "outgoing_traffic": 123456,
        "ingoing_traffic": 123456,
        "included_traffic": 654321,
        "protection": {"delete": False, "rebuild": False},
        "labels": {"key": "example"},
        "volumes": [1],
        "load_balancers": [1],
        "primary_disk_size": 50,
        "placement_group": {
            "id": 42,
            "name": "my-resource",
            "labels": {"key": "example"},
            "type": "spread",
            "created": "2016-01-30T23:55:00Z",
            "servers": [42],
        },
    },
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
    "next_actions": [
        {
            "id": 42,
            "command": "start_resource",
            "status": "running",
            "started": "2016-01-30T23:55:00Z",
            "finished": "2016-01-30T23:55:00Z",
            "progress": 100,
            "resources": [{"id": 42, "type": "server"}],
            "error": {"code": "action_failed", "message": "Action failed"},
        }
    ],
    "root_password": "YItygq1v3GYjjMomLaKc",
}


CREATE_STORAGE_BOX_RESPONSE: Final[JsonValue] = {
    "storage_box": {
        "id": 42,
        "name": "example",
        "storage_box_type": {
            "id": 42,
            "name": "bx11",
            "description": "BX11",
            "snapshot_limit": 10,
            "automatic_snapshot_limit": 10,
            "subaccounts_limit": 200,
            "size": 1073741824,
            "prices": [
                {
                    "location": "fsn1",
                    "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                    "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                    "setup_fee": {"net": "1.0000", "gross": "1.1900"},
                }
            ],
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
        },
        "location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "access_settings": {
            "reachable_externally": True,
            "samba_enabled": True,
            "ssh_enabled": True,
            "webdav_enabled": True,
            "zfs_enabled": True,
        },
        "snapshot_plan": {
            "max_snapshots": 10,
            "minute": 30,
            "hour": 3,
            "day_of_week": 7,
            "day_of_month": 1,
        },
        "protection": {"delete": False},
        "labels": {"key": "example"},
        "status": "active",
        "username": "u12345",
        "server": "u1337.your-storagebox.de",
        "system": "FSN1-BX355",
        "stats": {"size": 1, "size_data": 1, "size_snapshots": 1},
        "created": "2016-01-30T23:55:00Z",
    },
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


CREATE_STORAGE_BOX_SNAPSHOT_RESPONSE: Final[JsonValue] = {
    "snapshot": {"id": 42, "storage_box": 42},
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


CREATE_STORAGE_BOX_SUBACCOUNT_RESPONSE: Final[JsonValue] = {
    "subaccount": {"id": 42, "storage_box": 42},
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


CREATE_VOLUME_RESPONSE: Final[JsonValue] = {
    "volume": {
        "id": 42,
        "created": "2016-01-30T23:55:00Z",
        "name": "my-resource",
        "server": 12,
        "location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "size": 42,
        "linux_device": "/dev/disk/by-id/scsi-0HC_Volume_4711",
        "protection": {"delete": False},
        "labels": {"key": "example"},
        "status": "available",
        "format": "xfs",
    },
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
    "next_actions": [
        {
            "id": 42,
            "command": "start_resource",
            "status": "running",
            "started": "2016-01-30T23:55:00Z",
            "finished": "2016-01-30T23:55:00Z",
            "progress": 100,
            "resources": [{"id": 42, "type": "server"}],
            "error": {"code": "action_failed", "message": "Action failed"},
        }
    ],
}


CREATE_ZONE_RESPONSE: Final[JsonValue] = {
    "zone": {
        "id": 42,
        "name": "example.com",
        "created": "2016-01-30T23:55:00Z",
        "primary_nameservers": [
            {
                "address": "198.51.100.1",
                "port": 5353,
                "tsig_key": "example",
                "tsig_algorithm": "hmac-md5",
            }
        ],
        "labels": {"key": "example"},
        "protection": {"delete": False},
        "ttl": 10800,
        "status": "ok",
        "record_count": 1,
        "authoritative_nameservers": {
            "assigned": [
                "hydrogen.ns.hetzner.com.",
                "oxygen.ns.hetzner.com.",
                "helium.ns.hetzner.de.",
            ],
            "delegated": [
                "hydrogen.ns.hetzner.com.",
                "oxygen.ns.hetzner.com.",
                "helium.ns.hetzner.de.",
            ],
            "delegation_last_check": "2016-01-30T23:55:00Z",
            "delegation_status": "valid",
        },
        "registrar": "hetzner",
        "mode": "primary",
    },
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


CREATE_ZONE_RRSET_RESPONSE: Final[JsonValue] = {
    "rrset": {
        "id": "example",
        "name": "www",
        "type": "A",
        "ttl": 3600,
        "labels": {"key": "example"},
        "protection": {"change": False},
        "records": [{"value": "198.51.100.1", "comment": "My web server at Hetzner Cloud."}],
        "zone": 42,
    },
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


ERROR_RESPONSE: Final[JsonValue] = {
    "error": {"code": "example", "message": "example", "details": {"key": "value"}}
}


FIREWALLS_RESPONSE: Final[JsonValue] = {
    "firewalls": [
        {
            "id": 42,
            "name": "new-name",
            "labels": {"key": "example"},
            "created": "2016-01-30T23:55:00Z",
            "rules": [
                {
                    "description": "example",
                    "direction": "in",
                    "source_ips": [
                        "192.0.2.2/32",
                        "192.0.2.0/24",
                        "2001:0db8:9a3b:ee58:5ca:990c:8bc9:c03b/128",
                    ],
                    "destination_ips": ["example"],
                    "protocol": "tcp",
                    "port": "80",
                }
            ],
            "applied_to": [
                {
                    "type": "server",
                    "server": {"id": 42},
                    "label_selector": {"selector": "env=prod"},
                    "applied_to_resources": [{"type": "server", "server": {"id": 42}}],
                }
            ],
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


FIREWALL_RESPONSE: Final[JsonValue] = {
    "firewall": {
        "id": 42,
        "name": "new-name",
        "labels": {"key": "example"},
        "created": "2016-01-30T23:55:00Z",
        "rules": [
            {
                "description": "example",
                "direction": "in",
                "source_ips": [
                    "192.0.2.2/32",
                    "192.0.2.0/24",
                    "2001:0db8:9a3b:ee58:5ca:990c:8bc9:c03b/128",
                ],
                "destination_ips": ["example"],
                "protocol": "tcp",
                "port": "80",
            }
        ],
        "applied_to": [
            {
                "type": "server",
                "server": {"id": 42},
                "label_selector": {"selector": "env=prod"},
                "applied_to_resources": [{"type": "server", "server": {"id": 42}}],
            }
        ],
    }
}


FLOATING_IP_RESPONSE: Final[JsonValue] = {
    "floating_ip": {
        "id": 42,
        "name": "my-resource",
        "description": "This describes my resource",
        "ip": "2001:db8::/64",
        "type": "ipv6",
        "server": 42,
        "dns_ptr": [{"ip": "2001:db8::1", "dns_ptr": "server.example.com"}],
        "home_location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "blocked": False,
        "protection": {"delete": False},
        "labels": {"key": "example"},
        "created": "2016-01-30T23:55:00Z",
    }
}


GET_DATACENTER_RESPONSE: Final[JsonValue] = {
    "datacenter": {
        "id": 42,
        "name": "fsn1-dc8",
        "description": "Falkenstein DC Park 8",
        "location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "server_types": {
            "supported": [1, 2, 3],
            "available": [1, 2, 3],
            "available_for_migration": [1, 2, 3],
        },
    }
}


GET_ISO_RESPONSE: Final[JsonValue] = {
    "iso": {
        "id": 42,
        "name": "FreeBSD-11.0-RELEASE-amd64-dvd1",
        "description": "FreeBSD 11.0 x64",
        "type": "public",
        "deprecation": {
            "unavailable_after": "2023-09-01T00:00:00Z",
            "announced": "2023-06-01T00:00:00Z",
        },
        "architecture": "x86",
    }
}


GET_LOAD_BALANCER_TYPE_RESPONSE: Final[JsonValue] = {
    "load_balancer_type": {
        "id": 1,
        "name": "lb11",
        "description": "LB11",
        "max_connections": 20000,
        "max_services": 5,
        "max_targets": 25,
        "max_assigned_certificates": 10,
        "deprecated": "2016-01-30T23:50:00Z",
        "deprecation": {
            "unavailable_after": "2023-09-01T00:00:00Z",
            "announced": "2023-06-01T00:00:00Z",
        },
        "prices": [
            {
                "location": "fsn1",
                "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                "included_traffic": 654321,
                "price_per_tb_traffic": {"net": "1.0000", "gross": "1.1900"},
            }
        ],
    }
}


GET_LOCATION_RESPONSE: Final[JsonValue] = {
    "location": {
        "id": 42,
        "name": "fsn1",
        "description": "Falkenstein DC Park 1",
        "country": "DE",
        "city": "Falkenstein",
        "latitude": 50.47612,
        "longitude": 12.370071,
        "network_zone": "eu-central",
    }
}


GET_PRICING_RESPONSE: Final[JsonValue] = {
    "pricing": {
        "currency": "EUR",
        "vat_rate": "19.00",
        "primary_ips": [
            {
                "type": "ipv4",
                "prices": [
                    {
                        "location": "fsn1",
                        "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                        "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                    }
                ],
            }
        ],
        "floating_ips": [
            {
                "type": "ipv4",
                "prices": [
                    {"location": "fsn1", "price_monthly": {"net": "1.0000", "gross": "1.1900"}}
                ],
            }
        ],
        "image": {"price_per_gb_month": {"net": "1.0000", "gross": "1.1900"}},
        "volume": {"price_per_gb_month": {"net": "1.0000", "gross": "1.1900"}},
        "server_backup": {"percentage": "20.00"},
        "server_types": [
            {
                "id": 104,
                "name": "cpx22",
                "prices": [
                    {
                        "location": "fsn1",
                        "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                        "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                        "included_traffic": 654321,
                        "price_per_tb_traffic": {"net": "1.0000", "gross": "1.1900"},
                    }
                ],
            }
        ],
        "load_balancer_types": [
            {
                "id": 104,
                "name": "cpx22",
                "prices": [
                    {
                        "location": "fsn1",
                        "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                        "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                        "included_traffic": 654321,
                        "price_per_tb_traffic": {"net": "1.0000", "gross": "1.1900"},
                    }
                ],
            }
        ],
        "floating_ip": {"price_monthly": {"net": "1.0000", "gross": "1.1900"}},
    }
}


GET_SERVER_TYPE_RESPONSE: Final[JsonValue] = {
    "server_type": {
        "id": 1,
        "name": "cpx22",
        "description": "CPX22",
        "cores": 2,
        "memory": 4,
        "disk": 80,
        "deprecated": False,
        "prices": [
            {
                "location": "fsn1",
                "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                "included_traffic": 654321,
                "price_per_tb_traffic": {"net": "1.0000", "gross": "1.1900"},
            }
        ],
        "storage_type": "local",
        "cpu_type": "shared",
        "category": "Shared vCPU",
        "architecture": "x86",
        "deprecation": {
            "unavailable_after": "2023-09-01T00:00:00Z",
            "announced": "2023-06-01T00:00:00Z",
        },
        "locations": [
            {
                "id": 42,
                "name": "fsn1",
                "deprecation": {
                    "unavailable_after": "2023-09-01T00:00:00Z",
                    "announced": "2023-06-01T00:00:00Z",
                },
                "recommended": False,
                "available": True,
            }
        ],
    }
}


GET_STORAGE_BOX_TYPE_RESPONSE: Final[JsonValue] = {
    "storage_box_type": {
        "id": 42,
        "name": "bx11",
        "description": "BX11",
        "snapshot_limit": 10,
        "automatic_snapshot_limit": 10,
        "subaccounts_limit": 200,
        "size": 1073741824,
        "prices": [
            {
                "location": "fsn1",
                "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                "setup_fee": {"net": "1.0000", "gross": "1.1900"},
            }
        ],
        "deprecation": {
            "unavailable_after": "2023-09-01T00:00:00Z",
            "announced": "2023-06-01T00:00:00Z",
        },
    }
}


IMAGE_RESPONSE: Final[JsonValue] = {
    "image": {
        "id": 42,
        "type": "snapshot",
        "status": "available",
        "name": "ubuntu-24.04",
        "description": "Ubuntu 24.04 Standard 64 bit",
        "image_size": 2.3,
        "disk_size": 10,
        "created": "2016-01-30T23:55:00Z",
        "created_from": {"id": 1, "name": "Server"},
        "bound_to": 1,
        "os_flavor": "ubuntu",
        "os_version": "24.04",
        "rapid_deploy": False,
        "protection": {"delete": False},
        "deprecated": "2018-02-28T00:00:00Z",
        "deprecation": {
            "unavailable_after": "2023-09-01T00:00:00Z",
            "announced": "2023-06-01T00:00:00Z",
        },
        "deleted": "example",
        "labels": {"key": "example"},
        "architecture": "x86",
    }
}


LIST_DATACENTERS_RESPONSE: Final[JsonValue] = {
    "datacenters": [
        {
            "id": 42,
            "name": "fsn1-dc8",
            "description": "Falkenstein DC Park 8",
            "location": {
                "id": 42,
                "name": "fsn1",
                "description": "Falkenstein DC Park 1",
                "country": "DE",
                "city": "Falkenstein",
                "latitude": 50.47612,
                "longitude": 12.370071,
                "network_zone": "eu-central",
            },
            "server_types": {
                "supported": [1, 2, 3],
                "available": [1, 2, 3],
                "available_for_migration": [1, 2, 3],
            },
        }
    ],
    "recommendation": 1,
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_FLOATING_IPS_RESPONSE: Final[JsonValue] = {
    "floating_ips": [
        {
            "id": 42,
            "name": "my-resource",
            "description": "This describes my resource",
            "ip": "2001:db8::/64",
            "type": "ipv6",
            "server": 42,
            "dns_ptr": [{"ip": "2001:db8::1", "dns_ptr": "server.example.com"}],
            "home_location": {
                "id": 42,
                "name": "fsn1",
                "description": "Falkenstein DC Park 1",
                "country": "DE",
                "city": "Falkenstein",
                "latitude": 50.47612,
                "longitude": 12.370071,
                "network_zone": "eu-central",
            },
            "blocked": False,
            "protection": {"delete": False},
            "labels": {"key": "example"},
            "created": "2016-01-30T23:55:00Z",
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_IMAGES_RESPONSE: Final[JsonValue] = {
    "images": [
        {
            "id": 42,
            "type": "snapshot",
            "status": "available",
            "name": "ubuntu-24.04",
            "description": "Ubuntu 24.04 Standard 64 bit",
            "image_size": 2.3,
            "disk_size": 10,
            "created": "2016-01-30T23:55:00Z",
            "created_from": {"id": 1, "name": "Server"},
            "bound_to": 1,
            "os_flavor": "ubuntu",
            "os_version": "24.04",
            "rapid_deploy": False,
            "protection": {"delete": False},
            "deprecated": "2018-02-28T00:00:00Z",
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
            "deleted": "example",
            "labels": {"key": "example"},
            "architecture": "x86",
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_ISOS_RESPONSE: Final[JsonValue] = {
    "isos": [
        {
            "id": 42,
            "name": "FreeBSD-11.0-RELEASE-amd64-dvd1",
            "description": "FreeBSD 11.0 x64",
            "type": "public",
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
            "architecture": "x86",
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_LOAD_BALANCERS_RESPONSE: Final[JsonValue] = {
    "load_balancers": [
        {
            "id": 42,
            "name": "my-resource",
            "public_net": {
                "enabled": True,
                "ipv4": {"id": 42, "ip": "1.2.3.4", "blocked": False, "dns_ptr": "lb1.example.com"},
                "ipv6": {"id": 42, "ip": "1.2.3.4", "blocked": False, "dns_ptr": "lb1.example.com"},
            },
            "private_net": [{"network": 4711, "ip": "10.0.0.2"}],
            "location": {
                "id": 42,
                "name": "fsn1",
                "description": "Falkenstein DC Park 1",
                "country": "DE",
                "city": "Falkenstein",
                "latitude": 50.47612,
                "longitude": 12.370071,
                "network_zone": "eu-central",
            },
            "load_balancer_type": {
                "id": 1,
                "name": "lb11",
                "description": "LB11",
                "max_connections": 20000,
                "max_services": 5,
                "max_targets": 25,
                "max_assigned_certificates": 10,
                "deprecated": "2016-01-30T23:50:00Z",
                "deprecation": {
                    "unavailable_after": "2023-09-01T00:00:00Z",
                    "announced": "2023-06-01T00:00:00Z",
                },
                "prices": [
                    {
                        "location": "fsn1",
                        "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                        "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                        "included_traffic": 654321,
                        "price_per_tb_traffic": {"net": "1.0000", "gross": "1.1900"},
                    }
                ],
            },
            "protection": {"delete": False},
            "labels": {"key": "example"},
            "created": "2016-01-30T23:55:00Z",
            "services": [
                {
                    "protocol": "tcp",
                    "listen_port": 443,
                    "destination_port": 80,
                    "proxyprotocol": False,
                    "health_check": {
                        "protocol": "http",
                        "port": 4711,
                        "interval": 15,
                        "timeout": 10,
                        "retries": 3,
                        "http": {
                            "domain": "example.com",
                            "path": "/",
                            "response": '{"status": "ok"}',
                            "status_codes": ["2??", "3??"],
                            "tls": False,
                        },
                    },
                }
            ],
            "targets": [
                {
                    "type": "server",
                    "server": {"id": 80, "ip": "2001:db8::1"},
                    "health_status": [
                        {
                            "listen_port": 443,
                            "status": "healthy",
                            "detail": "unexpected_http_status",
                            "http_status_code": 503,
                        }
                    ],
                    "use_private_ip": True,
                }
            ],
            "algorithm": {"type": "round_robin"},
            "outgoing_traffic": 1,
            "ingoing_traffic": 1,
            "included_traffic": 10000,
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_LOAD_BALANCER_TYPES_RESPONSE: Final[JsonValue] = {
    "load_balancer_types": [
        {
            "id": 1,
            "name": "lb11",
            "description": "LB11",
            "max_connections": 20000,
            "max_services": 5,
            "max_targets": 25,
            "max_assigned_certificates": 10,
            "deprecated": "2016-01-30T23:50:00Z",
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
            "prices": [
                {
                    "location": "fsn1",
                    "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                    "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                    "included_traffic": 654321,
                    "price_per_tb_traffic": {"net": "1.0000", "gross": "1.1900"},
                }
            ],
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_LOCATIONS_RESPONSE: Final[JsonValue] = {
    "locations": [
        {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_NETWORKS_RESPONSE: Final[JsonValue] = {
    "networks": [
        {
            "id": 4711,
            "name": "mynet",
            "ip_range": "10.0.0.0/16",
            "subnets": [
                {
                    "type": "cloud",
                    "ip_range": "10.0.1.0/24",
                    "network_zone": "eu-central",
                    "gateway": "10.0.0.1",
                    "vswitch_id": 1000,
                }
            ],
            "routes": [{"destination": "10.100.1.0/24", "gateway": "10.0.1.1"}],
            "servers": [42],
            "load_balancers": [42],
            "protection": {"delete": False},
            "labels": {"key": "example"},
            "created": "2016-01-30T23:55:00Z",
            "expose_routes_to_vswitch": False,
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_NETWORK_MEMBERS_RESPONSE: Final[JsonValue] = {
    "members": [
        {
            "type": "server",
            "id": 42,
            "ip": "10.0.1.2",
            "status": "ok",
            "alias_ips": ["10.0.1.20"],
            "subnet": "10.0.1.0/24",
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_SERVERS_RESPONSE: Final[JsonValue] = {
    "servers": [
        {
            "id": 42,
            "name": "my-resource",
            "status": "running",
            "created": "2016-01-30T23:55:00Z",
            "public_net": {
                "ipv4": {
                    "id": 42,
                    "ip": "1.2.3.4",
                    "blocked": False,
                    "dns_ptr": "server01.example.com",
                },
                "ipv6": {
                    "id": 42,
                    "ip": "2001:db8::/64",
                    "blocked": False,
                    "dns_ptr": [{"ip": "2001:db8::1", "dns_ptr": "server.example.com"}],
                },
                "floating_ips": [478],
                "firewalls": [{"id": 42, "status": "applied"}],
            },
            "private_net": [
                {
                    "network": 4711,
                    "ip": "10.0.0.2",
                    "alias_ips": ["10.0.0.3", "10.0.0.4"],
                    "mac_address": "86:00:ff:2a:7d:e1",
                }
            ],
            "server_type": {
                "id": 1,
                "name": "cpx22",
                "description": "CPX22",
                "cores": 2,
                "memory": 4,
                "disk": 80,
                "deprecated": False,
                "prices": [
                    {
                        "location": "fsn1",
                        "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                        "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                        "included_traffic": 654321,
                        "price_per_tb_traffic": {"net": "1.0000", "gross": "1.1900"},
                    }
                ],
                "storage_type": "local",
                "cpu_type": "shared",
                "category": "Shared vCPU",
                "architecture": "x86",
                "deprecation": {
                    "unavailable_after": "2023-09-01T00:00:00Z",
                    "announced": "2023-06-01T00:00:00Z",
                },
                "locations": [
                    {
                        "id": 42,
                        "name": "fsn1",
                        "deprecation": {
                            "unavailable_after": "2023-09-01T00:00:00Z",
                            "announced": "2023-06-01T00:00:00Z",
                        },
                        "recommended": False,
                        "available": True,
                    }
                ],
            },
            "location": {
                "id": 42,
                "name": "fsn1",
                "description": "Falkenstein DC Park 1",
                "country": "DE",
                "city": "Falkenstein",
                "latitude": 50.47612,
                "longitude": 12.370071,
                "network_zone": "eu-central",
            },
            "image": {
                "id": 42,
                "type": "snapshot",
                "status": "available",
                "name": "ubuntu-24.04",
                "description": "Ubuntu 24.04 Standard 64 bit",
                "image_size": 2.3,
                "disk_size": 10,
                "created": "2016-01-30T23:55:00Z",
                "created_from": {"id": 1, "name": "Server"},
                "bound_to": 1,
                "os_flavor": "ubuntu",
                "os_version": "24.04",
                "rapid_deploy": False,
                "protection": {"delete": False},
                "deprecated": "2018-02-28T00:00:00Z",
                "deprecation": {
                    "unavailable_after": "2023-09-01T00:00:00Z",
                    "announced": "2023-06-01T00:00:00Z",
                },
                "deleted": "example",
                "labels": {"key": "example"},
                "architecture": "x86",
            },
            "iso": {
                "id": 42,
                "name": "FreeBSD-11.0-RELEASE-amd64-dvd1",
                "description": "FreeBSD 11.0 x64",
                "type": "public",
                "deprecation": {
                    "unavailable_after": "2023-09-01T00:00:00Z",
                    "announced": "2023-06-01T00:00:00Z",
                },
                "architecture": "x86",
            },
            "rescue_enabled": False,
            "locked": False,
            "backup_window": "22-02",
            "outgoing_traffic": 123456,
            "ingoing_traffic": 123456,
            "included_traffic": 654321,
            "protection": {"delete": False, "rebuild": False},
            "labels": {"key": "example"},
            "volumes": [1],
            "load_balancers": [1],
            "primary_disk_size": 50,
            "placement_group": {
                "id": 42,
                "name": "my-resource",
                "labels": {"key": "example"},
                "type": "spread",
                "created": "2016-01-30T23:55:00Z",
                "servers": [42],
            },
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_SERVER_TYPES_RESPONSE: Final[JsonValue] = {
    "server_types": [
        {
            "id": 1,
            "name": "cpx22",
            "description": "CPX22",
            "cores": 2,
            "memory": 4,
            "disk": 80,
            "deprecated": False,
            "prices": [
                {
                    "location": "fsn1",
                    "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                    "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                    "included_traffic": 654321,
                    "price_per_tb_traffic": {"net": "1.0000", "gross": "1.1900"},
                }
            ],
            "storage_type": "local",
            "cpu_type": "shared",
            "category": "Shared vCPU",
            "architecture": "x86",
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
            "locations": [
                {
                    "id": 42,
                    "name": "fsn1",
                    "deprecation": {
                        "unavailable_after": "2023-09-01T00:00:00Z",
                        "announced": "2023-06-01T00:00:00Z",
                    },
                    "recommended": False,
                    "available": True,
                }
            ],
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_SSH_KEYS_RESPONSE: Final[JsonValue] = {
    "ssh_keys": [
        {
            "id": 42,
            "name": "my-resource",
            "fingerprint": "b7:2f:30:a0:2f:6c:58:6c:21:04:58:61:ba:06:3b:2f",
            "public_key": "ssh-rsa AAAjjk76kgf...Xt",
            "labels": {"key": "example"},
            "created": "2016-01-30T23:55:00Z",
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_STORAGE_BOXES_RESPONSE: Final[JsonValue] = {
    "storage_boxes": [
        {
            "id": 42,
            "name": "example",
            "storage_box_type": {
                "id": 42,
                "name": "bx11",
                "description": "BX11",
                "snapshot_limit": 10,
                "automatic_snapshot_limit": 10,
                "subaccounts_limit": 200,
                "size": 1073741824,
                "prices": [
                    {
                        "location": "fsn1",
                        "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                        "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                        "setup_fee": {"net": "1.0000", "gross": "1.1900"},
                    }
                ],
                "deprecation": {
                    "unavailable_after": "2023-09-01T00:00:00Z",
                    "announced": "2023-06-01T00:00:00Z",
                },
            },
            "location": {
                "id": 42,
                "name": "fsn1",
                "description": "Falkenstein DC Park 1",
                "country": "DE",
                "city": "Falkenstein",
                "latitude": 50.47612,
                "longitude": 12.370071,
                "network_zone": "eu-central",
            },
            "access_settings": {
                "reachable_externally": True,
                "samba_enabled": True,
                "ssh_enabled": True,
                "webdav_enabled": True,
                "zfs_enabled": True,
            },
            "snapshot_plan": {
                "max_snapshots": 10,
                "minute": 30,
                "hour": 3,
                "day_of_week": 7,
                "day_of_month": 1,
            },
            "protection": {"delete": False},
            "labels": {"key": "example"},
            "status": "active",
            "username": "u12345",
            "server": "u1337.your-storagebox.de",
            "system": "FSN1-BX355",
            "stats": {"size": 1, "size_data": 1, "size_snapshots": 1},
            "created": "2016-01-30T23:55:00Z",
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_STORAGE_BOX_FOLDERS_RESPONSE: Final[JsonValue] = {"folders": ["example"]}


LIST_STORAGE_BOX_SNAPSHOTS_RESPONSE: Final[JsonValue] = {
    "snapshots": [
        {
            "storage_box": 42,
            "id": 42,
            "name": "my-snapshot",
            "description": "snapshot-0001",
            "labels": {"key": "example"},
            "stats": {"size": 1, "size_filesystem": 1},
            "is_automatic": True,
            "created": "2016-01-30T23:55:00Z",
        }
    ]
}


LIST_STORAGE_BOX_SUBACCOUNTS_RESPONSE: Final[JsonValue] = {
    "subaccounts": [
        {
            "storage_box": 42,
            "id": 42,
            "name": "my-name",
            "home_directory": "my-backup/server01",
            "access_settings": {
                "reachable_externally": True,
                "samba_enabled": True,
                "ssh_enabled": True,
                "webdav_enabled": True,
                "readonly": True,
            },
            "description": "my-backup-server01",
            "labels": {"key": "example"},
            "username": "u1337-sub1",
            "server": "u1337-sub1.your-storagebox.de",
            "created": "2016-01-30T23:55:00Z",
        }
    ]
}


LIST_STORAGE_BOX_TYPES_RESPONSE: Final[JsonValue] = {
    "storage_box_types": [
        {
            "id": 42,
            "name": "bx11",
            "description": "BX11",
            "snapshot_limit": 10,
            "automatic_snapshot_limit": 10,
            "subaccounts_limit": 200,
            "size": 1073741824,
            "prices": [
                {
                    "location": "fsn1",
                    "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                    "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                    "setup_fee": {"net": "1.0000", "gross": "1.1900"},
                }
            ],
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_VOLUMES_RESPONSE: Final[JsonValue] = {
    "volumes": [
        {
            "id": 42,
            "created": "2016-01-30T23:55:00Z",
            "name": "my-resource",
            "server": 12,
            "location": {
                "id": 42,
                "name": "fsn1",
                "description": "Falkenstein DC Park 1",
                "country": "DE",
                "city": "Falkenstein",
                "latitude": 50.47612,
                "longitude": 12.370071,
                "network_zone": "eu-central",
            },
            "size": 42,
            "linux_device": "/dev/disk/by-id/scsi-0HC_Volume_4711",
            "protection": {"delete": False},
            "labels": {"key": "example"},
            "status": "available",
            "format": "xfs",
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_ZONES_RESPONSE: Final[JsonValue] = {
    "zones": [
        {
            "id": 42,
            "name": "example.com",
            "created": "2016-01-30T23:55:00Z",
            "primary_nameservers": [
                {
                    "address": "198.51.100.1",
                    "port": 5353,
                    "tsig_key": "example",
                    "tsig_algorithm": "hmac-md5",
                }
            ],
            "labels": {"key": "example"},
            "protection": {"delete": False},
            "ttl": 10800,
            "status": "ok",
            "record_count": 1,
            "authoritative_nameservers": {
                "assigned": [
                    "hydrogen.ns.hetzner.com.",
                    "oxygen.ns.hetzner.com.",
                    "helium.ns.hetzner.de.",
                ],
                "delegated": [
                    "hydrogen.ns.hetzner.com.",
                    "oxygen.ns.hetzner.com.",
                    "helium.ns.hetzner.de.",
                ],
                "delegation_last_check": "2016-01-30T23:55:00Z",
                "delegation_status": "valid",
            },
            "registrar": "hetzner",
            "mode": "primary",
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LIST_ZONE_RRSETS_RESPONSE: Final[JsonValue] = {
    "rrsets": [
        {
            "id": "example",
            "name": "www",
            "type": "A",
            "ttl": 3600,
            "labels": {"key": "example"},
            "protection": {"change": False},
            "records": [{"value": "198.51.100.1", "comment": "My web server at Hetzner Cloud."}],
            "zone": 42,
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


LOAD_BALANCER_RESPONSE: Final[JsonValue] = {
    "load_balancer": {
        "id": 42,
        "name": "my-resource",
        "public_net": {
            "enabled": True,
            "ipv4": {"id": 42, "ip": "1.2.3.4", "blocked": False, "dns_ptr": "lb1.example.com"},
            "ipv6": {"id": 42, "ip": "1.2.3.4", "blocked": False, "dns_ptr": "lb1.example.com"},
        },
        "private_net": [{"network": 4711, "ip": "10.0.0.2"}],
        "location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "load_balancer_type": {
            "id": 1,
            "name": "lb11",
            "description": "LB11",
            "max_connections": 20000,
            "max_services": 5,
            "max_targets": 25,
            "max_assigned_certificates": 10,
            "deprecated": "2016-01-30T23:50:00Z",
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
            "prices": [
                {
                    "location": "fsn1",
                    "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                    "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                    "included_traffic": 654321,
                    "price_per_tb_traffic": {"net": "1.0000", "gross": "1.1900"},
                }
            ],
        },
        "protection": {"delete": False},
        "labels": {"key": "example"},
        "created": "2016-01-30T23:55:00Z",
        "services": [
            {
                "protocol": "tcp",
                "listen_port": 443,
                "destination_port": 80,
                "proxyprotocol": False,
                "health_check": {
                    "protocol": "http",
                    "port": 4711,
                    "interval": 15,
                    "timeout": 10,
                    "retries": 3,
                    "http": {
                        "domain": "example.com",
                        "path": "/",
                        "response": '{"status": "ok"}',
                        "status_codes": ["2??", "3??"],
                        "tls": False,
                    },
                },
            }
        ],
        "targets": [
            {
                "type": "server",
                "server": {"id": 80, "ip": "2001:db8::1"},
                "health_status": [
                    {
                        "listen_port": 443,
                        "status": "healthy",
                        "detail": "unexpected_http_status",
                        "http_status_code": 503,
                    }
                ],
                "use_private_ip": True,
            }
        ],
        "algorithm": {"type": "round_robin"},
        "outgoing_traffic": 1,
        "ingoing_traffic": 1,
        "included_traffic": 10000,
    }
}


METRICS_RESPONSE: Final[JsonValue] = {
    "metrics": {
        "start": "2017-01-01T00:00:00Z",
        "end": "2017-01-01T23:00:00Z",
        "step": 60,
        "time_series": {"key": {"values": [[1.5, "example"]]}},
    }
}


NETWORK_RESPONSE: Final[JsonValue] = {
    "network": {
        "id": 4711,
        "name": "mynet",
        "ip_range": "10.0.0.0/16",
        "subnets": [
            {
                "type": "cloud",
                "ip_range": "10.0.1.0/24",
                "network_zone": "eu-central",
                "gateway": "10.0.0.1",
                "vswitch_id": 1000,
            }
        ],
        "routes": [{"destination": "10.100.1.0/24", "gateway": "10.0.1.1"}],
        "servers": [42],
        "load_balancers": [42],
        "protection": {"delete": False},
        "labels": {"key": "example"},
        "created": "2016-01-30T23:55:00Z",
        "expose_routes_to_vswitch": False,
    }
}


PLACEMENT_GROUPS_RESPONSE: Final[JsonValue] = {
    "placement_groups": [
        {
            "id": 42,
            "name": "my-resource",
            "labels": {"key": "example"},
            "type": "spread",
            "created": "2016-01-30T23:55:00Z",
            "servers": [42],
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


PLACEMENT_GROUP_RESPONSE: Final[JsonValue] = {
    "placement_group": {
        "id": 42,
        "name": "my-resource",
        "labels": {"key": "example"},
        "type": "spread",
        "created": "2016-01-30T23:55:00Z",
        "servers": [42],
    }
}


PRIMARY_IP_RESPONSE: Final[JsonValue] = {
    "primary_ip": {
        "id": 42,
        "name": "my-resource",
        "labels": {"key": "example"},
        "created": "2016-01-30T23:55:00Z",
        "blocked": False,
        "location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "ip": "2001:db8::/64",
        "dns_ptr": [{"ip": "2001:db8::1", "dns_ptr": "server.example.com"}],
        "protection": {"delete": False},
        "type": "ipv6",
        "auto_delete": True,
        "assignee_type": "server",
        "assignee_id": 17,
    }
}


PRIMARY_I_PS_RESPONSE: Final[JsonValue] = {
    "primary_ips": [
        {
            "id": 42,
            "name": "my-resource",
            "labels": {"key": "example"},
            "created": "2016-01-30T23:55:00Z",
            "blocked": False,
            "location": {
                "id": 42,
                "name": "fsn1",
                "description": "Falkenstein DC Park 1",
                "country": "DE",
                "city": "Falkenstein",
                "latitude": 50.47612,
                "longitude": 12.370071,
                "network_zone": "eu-central",
            },
            "ip": "2001:db8::/64",
            "dns_ptr": [{"ip": "2001:db8::1", "dns_ptr": "server.example.com"}],
            "protection": {"delete": False},
            "type": "ipv6",
            "auto_delete": True,
            "assignee_type": "server",
            "assignee_id": 17,
        }
    ],
    "meta": {
        "pagination": {
            "page": 3,
            "per_page": 25,
            "previous_page": 2,
            "next_page": 4,
            "last_page": 4,
            "total_entries": 100,
        }
    },
}


REBUILD_SERVER_RESPONSE: Final[JsonValue] = {
    "root_password": "example",
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


REQUEST_SERVER_CONSOLE_RESPONSE: Final[JsonValue] = {
    "wss_url": "example",
    "password": "9MQaTg2VAGI0FIpc10k3UpRXcHj2wQ6x",
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


ROOT_PASSWORD_RESPONSE: Final[JsonValue] = {
    "root_password": "zCWbFhnu950dUTko5f40",
    "action": {
        "id": 42,
        "command": "start_resource",
        "status": "running",
        "started": "2016-01-30T23:55:00Z",
        "finished": "2016-01-30T23:55:00Z",
        "progress": 100,
        "resources": [{"id": 42, "type": "server"}],
        "error": {"code": "action_failed", "message": "Action failed"},
    },
}


RRSET_RESPONSE: Final[JsonValue] = {
    "rrset": {
        "id": "example",
        "name": "www",
        "type": "A",
        "ttl": 3600,
        "labels": {"key": "example"},
        "protection": {"change": False},
        "records": [{"value": "198.51.100.1", "comment": "My web server at Hetzner Cloud."}],
        "zone": 42,
    }
}


SERVER_RESPONSE: Final[JsonValue] = {
    "server": {
        "id": 42,
        "name": "my-resource",
        "status": "running",
        "created": "2016-01-30T23:55:00Z",
        "public_net": {
            "ipv4": {
                "id": 42,
                "ip": "1.2.3.4",
                "blocked": False,
                "dns_ptr": "server01.example.com",
            },
            "ipv6": {
                "id": 42,
                "ip": "2001:db8::/64",
                "blocked": False,
                "dns_ptr": [{"ip": "2001:db8::1", "dns_ptr": "server.example.com"}],
            },
            "floating_ips": [478],
            "firewalls": [{"id": 42, "status": "applied"}],
        },
        "private_net": [
            {
                "network": 4711,
                "ip": "10.0.0.2",
                "alias_ips": ["10.0.0.3", "10.0.0.4"],
                "mac_address": "86:00:ff:2a:7d:e1",
            }
        ],
        "server_type": {
            "id": 1,
            "name": "cpx22",
            "description": "CPX22",
            "cores": 2,
            "memory": 4,
            "disk": 80,
            "deprecated": False,
            "prices": [
                {
                    "location": "fsn1",
                    "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                    "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                    "included_traffic": 654321,
                    "price_per_tb_traffic": {"net": "1.0000", "gross": "1.1900"},
                }
            ],
            "storage_type": "local",
            "cpu_type": "shared",
            "category": "Shared vCPU",
            "architecture": "x86",
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
            "locations": [
                {
                    "id": 42,
                    "name": "fsn1",
                    "deprecation": {
                        "unavailable_after": "2023-09-01T00:00:00Z",
                        "announced": "2023-06-01T00:00:00Z",
                    },
                    "recommended": False,
                    "available": True,
                }
            ],
        },
        "location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "image": {
            "id": 42,
            "type": "snapshot",
            "status": "available",
            "name": "ubuntu-24.04",
            "description": "Ubuntu 24.04 Standard 64 bit",
            "image_size": 2.3,
            "disk_size": 10,
            "created": "2016-01-30T23:55:00Z",
            "created_from": {"id": 1, "name": "Server"},
            "bound_to": 1,
            "os_flavor": "ubuntu",
            "os_version": "24.04",
            "rapid_deploy": False,
            "protection": {"delete": False},
            "deprecated": "2018-02-28T00:00:00Z",
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
            "deleted": "example",
            "labels": {"key": "example"},
            "architecture": "x86",
        },
        "iso": {
            "id": 42,
            "name": "FreeBSD-11.0-RELEASE-amd64-dvd1",
            "description": "FreeBSD 11.0 x64",
            "type": "public",
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
            "architecture": "x86",
        },
        "rescue_enabled": False,
        "locked": False,
        "backup_window": "22-02",
        "outgoing_traffic": 123456,
        "ingoing_traffic": 123456,
        "included_traffic": 654321,
        "protection": {"delete": False, "rebuild": False},
        "labels": {"key": "example"},
        "volumes": [1],
        "load_balancers": [1],
        "primary_disk_size": 50,
        "placement_group": {
            "id": 42,
            "name": "my-resource",
            "labels": {"key": "example"},
            "type": "spread",
            "created": "2016-01-30T23:55:00Z",
            "servers": [42],
        },
    }
}


SNAPSHOT_RESPONSE: Final[JsonValue] = {
    "snapshot": {
        "storage_box": 42,
        "id": 42,
        "name": "my-snapshot",
        "description": "snapshot-0001",
        "labels": {"key": "example"},
        "stats": {"size": 1, "size_filesystem": 1},
        "is_automatic": True,
        "created": "2016-01-30T23:55:00Z",
    }
}


SSH_KEY_RESPONSE: Final[JsonValue] = {
    "ssh_key": {
        "id": 42,
        "name": "my-resource",
        "fingerprint": "b7:2f:30:a0:2f:6c:58:6c:21:04:58:61:ba:06:3b:2f",
        "public_key": "ssh-rsa AAAjjk76kgf...Xt",
        "labels": {"key": "example"},
        "created": "2016-01-30T23:55:00Z",
    }
}


STORAGE_BOX_RESPONSE: Final[JsonValue] = {
    "storage_box": {
        "id": 42,
        "name": "example",
        "storage_box_type": {
            "id": 42,
            "name": "bx11",
            "description": "BX11",
            "snapshot_limit": 10,
            "automatic_snapshot_limit": 10,
            "subaccounts_limit": 200,
            "size": 1073741824,
            "prices": [
                {
                    "location": "fsn1",
                    "price_hourly": {"net": "1.0000", "gross": "1.1900"},
                    "price_monthly": {"net": "1.0000", "gross": "1.1900"},
                    "setup_fee": {"net": "1.0000", "gross": "1.1900"},
                }
            ],
            "deprecation": {
                "unavailable_after": "2023-09-01T00:00:00Z",
                "announced": "2023-06-01T00:00:00Z",
            },
        },
        "location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "access_settings": {
            "reachable_externally": True,
            "samba_enabled": True,
            "ssh_enabled": True,
            "webdav_enabled": True,
            "zfs_enabled": True,
        },
        "snapshot_plan": {
            "max_snapshots": 10,
            "minute": 30,
            "hour": 3,
            "day_of_week": 7,
            "day_of_month": 1,
        },
        "protection": {"delete": False},
        "labels": {"key": "example"},
        "status": "active",
        "username": "u12345",
        "server": "u1337.your-storagebox.de",
        "system": "FSN1-BX355",
        "stats": {"size": 1, "size_data": 1, "size_snapshots": 1},
        "created": "2016-01-30T23:55:00Z",
    }
}


SUBACCOUNT_RESPONSE: Final[JsonValue] = {
    "subaccount": {
        "storage_box": 42,
        "id": 42,
        "name": "my-name",
        "home_directory": "my-backup/server01",
        "access_settings": {
            "reachable_externally": True,
            "samba_enabled": True,
            "ssh_enabled": True,
            "webdav_enabled": True,
            "readonly": True,
        },
        "description": "my-backup-server01",
        "labels": {"key": "example"},
        "username": "u1337-sub1",
        "server": "u1337-sub1.your-storagebox.de",
        "created": "2016-01-30T23:55:00Z",
    }
}


VOLUME_RESPONSE: Final[JsonValue] = {
    "volume": {
        "id": 42,
        "created": "2016-01-30T23:55:00Z",
        "name": "my-resource",
        "server": 12,
        "location": {
            "id": 42,
            "name": "fsn1",
            "description": "Falkenstein DC Park 1",
            "country": "DE",
            "city": "Falkenstein",
            "latitude": 50.47612,
            "longitude": 12.370071,
            "network_zone": "eu-central",
        },
        "size": 42,
        "linux_device": "/dev/disk/by-id/scsi-0HC_Volume_4711",
        "protection": {"delete": False},
        "labels": {"key": "example"},
        "status": "available",
        "format": "xfs",
    }
}


ZONEFILE: Final[JsonValue] = {"zonefile": "example"}


ZONE_RESPONSE: Final[JsonValue] = {
    "zone": {
        "id": 42,
        "name": "example.com",
        "created": "2016-01-30T23:55:00Z",
        "primary_nameservers": [
            {
                "address": "198.51.100.1",
                "port": 5353,
                "tsig_key": "example",
                "tsig_algorithm": "hmac-md5",
            }
        ],
        "labels": {"key": "example"},
        "protection": {"delete": False},
        "ttl": 10800,
        "status": "ok",
        "record_count": 1,
        "authoritative_nameservers": {
            "assigned": [
                "hydrogen.ns.hetzner.com.",
                "oxygen.ns.hetzner.com.",
                "helium.ns.hetzner.de.",
            ],
            "delegated": [
                "hydrogen.ns.hetzner.com.",
                "oxygen.ns.hetzner.com.",
                "helium.ns.hetzner.de.",
            ],
            "delegation_last_check": "2016-01-30T23:55:00Z",
            "delegation_status": "valid",
        },
        "registrar": "hetzner",
        "mode": "primary",
    }
}
