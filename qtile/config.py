
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

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group

# LAYOUTS

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": "e1acff",
    "border_normal": "1D2330"
}

layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.Stack(num_stacks=2),
    layout.RatioTile(**layout_theme),
]

# WIDGETS

widget_defaults = dict(
    font='sans',
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        bottom=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        'launch': ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),
                widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
                widget.QuickExit(),
            ],
            24,
        ),
    ),
]

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
