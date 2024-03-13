from urllib.parse import quote
from ..net import query_serializer
from .base import BaseService
from ..models.Pets import Pets as PetsModel
from ..models.Pet import Pet as PetModel


class Pets(BaseService):
    def list_pets(self, limit: int = None) -> PetsModel:
        """
        List all pets
        Parameters:
        ----------
            limit: int
                How many items to return at one time (max 100)
        """

        url_endpoint = "/pets"
        headers = {}
        query_params = []
        self._add_required_headers(headers)
        if limit:
            query_params.append(
                query_serializer.serialize_query("form", False, "limit", limit)
            )
        final_url = self._url_prefix + url_endpoint
        if len(query_params) > 0:
            final_url += "?" + "&".join(query_params)
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, list):
            return [PetModel(**model) for model in res]
        return res

    def create_pets(self, request_input: PetModel):
        """
        Create a pet
        """

        url_endpoint = "/pets"
        headers = {"Content-Type": "application/json"}
        self._add_required_headers(headers)

        final_url = self._url_prefix + url_endpoint
        res = self._http.post(final_url, headers, request_input, True)
        return res

    def show_pet_by_id(self, pet_id: str) -> PetModel:
        """
        Info for a specific pet
        Parameters:
        ----------
            pet_id: str
                The id of the pet to retrieve
        """

        url_endpoint = "/pets/{pet_id}"
        headers = {}
        self._add_required_headers(headers)
        if not pet_id:
            raise ValueError("Parameter pet_id is required, cannot be empty or blank.")
        url_endpoint = url_endpoint.replace(
            "{pet_id}",
            quote(str(query_serializer.serialize_path("simple", False, pet_id, None))),
        )
        final_url = self._url_prefix + url_endpoint
        res = self._http.get(final_url, headers, True)
        if res and isinstance(res, dict):
            return PetModel(**res)
        return res
