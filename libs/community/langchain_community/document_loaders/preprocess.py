"""Preprocess Reader."""
import os
from typing import List

from langchain_core.documents import Document

from langchain_community.document_loaders.base import BaseLoader


class PreprocessLoader(BaseLoader):
    def __init__(self, path, *args, **kwargs):
        """
        Preprocess is an API service that splits any kind of document into
        optimal chunks of text for use in language model tasks. Given documents
        as input Preprocess splits them into chunks of text that respect the layout
        and semantics of the original document.
        We split the content by taking into account sections, paragraphs,
        lists, images, data tables, text tables, and slides
        and following the content semantics for long texts.
        We support:
            - PDFs
            - Microsoft Office documents (Word, PowerPoint, Excel)
            - OpenOffice documents (ods, odt, odp)
            - HTML content (web pages, articles, emails)
            - Plain text
        You need a Preprocess API Key to use the SDK,
        to get one please reach out to support@preprocess.co asking for an API key.
        """
        try:
            from pypreprocess import Preprocess
        except ImportError:
            raise ImportError(
                "`pypreprocess` package not found, please run `pip install "
                + "pypreprocess`"
            )
        api_key = None
        if "api_key" in kwargs:
            api_key = kwargs["api_key"]
            if api_key is None or api_key == "":
                raise ValueError(
                    "Please provide an api key to be used while"
                    + "doing the auth with the system."
                )
        del kwargs["api_key"]

        _options = {}
        self._preprocess = Preprocess(api_key)
        self._filepath = None
        self._process_id = None

        if path is not None or path != "":
            self._filepath = path

        for key, value in kwargs.items():
            # You can set a filepath to let preprocess convert and chunk it for you
            if key == "filepath" and self._filepath is None:
                self._filepath = value
                self._preprocess.set_filepath(value)

            # or if you already called it before and have the process_id,
            # you can pass it to get you back the chunks again
            elif key == "process_id":
                self._process_id = value
                self._preprocess.set_process_id(value)

            # You can also set some options to suit your needs
            elif key in ["table_output_format", "table_output"]:
                _options["table_output_format"] = value

            elif key in ["repeat_table_header", "table_header"]:
                _options["repeat_table_header"] = value

            elif key in ["merge", "repeat_title"]:
                _options[key] = value

        if _options != {}:
            self._preprocess.set_options(_options)

        # Remember to path either filepath or process_id,
        # both of them can't be None or not passed
        if self._filepath is None and self._process_id is None:
            raise ValueError(
                "Please provide either filepath or process_id to handle the resutls."
            )

        self._chunks = None

    def load(self, return_whole_document=False) -> List[Document]:
        """
        This function loads to you the chunks from preprocess sdk
        and return it to you. If you want to return only the extracted text
        and handle it with custom pipelines set `return_whole_document = True`
        Otherwise this function will return to you a list of Documents each one
        containing a chunk with metadata of filename
        """
        if self._chunks is None:
            if self._process_id is not None:
                self._get_data_by_process()
            elif self._filepath is not None:
                self._get_data_by_filepath()

            if self._chunks is not None:
                if return_whole_document is True:
                    return [
                        Document(
                            text=" ".join(self._chunks),
                            metadata={"filename": os.path.basename(self._filepath)},
                        )
                    ]
                else:
                    return [
                        Document(
                            text=chunk,
                            metadata={"filename": os.path.basename(self._filepath)},
                        )
                        for chunk in self._chunks
                    ]
            else:
                raise Exception(
                    "There is error happened during handling your file,"
                    + " please try again."
                )

        else:
            if return_whole_document is True:
                return [
                    Document(
                        text=" ".join(self._chunks),
                        metadata={"filename": os.path.basename(self._filepath)},
                    )
                ]
            else:
                return [
                    Document(
                        text=chunk,
                        metadata={"filename": os.path.basename(self._filepath)},
                    )
                    for chunk in self._chunks
                ]

    def get_process_id(self):
        """
        This function you can call it to give you back the process_id
        to store it as you want to use it later.
        """
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
