
from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod1"
TERMINAL = "alacritty"
MY_BROWSER = "brave-browser"

keys = [

    ### THE BASICS
    Key([mod], "Return",
        lazy.spawn(TERMINAL),
        desc="Launch terminal"
    ),

    Key([mod, "shift"], "Return",
        lazy.spawn("dmenu_run -p 'Run: '"),
        desc="Spawn a command using dmenu_run"
    ),

    Key([mod, "shift"], "s",
        lazy.spawn("gnome-screenshot -i"),
        desc="Screenshot of an area to clipboard"
    ),

    Key([mod], "b",
        lazy.spawn(MY_BROWSER),
        desc="Spawn a command using dmenu_run"
    ),

    Key([mod], "Tab",
        lazy.next_layout(),
        desc="Toggle between layouts"
    ),

    Key([mod, "shift"], "Tab",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"
    ),

    Key([mod, "shift"], "c",
        lazy.window.kill(),
        desc="Kill focused window"
    ),

    Key([mod, "control"], "r",
        lazy.restart(),
        desc="Restart Qtile"
    ),
    Key([mod, "control"], "q",
        lazy.shutdown(),
        desc="Shutdown Qtile"
    ),

    ### Switch focus to specific monitor (out of three)
    Key([mod], "w",
        lazy.to_screen(2),
        desc='Keyboard focus to monitor 1'
    ),

    Key([mod], "e",
        lazy.to_screen(0),
        desc='Keyboard focus to monitor 2'
    ),

    Key([mod], "r",
        lazy.to_screen(1),
        desc='Keyboard focus to monitor 3'
    ),

    ### Switch focus of monitors
    Key([mod], "period",
        lazy.next_screen(),
        desc='Move focus to next monitor'
    ),

    Key([mod], "comma",
        lazy.prev_screen(),
        desc='Move focus to prev monitor'
    ),

    Key([mod], "h",
        lazy.layout.left(),
        desc="Move focus to left"
    ),
    Key([mod], "l",
        lazy.layout.right(),
        desc="Move focus to right"
    ),
    Key([mod], "j",
        lazy.layout.down(),
        desc="Move focus down"
    ),
    Key([mod], "k",
        lazy.layout.up(),
        desc="Move focus up"
    ),
    Key([mod], "space",
        lazy.layout.next(),
        desc="Move window focus to other window"
    ),

    ### Window Controls
    Key([mod, "shift"], "h",
        lazy.layout.shuffle_left(),
        desc="Move window to the left"
    ),
    Key([mod, "shift"], "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right"
    ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        desc="Move window down"
    ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        desc="Move window up"
    ),

    Key([mod], "f",
        lazy.window.toggle_floating(),
        desc='Toggle floating'
    ),

    ### VOLUME CONTROL
    Key([], "XF86AudioLowerVolume",
        lazy.spawn("amixer -D pulse set Master 5%- unmute"),
        desc="Turn master volume up 5%"
    ),
    Key([], "XF86AudioRaiseVolume",
        lazy.spawn("amixer -D pulse set Master 5%+ unmute"),
        desc="Turn master volume down 5%"
    ),

    ### LOCK SCREEN
    Key(["mod4"], "l",
        lazy.spawn("dm-tool lock"),
        desc="Lock screen"
    ),
]

# GROUPS / WORKSPACES

group_names = [("WWW", {'layout': 'monadtall'}),
               ("DEV", {'layout': 'monadtall'}),
               ("SYS", {'layout': 'monadtall'}),
               ("DOC", {'layout': 'monadtall'}),
               ("CHAT", {'layout': 'monadtall'}),
               ("VIRT", {'layout': 'monadtall'}),
               ("SSH", {'layout': 'monadtall'}),
               ("WWW2", {'layout': 'monadtall'}),
               ("GFX", {'layout': 'floating'})]

groups = [
    Group(name=name, layout=layout) for
    name, layout in group_names
]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(
        Key(
            [mod],
            str(i),
            lazy.group[name].toscreen()
        )
    ) # Switch to another group
    keys.append(
        Key(
            [mod, "shift"],
            str(i),
            lazy.window.togroup(name)
        )
    ) # Send current window to another group

# LAYOUTS

layout_theme = {
    "border_width": 2,
    "margin": 10,
    "border_focus": "e1acff",
    "border_normal": "1D2330"
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.Floating(**layout_theme)
]

# WIDGETS

colors = [
    ["#092441", "#092441"], # panel background
    ["#F77FF7", "#F77FF7"], # background for current screen tab
    ["#ffffff", "#ffffff"], # font color for group names
    ["#00bc20", "#00bc20"], # border line color for current tab
    ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
    ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
    ["#e1acff", "#e1acff"], # window name
    ["#ecbbfb", "#ecbbfb"]  # backbround for inactive screens
]

widget_defaults = dict(
    font='Ubuntu Mono',
    fontsize=12,
    padding=2,
    background=colors[0]
)

extension_defaults = widget_defaults.copy()

def widgets_list():
    return [
        widget.Sep(
            linewidth = 0,
            padding = 8
        ),
        widget.CurrentLayout(),
        widget.Sep(
            linewidth = 1,
            padding = 15,
            foreground = colors[5]
        ),
        widget.GroupBox(
            font = "Ubuntu Bold",
            fontsize = 9,
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 3,
            borderwidth = 3,
            active = colors[1],
            # inactive = colors[7]
            # rounded
            # highlight_color
            # highlight_method
            this_current_screen_border = colors[3],
            this_screen_border = colors[4]
            # other_current_screen_border
            # other_screen_border
            # foreground
            # background
        ),
        widget.Sep(
            linewidth = 1,
            padding = 15,
            foreground = colors[5]
        ),
        widget.Prompt(
        ),
        widget.Spacer(
            length=bar.STRETCH
        ),
        widget.Chord(
            chords_colors={
                'launch': ("#ff0000", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        widget.Systray(
            padding = 5
        ),
        widget.Sep(
            linewidth = 1,
            padding = 15,
            foreground = colors[5]
        ),
        widget.Volume(
            channel = "Master",
            device = "pulse",
            emoji = True,
            foreground = colors[2],
            background = colors[0],
            padding = 5
        ),
        widget.Volume(
            channel = "Master",
            device = "pulse",
            emoji = False,
            foreground = colors[2],
            background = colors[0],
            padding = 5
        ),
        widget.Sep(
            linewidth = 1,
            padding = 15,
            foreground = colors[5]
        ),
        widget.Net(
            interface = "enp6s0",
            format = '{down}↓↑{up}',
            foreground = colors[2],
            background = colors[0],
            padding = 5
        ),
        widget.Sep(
            linewidth = 1,
            padding = 15,
            foreground = colors[5]
        ),
        widget.Clock(
            format='%a %d-%m-%y %H:%M:%S'
        ),
        widget.Sep(
            linewidth = 0,
            padding = 8,
        )
    ]


def init_widgets_screen1():
    """Left of primary"""
    return widgets_list()


def init_widgets_screen2():
    """Primary"""
    return widgets_list()


def init_widgets_screen3():
    """Right of primary"""
    return widgets_list()

def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=25)),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=25)),
        Screen(top=bar.Bar(widgets=init_widgets_screen3(), opacity=1.0, size=25))
    ]

# Start screens
screens = init_screens()

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
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
