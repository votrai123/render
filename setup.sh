#!/bin/bash
export DATABASE_URL="postgresql://my_postgres_9p24_user:iuT5Yz7AmDNTsrsoLNMy6nJuoWmEliFQ@dpg-csh4ln3tq21c73e3fkpg-a.oregon-postgres.render.com/my_postgres_9p24"
export EXCITED="true"
export AUTH0_DOMAIN="dev-trainv.us.auth0.com"
export ALGORITHMS="RS256"
export API_AUDIENCE="capstone"

export FLASK_APP=flaskr
export FLASK_DEBUG=True
export FLASK_ENVIRONMENT=debug
echo "setup.sh script executed successfully!"
