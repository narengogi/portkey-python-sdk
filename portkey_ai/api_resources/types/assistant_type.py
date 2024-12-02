import json
from typing import Dict, Optional, Union
import httpx
from .utils import parse_headers
from typing import List, Any
from pydantic import BaseModel, PrivateAttr

__all__ = [
    "Assistant",
    "AssistantList",
    "AssistantDeleted",
    "ToolCodeInterpreter",
    "ToolRetrieval",
    "ToolFunction",
    "Tool",
]


class ToolCodeInterpreter(BaseModel, extra="allow"):
    type: Optional[str]


class ToolRetrieval(BaseModel, extra="allow"):
    type: Optional[str]


class ToolFunction(BaseModel, extra="allow"):
    type: Optional[str]


Tool = Union[ToolCodeInterpreter, ToolRetrieval, ToolFunction]


class Assistant(BaseModel, extra="allow"):
    id: Optional[str]
    created_at: Optional[int]
    description: Optional[str] = None
    file_ids: Optional[List[str]] = None
    instructions: Optional[str] = None
    metadata: Optional[object] = None
    model: Optional[str]
    name: Optional[str] = None
    object: Optional[str]
    tools: Optional[List[Tool]]
    _headers: Optional[httpx.Headers] = PrivateAttr()

    def __str__(self):
        del self._headers
        return json.dumps(self.dict(), indent=4)

    def __getitem__(self, key):
        return getattr(self, key, None)

    def get(self, key: str, default: Optional[Any] = None):
        return getattr(self, key, None) or default

    def get_headers(self) -> Optional[Dict[str, str]]:
        return parse_headers(self._headers)


class AssistantList(BaseModel, extra="allow"):
    object: Optional[str]
    data: Optional[List[Assistant]]
    _headers: Optional[httpx.Headers] = PrivateAttr()

    def __str__(self):
        del self._headers
        return json.dumps(self.dict(), indent=4)

    def __getitem__(self, key):
        return getattr(self, key, None)

    def get(self, key: str, default: Optional[Any] = None):
        return getattr(self, key, None) or default

    def get_headers(self) -> Optional[Dict[str, str]]:
        return parse_headers(self._headers)


class AssistantDeleted(BaseModel, extra="allow"):
    id: Optional[str]
    object: Optional[str]
    deleted: Optional[bool]
    _headers: Optional[httpx.Headers] = PrivateAttr()

    def __str__(self):
        del self._headers
        return json.dumps(self.dict(), indent=4)

    def get_headers(self) -> Optional[Dict[str, str]]:
        return parse_headers(self._headers)
