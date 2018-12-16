# (c) Copyright 2018 Trent Hauck
# All Rights Reserved
"""Categorical Fields such as a class value."""

from pathlib import Path
from typing import Callable, Dict, List, Set

from gcgc.fields.field import Field


class LabelField(Field):
    """A type of Field that can work with label values -- creates integers to represent strings."""

    def __init__(
        self, name: str, encoding_dict: Dict[str, int], decoding_dict: Dict[int, str]
    ) -> None:
        """Initalize the LabelField object."""

<<<<<<< HEAD
        super().__init__(name=name)

        self.encoding_dict = encoding_dict
        self.decoding_dict = decoding_dict

=======
>>>>>>> master
    def encode(self, label: str) -> int:
        """Look up the label in the encoding dict and return it."""

        return self.encoding_dict[label]

    def decode(self, label_int: int) -> str:
        """Look up the label's integer from the decoding dict and return it."""

        return self.decoding_dict[label_int]

    @classmethod
<<<<<<< HEAD
    def from_vocabulary(cls, name: str, vocab: List[str]) -> "LabelField":
=======
    def from_vocabulary(cls, name: str, vocab: Set[str]) -> "LabelField":
>>>>>>> master
        """From a set of strings create the encoding dict."""

        encoding_dict = {}
        decoding_dict = {}

        for i, s in enumerate(sorted(set(vocab))):
            encoding_dict[s] = i
            decoding_dict[i] = s

        return LabelField(name, encoding_dict, decoding_dict)


def default_preprocess(p: Path) -> str:
    """Stringify the Path, p."""
    return str(p)


class FileMetaDataField(LabelField):
    """A Field that is transformed from the input Path object associated with the file."""

    def __init__(
        self,
        name: str,
        encoding_dict: Dict[str, int],
        decoding_dict: Dict[int, str],
        preprocess: Callable[[Path], str] = default_preprocess,
    ) -> None:
        """Initalize the FileMetaDataField object."""

        super().__init__(name=name, encoding_dict=encoding_dict, decoding_dict=decoding_dict)
        self.preprocess = preprocess

    def encode(self, file: Path) -> int:
        """Preprocess the file path, then encode the resultant label."""

        label = self.preprocess(file)
        return super().encode(label)

    @classmethod
    def from_paths(
        cls, name: str, paths: List[Path], preprocess: Callable[[Path], str] = default_preprocess
    ):
        """Given a set of exemplar paths, create the (d-)encoding dict and return the field."""

        str_vocab = [preprocess(p) for p in paths]
        label_field = super().from_vocabulary(name, str_vocab)

        return cls(name, label_field.encoding_dict, label_field.decoding_dict, preprocess)


class AnnotationField(LabelField):
    """A Field that is pulled from the annotation dict."""

    def __init__(
        self,
        name: str,
        encoding_dict: Dict[str, int],
        decoding_dict: Dict[int, str],
        preprocess: Callable[[Dict], str],
    ) -> None:
        """Initalize the AnnotationField object."""

<<<<<<< HEAD
        super().__init__(name=name, encoding_dict=encoding_dict, decoding_dict=decoding_dict)
        self.preprocess = preprocess

    def encode(self, annotations: Dict) -> int:
        """Preprocess the file path, then encode the resultant label."""

        label = self.preprocess(annotations)
=======
    def encode(self, file: Path) -> int:
        """Preprocess the file path, then encode the resultant label."""

        label = self.preprocess(file)
>>>>>>> master
        return super().encode(label)

    @classmethod
    def from_annotations(
        cls, name: str, annotations: List[Dict], preprocess: Callable[[Dict], str]
    ) -> "AnnotationField":
        """Given a set of exemplar annotations, create the encoding dict and return the field."""

        str_vocab = [preprocess(a) for a in annotations]
        label_field = super().from_vocabulary(name, str_vocab)

        return cls(name, label_field.encoding_dict, label_field.decoding_dict, preprocess)


class DescriptionField(LabelField):
    """A Field created from the sequence description str."""

    def __init__(
        self,
        name: str,
        encoding_dict: Dict[str, int],
        decoding_dict: Dict[int, str],
        preprocess: Callable[[str], str],
    ) -> None:
        """Initalize the DescriptionField object."""

        super().__init__(name=name, encoding_dict=encoding_dict, decoding_dict=decoding_dict)
        self.preprocess = preprocess

    def encode(self, d: str) -> int:
        """Preprocess the descriptin, then encode the resultant label."""

        label = self.preprocess(d)
        return super().encode(label)

    @classmethod
    def from_descriptions(
        cls, name: str, descriptions: List[str], preprocess: Callable[[str], str]
    ) -> "DescriptionField":
        """Given a set of exemplar descriptions, create the encoding dict and return the field."""

        str_vocab = [preprocess(d) for d in descriptions]
        label_field = super().from_vocabulary(name, str_vocab)

        return cls(name, label_field.encoding_dict, label_field.decoding_dict, preprocess)
