# Add your plugins and plugin settings here.
# Of course uncomment this file out.

from os import environ

# To learn how to build images with your required plugins
# See https://github.com/netbox-community/netbox-docker/wiki/Using-Netbox-Plugins

PLUGINS = [
    'netbox_prometheus_sd',
    'netbox_bgp',
]

PLUGINS_CONFIG = {}
