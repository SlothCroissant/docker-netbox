# Add your plugins and plugin settings here.
# Of course uncomment this file out.

from os import environ

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

PLUGINS = [
    'netbox_prometheus_sd',
    'netbox_bgp',
    "netbox_diode_plugin",
]

PLUGINS_CONFIG = {
    "netbox_diode_plugin": {
        # Diode gRPC target for communication with Diode server
        "diode_target_override": "grpc://localhost:8080/diode",
        # NetBox username associated with changes applied via plugin
        "diode_username": "diode-ingest",
        # netbox-to-diode client secret from environment variable
        "netbox_to_diode_client_secret": environ.get("DIODE_CLIENT_SECRET", ""),
    },
}