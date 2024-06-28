"""Stub file for reflex/components/radix/themes/layout/grid.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Dict, Literal
from reflex.components.core.breakpoints import Responsive
from reflex.components.el import elements
from reflex.vars import Var
from ..base import LiteralAlign, LiteralJustify, LiteralSpacing, RadixThemesComponent

LiteralGridFlow = Literal["row", "column", "dense", "row-dense", "column-dense"]

class Grid(elements.Div, RadixThemesComponent):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        as_child: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        columns: Optional[
            Union[
                reflex.vars.Var[
                    Union[reflex.components.core.breakpoints.Breakpoints[str, str], str]
                ],
                str,
                reflex.components.core.breakpoints.Breakpoints[str, str],
            ]
        ] = None,
        rows: Optional[
            Union[
                reflex.vars.Var[
                    Union[reflex.components.core.breakpoints.Breakpoints[str, str], str]
                ],
                str,
                reflex.components.core.breakpoints.Breakpoints[str, str],
            ]
        ] = None,
        flow: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal["row", "column", "dense", "row-dense", "column-dense"],
                        reflex.components.core.breakpoints.Breakpoints[
                            str,
                            Literal[
                                "row", "column", "dense", "row-dense", "column-dense"
                            ],
                        ],
                    ]
                ],
                Literal["row", "column", "dense", "row-dense", "column-dense"],
                reflex.components.core.breakpoints.Breakpoints[
                    str, Literal["row", "column", "dense", "row-dense", "column-dense"]
                ],
            ]
        ] = None,
        align: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal["start", "center", "end", "baseline", "stretch"],
                        reflex.components.core.breakpoints.Breakpoints[
                            str,
                            Literal["start", "center", "end", "baseline", "stretch"],
                        ],
                    ]
                ],
                Literal["start", "center", "end", "baseline", "stretch"],
                reflex.components.core.breakpoints.Breakpoints[
                    str, Literal["start", "center", "end", "baseline", "stretch"]
                ],
            ]
        ] = None,
        justify: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal["start", "center", "end", "between"],
                        reflex.components.core.breakpoints.Breakpoints[
                            str, Literal["start", "center", "end", "between"]
                        ],
                    ]
                ],
                Literal["start", "center", "end", "between"],
                reflex.components.core.breakpoints.Breakpoints[
                    str, Literal["start", "center", "end", "between"]
                ],
            ]
        ] = None,
        spacing: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        reflex.components.core.breakpoints.Breakpoints[
                            str,
                            Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        ],
                    ]
                ],
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                reflex.components.core.breakpoints.Breakpoints[
                    str, Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                ],
            ]
        ] = None,
        spacing_x: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        reflex.components.core.breakpoints.Breakpoints[
                            str,
                            Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        ],
                    ]
                ],
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                reflex.components.core.breakpoints.Breakpoints[
                    str, Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                ],
            ]
        ] = None,
        spacing_y: Optional[
            Union[
                reflex.vars.Var[
                    Union[
                        Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        reflex.components.core.breakpoints.Breakpoints[
                            str,
                            Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                        ],
                    ]
                ],
                Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"],
                reflex.components.core.breakpoints.Breakpoints[
                    str, Literal["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
                ],
            ]
        ] = None,
        access_key: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        auto_capitalize: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        content_editable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        context_menu: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        dir: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        draggable: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        enter_key_hint: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        hidden: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        input_mode: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        item_prop: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        lang: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        role: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        slot: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        spell_check: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        tab_index: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
        ] = None,
        title: Optional[
            Union[reflex.vars.Var[Union[bool, int, str]], str, int, bool]
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
    ) -> "Grid":
        """Create a new component instance.

        Will prepend "RadixThemes" to the component tag to avoid conflicts with
        other UI libraries for common names, like Text and Button.

        Args:
            *children: Child components.
            as_child: Change the default rendered element for the one passed as a child, merging their props and behavior.
            columns: Number of columns
            rows: Number of rows
            flow: How the grid items are layed out: "row" | "column" | "dense" | "row-dense" | "column-dense"
            align: Alignment of children along the main axis: "start" | "center" | "end" | "baseline" | "stretch"
            justify: Alignment of children along the cross axis: "start" | "center" | "end" | "between"
            spacing: Gap between children: "0" - "9"
            spacing_x: Gap between children horizontal: "0" - "9"
            spacing_y: Gap between children vertical: "0" - "9"
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
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: Component properties.

        Returns:
            A new component instance.
        """
        ...

grid = Grid.create
