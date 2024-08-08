"""Preprocess Loader."""
import os
from typing import List

from langchain_core.documents import Document

from langchain_community.document_loaders.base import BaseLoader


class PreprocessLoader(BaseLoader):
    def __init__(self, path, *args, **kwargs):
        """
        Preprocess is an API service that splits documents into optimal chunks
        of text for use in language model tasks.
        It accepts various document formats as input and segments them into chunks
        that respect the original document's layout and semantics.
        This segmentation considers sections, paragraphs, lists, images,
        data tables, text tables, and slides,
        all while adhering to the semantics of lengthy texts.
        Supported formats include:
            - PDFs
            - Microsoft Office documents (Word, PowerPoint, Excel)
            - OpenOffice documents (ods, odt, odp)
            - HTML content (web pages, articles, emails)
            - Plain text

        You need a Preprocess API Key, to get one please reach out to
        support@preprocess.co

        You can instantiate the loader by passing the file path.
        If you wish to load already chunked files,
        this can be done by providing the process_id to the loader.
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
                raise ValueError("Please provide a valid api key")
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

            elif key in [
                    "merge", 
                    "repeat_title",
                    "keep_header",
                    "keep_footer",
                    "smart_header"
                    "image_text"
                ]:
                _options[key] = value

        if _options != {}:
            self._preprocess.set_options(_options)

        # Remember to path either filepath or process_id,
        # both of them can't be None or not passed
        if self._filepath is None and self._process_id is None:
            raise ValueError("Please provide filepath or process_id.")

        self._chunks = None

    def load(self, return_whole_document=False) -> List[Document]:
        """
        Retrieve document chunks for downstream use in generating embeddings.
        Preprocess automatically generates optimal text chunks based
        on the original document's layout and content semantics.
        Applying TextSplitters to Documents returned by this method is not recommended.

        If you want to obtain only the extracted text for processing with custom
        Document transformers, set return_whole_document to True.

        This function returns a list of Documents, each containing a chunk.
        The filename is included in the metadata.
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
        process_id allows you to initialize the loader
        without chunking the document again.
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
