import dataclasses
from typing import List

from libqtile import widget
from libqtile import bar
from libqtile.lazy import lazy

import colors


@dataclasses.dataclass
class Fonts:
    """Customize the fonts used in widgets.
    """

    default: str = 'Ubuntu Mono'
    bold: str = 'Ubuntu Bold'
    symbols: str = 'Noto Sans Mono'


@dataclasses.dataclass
class Symbols:
    """Customize the symbols used in widgets.
    """

    fonts: Fonts
    left_arrow: str = '\uE0B2'
    right_arrow: str = '\uE0B0'
    left_wing: str = '\uE0B3'
    right_wing: str = '\uE0B1'

    def arrow(self, symbol: str, bg: str = '', fg: str = '') -> widget.TextBox:
        _settings = {
            'text': symbol,
            'font': self.fonts.symbols,
            'background': bg,
            'foreground': fg,
            'fontsize': 31,
            'padding': 0
        }
        if not bg: _settings.pop('background')
        if not fg: _settings.pop('foreground')
        return widget.TextBox(**_settings)


@dataclasses.dataclass
class WidgetDefaults:

    font: str = 'Ubuntu Mono'
    fontsize: int = 12
    padding: int = 2
    background: str = colors.Normal.background
    foreground: str = colors.Normal.white


@dataclasses.dataclass
class _Widgets:
    """Base class for all default widgets.
    """

    terminal: str
    fonts: Fonts
    symbols: Symbols
    defaults: WidgetDefaults

    def get_widgets(self) -> List:
        all_widgets = []
        all_widgets.extend(self.left_widgets())
        all_widgets.extend(self.center_widgets())
        all_widgets.extend(self.right_widgets())
        return all_widgets

    def left_widgets(self) -> List:
        return [
            widget.GroupBox(
                font=self.fonts.bold,
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
            self.symbols.arrow(
                self.symbols.right_arrow,
                colors.Dim.blue,
                colors.Normal.inactive),
            widget.CurrentLayoutIcon(
                scale=0.8,
                padding=6,
                background=colors.Dim.blue),
            self.symbols.arrow(
                self.symbols.right_arrow,
                fg=colors.Dim.blue,
                bg=self.defaults.background)
        ]

    def center_widgets(self) -> List:
        return [
            widget.Spacer(
                length=bar.STRETCH,
                background=self.defaults.background),
            widget.Clock(
                format='%a %d-%m-%y %H:%M:%S',
                font='Ubuntu Bold',
                background=self.defaults.background),
            widget.Spacer(
                length=bar.STRETCH,
                background=self.defaults.background),
        ]

    def right_widgets(self) -> List:
        _widgets = []
        _widgets.extend(self.bluetooth())
        _widgets.extend(self.check_updates())
        _widgets.extend(self.volume())
        _widgets.extend(self.storage())
        _widgets.extend(self.memory())
        _widgets.extend(self.cpu())
        _widgets.extend(self.network())
        _widgets.extend(self.power())
        return _widgets

    def bluetooth(self) -> List:
        return [
            self.symbols.arrow(
                self.symbols.left_arrow,
                colors.Normal.background,
                colors.Normal.white),
            widget.Bluetooth(
                fmt='\uF294 {}',
                hci='/dev_04_52_C7_07_FC_60',
                background=colors.Normal.white,
                foreground=colors.Dim.blue)
        ]

    def check_updates(self) -> List:
        return [
            self.symbols.arrow(
                self.symbols.left_arrow,
                colors.Normal.white,
                colors.Normal.green),
            widget.CheckUpdates(
                display_format='\uF1B2 {updates}',
                distro='Arch_checkupdates',
                update_interval=900,
                no_update_string='\uF1B3 0',
                background=colors.Normal.green,
                colour_have_updates=colors.Dim.blue,
                execute=f'{self.terminal} -e sudo pacman -Syu'),
            self.symbols.arrow(
                self.symbols.left_wing,
                colors.Normal.green,
                colors.Normal.background),
            widget.CheckUpdates(
                display_format='\uF1B3 {updates}',
                custom_command='yay -Qu --aur',
                update_interval=900,
                no_update_string='\uF1B3 0',
                background=colors.Normal.green,
                colour_have_updates=colors.Dim.blue,
                execute=f'{self.terminal} -e yay -Syu --aur')
        ]

    def volume(self) -> List:
        return [
            self.symbols.arrow(
                self.symbols.left_arrow,
                colors.Bright.green,
                colors.Bright.yellow),
            widget.Volume(
                fmt='\uF028 {}',
                background=colors.Bright.yellow,
                foreground=colors.Dim.blue)
        ]

    def storage(self) -> List:
        return [
            self.symbols.arrow(
                self.symbols.left_arrow,
                colors.Bright.yellow,
                colors.Bright.cyan),
            widget.DF(
                format='\uF748 {r:.0f}%',
                visible_on_warn=False,
                background=colors.Bright.cyan,
                foreground=colors.Dim.blue,
                mouse_callbacks = {
                    'Button1': lazy.spawn(
                        self.terminal + ' --hold -e dust -d 1 -x /')
                }),
            self.symbols.arrow(
                self.symbols.left_wing,
                colors.Bright.cyan,
                colors.Normal.background),
            widget.DF(
                format='\uF023 {r:.0f}%',
                partition='/home/unicorn/Documents/vault',
                visible_on_warn=False,
                background=colors.Bright.cyan,
                foreground=colors.Dim.blue,
                mouse_callbacks = {
                    'Button1': lazy.spawn(
                        self.terminal +
                        ' --hold -e dust -d 1 -x /home/unicorn/Documents/vault')
                })
        ]

    def memory(self) -> List:
        return [
            self.symbols.arrow(
                self.symbols.left_arrow,
                colors.Bright.cyan,
                colors.Bright.red),
            widget.Memory(
                format='\uF85A {MemUsed:.2f}{mm}',
                measure_mem='G',
                background=colors.Bright.red,
                foreground=colors.Dim.blue,
                mouse_callbacks = {
                    'Button1': lazy.spawn(
                        self.terminal + ' --hold -e free -h')
                })
        ]

    def cpu(self) -> List:
        return [
            self.symbols.arrow(
                self.symbols.left_arrow,
                colors.Bright.red,
                colors.Bright.magenta),
            widget.CPU(
                format='\uE266 {freq_current}GHz\uE216{load_percent}% ',
                background=colors.Bright.magenta,
                foreground=colors.Dim.blue,
                mouse_callbacks = {
                    'Button1': lazy.spawn(self.terminal + ' -e htop')
                })
        ]

    def network(self) -> List:
        return [
            self.symbols.arrow(
                self.symbols.left_arrow,
                colors.Bright.magenta,
                colors.Bright.blue),
            widget.Net(
                fmt='\uF6FF {}',
                prefix='M',
                interface='enp6s0',
                format='{down}↓↑{up}',
                background=colors.Bright.blue,
                foreground=colors.Dim.blue,
                padding=5,
                mouse_callbacks = {
                    'Button1': lazy.spawn(self.terminal + ' -e ping 8.8.8.8')
                })
        ]

    def power(self) -> List:
        return [
            self.symbols.arrow(
                self.symbols.left_arrow,
                colors.Bright.blue,
                colors.Bright.black),
            widget.TextBox(
                text='\uF011',
                font=self.fonts.symbols,
                background=colors.Bright.black,
                foreground=colors.Bright.white,
                fontsize=15,
                padding=5,
                mouse_callbacks = {
                    'Button1': lazy.spawn('systemctl poweroff'),
                    'Button2': lazy.spawn('systemctl reboot'),
                    'Button3': lazy.spawn('systemctl hibernate')
                })
        ]


class WorkstationWidgets(_Widgets):
    """Widgets used for Workstation configurations.
    """


class LaptopWidgets(_Widgets):
    """Widgets used for Laptop configurations.
    """

