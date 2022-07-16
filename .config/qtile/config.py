import socket
import subprocess

from libqtile import hook

import configurations


# CONFIGURATIONS
configurations = {
    '0xUnicorn': configurations.WorkstationConfiguration,
    'Laptop': configurations.LaptopConfiguration
}

hostname = socket.gethostname()

conf = configurations[hostname]()
#try:
#    conf = configurations[hostname]()
#except IndexError:
#    pass
#    conf = configurations['Default']()

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

# FLOATING APPLICATIONS
floating_layout = conf.floating_layout()

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = conf.auto_minimize

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
wmname = "LG3D"

