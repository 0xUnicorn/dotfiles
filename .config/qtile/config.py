import os
import subprocess

from typing import List  # noqa: F401

from libqtile import qtile
from libqtile import hook
from libqtile import bar, layout, widget, extension
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

import colors


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])


MOD = "mod1"
TERMINAL = "alacritty"
MY_BROWSER = "brave"

keys = [

    # QTILE COMMANDS

    Key([MOD, "control"], "r",
        lazy.restart(),
        desc="Restart Qtile"),

    Key([MOD, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"),

    # POWER COMMANDS

    Key([MOD, "control", "shift"], "s",
        lazy.spawn('systemctl hibernate'),
        desc='Hibernate System'),

    Key([MOD, "control", "shift"], "q",
        lazy.spawn('systemctl poweroff'),
        desc='Poweroff System'),

    Key([MOD, "control", "shift"], "r",
        lazy.spawn('systemctl reboot'),
        desc='Reboot System'),

    # LAUNCH DMENU SCRIPTS

#    Key([MOD, "shift"], "0",
#        lazy.run_extension(extension.Dmenu(
#            command='ls -l'
#        ))),

    Key([MOD, "control"], "0",
        lazy.spawn('dmenu_ssh.sh'),
        desc="Launch SSH server list"),

    # LAUNCH APPLICATIONS

    Key([MOD], "Return",
        lazy.spawn(TERMINAL),
        desc="Launch terminal"),

    Key([MOD], "BackSpace",
        lazy.spawn('pcmanfm'),
        desc="Launch filemanager"),

    Key([MOD], "m",
        lazy.spawn('tidal-hifi'),
        desc="Launch Tidal"),

    Key([MOD], "a",
        lazy.spawn('authy'),
        desc="Launch Authy"),

    Key([MOD, 'shift'], 'm',
        lazy.spawn('thunderbird'),
        desc='Launch Thunderbird'),

    Key([MOD, "shift"], "s",
        lazy.spawn("gnome-screenshot -i"),
        desc="Screenshot of an area to clipboard"),

    Key([MOD], "d",
        lazy.spawn('discord'),
        desc="Launch Discord"),

    Key([MOD], "b",
        lazy.spawn(MY_BROWSER),
        desc="Spawn a command using dmenu_run"),

    Key([MOD, 'shift'], 'Return',
        lazy.run_extension(extension.DmenuRun(
            dmenu_prompt="\uF120",
            dmenu_font="Ubuntu Mono",
            background=colors.Normal.background,
            foreground=colors.Dim.white,
            selected_background=colors.Dim.magenta,
            selected_foreground=colors.Normal.background)),
        desc="Launch Dmenu"),

    # VOLUME CONTROL

    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -D pulse set Master 5%- unmute"),
        desc="Turn master volume up 5%"),

    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -D pulse set Master 5%+ unmute"),
        desc="Turn master volume down 5%"),

    # LOCK SCREEN

    Key(["mod4"], "l",
        lazy.spawn("dm-tool lock"),
        desc="Lock screen"),

    # SCREEN FOCUS

    Key([MOD], "q",
        lazy.to_screen(2),
        desc='Keyboard focus to monitor 1'),

    Key([MOD], "w",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 2'),

    Key([MOD], "e",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 3'),

    # SWITCH BETWEEN LAYOUTS

    Key([MOD], "Tab",
        lazy.next_layout(),
        desc="Toggle next layout"),

    Key([MOD, "shift"], "Tab",
        lazy.prev_layout(),
        desc="Toggle previous layout"),

    # MOVE LAYOUT FOCUS

    Key([MOD], "j",
        lazy.layout.down(),
        desc="Move layout focus down"),

    Key([MOD], "k",
        lazy.layout.up(),
        desc="Move layout focus up"),

    Key([MOD], "h",
        lazy.layout.left(),
        desc="Move layout focus left"),

    Key([MOD], "l",
        lazy.layout.up(),
        desc="Move layout focus right"),

    # SHUFFLE LAYOUT

    Key([MOD, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Shuffle layout to the left"),

    Key([MOD, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Shuffle layout to the right"),

    Key([MOD, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Shuffle layout down"),

    Key([MOD, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Shuffle layout up"),

    # CHANGE LAYOUT SIZES

    Key([MOD, "control"], "j",
        lazy.layout.shrink(),
        desc="Shrink the focused layout"),

    Key([MOD, "control"], "k",
        lazy.layout.grow(),
        desc="Grow the focused layout"),

    Key([MOD, "control"], "l",
        lazy.layout.normalize(),
        desc="Normalize the layout to default"),

    Key([MOD, "control"], "h",
        lazy.layout.maximize(),
        desc="Maximize the focused layout"),

    # CONTROL WINDOW

    Key([MOD], "f",
        lazy.window.toggle_floating(),
        desc='Toggle floating'),

    Key([MOD, "shift"], "c",
        lazy.window.kill(),
        desc="Kill focused window"),


]

# GROUPS

group_names = [
    ("WWW", 'monadtall'),
    ("DEV", 'monadtall'),
    ("SYS", 'monadtall'),
    ("DOC", 'monadtall'),
    ("COMMS", 'monadtall'),
    ("VIRT", 'monadtall'),
    ("SSH", 'monadtall'),
    ("WWW2", 'monadtall'),
    ("MEDIA", 'monadtall')
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


def _baseline_widgets():
    return [
        widget.GroupBox(
            font='Ubuntu Bold',
            fontsize=9,
            margin_x=0,
            padding_x=9,
            padding_y=5,
            borderwidth=0,
            use_mouse_wheel=False,
            highlight_method='block',
            background=colors.Normal.inactive,
            active=colors.Bright.green,
            inactive=colors.Normal.white,
            this_current_screen_border=colors.Dim.magenta,
            this_screen_border=colors.Normal.blue,
            other_current_screen_border=colors.Bright.magenta,
            other_screen_border=colors.Normal.white),
        widget.TextBox(
            text='\uE0B0',
            font='Symbols Nerd Font',
            background=colors.Dim.blue,
            foreground=colors.Normal.inactive,
            fontsize=31,
            padding=0),
        widget.CurrentLayoutIcon(
            scale=0.8,
            padding=6,
            background=colors.Dim.blue),
        widget.TextBox(
            text='\uE0B0',
            font='Symbols Nerd Font',
            #background=colors.Dim.blue,
            foreground=colors.Dim.blue,
            fontsize=31,
            padding=0)
    ]


left_clock_spacer = widget.Spacer(length=bar.STRETCH)

clock = widget.Clock(
    format='%a %d-%m-%y %H:%M:%S',
    font='Ubuntu Bold')

right_clock_spacer = widget.Spacer(length=bar.STRETCH)

arrow_bluetooth = widget.TextBox(
    text='\uE0B2',
    font='Symbols Nerd Font',
    background=colors.Normal.background,
    foreground=colors.Normal.white,
    fontsize=31,
    padding=0)

bluetooth = widget.Bluetooth(
    fmt='\uF294 {}',
    hci='/dev_04_52_C7_07_FC_60',
    background=colors.Normal.white,
    foreground=colors.Dim.blue)

arrow_check_updates = widget.TextBox(
    text='\uE0B2',
    font='Symbols Nerd Font',
    background=colors.Normal.white,
    foreground=colors.Normal.green,
    fontsize=31,
    padding=0)

check_updates_pacman = widget.CheckUpdates(
    display_format='\uF1B2 {updates}',
    distro='Arch_checkupdates',
    update_interval=900,
    no_update_string='\uF1B3 0',
    background=colors.Normal.green,
    colour_have_updates=colors.Dim.blue,
    execute=f'{TERMINAL} -e sudo pacman -Syu')

wing_check_updates = widget.TextBox(
    text='\uE0B3',
    font='Symbols Nerd Font',
    background=colors.Normal.green,
    foreground=colors.Normal.background,
    fontsize=31,
    padding=0)

check_updates_yay = widget.CheckUpdates(
    display_format='\uF1B3 {updates}',
    custom_command='yay -Qu --aur',
    update_interval=900,
    no_update_string='\uF1B3 0',
    background=colors.Normal.green,
    colour_have_updates=colors.Dim.blue,
    execute=f'{TERMINAL} -e yay -Syu --aur')

arrow_volume = widget.TextBox(
    text='\uE0B2',
    font='Symbols Nerd Font',
    background=colors.Bright.green,
    foreground=colors.Bright.yellow,
    fontsize=31,
    padding=0)

volume = widget.Volume(
    fmt='\uF028 {}',
    background=colors.Bright.yellow,
    foreground=colors.Dim.blue)

arrow_storage = widget.TextBox(
    text='\uE0B2',
    font='Symbols Nerd Font',
    background=colors.Bright.yellow,
    foreground=colors.Bright.cyan,
    fontsize=31,
    padding=0)

storage_root = widget.DF(
    format='\uF748 {r:.0f}%',
    visible_on_warn=False,
    background=colors.Bright.cyan,
    foreground=colors.Dim.blue,
    mouse_callbacks = {
        'Button1': lambda: qtile.cmd_spawn(
            TERMINAL + ' --hold -e dust -d 1 -x /')
    })

wing_storage = widget.TextBox(
    text='\uE0B3',
    font='Symbols Nerd Font',
    background=colors.Bright.cyan,
    foreground=colors.Normal.background,
    fontsize=31,
    padding=0)

storage_vault = widget.DF(
    format='\uF023 {r:.0f}%',
    partition='/home/unicorn/Documents/vault',
    visible_on_warn=False,
    background=colors.Bright.cyan,
    foreground=colors.Dim.blue,
    mouse_callbacks = {
        'Button1': lambda: qtile.cmd_spawn(
            TERMINAL + ' --hold -e dust -d 1 -x /home/unicorn/Documents/vault')
    })

arrow_memory = widget.TextBox(
    text='\uE0B2',
    font='Symbols Nerd Font',
    background=colors.Bright.cyan,
    foreground=colors.Bright.red,
    fontsize=31,
    padding=0)

memory = widget.Memory(
    format='\uF85A {MemUsed:.2f}{mm}',
    measure_mem='G',
    background=colors.Bright.red,
    foreground=colors.Dim.blue,
    mouse_callbacks = {
        'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' --hold -e free -h')
    })

arrow_cpu = widget.TextBox(
    text='\uE0B2',
    font='Symbols Nerd Font',
    background=colors.Bright.red,
    foreground=colors.Bright.magenta,
    fontsize=31,
    padding=0)

cpu = widget.CPU(
    format='\uE266 {freq_current}GHz\uE216{load_percent}% ',
    background=colors.Bright.magenta,
    foreground=colors.Dim.blue,
    mouse_callbacks = {
        'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' -e htop')
    })

arrow_net = widget.TextBox(
    text='\uE0B2',
    font='Symbols Nerd Font',
    background=colors.Bright.magenta,
    foreground=colors.Bright.blue,
    fontsize=31,
    padding=0)

net = widget.Net(
    fmt='\uF6FF {}',
    prefix='M',
    interface='enp6s0',
    format='{down}↓↑{up}',
    background=colors.Bright.blue,
    foreground=colors.Dim.blue,
    padding=5,
    mouse_callbacks = {
        'Button1': lambda: qtile.cmd_spawn(TERMINAL + ' -e ping 8.8.8.8')
    })

arrow_power = widget.TextBox(
    text='\uE0B2',
    font='Symbols Nerd Font',
    background=colors.Bright.blue,
    foreground=colors.Bright.black,
    fontsize=31,
    padding=0)

power = widget.TextBox(
    text='\uF011',
    font='Symbols Nerd Font',
    background=colors.Bright.black,
    foreground=colors.Bright.white,
    fontsize=15,
    padding=5,
    mouse_callbacks = {
        'Button1': lambda: qtile.cmd_spawn('systemctl poweroff'),
        'Button2': lambda: qtile.cmd_spawn('systemctl reboot'),
        'Button3': lambda: qtile.cmd_spawn('systemctl hibernate')
    })


def default_widgets():
    widgets = [
        left_clock_spacer,
        clock,
        right_clock_spacer,
        arrow_bluetooth,
        bluetooth,
        arrow_check_updates,
        check_updates_pacman,
        wing_check_updates,
        check_updates_yay,
        arrow_volume,
        volume,
        arrow_storage,
        storage_root,
        wing_storage,
        storage_vault,
        arrow_memory,
        memory,
        arrow_cpu,
        cpu,
        arrow_net,
        net,
        arrow_power,
        power
    ]
    all_widgets = _baseline_widgets() + widgets
    return all_widgets


def systray_widgets():
    widgets = default_widgets()
    status_notifier = widget.StatusNotifier()
    widgets.insert(6, status_notifier)
    return widgets


def init_screens():
    return [
#        Screen(top=bar.Bar(widgets=default_widgets(), size=20)),
#        Screen(top=bar.Bar(widgets=default_widgets(), size=20)),
        Screen(top=bar.Bar(widgets=systray_widgets(), size=20))
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
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
