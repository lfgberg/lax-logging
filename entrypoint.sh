#!/bin/bash
# entrypoint.sh

# Install JSON Datasource Plugin
grafana-cli plugins install marcusolsson-json-datasource

cp /custom-grafana-db/grafana.db /var/lib/grafana/grafana.db
chmod 777 /etc/grafana/grafana.ini
chmod 777 /var/lib/grafana/grafana.db

# Proceed with the default Grafana entrypoint
exec /bin/bash /run.sh
