from __future__ import print_function

import glob
import os
import struct
import sys


def create_index(tfrecord_file: str, index_file: str) -> None:
    """Create index from the tfrecords file.

    Stores starting location (byte) and length (in bytes) of each
    serialized record.

    Params:
    -------
    tfrecord_file: str
        Path to the TFRecord file.

    index_file: str
        Path where to store the index file.
    """
    pass


def create_indices(tfrecord_dir: str) -> None:
    """Create indices for all tfrecord files in the directory.

    Params:
    -------
    tfrecord_dir: str
        Path to the directory containing TFRecord files.
    """
    pass


def main():
    pass


if __name__ == "__main__":
    main()
