# -*- coding: utf-8 -*-
# @Time : 2026/5/14 18:20
# @Author  : Logan.Jin
# @Email   : loganjincn@gmail.com
# @Project : project-root-finder
# @File : root_finder.py
# @Software: PyCharm
import os
import pathlib
from functools import lru_cache
from typing import Optional, List

@lru_cache(maxsize=None)
def find_project_root_by_name(
    start_path: pathlib.Path,
    project_name: Optional[str] = None,
    extra_markers: Optional[List[str]] = None
) -> pathlib.Path:
    if project_name is None:
        project_name = os.environ.get("PROJECT_NAME") or "crawler"
        if not project_name:
            raise ValueError("请提供 project_name 或设置环境变量 PROJECT_NAME")
    for parent in [start_path] + list(start_path.parents):
        if parent.name == project_name:
            if not extra_markers:
                return parent
            for marker in extra_markers:
                if (parent / marker).exists():
                    return parent
            continue
    raise RuntimeError(
        f"未找到名称为 '{project_name}' 的项目根目录"
        + (f"（需包含以下标记之一：{extra_markers}）" if extra_markers else "")
    )
