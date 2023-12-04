import geoip2.database

# This reader object should be reused across lookups as creation of it is
# expensive.
with geoip2.database.Reader('lib/python3/dist-packages/maxmind-database.mmdb') as reader:
    response = reader.city('10.0.0.50');
    print(response.country.iso_code)