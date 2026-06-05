from typing import Any, Optional
from pydantic import BaseModel, ConfigDict


class ZfsProperty(BaseModel):
    model_config = ConfigDict(extra='ignore')

    parsed: Any
    rawvalue: str
    value: Optional[str] = None
    source: str
    source_info: Optional[str] = None

class Dataset(BaseModel):
    model_config = ConfigDict(extra="ignore")

    # always-present identity fields
    id: str
    name: str
    pool: str
    type: str
    mountpoint: Optional[str] = None

    # always-present encryption/lock state
    encrypted: bool
    encryption_root: Optional[str] = None
    key_loaded: bool
    locked: bool

    # ZFS properties — all wrapped in ZfsProperty.
    # All Optional because top-level summary entries omit some.
    used: Optional[ZfsProperty] = None
    available: Optional[ZfsProperty] = None
    compression: Optional[ZfsProperty] = None
    compressratio: Optional[ZfsProperty] = None
    quota: Optional[ZfsProperty] = None
    recordsize: Optional[ZfsProperty] = None
    creation: Optional[ZfsProperty] = None

    # recursion
    children: list["Dataset"] = []