"""Stub file for reflex/components/radix/themes/color_mode.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
import dataclasses
from typing import Literal, get_args
from reflex.components.component import BaseComponent
from reflex.components.core.cond import Cond, color_mode_cond, cond
from reflex.components.lucide.icon import Icon
from reflex.components.radix.themes.components.dropdown_menu import dropdown_menu
from reflex.components.radix.themes.components.switch import Switch
from reflex.style import (
    LIGHT_COLOR_MODE,
    color_mode,
    resolved_color_mode,
    set_color_mode,
    toggle_color_mode,
)
from reflex.utils import console
from reflex.vars import BaseVar, Var
from .components.icon_button import IconButton

DEFAULT_LIGHT_ICON: Icon
DEFAULT_DARK_ICON: Icon

class ColorModeIcon(Cond):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        cond: Optional[Union[reflex.vars.Var[Any], Any]] = None,
        comp1: Optional[BaseComponent] = None,
        comp2: Optional[BaseComponent] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "ColorModeIcon":
        """Create an icon component based on color_mode.

        Args:
            light_component: the component to display when color mode is default
            dark_component: the component to display when color mode is dark (non-default)

        Returns:
            The conditionally rendered component
        """
        ...

LiteralPosition = Literal["top-left", "top-right", "bottom-left", "bottom-right"]
position_values = get_args(LiteralPosition)
position_map = {
    "position": position_values,
    "left": ["top-left", "bottom-left"],
    "right": ["top-right", "bottom-right"],
    "top": ["top-left", "top-right"],
    "bottom": ["bottom-left", "bottom-right"],
}

class ColorModeIconButton(IconButton):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        position: Optional[
            Literal["top-left", "top-right", "bottom-left", "bottom-right"]
        ] = None,
        allow_system: Optional[bool] = False,
        as_child: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        size: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal["1", "2", "3", "4"],
                        reflex.components.core.breakpoints.Breakpoints[
                            str, Literal["1", "2", "3", "4"]
                        ],
                    ]
                ],
                Union[
                    Literal["1", "2", "3", "4"],
                    reflex.components.core.breakpoints.Breakpoints[
                        str, Literal["1", "2", "3", "4"]
                    ],
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                reflex.vars.Var[
                    Literal["classic", "solid", "soft", "surface", "outline", "ghost"]
                ],
                Literal["classic", "solid", "soft", "surface", "outline", "ghost"],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                reflex.vars.Var[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
        high_contrast: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        radius: Optional[
            Union[
                reflex.vars.Var[Literal["none", "small", "medium", "large", "full"]],
                Literal["none", "small", "medium", "large", "full"],
            ]
        ] = None,
        auto_focus: Optional[
<<<<<<< HEAD
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        disabled: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        form: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        form_action: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        form_enc_type: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        form_method: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        form_no_validate: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        form_target: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        name: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        type: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        value: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        access_key: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        auto_capitalize: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        content_editable: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        context_menu: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        dir: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        draggable: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        enter_key_hint: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        hidden: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        input_mode: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        item_prop: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        lang: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        role: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        slot: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        spell_check: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        tab_index: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
        ] = None,
        title: Optional[
            Union[reflex.vars.Var[Union[str, int, bool]], Union[str, int, bool]]
=======
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        disabled: Optional[Union[Var[bool], bool]] = None,
        form: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        form_action: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        form_enc_type: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        form_method: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        form_no_validate: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        form_target: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        name: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        type: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        value: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        access_key: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        auto_capitalize: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        content_editable: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        context_menu: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        dir: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        draggable: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        enter_key_hint: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        hidden: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        input_mode: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        item_prop: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        lang: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        role: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        slot: Optional[Union[Var[Union[bool, int, str]], Union[bool, int, str]]] = None,
        spell_check: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        tab_index: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
        ] = None,
        title: Optional[
            Union[Var[Union[bool, int, str]], Union[bool, int, str]]
>>>>>>> 2027a2f0 (order type annotations in pyi_generator (#3585))
        ] = None,
        loading: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "ColorModeIconButton":
        """Create a icon button component that calls toggle_color_mode on click.

        Args:
            *children: The children of the component.
            position: The position of the icon button. Follow document flow if None.
            allow_system: Allow picking the "system" value for the color mode.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            size: Button size "1" - "4"
            variant: Variant of button: "classic" | "solid" | "soft" | "surface" | "outline" | "ghost"
            color_scheme: Override theme color for button
            high_contrast: Whether to render the button with higher contrast color against background
            radius: Override theme radius for button: "none" | "small" | "medium" | "large" | "full"
            auto_focus: Automatically focuses the button when the page loads
            disabled: Disables the button
            form: Associates the button with a form (by id)
            form_action: URL to send the form data to (for type="submit" buttons)
            form_enc_type: How the form data should be encoded when submitting to the server (for type="submit" buttons)
            form_method: HTTP method to use for sending form data (for type="submit" buttons)
            form_no_validate: Bypasses form validation when submitting (for type="submit" buttons)
            form_target: Specifies where to display the response after submitting the form (for type="submit" buttons)
            name: Name of the button, used when sending form data
            type: Type of the button (submit, reset, or button)
            value: Value of the button, used when sending form data
            access_key:  Provides a hint for generating a keyboard shortcut for the current element.
            auto_capitalize: Controls whether and how text input is automatically capitalized as it is entered/edited by the user.
            content_editable: Indicates whether the element's content is editable.
            context_menu: Defines the ID of a <menu> element which will serve as the element's context menu.
            dir: Defines the text direction. Allowed values are ltr (Left-To-Right) or rtl (Right-To-Left)
            draggable: Defines whether the element can be dragged.
            enter_key_hint: Hints what media types the media element is able to play.
            hidden: Defines whether the element is hidden.
            input_mode: Defines the type of the element.
            item_prop: Defines the name of the element for metadata purposes.
            lang: Defines the language used in the element.
            role: Defines the role of the element.
            slot: Assigns a slot in a shadow DOM shadow tree to an element.
            spell_check: Defines whether the element may be checked for spelling errors.
            tab_index: Defines the position of the current element in the tabbing order.
            title: Defines a tooltip for the element.
            loading: If set, show an rx.spinner instead of the component children.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props to pass to the component.

        Returns:
            The button component.
        """
        ...

class ColorModeSwitch(Switch):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        default_checked: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        checked: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        disabled: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        required: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        name: Optional[Union[reflex.vars.Var[str], str]] = None,
        value: Optional[Union[reflex.vars.Var[str], str]] = None,
        size: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal["1", "2", "3"],
                        reflex.components.core.breakpoints.Breakpoints[
                            str, Literal["1", "2", "3"]
                        ],
                    ]
                ],
                Union[
                    Literal["1", "2", "3"],
                    reflex.components.core.breakpoints.Breakpoints[
                        str, Literal["1", "2", "3"]
                    ],
                ],
            ]
        ] = None,
        variant: Optional[
            Union[
                reflex.vars.Var[Literal["classic", "surface", "soft"]],
                Literal["classic", "surface", "soft"],
            ]
        ] = None,
        color_scheme: Optional[
            Union[
                reflex.vars.Var[
                    Literal[
                        "tomato",
                        "red",
                        "ruby",
                        "crimson",
                        "pink",
                        "plum",
                        "purple",
                        "violet",
                        "iris",
                        "indigo",
                        "blue",
                        "cyan",
                        "teal",
                        "jade",
                        "green",
                        "grass",
                        "brown",
                        "orange",
                        "sky",
                        "mint",
                        "lime",
                        "yellow",
                        "amber",
                        "gold",
                        "bronze",
                        "gray",
                    ]
                ],
                Literal[
                    "tomato",
                    "red",
                    "ruby",
                    "crimson",
                    "pink",
                    "plum",
                    "purple",
                    "violet",
                    "iris",
                    "indigo",
                    "blue",
                    "cyan",
                    "teal",
                    "jade",
                    "green",
                    "grass",
                    "brown",
                    "orange",
                    "sky",
                    "mint",
                    "lime",
                    "yellow",
                    "amber",
                    "gold",
                    "bronze",
                    "gray",
                ],
            ]
        ] = None,
        high_contrast: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        radius: Optional[
            Union[
                reflex.vars.Var[Literal["none", "small", "full"]],
                Literal["none", "small", "full"],
            ]
        ] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_blur: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_change: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_context_menu: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_double_click: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_focus: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_down: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_enter: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_leave: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_move: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_out: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_over: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_mouse_up: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_scroll: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        on_unmount: Optional[
            Union[EventHandler, EventSpec, list, function, BaseVar]
        ] = None,
        **props
    ) -> "ColorModeSwitch":
        """Create a switch component bound to color_mode.

        Args:
            *children: The children of the component.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            default_checked: Whether the switch is checked by default
            checked: Whether the switch is checked
            disabled: If true, prevent the user from interacting with the switch
            required: If true, the user must interact with the switch to submit the form
            name: The name of the switch (when submitting a form)
            value: The value associated with the "on" position
            size: Switch size "1" - "4"
            variant: Variant of switch: "classic" | "surface" | "soft"
            color_scheme: Override theme color for switch
            high_contrast: Whether to render the switch with higher contrast color against background
            radius: Override theme radius for switch: "none" | "small" | "full"
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props to pass to the component.

        Returns:
            The switch component.
        """
        ...

class ColorModeNamespace(BaseVar):
    icon = staticmethod(ColorModeIcon.create)
    button = staticmethod(ColorModeIconButton.create)
    switch = staticmethod(ColorModeSwitch.create)

color_mode = color_mode_var_and_namespace = ColorModeNamespace(
    **dataclasses.asdict(color_mode)
)
