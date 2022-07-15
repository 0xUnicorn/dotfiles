import os
import socket
import subprocess

from typing import List  # noqa: F401

from libqtile import hook
from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

import colors
import keybindings
import widgets


# APPLICATIONS
browser = 'brave'
file_manager = 'pcmanfm'
terminal = 'alacritty'

# SYSTEM
home = os.path.expanduser('~')
hostname = socket.gethostname()

# KEYBINDINGS
MOD = 'mod1' # DEPRECATED
keybind_keys = keybindings.Keys()
keys = keybindings.WorkstationKeybindings(
    keybind_keys, terminal, browser, file_manager).get_keybindings()


@hook.subscribe.startup_once
def start_once():
    subprocess.call([home + '/.config/qtile/autostart.sh'])


# GROUPS

group_names = [
    ('WWW', 'monadtall'),
    ('DEV', 'monadtall'),
    ('SYS', 'monadtall'),
    ('DOC', 'monadtall'),
    ('COMMS', 'monadtall'),
    ('VIRT', 'monadtall'),
    ('SSH', 'monadtall'),
    ('WWW2', 'monadtall'),
    ('MEDIA', 'monadtall')
]

groups = [
    Group(name=name, layout=layout) for
    name, layout in group_names
]

for i, (name, kwargs) in enumerate(group_names, 1):
# Switch to another group
    keys.append(Key([MOD], str(i), lazy.group[name].toscreen()))
# Send current window to another group
    keys.append(Key([MOD, "shift"], str(i), lazy.window.togroup(name)))

# LAYOUTS
layout_theme = {
    'margin': 10,
    'border_width': 1,
    'border_focus': colors.Dim.magenta,
    'border_normal': colors.Normal.inactive
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.MonadThreeCol(**layout_theme)
]

# WIDGETS
widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=12,
    padding=2,
    background=colors.Normal.background,
    foreground=colors.Normal.white)

fonts = widgets.Fonts(symbols='Symbols Nerd Font')
symbols = widgets.Symbols(fonts)
all_widgets = widgets.WorkstationWidgets(terminal, fonts, symbols).get_widgets()


def init_screens():
    return [
        Screen(top=bar.Bar(widgets=all_widgets.copy(), size=20)),
        Screen(top=bar.Bar(widgets=all_widgets.copy(), size=20)),
        Screen(top=bar.Bar(widgets=all_widgets.copy(), size=20))
    ]

# Start screens
screens = init_screens()

# Drag floating layouts.
mouse = [
    Drag([MOD], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([MOD], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([MOD], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

# FLOATING APPLICATIONS
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
    Match(title='authy'), # Authy
], **layout_theme)

auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
wmname = "LG3D"
