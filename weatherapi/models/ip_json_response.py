# -*- coding: utf-8 -*-

"""
    weatherapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class IpJsonResponse(object):

    """Implementation of the 'IpJson Response' model.

    TODO: type model description here.

    Attributes:
        ip (string): IP address
        mtype (string): ipv4 or ipv6
        continent_code (string): Continent code
        continent_name (string): Continent name
        country_code (string): Country code
        country_name (string): Name of country
        is_eu (bool): true or false
        geoname_id (int): Geoname ID
        city (string): City name
        region (string): Region name
        lat (float): Latitude in decimal degree
        lon (float): Longitude in decimal degree
        tz_id (string): Time zone
        localtime_epoch (int): Local time as epoch
        localtime (string): Date and time

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ip":'ip',
        "mtype":'type',
        "continent_code":'continent_code',
        "continent_name":'continent_name',
        "country_code":'country_code',
        "country_name":'country_name',
        "is_eu":'is_eu',
        "geoname_id":'geoname_id',
        "city":'city',
        "region":'region',
        "lat":'lat',
        "lon":'lon',
        "tz_id":'tz_id',
        "localtime_epoch":'localtime_epoch',
        "localtime":'localtime'
    }

    def __init__(self,
                 ip=None,
                 mtype=None,
                 continent_code=None,
                 continent_name=None,
                 country_code=None,
                 country_name=None,
                 is_eu=None,
                 geoname_id=None,
                 city=None,
                 region=None,
                 lat=None,
                 lon=None,
                 tz_id=None,
                 localtime_epoch=None,
                 localtime=None):
        """Constructor for the IpJsonResponse class"""

        # Initialize members of the class
        self.ip = ip
        self.mtype = mtype
        self.continent_code = continent_code
        self.continent_name = continent_name
        self.country_code = country_code
        self.country_name = country_name
        self.is_eu = is_eu
        self.geoname_id = geoname_id
        self.city = city
        self.region = region
        self.lat = lat
        self.lon = lon
        self.tz_id = tz_id
        self.localtime_epoch = localtime_epoch
        self.localtime = localtime


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        ip = dictionary.get('ip')
        mtype = dictionary.get('type')
        continent_code = dictionary.get('continent_code')
        continent_name = dictionary.get('continent_name')
        country_code = dictionary.get('country_code')
        country_name = dictionary.get('country_name')
        is_eu = dictionary.get('is_eu')
        geoname_id = dictionary.get('geoname_id')
        city = dictionary.get('city')
        region = dictionary.get('region')
        lat = dictionary.get('lat')
        lon = dictionary.get('lon')
        tz_id = dictionary.get('tz_id')
        localtime_epoch = dictionary.get('localtime_epoch')
        localtime = dictionary.get('localtime')

        # Return an object of this model
        return cls(ip,
                   mtype,
                   continent_code,
                   continent_name,
                   country_code,
                   country_name,
                   is_eu,
                   geoname_id,
                   city,
                   region,
                   lat,
                   lon,
                   tz_id,
                   localtime_epoch,
                   localtime)


