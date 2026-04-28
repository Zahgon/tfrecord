"""Reader utils."""

import functools
import gzip
import io
import os
import struct
import typing

import numpy as np

from tfrecord import example_pb2, iterator_utils


def tfrecord_iterator(
    data_path: str,
    index_path: typing.Optional[str] = None,
    shard: typing.Optional[typing.Tuple[int, int]] = None,
    compression_type: typing.Optional[str] = None,
) -> typing.Iterable[memoryview]:
    """Create an iterator over the tfrecord dataset.

    Since the tfrecords file stores each example as bytes, we can
    define an iterator over `datum_bytes_view`, which is a memoryview
    object referencing the bytes.

    Params:
    -------
    data_path: str
        TFRecord file path.

    index_path: str, optional, default=None
        Index file path. Can be set to None if no file is available.

    shard: tuple of ints, optional, default=None
        A tuple (index, count) representing worker_id and num_workers
        count. Necessary to evenly split/shard the dataset among many
        workers (i.e. >1).

    Yields:
    -------
    datum_bytes_view: memoryview
        Object referencing the specified `datum_bytes` contained in the
        file (for a single record).
    """
    def read_records(start_offset=None, end_offset=None):
        pass

    def gzip_file_size(file_path):
        pass

    pass


def process_feature(feature: example_pb2.Feature, typename: str, typename_mapping: dict, key: str):
    # NOTE: We assume that each key in the example has only one field
    # (either "bytes_list", "float_list", or "int64_list")!
    pass


def extract_feature_dict(features, description, typename_mapping):
    pass


def example_loader(
    data_path: str,
    index_path: typing.Union[str, None],
    description: typing.Union[typing.List[str], typing.Dict[str, str], None] = None,
    shard: typing.Optional[typing.Tuple[int, int]] = None,
    compression_type: typing.Optional[str] = None,
) -> typing.Iterable[typing.Dict[str, np.ndarray]]:
    """Create an iterator over the (decoded) examples contained within
    the dataset.

    Decodes raw bytes of the features (contained within the dataset)
    into its respective format.

    Params:
    -------
    data_path: str
        TFRecord file path.

    index_path: str or None
        Index file path. Can be set to None if no file is available.

    description: list or dict of str, optional, default=None
        List of keys or dict of (key, value) pairs to extract from each
        record. The keys represent the name of the features and the
        values ("byte", "float", or "int") correspond to the data type.
        If dtypes are provided, then they are verified against the
        inferred type for compatibility purposes. If None (default),
        then all features contained in the file are extracted.

    shard: tuple of ints, optional, default=None
        A tuple (index, count) representing worker_id and num_workers
        count. Necessary to evenly split/shard the dataset among many
        workers (i.e. >1).

    compression_type: str, optional, default=None
        The type of compression used for the tfrecord. Choose either
        'gzip' or None.

    Yields:
    -------
    features: dict of {str, np.ndarray}
        Decoded bytes of the features into its respective data type (for
        an individual record).
    """
    def get_value(feature):
        pass

    pass


def sequence_loader(
    data_path: str,
    index_path: typing.Union[str, None],
    context_description: typing.Union[typing.List[str], typing.Dict[str, str], None] = None,
    features_description: typing.Union[typing.List[str], typing.Dict[str, str], None] = None,
    shard: typing.Optional[typing.Tuple[int, int]] = None,
    compression_type: typing.Optional[str] = None,
) -> typing.Iterable[
    typing.Tuple[typing.Dict[str, np.ndarray], typing.Dict[str, typing.List[np.ndarray]]]
]:
    """Create an iterator over the (decoded) sequence examples contained within
    the dataset.

    Decodes raw bytes of both the context and features (contained within the
    dataset) into its respective format.

    Params:
    -------
    data_path: str
        TFRecord file path.

    index_path: str or None
        Index file path. Can be set to None if no file is available.

    context_description: list or dict of str, optional, default=None
        List of keys or dict (key, value) pairs to extract from the
        the context of each record. The keys represent the name of the
        features and the values ("byte", "float" or "int") correspond
        to the data type. If dtypes are provided, then they are verified
        against the inferred type for compatibility purposes. If None
        (default), then all features contained in the file are extracted.

    features_description: list or dict of str, optional, default=None
        Same as `context_description`, but applies to the features of
        each record.

    shard: tuple of ints, optional, default=None
        A tuple (index, count) representing worker_id and num_workers
        count. Necessary to evenly split/shard the dataset among many
        workers (i.e. >1).

    compression_type: str, optional, default=None
        The type of compression used for the tfrecord. Choose either
        'gzip' or None.

    Yields:
    -------
    A tuple of (context, features) for an individual record.

    context: dict of {str, np.ndarray}
        Decoded bytes of the context features into its respective data
        type.

    features: dict of {str, np.ndarray}
        Decoded bytes of the sequence features into its respective data
        type.
    """
    def get_value(feature):
        pass

    pass


def tfrecord_loader(
    data_path: str,
    index_path: typing.Union[str, None],
    description: typing.Union[typing.List[str], typing.Dict[str, str], None] = None,
    shard: typing.Optional[typing.Tuple[int, int]] = None,
    sequence_description: typing.Union[typing.List[str], typing.Dict[str, str], None] = None,
    compression_type: typing.Optional[str] = None,
) -> typing.Iterable[
    typing.Union[
        typing.Dict[str, np.ndarray],
        typing.Tuple[typing.Dict[str, np.ndarray], typing.Dict[str, typing.List[np.ndarray]]],
    ]
]:
    """Create an iterator over the (decoded) examples contained within
    the dataset.

    Decodes raw bytes of the features (contained within the dataset)
    into its respective format.

    Params:
    -------
    data_path: str
        TFRecord file path.

    index_path: str or None
        Index file path. Can be set to None if no file is available.

    description: list or dict of str, optional, default=None
        List of keys or dict of (key, value) pairs to extract from each
        record. The keys represent the name of the features and the
        values ("byte", "float", or "int") correspond to the data type.
        If dtypes are provided, then they are verified against the
        inferred type for compatibility purposes. If None (default),
        or an empty list or dictionary, then all features contained in
        the file are extracted.

    shard: tuple of ints, optional, default=None
        A tuple (index, count) representing worker_id and num_workers
        count. Necessary to evenly split/shard the dataset among many
        workers (i.e. >1).

    sequence_description: list or dict of str, optional, default=None
        Similar to `description`, but refers to the sequence features
        within a `SequenceExample`. When this field is `None`, then it
        is assumed that an `Example` is being read otherwise, a
        `SequenceExample` is read. If an empty list or dictionary is
        passed, then all features contained in the file are extracted.

    compression_type: str, optional, default=None
        The type of compression used for the tfrecord. Choose either
        'gzip' or None.

    Yields:
    -------
    features: dict of {str, value}
        Decoded bytes of the features into its respective data type (for
        an individual record). `value` is either going to be an np.ndarray
        in the instance of an `Example` and a list of np.ndarray in the
        instance of a `SequenceExample`.
    """
    pass


def multi_tfrecord_loader(
    data_pattern: str,
    index_pattern: typing.Union[str, None],
    splits: typing.Dict[str, float],
    description: typing.Union[typing.List[str], typing.Dict[str, str], None] = None,
    sequence_description: typing.Union[typing.List[str], typing.Dict[str, str], None] = None,
    compression_type: typing.Optional[str] = None,
    infinite: bool = True,
    shard: typing.Optional[typing.Tuple[int, int]] = None
) -> typing.Iterable[
    typing.Union[
        typing.Dict[str, np.ndarray],
        typing.Tuple[typing.Dict[str, np.ndarray], typing.Dict[str, typing.List[np.ndarray]]],
    ]
]:
    """Create an iterator by reading and merging multiple tfrecord datasets.

    Params:
    -------
    data_pattern: str
        Input data path pattern.

    index_pattern: str or None
        Input index path pattern.

    splits: dict
        Dictionary of (key, value) pairs, where the key is used to
        construct the data and index path(s) and the value determines
        the contribution of each split to the batch.

    description: list or dict of str, optional, default=None
        List of keys or dict of (key, value) pairs to extract from each
        record. The keys represent the name of the features and the
        values ("byte", "float", or "int") correspond to the data type.
        If dtypes are provided, then they are verified against the
        inferred type for compatibility purposes. If None (default),
        then all features contained in the file are extracted.

    sequence_description: list or dict of str, optional, default=None
        Similar to `description`, but refers to the sequence features
        within a `SequenceExample`. When this field is `None`, then it
        is assumed that an `Example` is being read otherwise, a
        `SequenceExample` is read. If an empty list or dictionary is
        passed, then all features contained in the file are extracted.

    compression_type: str, optional, default=None
        The type of compression used for the tfrecord. Choose either
        'gzip' or None.

    infinite: bool, optional, default=True
        Whether the returned iterator should be infinite or not

    shard: tuple of ints, optional, default=None
        A tuple (index, count) representing worker_id and num_workers
        count. Necessary to evenly split/shard the dataset among many
        workers (i.e. >1).

    Returns:
    --------
    it: iterator
        A repeating iterator that generates batches of data.
    """
    pass
