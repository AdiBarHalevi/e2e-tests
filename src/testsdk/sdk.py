"""
Creates a Testsdk class.
Generates the main SDK with all available queries as attributes.

Class:
    Testsdk
"""
from .net.environment import Environment

from .services.pets import Pets


class Testsdk:
    """
    A class representing the full Testsdk SDK

    Attributes
    ----------
    pets : Pets

    Methods
    -------
    set_base_url(url: str)
        Sets the end URL
    set_access_token(access_token)
        Set the access token
    """

    def __init__(self, access_token="", environment=Environment.DEFAULT) -> None:
        """
        Initializes the Testsdk SDK class.
        Parameters
        ----------
        environment: str
            The environment that the SDK is accessing
        access_token : str
            The access token
        """
        self.pets = Pets(access_token)

        self.set_base_url(environment.value)

    def set_base_url(self, url: str) -> None:
        """
        Sets the end URL

        Parameters
        ----------
            url:
                The end URL
        """
        self.pets.set_base_url(url)

    def set_access_token(self, token: str) -> None:
        """
        Sets auth token key

        Parameters
        ----------
        token: string
            Auth token value
        """
        self.pets.set_access_token(token)


# c029837e0e474b76bc487506e8799df5e3335891efe4fb02bda7a1441840310c
