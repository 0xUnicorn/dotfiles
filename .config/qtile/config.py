import socket
import subprocess

from libqtile import hook

import configurations


# CONFIGURATION
def get_configuration(hostname: str):
    devices = {
        '0xUnicorn': configurations.WorkstationConfiguration,
        'Laptop': configurations.LaptopConfiguration,
    }
    try:
        return devices[hostname]
    except IndexError:
        return configurations.DefaultConfiguration

hostname = socket.gethostname()
conf = get_configuration(hostname)()

# HOOKS
@hook.subscribe.startup_once
def start_once():
    subprocess.call([conf.home + '/.config/qtile/autostart.sh'])

# KEYBINDINGS
keys = conf.keys()

# GROUPS
groups = conf.groups()
conf.add_groups_keybindings(keys)

# LAYOUTS
layouts = conf.layouts()
auto_fullscreen = conf.auto_fullscreen
focus_on_window_activation = conf.focus_on_window_activation
reconfigure_screens = conf.reconfigure_screens
auto_minimize = conf.auto_minimize

# FLOATING APPLICATIONS
floating_layout = conf.floating_layout()

# SCREENS (DEFAULT MONITOR: 1)
monitors = conf.get_monitors()
screens = conf.screens(monitors)

# MOUSE ACTIONS
dgroups_key_binder = conf.dgroups_key_binder
dgroups_app_rules = conf.dgroups_app_rules
follow_mouse_focus = conf.follow_mouse_focus
bring_front_click = conf.bring_front_click
cursor_warp = conf.cursor_warp
mouse = conf.mouse()

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
wmname = "LG3D"

