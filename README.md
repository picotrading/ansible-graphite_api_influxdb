graphite_api_influxdb
=====================

Role which installs Graphite API with InfluxDB storage backend from RPM packages.
You must build the RPM packages and place them into a YUM repo (see
[`yumrepo`](https://github.com/picotrading/ansible-yumrepo) role). This role is
actually just a wrapper around the
[`graphite_api`](https://github.com/picotrading/ansible-graphite_api) role.


Example
-------

```
---

# Example of how to use the single host installation (graphite-api + influxdb on
# one host)
- hosts: myhost1
  roles:
    - graphite_api_influxdb

# Example how to customize InfluxDB connection and storage schema
- hosts: myhost2
  roles:
    - role: graphite_api_influxdb
      graphite_api_influxdb_server: my_influxdb_server_ip
      graphite_api_influxdb_user: my_user
      graphite_api_influxdb_password: myTopSecretPassword
      graphite_api_influxdb_db: my_db
      graphite_api_influxdb_schema:
        # Set defautl retention period to 60 seconds
        - ['', 60]
        # Set high-res-metrics retention period to 10 seconds
        - ['high-res-metrics', 10]

# Or you can create completely new config template
- hosts: myhost3
  roles:
    - role: graphite_api_influxdb
      graphite_api_influxdb_config:
        search_index: /var/lib/graphite-api/index
        finders:
          - graphite_influxdb.InfluxdbFinder
        functions:
          - graphite_api.functions.SeriesFunctions
          - graphite_api.functions.PieFunctions
        cache:
          type: filesystem
          dir: /tmp/graphite-api-cache
        time_zone: US/Central
        allowed_origins:
          - "*"
        influxdb:
          host: my_influxdb_server_ip
          port: "{{ graphite_api_influxdb_port }}"
          user: my_user
          pass: myTopSecretPassword
          db: my_db
          schema:
            - ['', 60]
            - ['high-res-metrics', 10]
            - ['low-res-metrics', 300]
```


Role variables
--------------

List of variables used by the role:

```
# Package to be installed (you can force a specific version here)
graphite_api_influxdb_pkg: python-graphite-influxdb

# Default cache dir
graphite_api_influxdb_cache_dir: /tmp/graphite-api-cache

# Default InfluxDB server
graphite_api_influxdb_server: 127.0.0.1

# Default InfluxDB port number
graphite_api_influxdb_port: 8086

# Default InfluxDB user name
graphite_api_influxdb_user: root

# Default InfluxDB user password
graphite_api_influxdb_password: root

# Default InfluxDB database name
graphite_api_influxdb_db: graphite

# Default storage schema (the same like Carbon schema)
graphite_api_influxdb_schema:
  - ['', 10]
  - ['high-res-metrics', 1]

# Default config template
graphite_api_influxdb_config:
  search_index: /var/lib/graphite-api/index
  finders:
    - graphite_influxdb.InfluxdbFinder
  functions:
    - graphite_api.functions.SeriesFunctions
    - graphite_api.functions.PieFunctions
  cache:
    type: filesystem
    dir: "{{ graphite_api_influxdb_cache_dir }}"
  time_zone: "{{ graphite_api_timezone }}"
  allowed_origins:
    - "{{ graphite_api_cors_hosts }}"
  influxdb:
    host: "{{ graphite_api_influxdb_server }}"
    port: "{{ graphite_api_influxdb_port }}"
    user: "{{ graphite_api_influxdb_user }}"
    pass: "{{ graphite_api_influxdb_password }}"
    db: "{{ graphite_api_influxdb_db }}"
    schema: "{{ graphite_api_influxdb_schema }}"
```


Dependencies
------------

* [`graphite_api`](https://github.com/picotrading/ansible-graphite_api) role


License
-------

MIT


Author
------

Jiri Tyr
