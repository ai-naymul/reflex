"""Stub file for reflex/components/recharts/polar.py"""
# ------------------- DO NOT EDIT ----------------------
# This file was generated by `reflex/utils/pyi_generator.py`!
# ------------------------------------------------------

from typing import Any, Dict, Literal, Optional, Union, overload
import reflex
from reflex.vars import Var, BaseVar, ComputedVar
from reflex.event import EventChain, EventHandler, EventSpec
from reflex.style import Style
from typing import Any, Dict, List, Union
from reflex.constants import EventTriggers
from reflex.event import EventHandler
from reflex.vars import Var
from .recharts import (
    LiteralAnimationEasing,
    LiteralGridType,
    LiteralLegendType,
    LiteralPolarRadiusType,
    LiteralScale,
    Recharts,
)

class Pie(Recharts):
    def get_event_triggers(self) -> dict[str, Union[Var, Any]]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
<<<<<<< HEAD
        data: Optional[
            Union[reflex.vars.Var[List[Dict[str, Any]]], List[Dict[str, Any]]]
        ] = None,
        data_key: Optional[
            Union[reflex.vars.Var[Union[str, int]], Union[str, int]]
        ] = None,
        cx: Optional[Union[reflex.vars.Var[Union[int, str]], Union[int, str]]] = None,
        cy: Optional[Union[reflex.vars.Var[Union[int, str]], Union[int, str]]] = None,
        inner_radius: Optional[
            Union[reflex.vars.Var[Union[int, str]], Union[int, str]]
        ] = None,
        outer_radius: Optional[
            Union[reflex.vars.Var[Union[int, str]], Union[int, str]]
        ] = None,
        start_angle: Optional[Union[reflex.vars.Var[int], int]] = None,
        end_angle: Optional[Union[reflex.vars.Var[int], int]] = None,
        min_angle: Optional[Union[reflex.vars.Var[int], int]] = None,
        padding_angle: Optional[Union[reflex.vars.Var[int], int]] = None,
        name_key: Optional[Union[reflex.vars.Var[str], str]] = None,
=======
        data: Optional[Union[Var[List[Dict[str, Any]]], List[Dict[str, Any]]]] = None,
        data_key: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None,
        cx: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None,
        cy: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None,
        inner_radius: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None,
        outer_radius: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None,
        start_angle: Optional[Union[Var[int], int]] = None,
        end_angle: Optional[Union[Var[int], int]] = None,
        min_angle: Optional[Union[Var[int], int]] = None,
        padding_angle: Optional[Union[Var[int], int]] = None,
        name_key: Optional[Union[Var[str], str]] = None,
>>>>>>> 2027a2f0 (order type annotations in pyi_generator (#3585))
        legend_type: Optional[
            Union[
                reflex.vars.Var[
                    Literal[
                        "line",
                        "plainline",
                        "square",
                        "rect",
                        "circle",
                        "cross",
                        "diamond",
                        "star",
                        "triangle",
                        "wye",
                        "none",
                    ]
                ],
                Literal[
                    "line",
                    "plainline",
                    "square",
                    "rect",
                    "circle",
                    "cross",
                    "diamond",
                    "star",
                    "triangle",
                    "wye",
                    "none",
                ],
            ]
        ] = None,
        label: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        label_line: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        fill: Optional[Union[reflex.vars.Var[str], str]] = None,
        stroke: Optional[Union[reflex.vars.Var[str], str]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_click: Optional[
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
        **props
    ) -> "Pie":
        """Create the component.

        Args:
            *children: The children of the component.
            data: data
            data_key: The key of each sector's value.
            cx: The x-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container width.
            cy: The y-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container height.
            inner_radius: The inner radius of pie, which can be set to a percent value.
            outer_radius: The outer radius of pie, which can be set to a percent value.
            start_angle: The angle of first sector.
            end_angle: The direction of sectors. 1 means clockwise and -1 means anticlockwise.
            min_angle: The minimum angle of each unzero data.
            padding_angle: The angle between two sectors.
            name_key: The key of each sector's name.
            legend_type: The type of icon in legend. If set to 'none', no legend item will be rendered.
            label: If false set, labels will not be drawn.
            label_line: If false set, label lines will not be drawn.
            fill: fill color
            stroke: stroke color
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class Radar(Recharts):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
<<<<<<< HEAD
        data_key: Optional[
            Union[reflex.vars.Var[Union[str, int]], Union[str, int]]
        ] = None,
        points: Optional[
            Union[reflex.vars.Var[List[Dict[str, Any]]], List[Dict[str, Any]]]
        ] = None,
        dot: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        stroke: Optional[Union[reflex.vars.Var[str], str]] = None,
        fill: Optional[Union[reflex.vars.Var[str], str]] = None,
        fill_opacity: Optional[Union[reflex.vars.Var[float], float]] = None,
        legend_type: Optional[Union[reflex.vars.Var[str], str]] = None,
        label: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        animation_begin: Optional[Union[reflex.vars.Var[int], int]] = None,
        animation_duration: Optional[Union[reflex.vars.Var[int], int]] = None,
=======
        data_key: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None,
        points: Optional[Union[Var[List[Dict[str, Any]]], List[Dict[str, Any]]]] = None,
        dot: Optional[Union[Var[bool], bool]] = None,
        stroke: Optional[Union[Var[str], str]] = None,
        fill: Optional[Union[Var[str], str]] = None,
        fill_opacity: Optional[Union[Var[float], float]] = None,
        legend_type: Optional[Union[Var[str], str]] = None,
        label: Optional[Union[Var[bool], bool]] = None,
        animation_begin: Optional[Union[Var[int], int]] = None,
        animation_duration: Optional[Union[Var[int], int]] = None,
>>>>>>> 2027a2f0 (order type annotations in pyi_generator (#3585))
        animation_easing: Optional[
            Union[
                reflex.vars.Var[
                    Literal["ease", "ease-in", "ease-out", "ease-in-out", "linear"]
                ],
                Literal["ease", "ease-in", "ease-out", "ease-in-out", "linear"],
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
    ) -> "Radar":
        """Create the component.

        Args:
            *children: The children of the component.
            data_key: The key of a group of data which should be unique in a radar chart.
            points: The coordinates of all the vertexes of the radar shape, like [{ x, y }].
            dot: If false set, dots will not be drawn
            stroke: Stoke color
            fill: Fill color
            fill_opacity: opacity
            legend_type: The type of icon in legend. If set to 'none', no legend item will be rendered.
            label: If false set, labels will not be drawn
            animation_begin: Specifies when the animation should begin, the unit of this option is ms.
            animation_duration: Specifies the duration of animation, the unit of this option is ms.
            animation_easing: The type of easing function. 'ease' | 'ease-in' | 'ease-out' | 'ease-in-out' | 'linear'
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class RadialBar(Recharts):
    def get_event_triggers(self) -> dict[str, Union[Var, Any]]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
<<<<<<< HEAD
        data_key: Optional[
            Union[reflex.vars.Var[Union[str, int]], Union[str, int]]
=======
        data_key: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None,
        min_angle: Optional[Union[Var[int], int]] = None,
        legend_type: Optional[Union[Var[str], str]] = None,
        label: Optional[
            Union[Var[Union[Dict[str, Any], bool]], Union[Dict[str, Any], bool]]
>>>>>>> 2027a2f0 (order type annotations in pyi_generator (#3585))
        ] = None,
        min_angle: Optional[Union[reflex.vars.Var[int], int]] = None,
        legend_type: Optional[Union[reflex.vars.Var[str], str]] = None,
        label: Optional[
            Union[
                reflex.vars.Var[Union[bool, Dict[str, Any]]],
                Union[bool, Dict[str, Any]],
            ]
        ] = None,
        background: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_click: Optional[
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
        **props
    ) -> "RadialBar":
        """Create the component.

        Args:
            *children: The children of the component.
            data_key: The key of a group of data which should be unique to show the meaning of angle axis.
            min_angle: Min angle of each bar. A positive value between 0 and 360.
            legend_type: Type of legend
            label: If false set, labels will not be drawn.
            background: If false set, background sector will not be drawn.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class PolarAngleAxis(Recharts):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
<<<<<<< HEAD
        data_key: Optional[
            Union[reflex.vars.Var[Union[str, int]], Union[str, int]]
        ] = None,
        cx: Optional[Union[reflex.vars.Var[Union[int, str]], Union[int, str]]] = None,
        cy: Optional[Union[reflex.vars.Var[Union[int, str]], Union[int, str]]] = None,
        radius: Optional[
            Union[reflex.vars.Var[Union[int, str]], Union[int, str]]
        ] = None,
        axis_line: Optional[
            Union[
                reflex.vars.Var[Union[bool, Dict[str, Any]]],
                Union[bool, Dict[str, Any]],
            ]
=======
        data_key: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None,
        cx: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None,
        cy: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None,
        radius: Optional[Union[Var[Union[int, str]], Union[int, str]]] = None,
        axis_line: Optional[
            Union[Var[Union[Dict[str, Any], bool]], Union[Dict[str, Any], bool]]
>>>>>>> 2027a2f0 (order type annotations in pyi_generator (#3585))
        ] = None,
        axis_line_type: Optional[Union[reflex.vars.Var[str], str]] = None,
        tick_line: Optional[
<<<<<<< HEAD
            Union[
                reflex.vars.Var[Union[bool, Dict[str, Any]]],
                Union[bool, Dict[str, Any]],
            ]
=======
            Union[Var[Union[Dict[str, Any], bool]], Union[Dict[str, Any], bool]]
>>>>>>> 2027a2f0 (order type annotations in pyi_generator (#3585))
        ] = None,
        tick: Optional[Union[reflex.vars.Var[Union[int, str]], Union[int, str]]] = None,
        ticks: Optional[
            Union[reflex.vars.Var[List[Dict[str, Any]]], List[Dict[str, Any]]]
        ] = None,
        orient: Optional[Union[reflex.vars.Var[str], str]] = None,
        allow_duplicated_category: Optional[Union[reflex.vars.Var[bool], bool]] = None,
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
    ) -> "PolarAngleAxis":
        """Create the component.

        Args:
            *children: The children of the component.
            data_key: The key of a group of data which should be unique to show the meaning of angle axis.
            cx: The x-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container width.
            cy: The y-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container height.
            radius: The outer radius of circle grid. If set a percentage, the final value is obtained by multiplying the percentage of maxRadius which is calculated by the width, height, cx, cy.
            axis_line: If false set, axis line will not be drawn. If true set, axis line will be drawn which have the props calculated internally. If object set, axis line will be drawn which have the props mergered by the internal calculated props and the option.
            axis_line_type: The type of axis line.
            tick_line: If false set, tick lines will not be drawn. If true set, tick lines will be drawn which have the props calculated internally. If object set, tick lines will be drawn which have the props mergered by the internal calculated props and the option.
            tick: The width or height of tick.
            ticks: The array of every tick's value and angle.
            orient: The orientation of axis text.
            allow_duplicated_category: Allow the axis has duplicated categorys or not when the type of axis is "category".
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class PolarGrid(Recharts):
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        cx: Optional[Union[reflex.vars.Var[Union[int, str]], Union[int, str]]] = None,
        cy: Optional[Union[reflex.vars.Var[Union[int, str]], Union[int, str]]] = None,
        inner_radius: Optional[
            Union[reflex.vars.Var[Union[int, str]], Union[int, str]]
        ] = None,
        outer_radius: Optional[
            Union[reflex.vars.Var[Union[int, str]], Union[int, str]]
        ] = None,
        polar_angles: Optional[Union[reflex.vars.Var[List[int]], List[int]]] = None,
        polar_radius: Optional[Union[reflex.vars.Var[List[int]], List[int]]] = None,
        grid_type: Optional[
            Union[
                reflex.vars.Var[Literal["polygon", "circle"]],
                Literal["polygon", "circle"],
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
    ) -> "PolarGrid":
        """Create the component.

        Args:
            *children: The children of the component.
            cx: The x-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container width.
            cy: The y-coordinate of center. If set a percentage, the final value is obtained by multiplying the percentage of container height.
            inner_radius: The radius of the inner polar grid.
            outer_radius: The radius of the outer polar grid.
            polar_angles: The array of every line grid's angle.
            polar_radius: The array of every line grid's radius.
            grid_type: The type of polar grids. 'polygon' | 'circle'
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

class PolarRadiusAxis(Recharts):
    def get_event_triggers(self) -> dict[str, Union[Var, Any]]: ...
    @overload
    @classmethod
    def create(  # type: ignore
        cls,
        *children,
        angle: Optional[Union[reflex.vars.Var[int], int]] = None,
        type_: Optional[
            Union[
                reflex.vars.Var[Literal["number", "category"]],
                Literal["number", "category"],
            ]
        ] = None,
        allow_duplicated_category: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        cx: Optional[Union[reflex.vars.Var[Union[int, str]], Union[int, str]]] = None,
        cy: Optional[Union[reflex.vars.Var[Union[int, str]], Union[int, str]]] = None,
        reversed: Optional[Union[reflex.vars.Var[bool], bool]] = None,
        orientation: Optional[Union[reflex.vars.Var[str], str]] = None,
        axis_line: Optional[
<<<<<<< HEAD
            Union[
                reflex.vars.Var[Union[bool, Dict[str, Any]]],
                Union[bool, Dict[str, Any]],
            ]
=======
            Union[Var[Union[Dict[str, Any], bool]], Union[Dict[str, Any], bool]]
>>>>>>> 2027a2f0 (order type annotations in pyi_generator (#3585))
        ] = None,
        tick: Optional[Union[reflex.vars.Var[Union[int, str]], Union[int, str]]] = None,
        tick_count: Optional[Union[reflex.vars.Var[int], int]] = None,
        scale: Optional[
            Union[
                reflex.vars.Var[
                    Literal[
                        "auto",
                        "linear",
                        "pow",
                        "sqrt",
                        "log",
                        "identity",
                        "time",
                        "band",
                        "point",
                        "ordinal",
                        "quantile",
                        "quantize",
                        "utc",
                        "sequential",
                        "threshold",
                    ]
                ],
                Literal[
                    "auto",
                    "linear",
                    "pow",
                    "sqrt",
                    "log",
                    "identity",
                    "time",
                    "band",
                    "point",
                    "ordinal",
                    "quantile",
                    "quantize",
                    "utc",
                    "sequential",
                    "threshold",
                ],
            ]
        ] = None,
        domain: Optional[List[int]] = None,
        style: Optional[Style] = None,
        key: Optional[Any] = None,
        id: Optional[Any] = None,
        class_name: Optional[Any] = None,
        autofocus: Optional[bool] = None,
        custom_attrs: Optional[Dict[str, Union[Var, str]]] = None,
        on_click: Optional[
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
        **props
    ) -> "PolarRadiusAxis":
        """Create the component.

        Args:
            *children: The children of the component.
            angle: The angle of radial direction line to display axis text.
            type_: The type of axis line. 'number' | 'category'
            allow_duplicated_category: Allow the axis has duplicated categorys or not when the type of axis is "category".
            cx: The x-coordinate of center.
            cy: The y-coordinate of center.
            reversed: If set to true, the ticks of this axis are reversed.
            orientation: The orientation of axis text.
            axis_line: If false set, axis line will not be drawn. If true set, axis line will be drawn which have the props calculated internally. If object set, axis line will be drawn which have the props mergered by the internal calculated props and the option.
            tick: The width or height of tick.
            tick_count: The count of ticks.
            scale: If 'auto' set, the scale funtion is linear scale. 'auto' | 'linear' | 'pow' | 'sqrt' | 'log' | 'identity' | 'time' | 'band' | 'point' | 'ordinal' | 'quantile' | 'quantize' | 'utc' | 'sequential' | 'threshold'
            domain: The domain of the polar radius axis, specifying the minimum and maximum values.
            style: The style of the component.
            key: A unique key for the component.
            id: The id for the component.
            class_name: The class name for the component.
            autofocus: Whether the component should take the focus once the page is loaded
            custom_attrs: custom attribute
            **props: The props of the component.

        Returns:
            The component.
        """
        ...

pie = Pie.create
radar = Radar.create
radial_bar = RadialBar.create
polar_angle_axis = PolarAngleAxis.create
polar_grid = PolarGrid.create
polar_radius_axis = PolarRadiusAxis.create
