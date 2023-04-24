# gb_flask

# Workaround for psycopg2 installation on M1
Got from [here](https://stackoverflow.com/questions/66888087/cannot-install-psycopg2-with-pip3-on-m1-mac):
```bash
brew install libpq --build-from-source
brew install openssl

export LDFLAGS="-L/opt/homebrew/opt/openssl@1.1/lib -L/opt/homebrew/opt/libpq/lib"
export CPPFLAGS="-I/opt/homebrew/opt/openssl@1.1/include -I/opt/homebrew/opt/libpq/include"

brew install postgresql
```