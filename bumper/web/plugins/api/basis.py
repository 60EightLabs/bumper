"""Basis plugin module."""

import logging
from collections.abc import Iterable
from typing import Any

from aiohttp import web
from aiohttp.web_exceptions import HTTPInternalServerError
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from aiohttp.web_routedef import AbstractRouteDef

from bumper.utils import utils

from .. import WebserverPlugin

_LOGGER = logging.getLogger("web_route_api_basis")


class BasisPlugin(WebserverPlugin):
    """Basis plugin."""

    @property
    def routes(self) -> Iterable[AbstractRouteDef]:
        """Plugin routes."""
        return [
            web.route(
                "*",
                "/basis/dc/get-by-area",
                _handle_get_by_area,
            ),
        ]


async def _handle_get_by_area(request: Request) -> Response:
    """Get by area."""
    try:
        area_code = request.query.get("area", "eu")
        code = 0
        data_str = "data"
        data: dict[str, Any] | str = {"dc": utils.get_dc_code(area_code)}

        if area_code not in utils.area_code_mapping:
            code = 4000
            data_str = "msg"
            msg_list = '", "'.join(utils.area_code_mapping.keys())
            data = f'area: area must be one of the following: "{msg_list}"'

        return web.json_response({"code": code, f"{data_str}": data})
    except Exception as e:
        _LOGGER.error(utils.default_exception_str_builder(e, "during handling request"), exc_info=True)
    raise HTTPInternalServerError