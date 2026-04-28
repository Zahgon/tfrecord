"""Writer utils."""

import io
import struct
import typing

import crc32c
import numpy as np

from tfrecord import example_pb2


class TFRecordWriter:
    """Opens a TFRecord file for writing.

    Params:
    -------
    data_path: str
        Path to the tfrecord file.
    """

    def __init__(self, data_path: str) -> None:
        self.file = io.open(data_path, "wb")

    def close(self) -> None:
        """Close the tfrecord file."""
        pass

    def write(
        self,
        datum: typing.Dict[str, typing.Tuple[typing.Any, str]],
        sequence_datum: typing.Union[
            typing.Dict[str, typing.Tuple[typing.List[typing.Any], str]], None
        ] = None,
    ) -> None:
        """Write an example into tfrecord file. Either as a Example
        SequenceExample depending on the presence of `sequence_datum`.
        If `sequence_datum` is None (by default), this writes a Example
        to file. Otherwise, it writes a SequenceExample to file, assuming
        `datum` to be the context and `sequence_datum` to be the sequential
        features.

        Params:
        -------
        datum: dict
            Dictionary of tuples of form (value, dtype). dtype can be
            "byte", "float" or "int".
        sequence_datum: dict
            By default, it is set to None. If this value is present, then the
            Dictionary of tuples of the form (value, dtype). dtype can be
            "byte", "float" or "int". value should be the sequential features.
        """
        pass

    @staticmethod
    def masked_crc(data: bytes) -> bytes:
        """CRC checksum."""
        pass

    @staticmethod
    def serialize_tf_example(datum: typing.Dict[str, typing.Tuple[typing.Any, str]]) -> bytes:
        """Serialize example into tfrecord.Example proto.

        Params:
        -------
        datum: dict
            Dictionary of tuples of form (value, dtype). dtype can be
            "byte", "float" or "int".

        Returns:
        --------
        proto: bytes
            Serialized tfrecord.example to bytes.
        """
        def serialize(value):
            pass

        pass

    @staticmethod
    def serialize_tf_sequence_example(
        context_datum: typing.Dict[str, typing.Tuple[typing.Any, str]],
        features_datum: typing.Dict[str, typing.Tuple[typing.List[typing.Any], str]],
    ) -> bytes:
        """Serialize sequence example into tfrecord.SequenceExample proto.

        Params:
        -------
        context_datum: dict
            Dictionary of tuples of form (value, dtype). dtype can be
            "byte", "float" or int.

        features_datum: dict
            Same as `context_datum`, but for the features.

        Returns:
        --------
        proto: bytes
            Serialized tfrecord.SequenceExample to bytes.
        """
        def serialize(value):
            pass

        def serialize_repeated(value):
            pass

        pass
