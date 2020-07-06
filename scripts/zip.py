#!/usr/bin/env python3

import os
import sys
import zipapp

sys.path.append(os.getcwd())
from fetcher.__version__ import __version__

# TODO put archive to a distribution directory

OUTPUT_FILENAME = f"基金信息生成器 {__version__}.pyz"
zipapp.create_archive(
    "fetcher", OUTPUT_FILENAME, interpreter="/usr/bin/env python3", compressed=True
)

# zipapp.create_archive(
#     os.getcwd(),
#     "基金信息生成器.pyz",
#     interpreter="/usr/bin/env python3",
#     main="fetcher.__main__:main",
#     filter=lambda x: os.path.splitext(x)[1] == "py",
#     compressed=True,
# )