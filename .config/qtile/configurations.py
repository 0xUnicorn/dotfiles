import os
import dataclasses
import subprocess

from typing import Any, Dict, List  # noqa: F401

from libqtile import bar
from libqtile import layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

import colors
import keybindings
import widgets


@dataclasses.dataclass
class _Configuration:

    # APPLICATIONS
    browser: str = 'brave'
    file_manager: str = 'pcmanfm'
    terminal: str = 'alacritty'

    # SYSTEM
    home: str = os.path.expanduser('~')

    # KEYBINDINGS
    keybind_keys: keybindings.Keys = dataclasses.field(
        default_factory=keybindings.Keys)

    #@abc.abstractmethod - mypy issue: github.com/python/mypy/issues/5374
    def keys(self) -> List:
        return NotImplemented

    # GROUPS
    group_names: list = dataclasses.field(default_factory=lambda: [
        ('WWW', 'monadtall'),
        ('DEV', 'monadtall'),
        ('SYS', 'monadtall'),
        ('DOC', 'monadtall'),
        ('COMMS', 'monadtall'),
        ('VIRT', 'monadtall'),
        ('SSH', 'monadtall'),
        ('WWW2', 'monadtall'),
        ('MEDIA', 'monadtall')
    ])

    def add_groups_keybindings(self, keys: List) -> None:
        _mod = [self.keybind_keys.alt]
        for i, (name, kwargs) in enumerate(self.group_names, 1):
            # Switch to another group
            keys.append(Key(_mod, str(i),
                            lazy.group[name].toscreen()))
            # Send current window to another group
            keys.append(Key(_mod + [self.keybind_keys.shift], str(i),
                            lazy.window.togroup(name)))

    def groups(self) -> List:
        return [Group(name=name, layout=layout) for
                name, layout in self.group_names]

    # LAYOUTS
    auto_fullscreen: bool = True
    focus_on_window_activation: str = 'smart'
    reconfigure_screens: bool = True
    # If things like steam games want to auto-minimize themselves when losing
    # focus, should we respect this or not?
    auto_minimize: bool = True

    layout_theme: Dict = dataclasses.field(default_factory=lambda: {
        'margin': 8,
        'border_width': 1,
        'border_focus': colors.Dim.magenta,
        'border_normal': colors.Normal.inactive
    })

    def layouts(self) -> List:
        return [layout.MonadTall(**self.layout_theme),
                layout.Max(**self.layout_theme),
                layout.MonadThreeCol(**self.layout_theme)]

    # FLOATING APPLICATIONS
    def floating_layout(self):
        return layout.Floating(float_rules=[
            # Run the utility of `xprop` to see the wm class and name of an X client.
            *layout.Floating.default_float_rules,
            Match(wm_class='confirmreset'),  # gitk
            Match(wm_class='makebranch'),  # gitk
            Match(wm_class='maketag'),  # gitk
            Match(wm_class='ssh-askpass'),  # ssh-askpass
            Match(title='branchdialog'),  # gitk
            Match(title='pinentry'),  # GPG key password entry
            Match(title='authy'), # Authy
        ], **self.layout_theme)

    # WIDGETS
    fonts: widgets.Fonts = dataclasses.field(default_factory=widgets.Fonts)

    @property
    def widget_defults(self) -> widgets.WidgetDefaults:
        return widgets.WidgetDefaults()

    @property
    def symbols(self) -> widgets.Symbols:
        return widgets.Symbols(self.fonts)

    #@abc.abstractmethod - mypy issue: github.com/python/mypy/issues/5374
    def get_widgets(self) -> Any:
        return NotImplemented

    # SCREENS
    def get_monitors(self) -> int:
        xrandr = subprocess.run(args='xrandr --listmonitors | wc -l',
                                shell=True,
                                capture_output=True)
        if xrandr.returncode == 0:
            try:
                return int(xrandr.stdout) - 1
            except ValueError:
                pass
        return 1

    def screens(self, monitors: int) -> List:
        return [Screen(top=bar.Bar(self.get_widgets(), size=20))
                for _ in range(monitors)]

    # MOUSE ACTIONS
    dgroups_key_binder: None = None
    dgroups_app_rules: list = dataclasses.field(default_factory=list)
    follow_mouse_focus: bool = True
    bring_front_click: bool = False
    cursor_warp: bool = False

    def mouse(self) -> List:
        return [
            Drag([self.keybind_keys.alt], "Button1",
                 lazy.window.set_position_floating(),
                 start=lazy.window.get_position()),

            Drag([self.keybind_keys.alt], "Button3",
                 lazy.window.set_size_floating(),
                 start=lazy.window.get_size()),

            Click([self.keybind_keys.alt], "Button2",
                  lazy.window.bring_to_front())
    ]


@dataclasses.dataclass
class DefaultConfiguration(_Configuration):

    nic: str = ''

    def keys(self) -> List:
        return keybindings.WorkstationKeybindings(
            self.keybind_keys,
            self.terminal,
            self.browser,
            self.file_manager
        ).get_keybindings()

    def get_widgets(self) -> List:
        return widgets.WorkstationWidgets(
            self.terminal,
            self.nic,
            self.fonts,
            self.symbols,
            self.widget_defults).get_widgets()


@dataclasses.dataclass
class WorkstationConfiguration(_Configuration):

    nic: str = 'enp6s0'
    fonts: widgets.Fonts = dataclasses.field(
        default_factory=lambda: widgets.Fonts(symbols='Symbols Nerd Font'))

    def keys(self) -> List:
        return keybindings.WorkstationKeybindings(
            self.keybind_keys,
            self.terminal,
            self.browser,
            self.file_manager
        ).get_keybindings()

    def get_widgets(self) -> List:
        return widgets.WorkstationWidgets(
            self.terminal,
            self.nic,
            self.fonts,
            self.symbols,
            self.widget_defults).get_widgets()


@dataclasses.dataclass
class LaptopConfiguration(_Configuration):

    nic: str = 'wlp4s0'

    def keys(self) -> List:
        return keybindings.LaptopKeybindings(
            self.keybind_keys,
            self.terminal,
            self.browser,
            self.file_manager
        ).get_keybindings()

    def get_widgets(self) -> List:
        return widgets.LaptopWidgets(
            self.terminal,
            self.nic,
            self.fonts,
            self.symbols,
            self.widget_defults).get_widgets()

