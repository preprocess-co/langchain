"""Preprocess Reader."""
import os
from typing import List
from langchain_community.document_loaders.base import BaseLoader
from langchain_core.documents import Document


class PreprocessLoader(BaseLoader):
    def __init__(self, api_key: str, *args, **kwargs):

        try:
            from pypreprocess import Preprocess
        except ImportError:
            raise ImportError(
                "`pypreprocess` package not found, please run `pip install pypreprocess`"
            )

        if api_key is None or api_key == "":
            raise ValueError(
                "Please provide an api key to be used while doing the auth with the system."
            )

        _options = {}
        self._preprocess = Preprocess(api_key)
        self._filepath = None
        self._process_id = None

        for key, value in kwargs.items():
            if key == "filepath":
                self._filepath = value
                self._preprocess.set_filepath(value)
            
            elif key == "process_id":
                self._process_id = value
                self._preprocess.set_process_id(value)

            elif key in ["table_output_format", "table_output"]:
                self._options["table_output_format"] = value

            elif key in ["repeat_table_header", "table_header"]:
                self._options["repeat_table_header"] = value

            elif key in ["merge", "repeat_title"]:
                self._options[key] = value

        if _options != {}:
            self._preprocess.set_options(_options)

        if self._filepath is None and self._process_id is None:
            raise ValueError(
                "Please provide either filepath or process_id to handle the resutls."
            )

        self._chunks = None

    def load(self) -> List[Document]:
        if self._chunks is None:
            if self._process_id is not None:
                self._get_data_by_process()
            elif self._filepath is not None:
                self._get_data_by_filepath()

            if self._chunks is not None:
                return [
                    Document(
                        text=chunk,
                        metadata={"filename": os.path.basename(self._filepath)},
                    )
                    for chunk in self._chunks
                ]
            else:
                raise Exception(
                    "There is error happened during handling your file, please try again."
                )

        else:
            return [
                Document(
                    text=chunk,
                    metadata={"filename": os.path.basename(self._filepath)},
                )
                for chunk in self._chunks
            ]

    def get_process_id(self):
        return self._process_id

    def _get_data_by_filepath(self) -> None:
        pp_response = self._preprocess.chunk()
        if pp_response.status == "OK" and pp_response.success is True:
            self._process_id = pp_response.data["process"]["id"]
            response = self._preprocess.wait()
            if response.status == "OK" and response.success is True:
                # self._filepath = response.data['info']['file']['name']
                self._chunks = response.data["chunks"]

    def _get_data_by_process(self) -> None:
        response = self._preprocess.wait()
        if response.status == "OK" and response.success is True:
            self._filepath = response.data["info"]["file"]["name"]
            self._chunks = response.data["chunks"]
