"""Preprocess Reader."""
import os
from typing import List
from langchain_community.document_loaders.base import BaseLoader
from langchain_core.documents import Document

from pypreprocess import Preprocess


class PreprocessLoader(BaseLoader):
    def __init__(self, api_key: str, *args, **kwargs):
        if api_key is None or api_key == "":
            raise ValueError(
                "Please provide an api key to be used while doing the auth with the system."
            )

        _info = {}
        self._preprocess = Preprocess(api_key)
        self._filepath = None
        self._process_id = None

        for key, value in kwargs.items():
            if key == "filepath":
                self._filepath = value
                self._preprocess.set_filepath(value)
            if key == "process_id":
                self._process_id = value
                self._preprocess.set_process_id(value)
            elif key in [
                "merge",
                "max",
                "min",
                "min_min",
                "table_output",
                "repeat_title",
                "table_header",
                "lamguage",
            ]:
                _info[key] = value

        if _info != {}:
            self._preprocess.set_info(_info)

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
