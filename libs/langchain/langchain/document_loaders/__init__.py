"""**Document Loaders**  are classes to load Documents.

**Document Loaders** are usually used to load a lot of Documents in a single run.

**Class hierarchy:**

.. code-block::

    BaseLoader --> <name>Loader  # Examples: TextLoader, UnstructuredFileLoader

**Main helpers:**

.. code-block::

    Document, <name>TextSplitter
"""

from typing import TYPE_CHECKING, Any
from langchain.document_loaders.acreom import AcreomLoader
from langchain.document_loaders.airbyte import (
    AirbyteCDKLoader,
    AirbyteGongLoader,
    AirbyteHubspotLoader,
    AirbyteSalesforceLoader,
    AirbyteShopifyLoader,
    AirbyteStripeLoader,
    AirbyteTypeformLoader,
    AirbyteZendeskSupportLoader,
)
from langchain.document_loaders.airbyte_json import AirbyteJSONLoader
from langchain.document_loaders.airtable import AirtableLoader
from langchain.document_loaders.apify_dataset import ApifyDatasetLoader
from langchain.document_loaders.arcgis_loader import ArcGISLoader
from langchain.document_loaders.arxiv import ArxivLoader
from langchain.document_loaders.assemblyai import AssemblyAIAudioTranscriptLoader
from langchain.document_loaders.async_html import AsyncHtmlLoader
from langchain.document_loaders.azlyrics import AZLyricsLoader
from langchain.document_loaders.azure_ai_data import (
    AzureAIDataLoader,
)
from langchain.document_loaders.azure_blob_storage_container import (
    AzureBlobStorageContainerLoader,
)
from langchain.document_loaders.azure_blob_storage_file import (
    AzureBlobStorageFileLoader,
)
from langchain.document_loaders.bibtex import BibtexLoader
from langchain.document_loaders.bigquery import BigQueryLoader
from langchain.document_loaders.bilibili import BiliBiliLoader
from langchain.document_loaders.blackboard import BlackboardLoader
from langchain.document_loaders.blob_loaders import (
    Blob,
    BlobLoader,
    FileSystemBlobLoader,
    YoutubeAudioLoader,
)
from langchain.document_loaders.blockchain import BlockchainDocumentLoader
from langchain.document_loaders.brave_search import BraveSearchLoader
from langchain.document_loaders.browserless import BrowserlessLoader
from langchain.document_loaders.chatgpt import ChatGPTLoader
from langchain.document_loaders.chromium import AsyncChromiumLoader
from langchain.document_loaders.college_confidential import CollegeConfidentialLoader
from langchain.document_loaders.concurrent import ConcurrentLoader
from langchain.document_loaders.confluence import ConfluenceLoader
from langchain.document_loaders.conllu import CoNLLULoader
from langchain.document_loaders.couchbase import CouchbaseLoader
from langchain.document_loaders.csv_loader import CSVLoader, UnstructuredCSVLoader
from langchain.document_loaders.cube_semantic import CubeSemanticLoader
from langchain.document_loaders.datadog_logs import DatadogLogsLoader
from langchain.document_loaders.dataframe import DataFrameLoader
from langchain.document_loaders.diffbot import DiffbotLoader
from langchain.document_loaders.directory import DirectoryLoader
from langchain.document_loaders.discord import DiscordChatLoader
from langchain.document_loaders.docugami import DocugamiLoader
from langchain.document_loaders.docusaurus import DocusaurusLoader
from langchain.document_loaders.dropbox import DropboxLoader
from langchain.document_loaders.duckdb_loader import DuckDBLoader
from langchain.document_loaders.email import (
    OutlookMessageLoader,
    UnstructuredEmailLoader,
)
from langchain.document_loaders.epub import UnstructuredEPubLoader
from langchain.document_loaders.etherscan import EtherscanLoader
from langchain.document_loaders.evernote import EverNoteLoader
from langchain.document_loaders.excel import UnstructuredExcelLoader
from langchain.document_loaders.facebook_chat import FacebookChatLoader
from langchain.document_loaders.fauna import FaunaLoader
from langchain.document_loaders.figma import FigmaFileLoader
from langchain.document_loaders.gcs_directory import GCSDirectoryLoader
from langchain.document_loaders.gcs_file import GCSFileLoader
from langchain.document_loaders.geodataframe import GeoDataFrameLoader
from langchain.document_loaders.git import GitLoader
from langchain.document_loaders.gitbook import GitbookLoader
from langchain.document_loaders.github import GitHubIssuesLoader
from langchain.document_loaders.google_speech_to_text import GoogleSpeechToTextLoader
from langchain.document_loaders.googledrive import GoogleDriveLoader
from langchain.document_loaders.gutenberg import GutenbergLoader
from langchain.document_loaders.hn import HNLoader
from langchain.document_loaders.html import UnstructuredHTMLLoader
from langchain.document_loaders.html_bs import BSHTMLLoader
from langchain.document_loaders.hugging_face_dataset import HuggingFaceDatasetLoader
from langchain.document_loaders.ifixit import IFixitLoader
from langchain.document_loaders.image import UnstructuredImageLoader
from langchain.document_loaders.image_captions import ImageCaptionLoader
from langchain.document_loaders.imsdb import IMSDbLoader
from langchain.document_loaders.iugu import IuguLoader
from langchain.document_loaders.joplin import JoplinLoader
from langchain.document_loaders.json_loader import JSONLoader
from langchain.document_loaders.lakefs import LakeFSLoader
from langchain.document_loaders.larksuite import LarkSuiteDocLoader
from langchain.document_loaders.markdown import UnstructuredMarkdownLoader
from langchain.document_loaders.mastodon import MastodonTootsLoader
from langchain.document_loaders.max_compute import MaxComputeLoader
from langchain.document_loaders.mediawikidump import MWDumpLoader
from langchain.document_loaders.merge import MergedDataLoader
from langchain.document_loaders.mhtml import MHTMLLoader
from langchain.document_loaders.modern_treasury import ModernTreasuryLoader
from langchain.document_loaders.mongodb import MongodbLoader
from langchain.document_loaders.news import NewsURLLoader
from langchain.document_loaders.notebook import NotebookLoader
from langchain.document_loaders.notion import NotionDirectoryLoader
from langchain.document_loaders.notiondb import NotionDBLoader
from langchain.document_loaders.obs_directory import OBSDirectoryLoader
from langchain.document_loaders.obs_file import OBSFileLoader
from langchain.document_loaders.obsidian import ObsidianLoader
from langchain.document_loaders.odt import UnstructuredODTLoader
from langchain.document_loaders.onedrive import OneDriveLoader
from langchain.document_loaders.onedrive_file import OneDriveFileLoader
from langchain.document_loaders.open_city_data import OpenCityDataLoader
from langchain.document_loaders.org_mode import UnstructuredOrgModeLoader
from langchain.document_loaders.pdf import (
    AmazonTextractPDFLoader,
    MathpixPDFLoader,
    OnlinePDFLoader,
    PDFMinerLoader,
    PDFMinerPDFasHTMLLoader,
    PDFPlumberLoader,
    PyMuPDFLoader,
    PyPDFDirectoryLoader,
    PyPDFium2Loader,
    PyPDFLoader,
    UnstructuredPDFLoader,
)
from langchain.document_loaders.polars_dataframe import PolarsDataFrameLoader
from langchain.document_loaders.powerpoint import UnstructuredPowerPointLoader
from langchain.document_loaders.preprocess import PreprocessLoader
from langchain.document_loaders.psychic import PsychicLoader
from langchain.document_loaders.pubmed import PubMedLoader
from langchain.document_loaders.pyspark_dataframe import PySparkDataFrameLoader
from langchain.document_loaders.python import PythonLoader
from langchain.document_loaders.readthedocs import ReadTheDocsLoader
from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain.document_loaders.reddit import RedditPostsLoader
from langchain.document_loaders.roam import RoamLoader
from langchain.document_loaders.rocksetdb import RocksetLoader
from langchain.document_loaders.rss import RSSFeedLoader
from langchain.document_loaders.rst import UnstructuredRSTLoader
from langchain.document_loaders.rtf import UnstructuredRTFLoader
from langchain.document_loaders.s3_directory import S3DirectoryLoader
from langchain.document_loaders.s3_file import S3FileLoader
from langchain.document_loaders.sharepoint import SharePointLoader
from langchain.document_loaders.sitemap import SitemapLoader
from langchain.document_loaders.slack_directory import SlackDirectoryLoader
from langchain.document_loaders.snowflake_loader import SnowflakeLoader
from langchain.document_loaders.spreedly import SpreedlyLoader
from langchain.document_loaders.srt import SRTLoader
from langchain.document_loaders.stripe import StripeLoader
from langchain.document_loaders.telegram import (
    TelegramChatApiLoader,
    TelegramChatFileLoader,
)
from langchain.document_loaders.tencent_cos_directory import TencentCOSDirectoryLoader
from langchain.document_loaders.tencent_cos_file import TencentCOSFileLoader
from langchain.document_loaders.tensorflow_datasets import TensorflowDatasetLoader
from langchain.document_loaders.text import TextLoader
from langchain.document_loaders.tomarkdown import ToMarkdownLoader
from langchain.document_loaders.toml import TomlLoader
from langchain.document_loaders.trello import TrelloLoader
from langchain.document_loaders.tsv import UnstructuredTSVLoader
from langchain.document_loaders.twitter import TwitterTweetLoader
from langchain.document_loaders.unstructured import (
    UnstructuredAPIFileIOLoader,
    UnstructuredAPIFileLoader,
    UnstructuredFileIOLoader,
    UnstructuredFileLoader,
)
from langchain.document_loaders.url import UnstructuredURLLoader
from langchain.document_loaders.url_playwright import PlaywrightURLLoader
from langchain.document_loaders.url_selenium import SeleniumURLLoader
from langchain.document_loaders.weather import WeatherDataLoader
from langchain.document_loaders.web_base import WebBaseLoader
from langchain.document_loaders.whatsapp_chat import WhatsAppChatLoader
from langchain.document_loaders.wikipedia import WikipediaLoader
from langchain.document_loaders.word_document import (
    Docx2txtLoader,
    UnstructuredWordDocumentLoader,
)
from langchain.document_loaders.xml import UnstructuredXMLLoader
from langchain.document_loaders.xorbits import XorbitsLoader
from langchain.document_loaders.youtube import (
    GoogleApiClient,
    GoogleApiYoutubeLoader,
    YoutubeLoader,
)

from langchain._api import create_importer

if TYPE_CHECKING:
    from langchain_community.document_loaders import (
        AcreomLoader,
        AirbyteCDKLoader,
        AirbyteGongLoader,
        AirbyteHubspotLoader,
        AirbyteJSONLoader,
        AirbyteSalesforceLoader,
        AirbyteShopifyLoader,
        AirbyteStripeLoader,
        AirbyteTypeformLoader,
        AirbyteZendeskSupportLoader,
        AirtableLoader,
        AmazonTextractPDFLoader,
        ApifyDatasetLoader,
        ArcGISLoader,
        ArxivLoader,
        AssemblyAIAudioTranscriptLoader,
        AsyncChromiumLoader,
        AsyncHtmlLoader,
        AZLyricsLoader,
        AzureAIDataLoader,
        AzureBlobStorageContainerLoader,
        AzureBlobStorageFileLoader,
        BibtexLoader,
        BigQueryLoader,
        BiliBiliLoader,
        BlackboardLoader,
        BlockchainDocumentLoader,
        BraveSearchLoader,
        BrowserlessLoader,
        BSHTMLLoader,
        ChatGPTLoader,
        CollegeConfidentialLoader,
        ConcurrentLoader,
        ConfluenceLoader,
        CoNLLULoader,
        CouchbaseLoader,
        CSVLoader,
        CubeSemanticLoader,
        DatadogLogsLoader,
        DataFrameLoader,
        DiffbotLoader,
        DirectoryLoader,
        DiscordChatLoader,
        DocugamiLoader,
        DocusaurusLoader,
        Docx2txtLoader,
        DropboxLoader,
        DuckDBLoader,
        EtherscanLoader,
        EverNoteLoader,
        FacebookChatLoader,
        FaunaLoader,
        FigmaFileLoader,
        FileSystemBlobLoader,
        GCSDirectoryLoader,
        GCSFileLoader,
        GeoDataFrameLoader,
        GitbookLoader,
        GithubFileLoader,
        GitHubIssuesLoader,
        GitLoader,
        GoogleApiClient,
        GoogleApiYoutubeLoader,
        GoogleDriveLoader,
        GoogleSpeechToTextLoader,
        GutenbergLoader,
        HNLoader,
        HuggingFaceDatasetLoader,
        IFixitLoader,
        ImageCaptionLoader,
        IMSDbLoader,
        IuguLoader,
        JoplinLoader,
        JSONLoader,
        LakeFSLoader,
        LarkSuiteDocLoader,
        MastodonTootsLoader,
        MathpixPDFLoader,
        MaxComputeLoader,
        MergedDataLoader,
        MHTMLLoader,
        ModernTreasuryLoader,
        MongodbLoader,
        MWDumpLoader,
        NewsURLLoader,
        NotebookLoader,
        NotionDBLoader,
        NotionDirectoryLoader,
        OBSDirectoryLoader,
        OBSFileLoader,
        ObsidianLoader,
        OneDriveFileLoader,
        OneDriveLoader,
        OnlinePDFLoader,
        OpenCityDataLoader,
        OutlookMessageLoader,
        PagedPDFSplitter,
        PDFMinerLoader,
        PDFMinerPDFasHTMLLoader,
        PDFPlumberLoader,
        PlaywrightURLLoader,
        PolarsDataFrameLoader,
        PsychicLoader,
        PubMedLoader,
        PyMuPDFLoader,
        PyPDFDirectoryLoader,
        PyPDFium2Loader,
        PyPDFLoader,
        PySparkDataFrameLoader,
        PythonLoader,
        ReadTheDocsLoader,
        RecursiveUrlLoader,
        RedditPostsLoader,
        RoamLoader,
        RocksetLoader,
        RSSFeedLoader,
        S3DirectoryLoader,
        S3FileLoader,
        SeleniumURLLoader,
        SharePointLoader,
        SitemapLoader,
        SlackDirectoryLoader,
        SnowflakeLoader,
        SpreedlyLoader,
        SRTLoader,
        StripeLoader,
        TelegramChatApiLoader,
        TelegramChatFileLoader,
        TelegramChatLoader,
        TencentCOSDirectoryLoader,
        TencentCOSFileLoader,
        TensorflowDatasetLoader,
        TextLoader,
        ToMarkdownLoader,
        TomlLoader,
        TrelloLoader,
        TwitterTweetLoader,
        UnstructuredAPIFileIOLoader,
        UnstructuredAPIFileLoader,
        UnstructuredCSVLoader,
        UnstructuredEmailLoader,
        UnstructuredEPubLoader,
        UnstructuredExcelLoader,
        UnstructuredFileIOLoader,
        UnstructuredFileLoader,
        UnstructuredHTMLLoader,
        UnstructuredImageLoader,
        UnstructuredMarkdownLoader,
        UnstructuredODTLoader,
        UnstructuredOrgModeLoader,
        UnstructuredPDFLoader,
        UnstructuredPowerPointLoader,
        UnstructuredRSTLoader,
        UnstructuredRTFLoader,
        UnstructuredTSVLoader,
        UnstructuredURLLoader,
        UnstructuredWordDocumentLoader,
        UnstructuredXMLLoader,
        WeatherDataLoader,
        WebBaseLoader,
        WhatsAppChatLoader,
        WikipediaLoader,
        XorbitsLoader,
        YoutubeAudioLoader,
        YoutubeLoader,
        YuqueLoader,
    )

from langchain_core.document_loaders import Blob, BlobLoader

# For backwards compatibility
_old_to_new_name = {
    "PagedPDFSplitter": "PyPDFLoader",
    "TelegramChatLoader": "TelegramChatFileLoader",
}

# Create a way to dynamically look up deprecated imports.
# Used to consolidate logic for raising deprecation warnings and
# handling optional imports.
DEPRECATED_LOOKUP = {
    "AcreomLoader": "langchain_community.document_loaders",
    "AsyncHtmlLoader": "langchain_community.document_loaders",
    "AsyncChromiumLoader": "langchain_community.document_loaders",
    "AZLyricsLoader": "langchain_community.document_loaders",
    "AirbyteCDKLoader": "langchain_community.document_loaders",
    "AirbyteGongLoader": "langchain_community.document_loaders",
    "AirbyteJSONLoader": "langchain_community.document_loaders",
    "AirbyteHubspotLoader": "langchain_community.document_loaders",
    "AirbyteSalesforceLoader": "langchain_community.document_loaders",
    "AirbyteShopifyLoader": "langchain_community.document_loaders",
    "AirbyteStripeLoader": "langchain_community.document_loaders",
    "AirbyteTypeformLoader": "langchain_community.document_loaders",
    "AirbyteZendeskSupportLoader": "langchain_community.document_loaders",
    "AirtableLoader": "langchain_community.document_loaders",
    "AmazonTextractPDFLoader": "langchain_community.document_loaders",
    "ApifyDatasetLoader": "langchain_community.document_loaders",
    "ArcGISLoader": "langchain_community.document_loaders",
    "ArxivLoader": "langchain_community.document_loaders",
    "AssemblyAIAudioTranscriptLoader": "langchain_community.document_loaders",
    "AzureAIDataLoader": "langchain_community.document_loaders",
    "AzureBlobStorageContainerLoader": "langchain_community.document_loaders",
    "AzureBlobStorageFileLoader": "langchain_community.document_loaders",
    "BSHTMLLoader": "langchain_community.document_loaders",
    "BibtexLoader": "langchain_community.document_loaders",
    "BigQueryLoader": "langchain_community.document_loaders",
    "BiliBiliLoader": "langchain_community.document_loaders",
    "BlackboardLoader": "langchain_community.document_loaders",
    "Blob": "langchain_community.document_loaders",
    "BlobLoader": "langchain_community.document_loaders",
    "BlockchainDocumentLoader": "langchain_community.document_loaders",
    "BraveSearchLoader": "langchain_community.document_loaders",
    "BrowserlessLoader": "langchain_community.document_loaders",
    "CSVLoader": "langchain_community.document_loaders",
    "ChatGPTLoader": "langchain_community.document_loaders",
    "CoNLLULoader": "langchain_community.document_loaders",
    "CollegeConfidentialLoader": "langchain_community.document_loaders",
    "ConcurrentLoader": "langchain_community.document_loaders",
    "ConfluenceLoader": "langchain_community.document_loaders",
    "CouchbaseLoader": "langchain_community.document_loaders",
    "CubeSemanticLoader": "langchain_community.document_loaders",
    "DataFrameLoader": "langchain_community.document_loaders",
    "DatadogLogsLoader": "langchain_community.document_loaders",
    "DiffbotLoader": "langchain_community.document_loaders",
    "DirectoryLoader": "langchain_community.document_loaders",
    "DiscordChatLoader": "langchain_community.document_loaders",
    "DocugamiLoader": "langchain_community.document_loaders",
    "DocusaurusLoader": "langchain_community.document_loaders",
    "Docx2txtLoader": "langchain_community.document_loaders",
    "DropboxLoader": "langchain_community.document_loaders",
    "DuckDBLoader": "langchain_community.document_loaders",
    "EtherscanLoader": "langchain_community.document_loaders",
    "EverNoteLoader": "langchain_community.document_loaders",
    "FacebookChatLoader": "langchain_community.document_loaders",
    "FaunaLoader": "langchain_community.document_loaders",
    "FigmaFileLoader": "langchain_community.document_loaders",
    "FileSystemBlobLoader": "langchain_community.document_loaders",
    "GCSDirectoryLoader": "langchain_community.document_loaders",
    "GCSFileLoader": "langchain_community.document_loaders",
    "GeoDataFrameLoader": "langchain_community.document_loaders",
    "GitHubIssuesLoader": "langchain_community.document_loaders",
    "GitLoader": "langchain_community.document_loaders",
    "GithubFileLoader": "langchain_community.document_loaders",
    "GitbookLoader": "langchain_community.document_loaders",
    "GoogleApiClient": "langchain_community.document_loaders",
    "GoogleApiYoutubeLoader": "langchain_community.document_loaders",
    "GoogleSpeechToTextLoader": "langchain_community.document_loaders",
    "GoogleDriveLoader": "langchain_community.document_loaders",
    "GutenbergLoader": "langchain_community.document_loaders",
    "HNLoader": "langchain_community.document_loaders",
    "HuggingFaceDatasetLoader": "langchain_community.document_loaders",
    "IFixitLoader": "langchain_community.document_loaders",
    "IMSDbLoader": "langchain_community.document_loaders",
    "ImageCaptionLoader": "langchain_community.document_loaders",
    "IuguLoader": "langchain_community.document_loaders",
    "JSONLoader": "langchain_community.document_loaders",
    "JoplinLoader": "langchain_community.document_loaders",
    "LarkSuiteDocLoader": "langchain_community.document_loaders",
    "LakeFSLoader": "langchain_community.document_loaders",
    "MHTMLLoader": "langchain_community.document_loaders",
    "MWDumpLoader": "langchain_community.document_loaders",
    "MastodonTootsLoader": "langchain_community.document_loaders",
    "MathpixPDFLoader": "langchain_community.document_loaders",
    "MaxComputeLoader": "langchain_community.document_loaders",
    "MergedDataLoader": "langchain_community.document_loaders",
    "ModernTreasuryLoader": "langchain_community.document_loaders",
    "MongodbLoader": "langchain_community.document_loaders",
    "NewsURLLoader": "langchain_community.document_loaders",
    "NotebookLoader": "langchain_community.document_loaders",
    "NotionDBLoader": "langchain_community.document_loaders",
    "NotionDirectoryLoader": "langchain_community.document_loaders",
    "OBSDirectoryLoader": "langchain_community.document_loaders",
    "OBSFileLoader": "langchain_community.document_loaders",
    "ObsidianLoader": "langchain_community.document_loaders",
    "OneDriveFileLoader": "langchain_community.document_loaders",
    "OneDriveLoader": "langchain_community.document_loaders",
    "OnlinePDFLoader": "langchain_community.document_loaders",
    "OpenCityDataLoader": "langchain_community.document_loaders",
    "OutlookMessageLoader": "langchain_community.document_loaders",
    "PagedPDFSplitter": "langchain_community.document_loaders",
    "PDFMinerLoader": "langchain_community.document_loaders",
    "PDFMinerPDFasHTMLLoader": "langchain_community.document_loaders",
    "PDFPlumberLoader": "langchain_community.document_loaders",
    "PlaywrightURLLoader": "langchain_community.document_loaders",
    "PolarsDataFrameLoader": "langchain_community.document_loaders",
    "PsychicLoader": "langchain_community.document_loaders",
    "PubMedLoader": "langchain_community.document_loaders",
    "PyMuPDFLoader": "langchain_community.document_loaders",
    "PyPDFDirectoryLoader": "langchain_community.document_loaders",
    "PyPDFium2Loader": "langchain_community.document_loaders",
    "PyPDFLoader": "langchain_community.document_loaders",
    "PySparkDataFrameLoader": "langchain_community.document_loaders",
    "PythonLoader": "langchain_community.document_loaders",
    "ReadTheDocsLoader": "langchain_community.document_loaders",
    "RecursiveUrlLoader": "langchain_community.document_loaders",
    "RedditPostsLoader": "langchain_community.document_loaders",
    "RSSFeedLoader": "langchain_community.document_loaders",
    "RoamLoader": "langchain_community.document_loaders",
    "RocksetLoader": "langchain_community.document_loaders",
    "S3DirectoryLoader": "langchain_community.document_loaders",
    "S3FileLoader": "langchain_community.document_loaders",
    "SRTLoader": "langchain_community.document_loaders",
    "SeleniumURLLoader": "langchain_community.document_loaders",
    "SharePointLoader": "langchain_community.document_loaders",
    "SitemapLoader": "langchain_community.document_loaders",
    "SlackDirectoryLoader": "langchain_community.document_loaders",
    "SnowflakeLoader": "langchain_community.document_loaders",
    "SpreedlyLoader": "langchain_community.document_loaders",
    "StripeLoader": "langchain_community.document_loaders",
    "TelegramChatLoader": "langchain_community.document_loaders",
    "TelegramChatApiLoader": "langchain_community.document_loaders",
    "TelegramChatFileLoader": "langchain_community.document_loaders",
    "TensorflowDatasetLoader": "langchain_community.document_loaders",
    "TencentCOSDirectoryLoader": "langchain_community.document_loaders",
    "TencentCOSFileLoader": "langchain_community.document_loaders",
    "TextLoader": "langchain_community.document_loaders",
    "ToMarkdownLoader": "langchain_community.document_loaders",
    "TomlLoader": "langchain_community.document_loaders",
    "TrelloLoader": "langchain_community.document_loaders",
    "TwitterTweetLoader": "langchain_community.document_loaders",
    "UnstructuredAPIFileIOLoader": "langchain_community.document_loaders",
    "UnstructuredAPIFileLoader": "langchain_community.document_loaders",
    "UnstructuredCSVLoader": "langchain_community.document_loaders",
    "UnstructuredEPubLoader": "langchain_community.document_loaders",
    "UnstructuredEmailLoader": "langchain_community.document_loaders",
    "UnstructuredExcelLoader": "langchain_community.document_loaders",
    "UnstructuredFileIOLoader": "langchain_community.document_loaders",
    "UnstructuredFileLoader": "langchain_community.document_loaders",
    "UnstructuredHTMLLoader": "langchain_community.document_loaders",
    "UnstructuredImageLoader": "langchain_community.document_loaders",
    "UnstructuredMarkdownLoader": "langchain_community.document_loaders",
    "UnstructuredODTLoader": "langchain_community.document_loaders",
    "UnstructuredOrgModeLoader": "langchain_community.document_loaders",
    "UnstructuredPDFLoader": "langchain_community.document_loaders",
    "UnstructuredPowerPointLoader": "langchain_community.document_loaders",
    "UnstructuredRSTLoader": "langchain_community.document_loaders",
    "UnstructuredRTFLoader": "langchain_community.document_loaders",
    "UnstructuredTSVLoader": "langchain_community.document_loaders",
    "UnstructuredURLLoader": "langchain_community.document_loaders",
    "UnstructuredWordDocumentLoader": "langchain_community.document_loaders",
    "UnstructuredXMLLoader": "langchain_community.document_loaders",
    "WeatherDataLoader": "langchain_community.document_loaders",
    "WebBaseLoader": "langchain_community.document_loaders",
    "WhatsAppChatLoader": "langchain_community.document_loaders",
    "WikipediaLoader": "langchain_community.document_loaders",
    "XorbitsLoader": "langchain_community.document_loaders",
    "YoutubeAudioLoader": "langchain_community.document_loaders",
    "YoutubeLoader": "langchain_community.document_loaders",
    "YuqueLoader": "langchain_community.document_loaders",
}

_import_attribute = create_importer(__package__, deprecated_lookups=DEPRECATED_LOOKUP)


def __getattr__(name: str) -> Any:
    """Look up attributes dynamically."""
    return _import_attribute(name)


__all__ = [
    "AcreomLoader",
    "AsyncHtmlLoader",
    "AsyncChromiumLoader",
    "AZLyricsLoader",
    "AcreomLoader",
    "AirbyteCDKLoader",
    "AirbyteGongLoader",
    "AirbyteJSONLoader",
    "AirbyteHubspotLoader",
    "AirbyteSalesforceLoader",
    "AirbyteShopifyLoader",
    "AirbyteStripeLoader",
    "AirbyteTypeformLoader",
    "AirbyteZendeskSupportLoader",
    "AirtableLoader",
    "AmazonTextractPDFLoader",
    "ApifyDatasetLoader",
    "ArcGISLoader",
    "ArxivLoader",
    "AssemblyAIAudioTranscriptLoader",
    "AsyncHtmlLoader",
    "AzureAIDataLoader",
    "AzureBlobStorageContainerLoader",
    "AzureBlobStorageFileLoader",
    "BSHTMLLoader",
    "BibtexLoader",
    "BigQueryLoader",
    "BiliBiliLoader",
    "BlackboardLoader",
    "Blob",
    "BlobLoader",
    "BlockchainDocumentLoader",
    "BraveSearchLoader",
    "BrowserlessLoader",
    "CSVLoader",
    "ChatGPTLoader",
    "CoNLLULoader",
    "CollegeConfidentialLoader",
    "ConcurrentLoader",
    "ConfluenceLoader",
    "CouchbaseLoader",
    "CubeSemanticLoader",
    "DataFrameLoader",
    "DatadogLogsLoader",
    "DiffbotLoader",
    "DirectoryLoader",
    "DiscordChatLoader",
    "DocugamiLoader",
    "DocusaurusLoader",
    "Docx2txtLoader",
    "DropboxLoader",
    "DuckDBLoader",
    "EtherscanLoader",
    "EverNoteLoader",
    "FacebookChatLoader",
    "FaunaLoader",
    "FigmaFileLoader",
    "FileSystemBlobLoader",
    "GCSDirectoryLoader",
    "GCSFileLoader",
    "GeoDataFrameLoader",
    "GithubFileLoader",
    "GitHubIssuesLoader",
    "GitLoader",
    "GitbookLoader",
    "GoogleApiClient",
    "GoogleApiYoutubeLoader",
    "GoogleSpeechToTextLoader",
    "GoogleDriveLoader",
    "GutenbergLoader",
    "HNLoader",
    "HuggingFaceDatasetLoader",
    "IFixitLoader",
    "IMSDbLoader",
    "ImageCaptionLoader",
    "IuguLoader",
    "JSONLoader",
    "JoplinLoader",
    "LarkSuiteDocLoader",
    "LakeFSLoader",
    "MHTMLLoader",
    "MWDumpLoader",
    "MastodonTootsLoader",
    "MathpixPDFLoader",
    "MaxComputeLoader",
    "MergedDataLoader",
    "ModernTreasuryLoader",
    "MongodbLoader",
    "NewsURLLoader",
    "NotebookLoader",
    "NotionDBLoader",
    "NotionDirectoryLoader",
    "OBSDirectoryLoader",
    "OBSFileLoader",
    "ObsidianLoader",
    "OneDriveFileLoader",
    "OneDriveLoader",
    "OnlinePDFLoader",
    "OpenCityDataLoader",
    "OutlookMessageLoader",
    "PDFMinerLoader",
    "PDFMinerPDFasHTMLLoader",
    "PDFPlumberLoader",
    "PagedPDFSplitter",
    "PreprocessLoader",
    "PlaywrightURLLoader",
    "PolarsDataFrameLoader",
    "PsychicLoader",
    "PubMedLoader",
    "PyMuPDFLoader",
    "PyPDFDirectoryLoader",
    "PagedPDFSplitter",
    "PyPDFLoader",
    "PyPDFium2Loader",
    "PySparkDataFrameLoader",
    "PythonLoader",
    "RSSFeedLoader",
    "ReadTheDocsLoader",
    "RecursiveUrlLoader",
    "RedditPostsLoader",
    "RoamLoader",
    "RocksetLoader",
    "S3DirectoryLoader",
    "S3FileLoader",
    "SRTLoader",
    "SeleniumURLLoader",
    "SharePointLoader",
    "SitemapLoader",
    "SlackDirectoryLoader",
    "SnowflakeLoader",
    "SpreedlyLoader",
    "StripeLoader",
    "TelegramChatApiLoader",
    "TelegramChatFileLoader",
    "TelegramChatLoader",
    "TensorflowDatasetLoader",
    "TencentCOSDirectoryLoader",
    "TencentCOSFileLoader",
    "TextLoader",
    "ToMarkdownLoader",
    "TomlLoader",
    "TrelloLoader",
    "TwitterTweetLoader",
    "UnstructuredAPIFileIOLoader",
    "UnstructuredAPIFileLoader",
    "UnstructuredCSVLoader",
    "UnstructuredEPubLoader",
    "UnstructuredEmailLoader",
    "UnstructuredExcelLoader",
    "UnstructuredFileIOLoader",
    "UnstructuredFileLoader",
    "UnstructuredHTMLLoader",
    "UnstructuredImageLoader",
    "UnstructuredMarkdownLoader",
    "UnstructuredODTLoader",
    "UnstructuredOrgModeLoader",
    "UnstructuredPDFLoader",
    "UnstructuredPowerPointLoader",
    "UnstructuredRSTLoader",
    "UnstructuredRTFLoader",
    "UnstructuredTSVLoader",
    "UnstructuredURLLoader",
    "UnstructuredWordDocumentLoader",
    "UnstructuredXMLLoader",
    "WeatherDataLoader",
    "WebBaseLoader",
    "WhatsAppChatLoader",
    "WikipediaLoader",
    "XorbitsLoader",
    "YoutubeAudioLoader",
    "YoutubeLoader",
    "YuqueLoader",
]
