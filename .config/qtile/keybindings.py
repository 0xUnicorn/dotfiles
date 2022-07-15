import dataclasses
import abc
from typing import List

from libqtile import config
from libqtile import extension
from libqtile.lazy import lazy

import colors


@dataclasses.dataclass
class Keys:
    """Customize the keys used in the keybindings.
    """

    alt: str = 'mod1'
    super_: str = 'mod4'
    shift: str = 'shift'
    ctrl: str = 'control'


@dataclasses.dataclass
class _Keybindings:
    """Base class for all default keybindings.
    """

    keys: Keys
    terminal: str
    browser: str
    file_manager: str

    def get_keybindings(self) -> List:
        all_keybindings = []
        all_keybindings.extend(self.qtile_controls())
        all_keybindings.extend(self.power_controls())
        all_keybindings.extend(self.applications())
        all_keybindings.extend(self.dmenu())
        all_keybindings.extend(self.volume_controls())
        all_keybindings.extend(self.screen_lock())
        all_keybindings.extend(self.screen_focus())
        all_keybindings.extend(self.switch_layouts())
        all_keybindings.extend(self.layout_focus())
        all_keybindings.extend(self.layout_shuffle())
        all_keybindings.extend(self.layout_sizes())
        all_keybindings.extend(self.window_controls())
        return all_keybindings

    def qtile_controls(self) -> List:
        _mod = [self.keys.alt, self.keys.ctrl]
        return [
            config.Key(_mod, 'r',
                       lazy.restart(),
                       desc='Restart Qtile'),

            config.Key(_mod, 'q',
                       lazy.shutdown(),
                       desc='Shutdown Qtile'),
        ]

    def power_controls(self) -> List:
        _mod = [self.keys.alt, self.keys.ctrl, self.keys.shift]
        return [
            config.Key(_mod, 's',
                       lazy.spawn('systemctl hibernate'),
                       desc='Hibernate System'),

            config.Key(_mod, 'q',
                       lazy.spawn('systemctl poweroff'),
                       desc='Poweroff System'),

            config.Key(_mod, 'r',
                       lazy.spawn('systemctl reboot'),
                       desc='Reboot System'),
        ]

    def applications(self) -> List:
        _terminal = config.Key([self.keys.alt], 'Return',
                               lazy.spawn(self.terminal),
                               desc='Launch terminal')

        _apps_chord = config.KeyChord([self.keys.alt], 'a', [
            config.Key([], 'BackSpace',
                       lazy.spawn(self.file_manager),
                       desc='Launch filemanager'),

            config.Key([], 'm',
                       lazy.spawn('tidal-hifi'),
                       desc='Launch Tidal'),

            config.Key([], 'a',
                       lazy.spawn('authy'),
                       desc='Launch Authy'),

            config.Key([], 't',
                       lazy.spawn('thunderbird'),
                       desc='Launch Thunderbird'),

            config.Key([], 's',
                       lazy.spawn('gnome-screenshot -i'),
                       desc='Screenshot selection'),

            config.Key([], 'd',
                       lazy.spawn('discord'),
                       desc='Launch Discord'),

            config.Key([], 'b',
                       lazy.spawn(self.browser),
                       desc='Launch browser'),
        ])
        return [_terminal, _apps_chord]

    def dmenu(self) -> List:
        return [
            config.KeyChord([self.keys.alt], 'd', [
                config.Key([], 'Return',
                           lazy.run_extension(extension.DmenuRun(
                               dmenu_prompt='\uF120',
                               dmenu_font='Ubuntu Mono',
                               background=colors.Normal.background,
                               foreground=colors.Dim.white,
                               selected_background=colors.Dim.magenta,
                               selected_foreground=colors.Normal.background)),
                           desc='Launch Dmenu'),
        ])]

    def volume_controls(self) -> List:
        return [
            config.Key([], 'XF86AudioLowerVolume',
                       lazy.spawn('amixer -D pulse set Master 5%- unmute'),
                       desc='Turn master volume up 5%'),

            config.Key([], 'XF86AudioRaiseVolume',
                       lazy.spawn('amixer -D pulse set Master 5%+ unmute'),
                       desc='Turn master volume down 5%'),

            config.Key([], 'XF86AudioMute',
                       lazy.spawn('amixer -D pulse set Master toggle'),
                       desc='Mute/unmute master volume'),
        ]

    def screen_lock(self) -> List:
        return [
            config.Key([self.keys.super_], 'l',
                       lazy.spawn('dm-tool lock'),
                       desc='Lock screen'),
        ]

    def screen_focus(self) -> List:
        _mod = [self.keys.alt]
        return [
            config.Key(_mod, 'w',
                       lazy.to_screen(0),
                       desc='Focus monitor 0'),

            config.Key(_mod, 'e',
                       lazy.to_screen(1),
                       desc='Focus monitor 1'),

            config.Key(_mod, 'q',
                       lazy.to_screen(2),
                       desc='Focus monitor 2'),
        ]

    def switch_layouts(self) -> List:
        _mod = [self.keys.alt]
        return [
            config.Key(_mod, 'Tab',
                       lazy.next_layout(),
                       desc='Next layout'),

            config.Key(_mod + [self.keys.shift], 'Tab',
                       lazy.prev_layout(),
                       desc='Previous layout'),
        ]

    def layout_focus(self) -> List:
        _mod = [self.keys.alt]
        return [
            config.Key(_mod, 'k',
                       lazy.layout.up(),
                       desc='Move layout focus up'),

            config.Key(_mod, 'j',
                       lazy.layout.down(),
                       desc='Move layout focus down'),

            config.Key(_mod, 'h',
                       lazy.layout.left(),
                       desc='Move layout focus left'),

            config.Key(_mod, 'l',
                       lazy.layout.up(),
                       desc='Move layout focus right'),
        ]

    def layout_shuffle(self) -> List:
        _mod = [self.keys.alt, self.keys.shift]
        return [
            config.Key(_mod, 'k',
                       lazy.layout.shuffle_up(),
                       desc='Shuffle layout up'),

            config.Key(_mod, 'j',
                       lazy.layout.shuffle_down(),
                       desc='Shuffle layout down'),

            config.Key(_mod, 'h',
                       lazy.layout.shuffle_left(),
                       desc='Shuffle layout to the left'),

            config.Key(_mod, 'l',
                       lazy.layout.shuffle_right(),
                       desc='Shuffle layout to the right'),
        ]

    def layout_sizes(self) -> List:
        _mod = [self.keys.alt, self.keys.ctrl]
        return [
            config.Key(_mod, 'k',
                       lazy.layout.grow(),
                       desc='Grow the focused layout'),

            config.Key(_mod, 'j',
                       lazy.layout.shrink(),
                       desc='Shrink the focused layout'),

            config.Key(_mod, 'l',
                       lazy.layout.normalize(),
                       desc='Normalize the focused layout to default'),

            config.Key(_mod, 'h',
                       lazy.layout.maximize(),
                       desc='Maximize the focused layout'),
        ]

    def window_controls(self) -> List:
        _mod = [self.keys.alt]
        return [
            config.Key(_mod, 'f',
                       lazy.window.toggle_floating(),
                       desc='Toggle floating'),

            config.Key(_mod + [self.keys.shift], 'c',
                       lazy.window.kill(),
                       desc='Kill focused window'),
        ]


@dataclasses.dataclass
class WorkstationKeybindings(_Keybindings):
    """Keybindings used for Workstation configurations.
    """


@dataclasses.dataclass
class LaptopKeybindings(_Keybindings):
    """Keybindings used for Laptop configurations.
    """

